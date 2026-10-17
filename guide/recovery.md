# Recover without making the problem larger

**Use when:** a button does nothing, a value does not update, the agent repeats failed fixes, or a change needs to be undone. First establish what is true now.

## Reproduce before another patch

Record the starting state, exact actions, expected result, actual result, environment, and revision. Before clicking, establish the [effective backend and safe test setup](verification.md#before-an-interaction-check); a local URL does not prove isolated data. Automate a reported runtime regression with a real browser or equivalent user interaction in that setup. If access or side effects are unresolved, start with code/log inspection and prepare the reproduction without executing it. A reliable reproduction gives each attempted fix a clear test.

```text
The owner filter appears to change, but the visible rows stay the same.
Reproduce with two owners using test data. Inspect the UI event, selected
state, request parameters, response, and rendered rows. State the first
boundary where expected and actual behavior diverge. Fix that cause,
then rerun the original behavior and reset/empty-state cases. Keep a
reusable runtime check. Pause unrelated feature work until it passes.
```

## Follow the data across the seam

| Observation | Inspect next | Avoid assuming |
| --- | --- | --- |
| Clicking has no visible effect | Event handler, disabled state, validation, console | The API is broken |
| Request succeeds; UI is stale | Response shape, state update, cache invalidation, rendering | A successful response proves the feature works |
| UI updates; refresh loses the change | Persistence write, save failure, read source | The local state was saved |
| Local works; preview/live fails | Deployed revision, config names, origins, service permissions | The environments are equivalent |
| Auth works only in an old session | Cookies/storage, expiry, redirects, fresh login | The login flow was tested |
| One agent works; another cannot | Workspace root, instructions, environment, tool access | The second model is weaker |
| Test hangs or fails without code evidence | Process health, resource limits, dependency/service state | Every failure is an application bug |

Inspect secret *presence and configuration names* without printing values. Use logs that expose the failing boundary while protecting user data. Change one plausible cause at a time and rerun the same reproduction. A large patch that happens to make the symptom disappear is harder to trust and recover.

## Know what undo can restore

For unexpected external actions, stop the job and revoke affected access through the [agreed route](advanced.md#add-tools-with-a-job-and-a-boundary), then inspect what already happened. Restoring files alone does not contain an active connection.

Before restoring anything, preserve work that must survive and identify the state you changed:

- **Files:** inspect the diff and choose the intended commit, branch, or checkpoint.
- **Conversation/instructions:** a file restore may leave a chat that describes changes no longer present.
- **Data:** restoring code does not necessarily restore database rows or schema.
- **Deployment/configuration:** a rollback may leave environment settings or connected services unchanged.
- **External effects:** sent messages, payments, created tickets, and published content need their own correction paths.

Product semantics differ. Cursor's documented checkpoint restores files while retaining the conversation; Replit's database recovery has separate conditions. See the precise, dated [platform notes](platforms.md). Git history is useful for files; it is not a transaction log for every connected system.

For data changes, agree the backup, migration recovery, and responsible owner before execution. After any restore, run the original behavior again and inspect the state you intended to recover. A successful rollback notification is not proof that all effects were reversed.

## Stop a loop deliberately

If repeated edits produce no new evidence, stop changing code. List what is known, hypotheses ruled out, the smallest remaining reproduction, and the next diagnostic check. Ask for missing context or involve the owner of the failing system when access or domain knowledge is the blocker.

Start a fresh session from a [handoff](../templates/handoff.md) when the conversation is misleading or overloaded. Preserve the reproduction and exact evidence. Do not erase the work history or discard unrelated changes to make the session feel clean.

**Done means:** the original failure no longer reproduces, nearby behavior still holds, the regression check can be rerun, and any remaining environment or live verification gap is explicit.
