# Lab 06 release checklist

## Activity 1 — Signed Android build

- [x] Android release configuration: applicationId `lk.fitflow.it23379442`, 1.1.0 (2), min API 26, target API 36.
- [x] Local 3072-bit RSA release keystore generated and excluded from Git.
- [x] R8 release optimization and obfuscation configured; ZIP-compressed web assets; zipalign.
- [x] Signed APK generated and v2/v3 signature verified.
- [x] APK installed and launched on Pixel 7 emulator.
- [ ] Generate a production AAB using a standard Android Gradle release project before Google Play upload.
- [ ] Test physical devices and minimum supported Android version.

## Activity 2 — Assets

- [x] Original violet/mint identity, vector-style UI icons, launcher resources and adaptive icon.
- [x] 512 x 512 Google Play icon, 1024 x 1024 master icon, 1024 x 500 feature graphic.
- [x] Captured actual app/browser screen evidence; filenames distinguish native and responsive web captures.
- [ ] Capture genuine iPhone/iPad screenshots only after building and testing an iOS app.
- [ ] Review store screenshots against final supported devices and current store requirements.

## Activity 3 — Google Play Console (pending account access)

1. Sign in to the owner's verified Google Play Developer account.
2. Create an app named FitFlow in Health & Fitness, English; proposed free distribution requires owner confirmation in the console.
3. Prepare and upload the signed production AAB; enable Play App Signing and preserve the upload key.
4. Complete content rating, ads, target audience, health apps, data safety, app access, and privacy URL sections based on actual behavior. Do not infer legal compliance from this checklist.
5. Select intended countries and device coverage; review pre-launch results.
6. Use Internal testing first. Add authorized tester emails, share opt-in link, install from Play, and record results.
7. Listing experiment proposal: compare the current “Find your rhythm” feature graphic against a “Build a small daily habit” alternative; measure listing conversion. No experiment has been run.

Evidence still required: console app record, completed content forms, signing settings, uploaded version, pre-launch report, and internal-track opt-in link. No account details or screenshots are invented.

## Activity 4 — App Store Connect and TestFlight (pending)

The current repository contains an Android app and a browser UI; **it contains no iOS binary**. An iOS shell/project, macOS/Xcode or approved cloud build, Apple Developer membership, signing, and real Apple-device testing are prerequisites.

1. Implement an iOS app and test its storage, navigation, safe areas, and accessibility.
2. Register the bundle identifier and App Store Connect record (proposed identifier `lk.fitflow.it23379442`; availability is unverified).
3. Supply app name, category, version, keywords, support contact, privacy policy URL, screenshots, and accurate privacy labels.
4. Archive/sign/upload using the owner's account. Resolve processing or validation failures.
5. Create internal tester groups; external testing may require beta review. Monitor build expiry and feedback.

Evidence still required: app record, processed build, tester groups, invitations, device installation, feedback, expiry date, and review status.

## Activity 5 — Privacy and release documentation

- [x] Implementation-matched draft privacy notice, in-app notice, release notes.
- [x] Local profile editing, export, and delete-all controls.
- [x] Owner supplied support email: akilatheshan23@gmail.com.
- [ ] Campus was not supplied; confirm before final report submission.
- [ ] Verify public access after pushing the privacy notice to GitHub; the exact repository policy URL is linked in the app.
- [ ] Obtain deployment-specific legal/privacy review before claiming GDPR/HIPAA compliance or store readiness.

## Activity 6 — Internal testing and approval

- [x] Local browser interaction checks and native emulator smoke test recorded.
- [ ] Play Internal Testing deployment and TestFlight deployment.
- [ ] At least five genuine human testing sessions, with consent and feedback records.
- [ ] Physical-device performance, battery, offline, orientation, font scaling, and TalkBack testing.
- [ ] Crash reporting decision; this offline build intentionally has no telemetry SDK.
- [ ] Fix release-blocking issues, rerun affected cases, and obtain lecturer/team approval.

Approval record: **NOT REQUESTED / NOT GRANTED**. This project must not be represented as externally approved or store-deployed.
