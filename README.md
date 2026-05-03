# lang-ship Arduino Core package index

This repository publishes the merged Arduino Boards Manager package index for:

- `tanakamasayuki/host-arduino-core`
- `tanakamasayuki/native-arduino-core`

`package_index.json` is updated by GitHub Actions after either source repository finishes its release workflow, then published with GitHub Pages.

## Required repository settings

In both source repositories, add an Actions secret named `LANG_SHIP_ARDUINO_CORE_PAT`.

The token must be able to call `repository_dispatch` on this repository. A fine-grained personal access token should grant this repository `Contents: read and write`.

In this repository, set GitHub Pages source to `GitHub Actions`.
