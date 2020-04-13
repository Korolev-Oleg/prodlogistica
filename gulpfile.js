'use-strict'
const {src, dest, watch, parallel} = require('gulp');
const sass = require('gulp-sass');
const webpack = require('webpack')
const webpackStream = require('webpack-stream')
const webpackConfig = require('./webpack.config')

gPaths = {
  src: './sources/',
  dest: './prodlogistica/static/',
}

paths = {
  css: {
    src: gPaths.src + 'sass/app.sass',
    dest: gPaths.dest + 'css',
    watch: gPaths.src + '**/*.sass'
  },
  js: {
    src: gPaths.src + 'js/*.js',
    dest: gPaths.dest + 'js',
    watch: gPaths.src + '**/*.js'
  },
  fonts: {
    src: gPaths.src + 'fonts/**/*.ttf',
    dest: gPaths.dest + 'fonts'
  }
};

function scripts(cb) {
  return src(paths.js.src)
  .pipe(webpackStream(webpackConfig), webpack)
  .pipe(dest(paths.js.dest));
};

function styles(cb) {
  return src(paths.css.src)
  .pipe(sass())
  .pipe(dest(paths.css.dest));
}

function build(){
  scripts();
  styles();
}

exports.default = function() {
  build()
  watch(paths.js.watch, scripts);
  watch(paths.css.watch, styles);
}