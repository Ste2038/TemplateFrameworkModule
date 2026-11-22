# Branches, releases and PCB markings

This policy applies to TemplateFrameworkModule and every project derived from it.

## Branch policy

- `develop`: active design, prototype work, documentation and template upgrades. Feature branches may branch from develop and merge back into develop.
- `master`: reviewed release baseline. Merge production-ready work from develop, then create an immutable annotated version tag on the resulting master commit.
- Keep master as the default branch for GitHub template generation so new projects start from a released baseline. Do not perform routine development directly on master.

For this repository, v1.0 is a release of a reusable template, not certification that its blank electrical design or enclosure is ready to manufacture. In derived hardware projects, release readiness includes the electrical, fabrication and physical checks in MODULE.md.

## Start a derived project

After generating and cloning a repository, create `develop` from its initial `master` before renaming the project or designing. If its default branch is called main, rename that initial branch to master and configure the remote default branch accordingly. Do not overwrite an existing master branch.

```sh
git switch master
git switch -c develop
python3 scripts/new_module.py MyModule
```

Complete TEMPLATE_TRACKING.md using the actual source tag and source commit. Commit module setup to develop and push it with `git push -u origin develop`. For native KiCad creation, initialize Git with master as the initial branch, save the untouched generated baseline, then create develop; manually reset PCB_REVISION to a development revision because the naming script is not used.

## Prepare and publish a release

1. On develop, choose the next unused version tag. Set the project's PCB_REVISION variable to that exact tag (for example v1.0); update title/revision fields and documentation where present. The existing F.SilkS text `${PCB_REVISION}` must resolve to that value. Template releases also update TEMPLATE_VERSION; module releases preserve their separate template provenance.
2. Finish the release checklist. Run ERC/DRC and relevant exports, inspect the actual silkscreen output, and record physical/electrical tests and unresolved limitations. Commit all release changes on develop. Do not label changed prototype hardware as an older released revision.
3. Fetch the remote and ensure local master is current, the worktree is clean, and the intended tag does not exist locally or remotely. Review the diff from master to develop, including module-specific circuitry and mechanical changes.
4. Merge develop into master. Resolve any conflicts and repeat affected checks on the actual merged result before tagging. Use an annotated tag and never move a published tag.
5. Push master and the exact release tag, then synchronize develop with master and return to develop. A GitHub Release page with attached manufacturing files can be created separately when needed.

Example commands after release preparation (replace vX.Y with the intended unused tag):

```sh
git switch master
git pull --ff-only origin master
git merge --no-ff develop
# Verify the merged result before tagging.
git tag -a vX.Y -m "Release vX.Y"
git push --atomic origin master refs/tags/vX.Y
git switch develop
git merge --ff-only master
git push -u origin develop
```

If develop has advanced independently after the release merge, review and merge master normally instead of forcing a fast-forward. Never force-push to make the histories match. Before the next design edit, change PCB_REVISION to a development identifier such as v1.1-dev and document the unreleased work. The exact release tag must remain visible on the PCB silkscreen in every production export.

## Traceability

The silkscreen identifies the PCB's release in its own repository. TEMPLATE_TRACKING.md identifies the source template and its upgrades. These are independent: a module at v2.0 may still derive from template v1.0. Keep both records, the release tag, manufacturing output and validation evidence consistent. Preserve all previous published tags.
