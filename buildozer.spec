[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Requisitos ajustados: sqlite3 já vem no python3, mas o openssl é vital para conexões
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 21

# Configurações de ferramentas (Ajustadas para o servidor do GitHub)
android.sdk = 34
android.ndk = 25b
android.accept_sdk_license = True

# Caminhos diretos: Esses endereços garantem que ele ache as ferramentas de primeira
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25.2.9519653

android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
