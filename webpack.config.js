'use strict'

const path = require('path');
const webpack = require('webpack');

module.exports = {
  mode: 'production',
  entry: {
    app: "./sources/js/app",
    home: "./sources/js/home",
    about: "./sources/js/about",
    // contacts:"./sources/js/contacts",
    // catalog:"./sources/js/catalog"
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
