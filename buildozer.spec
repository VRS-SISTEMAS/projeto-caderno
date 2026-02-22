[app]
title = VRS Caderno Digital
package.name = cadernovrs
package.domain = org.vrs
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,db
version = 0.1
requirements = python3,kivy==2.3.0,kivymd==1.2.0,pillow,sqlite3

orientation = portrait
fullscreen = 0

# VERSÕES ESTÁVEIS PARA NÃO TRAVAR
android.api = 31
android.minapi = 21
android.ndk = 23b
android.accept_sdk_license = True
android.skip_update = False
android.archs = arm64-v8as
