# Protecting secrets locally

**Purpose:** Keep secrets (API keys, tokens, local paths, credentials) out of the repo and off remotes. This file is for humans and agents: follow it so nothing sensitive gets committed or pushed.

---

## Do

- **Use environment variables** for keys and secrets. In code or scripts, read from `process.env`, `os.environ`, or your shell config; never hardcode.
- **Use a local-only file** that is **not** committed. Examples:
  - **.env** (already in .gitignore in this repo) — load with your app or a dotenv helper; never commit.
  - **.episteme-local/** — in .gitignore; put local config or override files here; do not commit.
- **Add new secret files or dirs to .gitignore** before creating them, so they never get staged by mistake.
- **Review before push:** Run `git status` and `git diff --staged`; if you see .env, .episteme-local, or any file that might contain secrets, unstage and add to .gitignore.

---

## Do not

- **Do not** put API keys, passwords, tokens, or credentials in any file that is tracked by git.
- **Do not** commit **.env**, **.env.local**, or similar. This repo’s .gitignore already excludes `.env` and `.episteme-local/`; keep that.
- **Do not** paste secrets into agent docs, READMEs, or example configs that get committed. Use placeholders (e.g. `YOUR_API_KEY`, `https://your-canonical-repo`) and document “set locally.”

---

## If something secret was committed

1. **Do not push** if you haven’t yet. Remove the file from the index (`git rm --cached <file>`), add it to .gitignore, then commit the .gitignore change. Rewrite the secret if it was already in history.
2. **If already pushed:** Rotate the secret immediately (revoke and issue a new key). Consider history rewrite (e.g. `git filter-branch` or BFG) only if the repo is private and you understand the impact; otherwise rotation is the safe default.

---

## Checklist for agents

When creating or editing config or docs that might reference secrets: (1) Use placeholders, not real values. (2) Mention that the user should set env vars or a local file. (3) Point here (SECRETS.md) so the user knows how to protect them.
