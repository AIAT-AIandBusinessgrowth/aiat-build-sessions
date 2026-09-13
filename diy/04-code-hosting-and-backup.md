# Code hosting and backup

Save a second copy of your app’s code, then open it and check your latest change. A repository is a project folder whose changes Git records. If your builder already connects to GitHub, start with section 5; otherwise follow the setup below.

| | |
|---|---|
| **Prerequisites** | [Accounts and 2FA](01-accounts-and-2fa.md) |
| **Time** | ~30 min |
| **Outcome** | After this you can create a private repository with your own account, connect to it and check that your last change arrived |
| **Last verified** | 2026-09-13 |

## Why this matters

If your only copy is on one laptop or in one builder account, losing access can mean losing the project. A code host stores the files and the changes you send to it. You or your organisation arrange the account.

## Do it

### 1. Pick a code host

Check what you need before choosing a host: Are private repositories free? How many people can join a private project for free? Does it offer 2FA? Where is it hosted? Can you move your repositories elsewhere later? All of the hosts below use Git, so you can move.

| Host | Free tier (vendor statement) | Source |
|---|---|---|
| GitHub | Unlimited public and private repositories, 2,000 CI/CD minutes per month | [github.com/pricing](https://github.com/pricing) |
| GitLab.com | Up to five users in a private top-level group; 400 compute minutes per month | [free user limit](https://docs.gitlab.com/user/free_user_limit/), [compute minutes](https://docs.gitlab.com/ci/pipelines/compute_minutes/) |
| Codeberg | Free, run by the non-profit association Codeberg e.V.; expects you to put a free and open-source licence on work you publish | [Codeberg FAQ](https://docs.codeberg.org/getting-started/faq/) |
| Bitbucket | Free for up to 5 users, unlimited public and private repositories, 1 GB LFS storage, 50 build minutes | [bitbucket pricing](https://www.atlassian.com/software/bitbucket/pricing) |

All figures checked 2026-09-13. Codeberg's FAQ has its own section on private repositories: read it before you plan to keep closed work there.

You can also run your own Git server with open-source software. That means you are responsible for updates, security and backups. It is not covered here.

### 2. Create your first private repository

1. Create the account with 2FA on ([Accounts and 2FA](01-accounts-and-2fa.md)).
2. **Browser lane:** do not create a repository by hand. Your builder creates it when you connect it to GitHub (section 5).
3. **CLI lane:** decide how you start. The choice changes the steps in section 4.
   - **Variant (a), you already have a folder on your laptop**, for example `playground` from [Your first build](../tracks/01-first-build/01-your-first-build.md): create a new repository called `playground`, set it to **private**, and do **not** add a README, a licence or a `.gitignore`. The repository must be empty.
   - **Variant (b), you start with nothing on your laptop:** create a new repository called `playground`, set it to **private**, and tick "Add a README".
4. Open the repository page and find the clone URL. There are two kinds: HTTPS and SSH.

### 3. Sign in from your laptop (CLI lane)

GitHub does not accept your account password for Git over HTTPS. Its docs say: "Password-based authentication for Git has been removed in favor of more secure authentication methods" ([source](https://docs.github.com/en/get-started/git-basics/about-remote-repositories), checked 2026-09-13). Pick one of these ways.

**GitHub Desktop (easiest)**

- GitHub Desktop signs you in through the browser. It can create the repository, commit and push for you.

**HTTPS with Git Credential Manager**

- The first time you push, Git Credential Manager opens a browser sign-in and stores the result safely, so you do not sign in again. It runs on Windows, macOS and Linux ([source](https://github.com/git-ecosystem/git-credential-manager), checked 2026-09-13).

**A fine-grained personal access token (only if the two ways above do not work)**

- A token is a long secret that Git accepts instead of a password. Create a fine-grained token in your GitHub settings ([source](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens), checked 2026-09-13).
- Least privilege: give it access to the one repository it needs, and only the permissions it needs.
- Set an expiry date.
- Store it in your password manager. Paste it when Git asks for a password. Never put it in a file, a commit or a prompt.

**SSH key (more setup, no passwords afterwards)**

1. Generate a key pair on your laptop:
   ```bash
   ssh-keygen -t ed25519 -C "you@example.com"
   ```
2. Set a passphrase when asked. It protects the key if your laptop is stolen.
3. You now have two files. The one ending in `.pub` is the **public key**: copy its content into the SSH keys section of your account settings. The other file is the **private key**: it stays on your laptop, and you never paste it anywhere.
4. Follow your host's guide to test the connection. For GitHub: [Generating a new SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

### 4. Tell Git who you are, then push and check

**Once per laptop, before your first commit.** Git writes a name and an e-mail address into every commit:

```bash
git config --global user.name "Your Name"
git config --global user.email "you@example.com"
```

Anyone who can see the repository can read this address, and on a public repository that is everyone. If you do not want to show your own address, use the noreply address GitHub gives you in your e-mail settings ([source](https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address), checked 2026-09-13).

Choose the variant that matches what already exists. Do not run both. GitHub Desktop can instead add the existing local folder and **Publish repository**, with **Keep this code private** selected.

**Variant (a): an existing local app, no remote yet**

Open your app folder. If a terminal is already in `playground`, do not run `cd playground` again. Check the state:

```bash
git status --short
git remote -v
```

If Git says this is not a repository, confirm you are in the intended app folder, then run `git init`. If `origin` already has the intended URL, skip adding a remote and use `git push`. If it points somewhere unexpected, stop and check before changing it.

If you have uncommitted changes, inspect them and stage the specific files. This example is for the single-file first build; substitute the filenames you reviewed:

```bash
git diff -- index.html
git add index.html
git diff --cached
git commit -m "feat: save first working app"
```

Also commit your reviewed project instructions and `.gitignore` by filename if they exist. Never stage `.env` or credentials. If `git status` is clean and a commit already exists, skip this commit step.

Only when there is **no origin**, connect the empty private repository you created in section 2. Create one now only if you have not already done so. Copy its URL, replacing `<your-user>` below. In this new practice project:

```bash
git remote add origin https://github.com/<your-user>/playground.git
git branch -M main
git push -u origin main
```

**Variant (b): a repository on the host, no local folder yet**

From a parent folder with no existing `playground` subfolder:

```bash
git clone https://github.com/<your-user>/playground.git
cd playground
```

A clone already knows where to push. After a change, inspect `git status --short` and `git diff`, stage the filenames you reviewed, commit, then run `git push`. Do not run `git remote add origin` again.

**If the push is rejected**

- Do not use `git push --force` to get past a rejection. It can replace the shared history and make other people’s work difficult to recover.
- If you created the repository with a README by mistake and have a folder on your laptop: clone the repository into a new folder (variant b), copy your files into it, then commit and push from there.
- If you pushed from another computer before: first save your local work, then try `git pull --ff-only`. If it reports divergent history, ask for a merge/rebase explanation and inspect both histories; do not force-push.
- Paste the error text into your agent and ask what it means. Do not paste tokens or keys with it.

Then open the repository page in the browser and check that your last change is there. This confirms that the change reached the code host. It does not check your database, uploaded files or other backups.

### 5. Connect a browser builder (browser lane)

Most app builders offer a GitHub connection or a ZIP export. Connect it, make a change in the builder, and check that a new commit shows up in your repository. See the [tool matrix](tool-matrix-2026-09.md) for which builder exports how.

## Done when

- [ ] I have an account on a code host, with 2FA on.
- [ ] I have a private repository called `playground`.
- [ ] I pushed a change, or my builder synced one.
- [ ] I opened the repository page and saw that change.

## Watch out

- **A remote is not a backup of everything.** Your repository holds code. It does not hold your database content, uploaded files, environment variables set on a hosting platform, or your chat history with the builder. Read [Keep your work safe](../tracks/06-keep-and-ship/01-keep-your-work-safe.md).
- Never commit `.env` files or keys. See [Secrets and keys](07-secrets-and-keys.md).
- Private means private to you and the people you invite. Public means anyone on the internet, including search engines and bots.
- On GitHub Free, GitHub Pages works only from public repositories ([source](https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits), checked 2026-09-13).

## Sources

- GitHub pricing: https://github.com/pricing (checked 2026-09-13)
- GitHub's plans: https://docs.github.com/en/get-started/learning-about-github/githubs-plans (checked 2026-09-13)
- GitHub Pages limits: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits (checked 2026-09-13)
- GitHub, Generating a new SSH key: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent (checked 2026-09-13)
- GitHub, About remote repositories (no password authentication for Git): https://docs.github.com/en/get-started/git-basics/about-remote-repositories (checked 2026-09-13)
- GitHub, Managing your personal access tokens: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens (checked 2026-09-13)
- GitHub, Setting your commit email address (noreply address): https://docs.github.com/en/account-and-profile/how-tos/email-preferences/setting-your-commit-email-address (checked 2026-09-13)
- Git Credential Manager: https://github.com/git-ecosystem/git-credential-manager (checked 2026-09-13)
- GitLab, Free user limit: https://docs.gitlab.com/user/free_user_limit/ (checked 2026-09-13)
- GitLab, Compute minutes: https://docs.gitlab.com/ci/pipelines/compute_minutes/ (checked 2026-09-13)
- Codeberg FAQ: https://docs.codeberg.org/getting-started/faq/ (checked 2026-09-13)
- Bitbucket pricing: https://www.atlassian.com/software/bitbucket/pricing (checked 2026-09-13)
