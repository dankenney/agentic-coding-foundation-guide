# Debugging and recovery

When a button does nothing, a value won't update, or the agent keeps trying fixes that don't work, pause and reproduce the problem. If you need to undo a change, first check which parts of the system it affected.

## Reproduce before another patch

Record the starting state, exact actions, expected and actual results, environment, and revision. Before clicking, confirm the [effective backend and safe test setup](verification.md#before-an-interaction-check). A local URL can still use shared or production data. Automate a reported runtime regression with a real browser or equivalent user interaction in that setup. If access or side effects remain unresolved, inspect the code and logs and prepare the reproduction without running it. Once you can reproduce the failure reliably, you can check each attempted fix against it.

```text
The owner filter appears to change, but the visible rows stay the same.
Reproduce with two owners using test data. Inspect the UI event, selected
state, request parameters, response, and rendered rows. State the first
boundary where expected and actual behavior diverge. Fix that cause,
then rerun the original behavior and reset/empty-state cases. Keep a
reusable runtime check. Pause unrelated feature work until it passes.
```

## Find where the behavior breaks

| Observation | Inspect next | Avoid assuming |
| --- | --- | --- |
| Clicking has no visible effect | Event handler, disabled state, validation, console | The API is broken |
| Request succeeds; UI is stale | Response shape, state update, cache invalidation, rendering | A successful response proves the feature works |
| UI updates; refresh loses the change | Persistence write, save failure, read source | The local state was saved |
| Local works; preview/live fails | Deployed revision, config names, origins, service permissions | The environments are equivalent |
| Auth works only in an old session | Cookies/storage, expiry, redirects, fresh login | The login flow was tested |
| One agent works; another cannot | Workspace root, instructions, environment, tool access | The second model is weaker |
| Test hangs or fails without code evidence | Process health, resource limits, dependency/service state | Every failure is an application bug |

Check whether secrets are present and which configuration names the app uses, without printing secret values. Use logs that help locate the failure while protecting user data. Change one plausible cause at a time and rerun the same reproduction. If a large patch makes the symptom disappear, you'll have more work to establish which change fixed it and what to undo if it returns.

## Know what undo can restore

If an agent takes an unexpected external action, stop the job and revoke the affected access through the [agreed route](advanced.md#connect-a-service-for-a-specific-task). Then check what already happened. You'll need to address an active connection even if you restore the files.

Before restoring anything, preserve work you need to keep and identify what changed:

- **Files:** inspect the diff and choose the intended commit, branch, or checkpoint.
- **Conversation/instructions:** a file restore may leave a chat that describes changes no longer present.
- **Data:** restoring code does not necessarily restore database rows or schema.
- **Deployment/configuration:** a rollback may leave environment settings or connected services unchanged.
- **External effects:** sent messages, payments, created tickets, and published content need their own correction paths.

Check the product's restore behavior before relying on it. Cursor's documented checkpoint restores files while retaining the conversation; Replit's database recovery has separate conditions. The dated [platform notes](platforms.md) give the details. Git history can help recover files, but it doesn't record every change in connected systems.

Before changing data, agree on the backup, migration recovery, and responsible owner. After any restore, rerun the original behavior and inspect the state you meant to recover. A rollback notification alone can't establish that every effect was reversed.

## When repeated fixes aren't helping

If repeated edits produce no new evidence, stop changing code. Write down what you know, which hypotheses you've ruled out, the smallest remaining reproduction, and the next check that could narrow the problem. Ask for missing context or involve the system's owner when access or domain knowledge is blocking you.

When the conversation has become misleading or overloaded, use a [handoff](../templates/handoff.md) to start a fresh session. Keep the reproduction and exact evidence, along with the work history and unrelated changes you'll still need.

Before calling the fix complete, confirm the original failure no longer reproduces and nearby behavior still works. Make sure someone else can rerun the regression check, and report any checks you couldn't complete in the intended environment or on the live version.
