[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Adicionei o sqlite3 nos requisitos para garantir o banco de dados
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sqlite3

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

# IMPORTANTE: Use exatamente estas versões que já estão no servidor
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# Caminhos diretos do GitHub Actions para evitar o erro de download
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
