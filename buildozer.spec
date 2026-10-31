name: Build APK
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-java@v3
        with:
          java-version: '17'
          distribution: 'temurin'
      - uses: actions/setup-python@v4
        with:
          python-version: '3.10'
      - name: Build
        run: |
          pip install buildozer
          buildozer android debug
      - uses: actions/upload-artifact@v4
        with:
          name: apk
          path: bin/*.apk