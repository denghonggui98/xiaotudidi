import os

def before_apk_build(context):
    print("Running pre-build hook...")
    # 确保NDK路径正确
    ndk_path = os.environ.get('ANDROID_NDK_HOME')
    if ndk_path and os.path.exists(ndk_path):
        context.android_ndk = ndk_path
        print(f"NDK path set to: {ndk_path}")
    else:
        # 如果环境变量未设置或路径不存在，使用默认路径
        default_ndk_path = "/home/runner/.buildozer/android/platform/android-ndk-r25b"
        if os.path.exists(default_ndk_path):
            context.android_ndk = default_ndk_path
            print(f"NDK path set to default: {default_ndk_path}")
    
    # 确保SDK路径正确
    sdk_path = os.environ.get('ANDROID_SDK_ROOT')
    if sdk_path and os.path.exists(sdk_path):
        context.android_sdk = sdk_path
        print(f"SDK path set to: {sdk_path}")
        
    print("Hook execution completed.")