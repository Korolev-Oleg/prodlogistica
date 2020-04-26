'use strict'

const path = require('path');
const webpack = require('webpack');

module.exports = {
    mode: 'development',
    output: {
        filename: 'app.js',
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