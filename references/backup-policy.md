# Backup policy and execution

Read when defining/changing a policy or executing its backup/restore procedure. Normal resume needs only the recorded project policy. Ask the user to choose a method after explaining project-specific coverage. Never silently substitute a method.

## Offer a concrete choice

| Choice | Coverage and tradeoff |
| --- | --- |
| Local snapshot/archive | Can capture selected source, documents, and untracked assets quickly; a copy on the same disk does not cover disk failure. Choose an approved destination outside the source tree. |
| Git checkpoints | Efficient versioned history of committed content; uncommitted, untracked, ignored, external data, and live databases require separate coverage. A local repository does not cover device loss. |
| Hybrid | Git for source/history plus local or separately stored snapshots/data exports for gaps; more coverage with additional storage and maintenance. |
| Existing/custom service | Reuse a verified filesystem snapshot, backup service, private remote, or database-native backup; document actual recovery coverage and authority. Sync alone may propagate deletions. |
| Explicitly declined | Record the user's choice and concrete exposure; do not pretend recovery exists or repeatedly ask for the same approval. Other applicable safety requirements still apply. |

Do not assume cloud upload, remote creation, scheduling, Git commits, pruning, or live-data access is authorized by choosing a label. Agree on the relevant operations as part of the concrete policy. Persist decisions so routine execution within that scope does not require repeated questions.

## Minimum usable policy

For an explicit opt-out, record only the decision/date and concrete recovery exposure in 1-2 lines; omit unused policy fields. For an active policy, record method; source and coverage; destination/provider and access; exclusions; triggers; retention; allowed local/commit/remote actions; verification; safe restore procedure; and failure behavior. Explicitly identify secrets, databases, uploads/user files, external services, Git LFS/submodules, or ignored/untracked assets when present. Do not collect credentials in documentation.

Choose triggers proportional to recovery cost: an existing-project baseline before modifying it, meaningful milestones, and before disruptive refactors, migrations, deletions, or dependency/toolchain changes. Do not archive the entire project after every read or keystroke. Scheduled execution requires a real configured scheduler and user authority; recording a frequency is not creating an automation.

Retention defines desired count/age and separately whether pruning is authorized. Never delete old backups solely because a suggested retention field exists. Keep at least a verified recovery point until a new one is verified. Use UTC or an explicit offset in timestamps; select unique names so a prior snapshot is not overwritten.

## Local snapshots

1. Inspect and resolve absolute source and destination paths. Ensure the destination is outside the source and that enumeration will not recurse through the backup itself or follow unexpected links/junctions outside scope. On Windows, use one shell for filesystem operations and literal paths.
2. Establish an explicit file inventory. Include relevant untracked work and existing project documentation. Exclude regenerable dependencies, caches, builds, and temporary output; handle `.git` intentionally. State how ignored but important assets are covered.
3. Exclude secrets unless secure backup of them is explicitly required and the destination/access/encryption is approved. State the resulting restore limitation. Never publish raw `.env`, keys, credentials, or sensitive records to a repository or ordinary shared archive.
4. Copy/archive to a new destination. Check actual success, inventory/counts, and readability; use a checksum manifest where appropriate. A successfully created empty ZIP is not evidence of coverage. For active files/data, use a consistent snapshot/quiescence or supported export; do not treat a live database file copy as a verified recoverable backup.
5. Record the artifact path/ID, time, coverage/exclusions, verification, and restore instructions in PROJECT_STATUS.md. Keep large manifests/logs out of Markdown and ordinary context. Record restore confidence honestly: inventory checked, extraction checked, or actual restore tested.

## Git checkpoints

Inspect repository root, branch, status including untracked files, ignored important assets, and staged content. Avoid `git add .` or `git add -A` when they could include unrelated work or secrets. Stage only authorized files; preserve existing staging and do not include the user's unrelated staged work in a checkpoint. If isolation is unclear, ask or use an approved local snapshot of the worktree instead.

Do not initialize/reconfigure a repository, change remotes, commit unrelated changes, reset, clean, stash, rewrite history, or force-push as a backup shortcut. Commit only under recorded commit authority; remote writes need an approved destination and upload authority. Record the actual commit ID and covered paths. Checkpoint references protect only included content; cover gaps by the chosen supplementary method. If using a remote as recovery, record upload result separately from local commit success.

## Data, restore, and failures

For database-backed projects, use a supported consistent backup/export procedure appropriate to the datastore. Record schema/migration version, data scope, media/uploads, encryption/access requirements, and the matching restoration procedure. Source code rollback does not reverse a data migration.

Restore into a separate temporary location first when possible; inspect content and relevant checks before proposing replacement of working files. Actual restoration over current work is a separate consequential action requiring applicable user authority and protection of the current state. Never auto-run a destructive restore command just to test the backup.

On failure, preserve partial diagnostic evidence, report the concrete error and lost coverage, and retry only a bounded safe correction (normally once). If protection is required by the agreed policy, pause dependent mutations and offer a concrete alternative. Continue independent safe work; do not mark the backup complete or silently downgrade the policy.
