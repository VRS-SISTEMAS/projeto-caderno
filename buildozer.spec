[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1

# Requisitos: Adicionei o sdl2_ttf que é essencial para renderizar textos no Android
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,openssl,sdl2_ttf==2.0.15

orientation = portrait
osx.python_version = 3
osx.kivy_version = 2.3.0
fullscreen = 0

# Permissões e APIs
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21

# Configurações de ferramentas
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license = True

# Deixe o Buildozer gerenciar os caminhos internamente agora para evitar erro de 'not found'
android.archs = arm64-v8a, armeabi-v7a
android.allow_backup = True

[buildozer]
log_level = 2
warn_on_root = 1
