[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Ajuste nos requisitos: Adicionei o sqlite3 e retirei a versão fixa do sdl2_ttf
# para deixar o Buildozer escolher a melhor para o Android 13/14
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl,sqlite3,sdl2_ttf

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

# MODO PILOTO AUTOMÁTICO:
# Removemos as versões fixas de SDK e NDK para o servidor não conflitar
android.accept_sdk_license = True
android.skip_update = False

# Arquiteturas modernas
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
