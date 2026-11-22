# GitHub template workflow

## Source repository

The template is published at https://github.com/Ste2038/TemplateFrameworkModule with SSH remote `git@github.com:Ste2038/TemplateFrameworkModule.git`. The release branch is `master`; this release is `v1.0`. Repository administrators should enable **Settings → General → Template repository** if it is not already enabled.

Use the immutable source tag to identify the release. In a checkout of the source template, resolve its commit with:

```sh
git rev-parse 'v1.0^{commit}'
```

Verify a newly generated project's contents against the intended source release before recording its provenance; the repository's default branch may contain later changes.

Follow [RELEASE_WORKFLOW.md](RELEASE_WORKFLOW.md): develop on `develop`, merge production-ready work into `master`, and tag the master release commit. This policy is inherited by every generated project.

## Create each future module

1. Open the template on GitHub and choose **Use this template → Create a new repository**.
2. Select owner, module repository name and visibility. Use the default branch; including all branches is unnecessary for this scaffold.
3. Clone the new module repository and enter it:

```sh
git clone git@github.com:YOUR_ACCOUNT/MyModule.git
cd MyModule
git switch -c develop master
python3 scripts/new_module.py MyModule
```

4. Open MyModule.kicad_pro and update docs/MODULE.md, README.md, title blocks and revision information. Before design work, complete [TEMPLATE_TRACKING.md](TEMPLATE_TRACKING.md) with the actual source template URL, tag and full source commit SHA. The generated repository commit is not the source template commit. Follow [TEMPLATE_UPGRADES.md](TEMPLATE_UPGRADES.md) for version identification and future upgrades.
5. Review and commit the renamed files and module definition, then push develop to the new module repository with `git push -u origin develop`.

Use a filesystem-safe name beginning with a letter, followed by letters, numbers, underscores or hyphens. Run the rename once with KiCad closed. It refuses an already renamed project, filename collisions, and the original TemplateFrameworkModule folder. It changes the project trio and project metadata, resets PCB_REVISION to v0.1-dev, and preserves TEMPLATE_VERSION; it does not rewrite prose or alter schematic/board UUIDs. Run it before adding custom sheets or a .kicad_dru file. If you downloaded a ZIP instead, name its extracted folder after the new module and initialize a fresh repository there.

A generated repository has its own history and is not a fork. Later template changes do not propagate automatically. Port selected improvements deliberately and verify them in the receiving design; do not merge entire unrelated histories to update a module.

## KiCad's native template browser

The root meta/info.html also enables native KiCad templates. Place a clean copy of this folder under your KiCad user-template directory and select it through **File → New Project from Template** (configure template search paths for your installation). Exclude .git, backups and outputs from that copy. KiCad renames the project files itself, so do not run new_module.py afterward. Verify copied documentation and dotfiles before initializing Git. Native creation makes a local project; it does not create a GitHub repository or configure a remote. Prefer GitHub's template workflow when you want the complete repository structure.

## References

- [GitHub: creating a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
- [GitHub: creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [KiCad 9: project templates](https://docs.kicad.org/9.0/en/kicad/kicad.html#project_templates)
