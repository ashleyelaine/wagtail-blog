module.exports = {
  // Browser-sync configs
  browsersync: {
    proxy: 'localhost:8000',
    xip: false
  },

  // gulp-using - Files logger so easier to debug stuff later
  using_opts: {
    prefix: 'Compiling...',
    path: 'relative',
    color: 'green',
    filesize: true
  },

  gulpfile: './gulpfile.js',

  /* ------ ASSETS SOURCE ------ */

  paths: {

    root_dest: './static',

    fonts_vendor: [
      'node_modules/bootstrap/assets/fonts/bootstrap/*',
      'node_modules/font-awesome/fonts/*',
    ],
    fonts_src: [
      'assets/fonts/**/*',
    ],
    fonts_watch: ['assets/fonts'],
    fonts_dest: './static/fonts',

    html_src: ['**/templates/**/*.html'],
    html_watch: ['**/templates/**/*.html'],

    images_src: ['./assets/images/**/*'],
    images_watch: ['./assets/images/**/*'],
    images_dest: './static/images',

    scripts_vendor: [
      'node_modules/jquery/dist/jquery.min.js',
      'node_modules/popper.js/dist/umd/popper.js',
      'node_modules/bootstrap/dist/js/bootstrap.min.js',
    ],
    scripts_src: [
      './assets/js/**/*.js',
    ],
    scripts_watch: ['assets/js/**/*.js'],
    scripts_out: 'app.js',
    scripts_dest: './static',

    scss_vendor: [
      'node_modules/bootstrap/scss/bootstrap.scss',
    ],
    scss_src: [
      './assets/scss/**/*.scss',
    ],
    scss_watch: ['assets/scss/**/*.scss'],
    scss_out: 'app.css',
    scss_dest: './static'
  },
};
