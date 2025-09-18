import js from "@eslint/js";
import globals from "globals";
import jest from "eslint-plugin-jest";

export default [
  { 
    files: ["**/*.{js,mjs,cjs}"],
    plugins: { 
      js 
    },
    languageOptions: { 
      globals: globals.node 
    },
    rules: {
      ...js.configs.recommended.rules
    }
  },

  {
    files: ['**/*.test.js'],
    plugins: {
      jest,
    },
    ...jest.configs['flat/recommended'],
    rules: {
      ...jest.configs['flat/recommended'].rules,
    }
  }
];
