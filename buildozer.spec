[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Adicionado jnius para a trava de hardware funcionar
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sqlite3,pyjnius

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 21
android.ndk = 27c
android.accept_sdk_license = True
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1
