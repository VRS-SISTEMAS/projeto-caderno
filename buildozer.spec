[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Requirements: Simplificados para o Buildozer baixar as versões mais compatíveis
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl,sqlite3

orientation = portrait
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

# --- MODO REPARO AUTOMÁTICO ---
# Removi as linhas que forçavam o NDK antigo. 
# Isso obriga o Buildozer a baixar o NDK correto para o servidor atual.
android.accept_sdk_license = True
android.skip_update = False
android.copy_libs = 1

# Arquiteturas modernas
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
