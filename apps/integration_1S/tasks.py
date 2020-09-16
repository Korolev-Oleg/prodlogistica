from dataclasses import dataclass
from random import choices
from string import ascii_letters

from redis import Redis
import requests

PROTOCOL = 'https'
# SERVER_1S = '77.37.174.39:33896'
SERVER_1S = '127.0.0.1:5001'
ACTION = 'start_uploading'

HOST_1S = f'{PROTOCOL}://{SERVER_1S}/{ACTION}'


def get_from_redis(key_name: str) -> any:
    return Redis().get(key_name).decode('utf-8')


@dataclass
class StatusCodes:
    connection_failed = 'Connection to the 1s server failed.'
    connection_to_1C_server = 'Start connection to the 1s server.'
    connected = 'Connected to 1S server success, start integration.'
    uploading = 'Uploading from 1S database started.'  # when flask in {HOST_1S} send data to the {HOST}/api
    uploaded = 'Integration complete.'  # when uploading finished
    null = None  # when redis restarted
    key_name = '1CIntegrationStatusCode'


@dataclass
class Exceptions:
    status_code_error = Exception('1S integration status code is incorrect')
    connection_error = Exception(f'Connection to the {HOST_1S} error')
    wrong_token = Exception('Wrong token value')


@dataclass
class SuccessToken:
    key_name = '1CIntegrationSecretKey'
    json_key = 'token'
    value: str


class IntegrationController:
    status_codes = StatusCodes
    secret_key = SuccessToken
    uploaded_at: str
    status: str

    def __init__(self, hot_start=False, bits=512):
        self.redis = Redis()
        self.status = self.__get_status__()
        self.secret_key_bits = bits
        self.__preparing__()

        if hot_start:
            self.start()

    def __preparing__(self) -> None:
        if self.__is_status_code_correct__(self.status):
            is_uploaded = self.status == StatusCodes.uploaded
            is_null = self.status == StatusCodes.null
            is_failed = self.status == StatusCodes.connection_failed
            if is_uploaded or is_null or is_failed:
                self.__save_status_to_redis__(StatusCodes.connection_to_1C_server)
                self.__new_token__()
            else:
                self.__upload_token__()

    def __new_token__(self) -> None:
        """ Create new token and save it in redis """
        SuccessToken.value = ''.join(choices(ascii_letters, k=self.secret_key_bits))
        self.redis.set(name=SuccessToken.key_name, value=SuccessToken.value)

    def __upload_token__(self) -> None:
        """ Load SuccessToken.value from redis  """
        SuccessToken.value = self.redis.get(SuccessToken.key_name).decode('utf-8')

    def __get_status__(self) -> str:
        """
        load status from redis db
        @return: str StatusCodes.status_code
        """
        status_code = self.redis.get(StatusCodes.key_name)
        if status_code:
            return status_code.decode('utf-8')
        else:
            return StatusCodes.null

    @staticmethod
    def __is_status_code_correct__(status_code: str) -> bool:
        """ Checks if status_code exists in StatusCodes.__dict__"""
        for attribute in StatusCodes.__dict__:
            if not attribute.startswith('__') and not attribute.endswith('__'):
                if status_code == StatusCodes().__getattribute__(attribute):
                    return True

        raise IOError(Exceptions.status_code_error)

    def __check_token__(self, key):
        if self.status == StatusCodes.connection_to_1C_server or self.status == StatusCodes.uploading:
            SuccessToken.value = get_from_redis(SuccessToken.key_name)
            return key == SuccessToken.value

    def __save_status_to_redis__(self, status_code: str) -> None:
        if self.__is_status_code_correct__(status_code):
            self.redis.set(name=StatusCodes.key_name, value=status_code)
            self.status = status_code

    def set_status(self, status_code: str, success_token: str) -> None:
        """
        Save status_code in to the redis
        @param success_token: generated during integration init
        @param status_code: StatusCode.value
        """
        if self.__check_token__(success_token):
            self.__save_status_to_redis__(status_code)
        else:
            raise IOError(Exceptions.wrong_token)

    def start(self) -> None:
        if self.status == StatusCodes.connection_to_1C_server:
            json = {
                SuccessToken.json_key: SuccessToken.value,
                'action': StatusCodes.uploading
            }
            try:
                # TODO verify=False! зарегистрировать сертификаты.
                response = requests.post(url=HOST_1S, json=json, verify=False)
                if response.status_code == requests.status_codes.codes.all_ok:
                    # TODO сделать проверку ответов
                    print('response.text: ', response.text)
                else:
                    raise IOError(Exceptions.connection_error)

            except requests.exceptions.ConnectionError as error:
                # TODO сделать логирование ошибок
                self.__save_status_to_redis__(StatusCodes.connection_failed)
                print('ERROR!', error)


if __name__ == '__main__':
    IntegrationController(hot_start=True)
