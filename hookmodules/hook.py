import os

def before_apk_build(context):
    print("Running pre-build hook...")
    # 确保NDK路径正确
    ndk_path = os.environ.get('ANDROID_NDK_HOME')
    if ndk_path:
        context.android_ndk = ndk_path
    # 确保SDK路径正确
    sdk_path = os.environ.get('ANDROID_SDK_ROOT')
    if sdk_path:
        context.android_sdk = sdk_path
