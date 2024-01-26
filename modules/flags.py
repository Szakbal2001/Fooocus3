disabled = 'Disabled'
enabled = 'Enabled'
subtle_variation = 'Vary (Subtle)'
strong_variation = 'Vary (Strong)'
upscale_15 = 'Upscale (1.5x)'
upscale_2 = 'Upscale (2x)'
upscale_fast = 'Upscale (Fast 2x)'

uov_list = [
    disabled, subtle_variation, strong_variation, upscale_15, upscale_2, upscale_fast
]

KSAMPLER_NAMES = ["euler", "euler_ancestral", "heun", "heunpp2","dpm_2", "dpm_2_ancestral",
                  "lms", "dpm_fast", "dpm_adaptive", "dpmpp_2s_ancestral", "dpmpp_sde", "dpmpp_sde_gpu",
                  "dpmpp_2m", "dpmpp_2m_sde", "dpmpp_2m_sde_gpu", "dpmpp_3m_sde", "dpmpp_3m_sde_gpu", "ddpm", "lcm"]

SCHEDULER_NAMES = ["normal", "karras", "exponential", "sgm_uniform", "simple", "ddim_uniform", "lcm", "turbo"]
SAMPLER_NAMES = KSAMPLER_NAMES + ["ddim", "uni_pc", "uni_pc_bh2"]

sampler_list = SAMPLER_NAMES
scheduler_list = SCHEDULER_NAMES

cn_ip = "ImagePrompt"
cn_ip_face = "FaceSwap"
cn_canny = "PyraCanny"
cn_cpds = "CPDS"

ip_list = [cn_ip, cn_canny, cn_cpds, cn_ip_face]
default_ip = cn_ip

default_parameters = {
    cn_ip: (0.5, 0.6), cn_ip_face: (0.9, 0.75), cn_canny: (0.5, 1.0), cn_cpds: (0.5, 1.0)
}  # stop, weight

metadata_scheme =[
    ('Fooocus (json)', 'fooocus'),
    ('A1111 (plain text)', 'a1111'),
]

inpaint_engine_versions = ['None', 'v1', 'v2.5', 'v2.6']

performance_selections = [
    ('Quality <span style="color: grey;"> \U00002223 60 steps</span>', 'Quality'),
    ('Speed <span style="color: grey;"> \U00002223 30 steps</span>', 'Speed'),
    ('Extreme Speed (LCM) <span style="color: grey;"> \U00002223 8 steps, intermediate results disabled</span>', 'Extreme Speed')
]

output_formats = ['png', 'jpg', 'webp']

inpaint_mask_models = [
    'u2net', 'u2netp', 'u2net_human_seg', 'u2net_cloth_seg', 'silueta', 'isnet-general-use', 'isnet-anime', 'sam'
]

inpaint_mask_cloth_category = ['full', 'upper', 'lower']

inpaint_mask_sam_model = ['sam_vit_b_01ec64', 'sam_vit_h_4b8939', 'sam_vit_l_0b3195']

inpaint_option_default = 'Inpaint or Outpaint (default)'
inpaint_option_detail = 'Improve Detail (face, hand, eyes, etc.)'
inpaint_option_modify = 'Modify Content (add objects, change background, etc.)'
inpaint_options = [inpaint_option_default, inpaint_option_detail, inpaint_option_modify]

desc_type_photo = 'Photograph'
desc_type_anime = 'Art/Anime'
