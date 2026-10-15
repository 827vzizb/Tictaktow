[app]

# (str) Title of your application
title = Sahi Game

# (str) Package name
package.name = sahigame

# (str) Package domain
package.domain = com.sahi.game

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,kv,atlas,json

# (str) Application versioning
version = 1.0.0

# (list) Application requirements
requirements = python3,kivy==2.3.0,pyjnius,requests

# (str) Supported orientation
orientation = portrait

# (bool) Fullscreen
fullscreen = 0

# (list) Permissions
android.permissions = INTERNET, READ_EXTERNAL_STORAGE, WRITE_EXTERNAL_STORAGE, ACCESS_FINE_LOCATION, POST_NOTIFICATIONS

# (int) Target Android API
android.api = 33

# (int) Minimum API supported
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Auto accept SDK license
android.accept_sdk_license = True

# (str) Android archs
android.archs = arm64-v8a

[buildozer]
log_level = 2
warn_on_root = 1
