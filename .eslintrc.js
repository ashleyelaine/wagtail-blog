module.exports = {
  extends: ['eslint:recommended', 'google'],
  env: {
    browser: true,
    jasmine: true,
    node: true,
  },
  parserOptions: {
    ecmaVersion: 6
  },
  rules: {
    'camelcase': 0,
    'max-len': 0,
    'no-console': 'off',
    'no-multi-spaces': 0,
    'no-use-before-define': 2,
    'no-var': 0,
    'no-warning-comments': 0,
    'one-var': 0,
    'require-jsdoc': 0,
    'valid-jsdoc': 0,
    'no-undef': 0,
  },
};
