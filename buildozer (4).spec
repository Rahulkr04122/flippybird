[app]
# (str) Title of your application
title = flippygame

# (str) Package name
package.name = com.flippygame

# (str) Package domain (needed for android/ios packaging)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Application requirements
requirements = python3==3.10.14,hostpython3==3.10.14,kivymd,pillow

# (str) Icon of the application
icon.filename = icon.png

# (str) Application versioning (method 1)
version = 0.1

# (list) Permissions
android.permissions = INTERNET

# (int) Minimum API needed for the application
android.api = 19

# (int) Android SDK version to use
android.sdk = 26

# (int) Android NDK version to use
android.ndk = 19b

# (bool) Indicate whether the application should be fullscreen or not
fullscreen = 0

# via pip (latest stable, recommended)
# if you use a virtualenv, don't use the `--user` option
pip install --user buildozer

# latest dev version
# if you use a virtualenv, don't use the `--user` option
pip install --user https://github.com/kivy/buildozer/archive/master.zip

# git clone, for working on buildozer
git clone https://github.com/kivy/buildozer
cd buildozer
python setup.py build
pip install -e

pip install pip==24.0

# (str) Presplash background color (for Android only)
# (str) Background color in rrggbb format
#presplash.color = #FFFFFF

# (str) Presplash image to use
#presplash.filename = presplash.png

# (str) Icon of the application
icon.filename = icon.png

# (str) Supported orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (bool) If True display an expandable list of all the permissions the application requests
android.show_all_permissions = False

# (bool) If True, the application will ask for the permission if needed
android.ask_for_permissions = True

# (str) Text messages will be translated (default is False)
#android.allow_translation = True


# (list) Application categories
# Available options are: 'Game', 'Wallpaper', 'Launcher', 'Browser', 'Keyboard', 'Music', 'Video', 'Audio', 'Image', 'Location', 'Contact', 'Calendar', 'Settings', 'Phone', 'Other'
#android.app_category = 'Game'

# (str) Primary theme color (for Android only)
#primary_theme_color =

# (str) Secondary theme color (for Android only)
#secondary_theme_color =

# (str) Orientation (one of landscape, sensorLandscape, portrait or all)
orientation = portrait

# (list) Permissions
#android.permissions = INTERNET

# (bool) If True display an expandable list of all the permissions the application requests
android.show_all_permissions = False

# (bool) If True, the application will ask for the permission if needed
android.ask_for_permissions = True

# (str) The service name, null if not set
#android.service =

# (str) The package name of the service to export
#android.service.intent.action =

# (str) The version name of the service to export
#android.service.intent.version =

# (list) The intent services to use
#android.services =

# (str) Path to a custom toolchain to use for building
#osx.toolchain = /usr/local

# (str) Path to a custom AndroidSDK
#android.sdk = /opt/android-sdk

# (str) Path to a custom Android NDK
#android.ndk = /opt/android-ndk

# (bool) Show build log in python-for-android output
#p4a.show_logs = False

# (str) The Android arch to build for, choices: armeabi-v7a, arm64-v8a, x86, x86_64
#android.arch = armeabi-v7a

# (str) Custom source folders for requirements
# Sets custom source for any requirements with recipes
# This can point to a folder, a git repository or a zip url
#requirements.source.kivy = ../../kivy

# (str) Change the command to compile the kivy bits
# By default uses the same command as regular requirements
# You can also put a custom compilation command, such as "./compile_kivy.sh".
#requirements.source.kivy = ../../kivy

# (list) The Android permissions
# It should be a list of permissions, e.g ["internet", "camera"]
#android.permissions = INTERNET

# (str) aapt flags for the compilation
#android.aapt_flags = --ignore-assets '*.ogg'

# (str) Android logcat filters to use
#android.logcat_filters = *:S python:D

# (bool) Copy library instead of making a libpymodules.so
#android.copy_libs = 1

# (bool) Uses a black theme on Windows
#p4a.windows.black_theme = False

# (str) Application needs to be signed with a custom certificate
# (str) Path to the keystore
#android.keystore = myapp.keystore

# (str) Password for the keystore
#android.keystore_pass = mykey

# (str) Alias for the key
#android.key_alias = myalias

# (str) Password for the key
#android.key_alias_pass = mykey

# (bool) Uses old toolchain if True
#p4a.old_toolchain = False

# (str) One of phone, tablet, androidtv or wear
#android.minapi = 21

# (str) One of phone, tablet, androidtv or wear
#android.minapi = 21

# (str) Python-for-android URL to use for downloading source packages
#p4a.source_dir = /home/user/source

# (str) The NDK API to use
#android.ndk_api = 21

# (str) Bootstrap to use for android builds
# p4a.bootstrap = sdl2
# p4a.bootstrap = pygame

# (int) Target SDK version to use for android builds
#android.sdk = 19

# (str) Android NDK version to use
#android.ndk = 19b

# (str) Android NDK directory (if empty, it will be automatically downloaded.)
#android.ndk_path = /opt/android-ndk

# (str) Android SDK directory (if empty, it will be automatically downloaded.)
#android.sdk_path = /opt/android-sdk

# (str) Android entry point
#android.entry_point = org.renpy.android.PythonActivity

# (str) Android entry point
#android.entry_point = org.kivy.android.PythonActivity

# (list) Permissions
#android.permissions = INTERNET

# (bool) If True, then the screen will not turn off automatically.
# This is suitable for video player applications.
#android.wakelock = True

# (str) Android NDK version to use
#android.ndk = 19b

# (bool) Use --private data storage
#android
