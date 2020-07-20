'use strict';

const path = require('path');
const webpack = require('webpack');

const isDev = process.env.NODE_ENV === 'development'

module.exports = {
  mode: isDev? 'production': 'development',
  entry: {
    app: "./js/app",
    home: "./js/home",
    about: "./js/about",
    contacts:"./js/contacts",
    // catalog:"./js/catalog"
  },
  output: {
    path: __dirname + '/config/static',
    filename: '[name].js',
      library: '[name]'
    },
    module: {
        rules: [
        {
            test: /.js$/,
            exclude: /(node_modules)/,
            use: {
                loader: 'babel-loader',
                // options: {
                //     presets: ['@babel/preset-env']
                // }
            }
        },
    ]
    },
    plugins: [
        new webpack.ProvidePlugin({
            $: 'jquery',
            jQuery: 'jquery',
            'window.jQuery': 'jquery',
          }),
    ],
};
