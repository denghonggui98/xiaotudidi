import os

def before_apk_build(context):
    print("Running pre-build hook...")
    print("Initial context.android_ndk:", getattr(context, 'android_ndk', 'Not set'))
    
    # 获取所有相关的NDK环境变量
    ndk_home = os.environ.get('ANDROID_NDK_HOME')
    ndk_root = os.environ.get('ANDROID_NDK_ROOT')
    android_ndk = os.environ.get('ANDROID_NDK')
    android_ndk_old = os.environ.get('ANDROIDNDK')
    
    print(f"Environment variables:")
    print(f"  ANDROID_NDK_HOME: {ndk_home}")
    print(f"  ANDROID_NDK_ROOT: {ndk_root}")
    print(f"  ANDROID_NDK: {android_ndk}")
    print(f"  ANDROIDNDK: {android_ndk_old}")
    
    # 按优先级设置NDK路径
    ndk_path = None
    for path in [ndk_home, ndk_root, android_ndk, android_ndk_old]:
        if path and os.path.exists(path):
            ndk_path = path
            break
    
    # 如果环境变量未设置或路径不存在，使用默认路径
    if not ndk_path:
        default_ndk_paths = [
            "/home/runner/.buildozer/android/platform/android-ndk-r25b",
            "/usr/local/lib/android/sdk/ndk/27.3.13750724",
            "/usr/local/lib/android/sdk/ndk/25.2.9519653"
        ]
        
        for path in default_ndk_paths:
            if os.path.exists(path):
                ndk_path = path
                break
    
    if ndk_path and os.path.exists(ndk_path):
        context.android_ndk = ndk_path
        print(f"NDK path set to: {ndk_path}")
    else:
        print("Warning: No valid NDK path found")
    
    # 确保SDK路径正确
    sdk_path = os.environ.get('ANDROID_SDK_ROOT')
    if sdk_path and os.path.exists(sdk_path):
        context.android_sdk = sdk_path
        print(f"SDK path set to: {sdk_path}")
        
    print("Hook execution completed.")