[app]

# 应用程序名称和包信息
title = XiaoTuDiDi
package.name = xiaotudidi
package.domain = org.test

# 源代码位置和文件
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
source.exclude_dirs = tests, bin, .pytest_cache, __pycache__, .git, .github, venv, .buildozer

# 应用程序配置
orientation = portrait
fullscreen = 0
version.regex = __version__ = ['"](.*)['"]
version.filename = %(source.dir)s/main.py

# 依赖项配置
requirements = hostpython3==3.9.18,python3==3.9.18,kivy==2.2.1,pillow==10.0.0,cython==3.0.2

# Android配置
android.archs = arm64-v8a
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 34
android.minapi = 21
android.sdk = 34
android.ndk = 25b
android.ndk_api = 21
android.bootstrap = sdl2

# Java和Gradle配置
android.java_version = 17
android.accept_sdk_license = True
android.gradle_dependencies = org.jetbrains.kotlin:kotlin-stdlib-jdk7:1.5.31
android.enable_androidx = True

# 构建和输出配置
android.build_mode = debug
android.release_artifact = apk
android.logcat_filters = *:S python:D
android.copy_libs = 1
android.debug_symbols = True

# Hook模块配置
p4a.hook = hookmodules/hook.py

# 输出目录配置
android.output_dir = bin

[buildozer]
# 日志配置
log_level = 2
warn_on_root = 1

# 构建目录配置
build_dir = .buildozer
bin_dir = bin