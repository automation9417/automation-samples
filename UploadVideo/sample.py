import os
import upload_instagram, upload_tiktok, upload_twitter

caption = 'Clicknium introduction'
cover_image = os.path.join(os.getcwd(), "media", "logo.png")
video_file = os.path.join(os.getcwd(), "media", "clicknium_introduction.mp4")
upload_tiktok.upload(caption, video_file)
short_video_file = os.path.join(os.getcwd(), "media", "short_introduction.mp4")
upload_twitter.upload(caption, short_video_file)
upload_instagram.upload(caption, cover_image, video_file)

