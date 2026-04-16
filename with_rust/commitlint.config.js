const AllowedScopes = ['questions', 'utils', 'workspace'];

const Configuration = {
    parserPreset: {
        parserOpts: {
            // Match: "scope: subject"
            headerPattern: /^([\w,]+): (.+)$/,
            headerCorrespondence: ['scope', 'subject'],
        },
    },
    plugins: [
        {
            rules: {
                'multi-scope-enum': ({ header }) => {
                    const match = header.match(/^([\w,]+):/);
                    if (!match) return [false, 'Cannot parse header'];
                    const scopes = match[1].split(',').map((s) => s.trim());
                    const invalid = scopes.filter((s) => !AllowedScopes.includes(s));
                    if (invalid.length > 0) {
                        return [false, `Invalid scope(s): ${invalid.join(', ')}`];
                    }
                    return [true];
                },
            },
        },
    ],
    formatter: '@commitlint/format',
    rules: {
        'scope-empty': [2, 'never'],
        'scope-enum': [0],
        'subject-empty': [2, 'never'],
        'multi-scope-enum': [2, 'always'],
        'type-empty': [0],
        'type-enum': [0],
        'header-max-length': [2, 'always', 100],
    },
    ignores: [(commit) => commit === ''],
    defaultIgnores: true,
};

module.exports = Configuration;
