[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Requirements: sqlite3 ja esta no python3, tirei o sdl2_ttf para evitar conflito de compilação
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl

orientation = portrait
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 21

# --- AJUSTE DEFINITIVO GITHUB 2026 ---
# Usando a API 34 para casar com o NDK 27 que o servidor ja possui
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
android.ndk = 27b

android.accept_sdk_license = True
android.skip_update = False
android.copy_libs = 1

# Arquiteturas
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
