# Secrets and keys

| | |
|---|---|
| **Prerequisites** | [Code hosting and backup](04-code-hosting-and-backup.md) |
| **Time** | ~20 min |
| **Outcome** | After this you can keep API keys out of your code, your repository and your prompts, and you know what to do when one leaks |
| **Last verified** | 2026-09-13 |

## Why this matters

An API key is a password that spends money. Whoever has it can use your account and your quota. Agents write code fast, and they write keys into files if you let them. Once a key is in a public repository or a prompt, you no longer control who has seen it.

## Do it

### 1. Keep keys in a `.env` file

1. In your project folder, create a file called `.env`:
   ```
   PAYMENT_API_KEY=paste-the-real-key-here
   ```
2. Add `.env` to `.gitignore` **before** your first commit:
   ```
   .env
   .env.*
   !.env.example
   ```
3. Create `.env.example` with the same names and fake values, and commit that one:
   ```
   PAYMENT_API_KEY=your-key-here
   ```
4. Your code reads the value from the environment, it never contains the key itself.
5. Check with `git status` that `.env` does not show up as a file to commit.

Tell your agent the rule in plain words: "Read API keys from environment variables. Never write a key into a source file."

### 2. Use the platform's environment variables when you deploy

Hosting platforms have a settings page called "Environment variables" or similar. Put the key there, not in the code. See [Deploy and share](05-deploy-and-share.md).

Anything that runs in the browser is public. A key in front-end JavaScript can be read by every visitor. Keys belong on the server side.

### 3. Know what GitHub does for you, and what it does not

- **Secret scanning** runs automatically and for free on public repositories. For organisation-owned private repositories it needs GitHub Secret Protection on GitHub Team or GitHub Enterprise Cloud, which is paid ([source](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning), checked 2026-09-13).
- **Push protection for users** is enabled by default and stops you from pushing secrets to public repositories on GitHub ([source](https://docs.github.com/en/code-security/concepts/secret-security/push-protection), checked 2026-09-13).
- In a private repository on a free plan, you are the only safety net. Keep `.gitignore` right.

### 4. If a key leaked

1. **Revoke or rotate the key at the provider, right now.** Log in to the provider's dashboard, delete the key, create a new one.
2. Put the new key in `.env` or the platform settings.
3. Check the provider's usage page for calls you did not make.
4. Then clean up the repository if you want to.

Deleting the commit is not enough. The key stays in the Git history, in every clone and fork, and in anything that already copied it. Only revoking makes the old key useless. More: [If something went wrong](../tracks/02-data-first/04-if-something-went-wrong.md).

### 5. Never paste keys into a prompt

What you type into an AI tool goes to the vendor. On personal plans it may be stored and, depending on your settings, used for training ([Data processing agreements](03-data-processing-agreements.md)). The agent does not need to see the key. It needs to know the name of the environment variable.

## Done when

- [ ] My project has `.env` in `.gitignore` and a committed `.env.example` with fake values.
- [ ] `git status` does not list `.env`.
- [ ] Keys for deployed apps are set in the platform's environment variables.
- [ ] I know where to revoke each key I own.
- [ ] I have never pasted a key into a prompt, or I revoked that key.

## Watch out

- Screenshots and screen shares show keys too.
- Logs and error messages can print environment variables. Check what your app logs.
- Agents sometimes "helpfully" copy a value from `.env` into a config file. Review the diff before you commit.
- A key with no spend cap is the worst kind to leak. See [Costs, limits and spend caps](06-costs-limits-spend-caps.md).

## Sources

- GitHub, About secret scanning: https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning (checked 2026-09-13)
- GitHub, About push protection: https://docs.github.com/en/code-security/concepts/secret-security/push-protection (checked 2026-09-13)
