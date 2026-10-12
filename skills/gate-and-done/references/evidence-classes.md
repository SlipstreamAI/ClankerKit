# Evidence classes

Use these names so handoffs compare across reviews.

| Class | What it is | Enough for |
| --- | --- | --- |
| synthetic | Mocks, stubs, or a harness that replaces the boundary | A lead only. Not enough for a runtime-visible claim. |
| targeted | A test that exercises the real unit or module without replacing the claim | Internal-only claims. |
| runtime-relevant | A path a real caller can hit: UI, API, CLI, job, or deployed preview | Runtime-visible claims. |
| failure-mode | The same path when a dependency fails, input is empty, or auth is missing | Boundary-sensitive claims. |

Downgrade when the class is missing. Security-sensitive claims do not pass on synthetic evidence alone.
