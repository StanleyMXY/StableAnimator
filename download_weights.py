import os
os.environ.setdefault("HF_HOME", "D:/model_cache/huggingface")
from huggingface_hub import snapshot_download

path = snapshot_download(
    "FrancisRing/StableAnimator",
    cache_dir="D:/model_cache/huggingface",
    local_dir="D:/Projects/StableAnimator/checkpoints",
    allow_patterns=[
        "Animation/*",
        "DWPose/*",
        "models/antelopev2/*",
        "stable-video-diffusion-img2vid-xt/feature_extractor/*",
        "stable-video-diffusion-img2vid-xt/image_encoder/*",
        "stable-video-diffusion-img2vid-xt/scheduler/*",
        "stable-video-diffusion-img2vid-xt/unet/*",
        "stable-video-diffusion-img2vid-xt/vae/*",
        "stable-video-diffusion-img2vid-xt/model_index.json",
        "stable-video-diffusion-img2vid-xt/svd_xt.safetensors",
        "stable-video-diffusion-img2vid-xt/svd_xt_image_decoder.safetensors",
    ],
)
print("Downloaded to:", path)
