import { eslintConfig as typescript } from '@gewis/eslint-config-typescript';
import { eslintConfig as react } from '@gewis/eslint-config-react';
import { eslintConfig as prettier } from '@gewis/prettier-config';

export default [...typescript, ...react, prettier];
