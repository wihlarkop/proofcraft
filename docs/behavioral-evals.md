# Behavioral evals

Static validation checks skill structure, reference links and generated freshness. It does not run models or prove skill behavior. Behavioral evals are optional contributor tooling: Python prepares disposable projects and Promptfoo owns model execution, grading, traces, results and the viewer. No Node dependency is added to building, validating, installing or using distributed skills.

## Requirements and authentication

- Python 3.12+, Git, and **Node >=22.22.0** with `npx` for behavioral commands (Node 24 LTS recommended).
- **Promptfoo 0.123.1** and **Codex SDK 0.159.3**, invoked as pinned `npx --package` packages. The npm registry versions were checked on 2026-10-02. First use downloads into npm's normal cache; nothing is cloned or vendored. This is smaller than a dev package manifest/lockfile, though transitive dependencies are not locked.
- Sign in with `codex login` (PowerShell: `codex.cmd login`). With `apiKey`, `OPENAI_API_KEY` and `CODEX_API_KEY` unset, the provider reuses the existing Codex/ChatGPT login. The wrapper never reads, copies, writes or embeds credentials, and leaves `CODEX_HOME` unchanged. If either API-key environment variable is set, Promptfoo may use it instead. Runs consume the chosen account's allowance; graders also call a model.

The default model is `gpt-5.5` with medium reasoning for both target and rubric grader. Use `--model` to select another model available to your account. Model availability depends on sign-in/account, not just the SDK catalog; a documented model can still be unavailable to a particular ChatGPT login. Personal Codex configuration/user-level skills may still affect runs because login reuse keeps the existing Codex home; inspect traces for contamination. Fixture-local guidance limits project context, but does not claim complete harness isolation.

## Commands (also work from PowerShell)

```text
python scripts/eval.py shape
python scripts/eval.py improve
python scripts/eval.py --all
python scripts/eval.py shape --filter recommend-clear-next-feature
python scripts/eval.py --all --validate
python scripts/eval.py shape --prepare-only
python scripts/eval.py --view
```

`--all` means all **migrated** cases, not the entire skill-local or suite eval collection. `--filter` matches a substring of `skill:scenario-id` before setup. `--validate` invokes Promptfoo's native config validator without model calls; `--prepare-only` needs neither Node nor authentication. The wrapper validates config before every eval and propagates Promptfoo's exit status. Evaluation uses `--no-cache --no-share` for fresh local evidence.

For this pinned version/configuration, **do not use native `eval --resume`**: an interrupted run's saved per-test provider filters were lost on resume, expanding ten intended calls into a 100-call matrix. Start a fresh wrapper run, selecting a remaining case with `--filter` when useful. The wrapper intentionally has no resume option. Keep this limitation until an upstream fix is verified; no local scheduler or metadata adapter works around it.

The underlying command is:

```text
npx --yes --package=promptfoo@0.123.1 --package=@openai/codex-sdk@0.159.3 promptfoo eval -c <generated-config> --no-cache --no-share -o <results.json>
```

On Windows the wrapper locates `npx.cmd`, avoiding PowerShell script-signature restrictions. Promptfoo's native viewer is launched with the same repository-local state directory. To inspect a generated config directly, set `PROMPTFOO_CONFIG_DIR` to the absolute `.eval-workspace/promptfoo/state` path before invoking the pinned CLI.

## Workspaces, assertions and evidence

Each invocation retains an ignored `.eval-workspace/promptfoo/run-*/` directory containing the built distribution, generated `promptfooconfig.json`, independent fixture repositories, Promptfoo `results.json`, and before/after source hashes. Promptfoo history/database, traces and logs live in `.eval-workspace/promptfoo/state/`; npm packages stay in npm's cache and Codex session state stays in its normal home. These files may contain model outputs, inspected fixture content and local paths. They are local, ignored artifacts, not release inputs.

The current distribution is built from `src/` into the run directory; checked-in `skills/` is untouched. Each fixture receives ordinary copies of the generated shape, improve, debug, continue, implement, architect and performance-engineering skills in `.agents/skills/`. No duplicate skill text is maintained. A fixture's own Git root and `AGENTS.md` stop parent-project context discovery. Every scenario/variant has a separate fixture.

The target provider is `openai:codex-sdk`, with explicit absolute `working_dir`, `approval_policy: never`, network/search disabled, streaming and deep tracing enabled, no thread persistence, no extra writable directories, minimal environment inheritance and subagents disabled. All initial reasoning/control cases use `sandbox_mode: read-only`. **`recommend-control-spec-request` uses `workspace-write`** because its original expected outcome requires recording a spec; only its disposable fixture is writable. No probe runs with the Proofcraft checkout as its working directory. Before/after hashes cover tracked and nonignored new repository files, preserve preexisting dirty work, and fail the command if files change; they detect changes rather than automatically restoring them. Avoid editing source during a run.

Deterministic assertions check skill reads, key observable output and the requested spec artifact. Model grading is reserved for semantic behavior: supported advice versus speculation, honoring deferrals/non-goals, mode transitions and preservation/escalation judgments. Rubrics retain each selected scenario's full canonical expected outcome and include the original request/evidence for judging grounding. The grader is explicitly another read-only Codex provider in an empty fixture, so grading also supports ChatGPT login without an API key.

Codex `skill-used` / `not-skill-used` are **heuristics**, based on successful direct `SKILL.md` command reads, not first-class invocation events. Wildcard reads are not reliable invocation proof. In the pinned provider, leading `./` and doubled Windows separators can also hide successful reads; fixture guidance requests direct forward-slash skill paths and UTF-8 reads. It does not select a skill or mode, and no metadata adapter is added. Open results in the native viewer and inspect final output, rubric reason, `metadata.skillCalls` (`source: heuristic`), session IDs and command/file trajectory spans. A routing assertion passing does not prove the correct shape mode; the separate semantic rubric checks that. The deferred-opportunities case also requires a traced shape instruction read. MCP/search/file traces are supported by upstream, but these fixtures need no external MCP or search tools.

## Initial coverage and comparison

Selected existing shape cases: `recommend-documented-deferred-opportunities`, `recommend-clear-next-feature`, `recommend-generic-feature-pressure`, `recommend-insufficient-repository-evidence`, `recommend-human-selection-to-shape`, `recommend-control-normal-shape`, and `recommend-control-spec-request`.

Selected existing improve cases: `leave-good-code-alone`, `architecture-escalation`, and `performance-needs-evidence`. These intentionally exercise reasoning/preservation boundaries; write-capable refactoring and the rest of the routing suite remain future coverage. Fixtures are small capability/code snapshots, not full application/runtime acceptance evidence.

Comparison accepts a **previously built distribution directory**, containing the same seven catalog skills:

```text
python scripts/eval.py shape --baseline C:/path/to/previous-checkout/skills
```

Build that baseline from its own canonical source first using its `scripts/build.py`, or use a trustworthy released distribution. The wrapper copies it into independent fixtures and Promptfoo represents current/baseline as provider columns against the same cases and assertions. Use the same model/auth/configuration and inspect evidence in both columns. This does not resolve Git refs, create worktrees or automatically extract previous-main skills; robust Git baseline materialization and broader routing/refactoring coverage are the next increments. No paid/model CI execution is added.

Add bounded selections/assertions under `evals/behavioral/` and fixtures under its `fixtures/` directory. Keep prompts/expected outcomes in canonical skill-local eval files. Do not hand-edit generated config or weaken a canonical outcome to make a model pass.

Behavioral cases are strongest when grounded in real historical failures, regressions, or difficult decisions. When a meaningful prior baseline exists, comparison can establish whether a scenario distinguishes the behavior it claims to protect. Baseline separation is evidence, not a target to game: do not weaken assertions or expected outcomes merely to make an older baseline fail.

A baseline passing a case is not automatically wrong; a whole suite unable to distinguish protected behavior may indicate weak scenarios.

## Static and setup checks

```text
python scripts/build.py
python scripts/validate.py
python scripts/check_generated.py
python -m unittest discover -s tests -p test_eval_runner.py
git diff --check
```

Setup tests need only Python and Git. They check comparison isolation, selection, canonical prompt/rubric preservation and missing baseline failures; behavioral model calls remain separate.

Primary references: [Codex provider](https://www.promptfoo.dev/docs/providers/openai-codex-sdk/), [agent skill testing](https://www.promptfoo.dev/docs/guides/test-agent-skills/), [test/provider filtering](https://www.promptfoo.dev/docs/configuration/test-cases/), [CLI and state](https://www.promptfoo.dev/docs/usage/command-line/), and [published package metadata](https://registry.npmjs.org/promptfoo/0.123.1).
