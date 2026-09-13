# Accounts and two-factor authentication

| | |
|---|---|
| **Prerequisites** | None |
| **Time** | ~30 min |
| **Outcome** | After this you can sign in to every tool with your own account, protected by a password manager and a second factor |
| **Last verified** | 2026-09-13 |

## Why this matters

Every tool in this material hangs off an e-mail address. Whoever controls that mailbox can reset your passwords, so it has to be yours alone. You set up these accounts yourself. Nobody creates or manages them for you, and if you attend a session, the session host does not either. That is on purpose: the accounts, and everything you build with them, stay with you.

A shared login also means shared history. If three people use one account, nobody can tell who asked the agent to do what.

## Do it

### 1. One e-mail account that is yours

- Use a personal mailbox that only you can read. Not a team inbox, not a shared family account.
- If you want to use your work address for tools, ask your employer first. Some organisations do not allow it, and they decide.
- Before you use a personal AI account for work, or install a tool on a work laptop, check your employer's IT rules.

### 2. A password manager

- Pick one: the one built into your operating system or browser, or a separate app. Criteria before brands: Does it sync across your devices? Can you export your data? Does it support passkeys and one-time codes?
- A separate app may need to be installed. If you cannot install software on your laptop, use the password manager built into your browser, a browser extension, or a phone app.
- Let it generate a long, unique password for every tool. Never reuse a password.

### 3. Two-factor authentication (2FA) with an authenticator app

1. Install an authenticator app on your phone (any app that shows six-digit time-based codes works). An authenticator app needs a smartphone. Without one, use a passkey (step 4) or a password manager that can show one-time codes.
2. Turn on 2FA for your e-mail account first, then for GitHub or your code host, then for each AI tool that offers it.
3. Choose "authenticator app" when you have the choice. Text messages (SMS) are a weaker second factor.
4. Save the recovery codes in your password manager. Without them, a lost phone can mean a lost account.

### 4. A passkey as a backup

A passkey lets you sign in with your device (fingerprint, face or device PIN) instead of a password. GitHub lists passkeys as a sign-in method on GitHub Free ([source](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github), checked 2026-09-13). Add one where a tool offers it, and keep the authenticator app as well.

### 5. GitHub: 2FA is mandatory for contributors

Since March 2023, GitHub requires users who contribute code on GitHub.com to enable 2FA. If your account is selected, you get a 45-day setup period, then a 7-day grace period. After that you cannot use GitHub.com until you turn 2FA on ([source](https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication), checked 2026-09-13). Do not wait for the reminder: turn it on the day you create the account.

## Done when

- [ ] I have an e-mail account that only I can read.
- [ ] My passwords live in a password manager, one unique password per tool.
- [ ] 2FA with an authenticator app is on for my e-mail account.
- [ ] 2FA is on for GitHub (or my code host) and for every AI tool that offers it.
- [ ] My recovery codes are saved in the password manager.
- [ ] I added a passkey where the tool offers one.

## Watch out

- "Sign in with Google" or "Sign in with GitHub" moves all the risk to that one account. That is fine if that account has 2FA, and bad if it does not.
- Never share a login with a colleague, not even for a quick test. Invite them to the project instead, if the tool allows it.
- A new phone: move your authenticator codes before you wipe the old one.

## Sources

- GitHub, About mandatory two-factor authentication: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication (checked 2026-09-13)
- GitHub, About authentication to GitHub (passkeys): https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github (checked 2026-09-13)
- GitHub, About passkeys: https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys (checked 2026-09-13)
