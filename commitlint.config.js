export default {
  extends: ['@commitlint/config-conventional'],

  ignores: [(commit) => /[ci skip]/i.test(commit), (commit) => /[skip ci]/i.test(commit)],
};
