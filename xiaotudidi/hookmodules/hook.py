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
        default_ndk_paths = [
            "/home/runner/.buildozer/android/platform/android-ndk-r25b",
            "/usr/local/lib/android/sdk/ndk/27.3.13750724",
            "/usr/local/lib/android/sdk/ndk/25.2.9519653"
        ]
        
        for path in default_ndk_paths:
            if os.path.exists(path):
                context.android_ndk = path
                print(f"NDK path set to default: {path}")
                break
        else:
            print("Warning: No valid NDK path found")
    
    # 确保SDK路径正确
    sdk_path = os.environ.get('ANDROID_SDK_ROOT')
    if sdk_path and os.path.exists(sdk_path):
        context.android_sdk = sdk_path
        print(f"SDK path set to: {sdk_path}")
        
    print("Hook execution completed.")