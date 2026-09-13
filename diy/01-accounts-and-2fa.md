# Accounts and two-factor authentication

Set up one account you can sign in to and recover if you lose your phone. Two-factor authentication (2FA) adds a second sign-in check, such as a code from an app. You can add other tool accounts later.

| | |
|---|---|
| **Prerequisites** | None |
| **Time** | ~30 min |
| **Outcome** | After this you can sign in to every tool with your own account, protected by a password manager and a second factor |
| **Last verified** | 2026-09-13 |

## Why this matters

Your e-mail account is often how you recover access to other tools. Protect it first, then the tool you want to use. Use your own login or the individual account your organisation provides. The course does not provide accounts.

With a shared login, people can also see one another’s history. Separate accounts make it easier to keep access and work apart.

## Do it

### 1. One e-mail account that is yours

- Use a mailbox assigned to you, rather than a shared team or family inbox. Your organisation may manage a work mailbox; follow its access rules.
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

- If you use "Sign in with Google" or "Sign in with GitHub", losing access to that account can also lock you out of connected tools. Protect that account with 2FA and save its recovery options.
- Never share a login with a colleague, not even for a quick test. Invite them to the project instead, if the tool allows it.
- A new phone: move your authenticator codes before you wipe the old one.

## Sources

- GitHub, About mandatory two-factor authentication: https://docs.github.com/en/authentication/securing-your-account-with-two-factor-authentication-2fa/about-mandatory-two-factor-authentication (checked 2026-09-13)
- GitHub, About authentication to GitHub (passkeys): https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github (checked 2026-09-13)
- GitHub, About passkeys: https://docs.github.com/en/authentication/authenticating-with-a-passkey/about-passkeys (checked 2026-09-13)
