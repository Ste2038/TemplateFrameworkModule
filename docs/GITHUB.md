# GitHub template workflow

## Publish this folder as the template repository

No GitHub remote has been created by the scaffold setup. Decide the owner/account, visibility and license before publishing. Create an empty GitHub repository named TemplateFrameworkModule (do not prepopulate README, license or .gitignore). From this folder:

```sh
git init -b main
git add .
git diff --cached --stat
git commit -m "Create KiCad module template"
git remote add origin git@github.com:YOUR_ACCOUNT/TemplateFrameworkModule.git
git push -u origin main
```

Replace YOUR_ACCOUNT. Review staged files before committing. If Git is already initialized, skip initialization and inspect existing remotes rather than overwriting them. On GitHub open repository **Settings → General**, enable **Template repository**, and verify that **Use this template** appears. Repository admin access is required. Set an appropriate description and choose licensing deliberately; this scaffold grants no explicit reuse license.

## Create each future module

1. Open the template on GitHub and choose **Use this template → Create a new repository**.
2. Select owner, module repository name and visibility. Use the default branch; including all branches is unnecessary for this scaffold.
3. Clone the new module repository and enter it:

```sh
git clone git@github.com:YOUR_ACCOUNT/MyModule.git
cd MyModule
python3 scripts/new_module.py MyModule
```

4. Open MyModule.kicad_pro and update docs/MODULE.md, README.md, title blocks and revision information. Before design work, complete [TEMPLATE_TRACKING.md](TEMPLATE_TRACKING.md) with the actual source template URL, tag and full source commit SHA. The generated repository commit is not the source template commit. Follow [TEMPLATE_UPGRADES.md](TEMPLATE_UPGRADES.md) for version identification and future upgrades.
5. Review and commit the renamed files and module definition, then push to the new module repository.

Use a filesystem-safe name beginning with a letter, followed by letters, numbers, underscores or hyphens. Run the rename once with KiCad closed. It refuses an already renamed project, filename collisions, and the original TemplateFrameworkModule folder. It changes the project trio and project metadata only; it does not rewrite prose or alter schematic/board UUIDs. Run it before adding custom sheets or a .kicad_dru file. If you downloaded a ZIP instead, name its extracted folder after the new module and initialize a fresh repository there.

A generated repository has its own history and is not a fork. Later template changes do not propagate automatically. Port selected improvements deliberately and verify them in the receiving design; do not merge entire unrelated histories to update a module.

## KiCad's native template browser

The root meta/info.html also enables native KiCad templates. Place a clean copy of this folder under your KiCad user-template directory and select it through **File → New Project from Template** (configure template search paths for your installation). Exclude .git, backups and outputs from that copy. KiCad renames the project files itself, so do not run new_module.py afterward. Verify copied documentation and dotfiles before initializing Git. Native creation makes a local project; it does not create a GitHub repository or configure a remote. Prefer GitHub's template workflow when you want the complete repository structure.

## References

- [GitHub: creating a template repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-template-repository)
- [GitHub: creating a repository from a template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- [KiCad 9: project templates](https://docs.kicad.org/9.0/en/kicad/kicad.html#project_templates)
