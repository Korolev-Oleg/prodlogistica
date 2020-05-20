'use-strict';
const {src, dest, watch, parallel} = require('gulp');
const sass = require('gulp-sass');
const webpack = require('webpack');
const webpackStream = require('webpack-stream');
const webpackConfig = require('./webpack.config');
const sourcemaps = require('gulp-sourcemaps');
const cls = require('gulp-clean');
const gulpif = require('gulp-if');
const cssminifi = require('gulp-minify-css');

let DEVMODE = false;

gPaths = {
  src: './sources/',
  dest: './config/static/',
};

paths = {
  css: {
    src: gPaths.src + 'sass/*.sass',
    dest: gPaths.dest + 'css',
    watch: [gPaths.src + 'sass/**/*.sass', gPaths.src + 'sass/**/*.scss'],
  },
  js: {
    src: gPaths.src + 'js',
    dest: gPaths.dest + 'js',
    watch: gPaths.src + '**/*.js'
  },
  fonts: {
    src: gPaths.src + 'fonts/**/*.ttf',
    dest: gPaths.dest + 'fonts'
  }
};

function build_scripts(cb) {
  return src(paths.js.src)
  .pipe(webpackStream(webpackConfig), webpack)
  .pipe(dest(paths.js.dest));
}

function build_styles(cb) {
  return src(paths.css.src)
    .pipe(gulpif(DEVMODE, sourcemaps.init()))
    .pipe(sass({
      includePaths: ['node_modules']
    }).on('error', sass.logError))
    .pipe(gulpif(DEVMODE, sourcemaps.write(), cssminifi()))
    .pipe(dest(paths.css.dest));
}

function clean_js() {
  /* Clean all scripts in dest dir */
  return src(paths.js.dest + '/*', {read: false})
    .pipe(cls());
}

function clean_css() {
  /* Clean all styles in dest dir */
  return src(paths.css.dest + '/*', {read: false})
    .pipe(cls())
}

function dev_build(){
  DEVMODE = true;
  build_scripts();
  build_styles();
}

exports.build = function() {
  clean_css();
  clean_js();
  build_scripts();
  build_styles();
};

exports.default = function() {
  dev_build();
  watch(paths.js.watch, build_scripts);
  watch(paths.css.watch, build_styles);
};
