[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Requirements: Adicionei o sdl2_ttf que ajuda na estabilidade das fontes no Android
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl,sqlite3,sdl2_ttf

orientation = portrait
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

# --- AJUSTE PARA GITHUB ACTIONS 2026 ---
# Estas linhas forçam o Buildozer a usar as ferramentas que já estão no servidor
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/27.3.13750724
android.ndk = 27c

android.accept_sdk_license = True
android.skip_update = False
android.copy_libs = 1

# Arquiteturas para rodar em qualquer celular moderno
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1S
