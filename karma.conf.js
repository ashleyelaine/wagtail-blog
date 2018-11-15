// Karma configuration
// Generated on Wed Jan 18 2017 13:55:48 GMT-0600 (CST)

module.exports = function(config) {
  config.set({

    basePath: '',

    frameworks: ['browserify', 'jasmine'],

    /*
      the code needed to run the tests.
      e.g. app code, test files, sometimes a framework
    */
    files: [
      'assets/js/*.js',
      'assets/js/tests/*.spec.js'
    ],

    exclude: [
    ],

    preprocessors: {
      'assets/js/*.js': ['browserify'],
      'assets/js/tests/*.spec.js': ['browserify']
    },

    reporters: ['dots'],

    port: 9876,

    colors: true,

    logLevel: config.LOG_INFO,

    autoWatch: false,

    /*
      karma will automatically look for and load npm packages that
      start with karma. e.g. karma-istanbul. but sometimes
      you will want to list them explicitly here
    */
    //plugins: [],

    browsers: ['PhantomJS'],

    singleRun: false,

    concurrency: Infinity
  })
}
