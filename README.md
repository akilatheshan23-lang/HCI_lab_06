# FitFlow — Find your rhythm

An original violet, mint, and soft-neutral fitness application for **IT3060 Human Computer Interaction, Lab Exercise 06**.

**Student:** Weerasingha V.P.K.P.A.T · **IT23379442** · **WE_07**

## Run it

- Android: install `releases/FitFlow-1.1.0-release.apk` on Android 8.0 or newer. This is a locally signed coursework build, not a Google Play download.
- Web: run `python scripts/serve.py`, then open `http://127.0.0.1:4173`.
- Build: install Python 3, JDK 17+, Android SDK Platform 36 and Build Tools 36.1.0; set `JAVA_HOME` and `ANDROID_HOME`; run `python scripts/build_android.py`.
- Open this folder in VS Code. No npm install or cloud account is needed to run the app.

## Working features

- Validated local profile setup with age, height, weight, and fitness focus.
- Dashboard with current-day workout totals, meal energy, hydration, and weekly calendar.
- Six timed routines; category filters; pause/resume/skip; completed-session history.
- Local rule-based Daily Flow recommendations based on the selected focus.
- Meal journal with calories and macros; delete meals; daily water journal and undo.
- Seven-day activity chart, real recorded history, weight journal, and streaks.
- Community **demo** with clearly labeled sample posts, private notes, and local likes.
- Editable profile, JSON export, privacy notice, and confirmed local deletion.
- Responsive desktop, tablet, and mobile layouts; semantic controls, focus outlines, modal focus handling, reduced-motion support.

## Honest scope

This release is a working **local-first Android/web coursework app**, not a production cloud fitness service. It does not have cloud authentication, a backend database, generative AI, public social posting, push notifications, or analytics. Initial journal targets are user-editable placeholders, not medical or dietary advice.

The APK is built with Java + Android WebView, serving packaged HTML/CSS/JavaScript through an intercepted local HTTPS origin. It does not request INTERNET permission. No JavaScript/native bridge is exposed, file access is disabled, external navigation is blocked except the exact privacy-policy link opened in the system browser, and Android backup is disabled. Local app data is not separately encrypted; do not enter sensitive medical records.

The lab requests store deployments. **Google Play upload, an AAB, an iOS binary, TestFlight, human tester feedback, battery measurements, and lecturer approval are not completed.** See the report and `docs/release-checklist.md`; no evidence for these activities has been fabricated.

## Project map

| Path | Purpose |
| --- | --- |
| `web/` | Complete responsive UI and application logic |
| `android/` | Native shell, manifest, adaptive icons, R8 keep rules |
| `scripts/` | Local preview, asset generation, APK build, optional Playwright tests |
| `releases/` | Signed APK, SHA-256 metadata, signature verification |
| `store-assets/` | 512/1024 icons, feature graphic, screenshot assets |
| `docs/` | Lab report, privacy, release notes, test evidence, release checklist |
| `.private/` | Local-only signing key and password; excluded from Git |

## Signing key management

The build creates `.private/fitflow-release.jks` and `.private/signing-password.txt` only when a key is absent. Preserve both securely outside Git. The password is randomly generated, not embedded in code. Keep an encrypted backup; restrict access to the project owner. Losing the signing key can prevent updates to installed APKs. The same alias (`fitflow-release`) is reused for subsequent builds. Increase versionCode and versionName in `android/AndroidManifest.xml` before a new release; update metadata in the build script as well.

Build uses the official AAPT2 resource compiler, javac, R8 in release mode, ZIP compression, zipalign, and apksigner. `releases/signature-verification.txt` proves APK Signature Scheme v2/v3 verification. `releases/build-info.json` records the exact APK hash and size. R8 mappings remain in `build/android/mapping.txt`; retain them privately with each release for debugging.

## Verification

See `docs/evidence/verification.json` for actual checks performed. A standalone `scripts/test_ui.cjs` is supplied for repeatable extended browser regression tests; its headless browser launch was blocked by this execution environment and must not be represented as a passing automated suite. Actual browser interaction checks and the signed Android emulator install were performed separately.

## Design and reference use

The supplied campus lab sheet defines the six activity headings. The supplied friend's report was reviewed as an example of report structure and screen coverage. Its identity, text, green UI, credentials, screenshots, and claimed tester feedback were not copied into this project. The illustrated runner and icons are code-drawn assets created for this app.

## Repository

https://github.com/akilatheshan23-lang/HCI_lab_06
