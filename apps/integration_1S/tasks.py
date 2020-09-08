"""
Integration module with 1C server
flask on 1s server host:port: 77.37.174.39:33896

the module starts unloading the database from the 1C server
"""

from celery_config import app
from requests import post

import rsa
from redis import Redis
from dependency_injector import containers
from dependency_injector import providers
from dataclasses import dataclass

SERVER_1S_HOST = "77.37.174.39:33896/start_uploading"


@dataclass
class StatusCodes:
    uploading = 'uploading'
    connection = 'connection'
    uploaded = 'uploaded'
    null = 'nil'
    key_name = '1CIntegrationStatusCode'


@dataclass
class RSAKeys:
    n: int  # pk + prk
    e: int  # pk + prk
    d: int  # prk
    p: int  # prk
    q: int  # prk
    public: object
    private: object
    key_name_n = '1CPublicRSAn'
    key_name_e = '1CPublicRSAe'
    key_name_d = '1CPublicRSAd'
    key_name_p = '1CPublicRSAp'
    key_name_q = '1CPublicRSAq'


class IntegrationController:
    """
    The module, upon initialization, determines the unloading status and creates
    a key pair that implements encryption using the RSA method. Further, the
    status and keys are saved in the redis database. At the end, the module
    sends a POST request to the unloading module address on the 1C side, which
    contains information about the public key.
    The module also provides a method for decrypting data, their verification is
    carried out by the hash sum
    """
    status_codes = StatusCodes
    status_code_error = Exception('StatusCodeError')
    encrypt_bits: int
    uploaded_at: str
    status: str
    rsa_keys = RSAKeys

    def __init__(self, encrypt_bits=512):
        self.redis = Redis()
        self.status = self.__get_status__()
        self.encrypt_bits = encrypt_bits
        self.__preparing__()

    def __preparing__(self):
        if self.__is_status_code_correct__(self.status):
            is_status_uploaded = self.status == self.status_codes.uploaded
            is_status_null = self.status == self.status_codes.null
            if is_status_uploaded or is_status_null:
                self.set_status(self.status_codes.connection)
                self.__render_new_keys__()
            else:
                self.__get_keys__()

        else:
            raise IOError(self.status_code_error)

    def start(self) -> None:
        # TODO дописать запрос на серевер с выгрузкой ключей
        if self.status == self.status_codes.connection:
            json = {
                    'keys': {
                        'n': self.rsa_keys.n,
                        'e': self.rsa_keys.e,
                    },
                    'action': self.status_codes.uploading
                }
            post(url=SERVER_1S_HOST, json=json)

    def __get_status__(self) -> str:
        """
        load status from redis db
        @return: str StatusCodes.status_code
        """
        status_code = self.redis.get(self.status_codes.key_name)
        if status_code:
            return status_code.decode('utf-8')
        else:
            return self.status_codes.null

    def __get_keys__(self) -> None:
        """ Load keys from redis """
        def get(key):
            return int(self.redis.get(key).decode('utf-8'))

        self.rsa_keys.n = get(self.rsa_keys.key_name_n)
        self.rsa_keys.e = get(self.rsa_keys.key_name_e)
        self.rsa_keys.d = get(self.rsa_keys.key_name_d)
        self.rsa_keys.p = get(self.rsa_keys.key_name_p)
        self.rsa_keys.q = get(self.rsa_keys.key_name_q)

        self.rsa_keys.public = rsa.PublicKey(
            n=self.rsa_keys.n,
            e=self.rsa_keys.e)

        self.rsa_keys.private = rsa.PrivateKey(
            n=self.rsa_keys.n,
            e=self.rsa_keys.e,
            d=self.rsa_keys.d,
            p=self.rsa_keys.p,
            q=self.rsa_keys.q)

    def __render_new_keys__(self) -> None:
        """ Generate new RSA keys and save it in to the redis"""
        (self.rsa_keys.private, self.rsa_keys.public) = rsa.newkeys(nbits=self.encrypt_bits)
        self.rsa_keys.n = self.rsa_keys.private.n
        self.rsa_keys.e = self.rsa_keys.private.e
        self.rsa_keys.d = self.rsa_keys.public.d
        self.rsa_keys.p = self.rsa_keys.public.p
        self.rsa_keys.q = self.rsa_keys.public.q

        keys_dict = {
            self.rsa_keys.key_name_n: self.rsa_keys.n,
            self.rsa_keys.key_name_e: self.rsa_keys.e,
            self.rsa_keys.key_name_d: self.rsa_keys.d,
            self.rsa_keys.key_name_p: self.rsa_keys.p,
            self.rsa_keys.key_name_q: self.rsa_keys.q,
        }
        self.redis.mset(keys_dict)

    def __is_status_code_correct__(self, status_code) -> bool:
        """
        Check status_code
        @param status_code: str arg from get_status()
        @return: bool code status check result
        """
        if status_code == self.status_codes.uploaded: return True
        if status_code == self.status_codes.connection: return True
        if status_code == self.status_codes.uploading: return True
        if status_code == self.status_codes.null: return True
        return False

    def set_status(self, status_code) -> str or object:
        """
        Save status_code in to the redis
        @param status_code: str -> StatusCode.value
        """
        if self.__is_status_code_correct__(status_code):
            self.redis.set(name=self.status_codes.key_name, value=status_code)
            self.status = status_code
        else:
            raise IOError(self.status_code_error)


if __name__ == '__main__':
    integration = IntegrationController()
    integration.start()
