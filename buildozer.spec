[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Requirements estáveis
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl,sqlite3

orientation = portrait
fullscreen = 0

# Use a API 33, que é a mais compatível com o NDK 25b que o Buildozer prefere
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license = True

# NÃO coloque caminhos manuais aqui desta vez
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
