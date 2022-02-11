import rclone

cfg_path = r'/Users/cenkakdeniz/.config/rclone/rclone.conf'
import logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s [%(levelname)s]: %(message)s")

with open(cfg_path) as f:
   cfg = f.read()
rcln = rclone.with_config(cfg)
copy_dict = ["--log-file=mylogfile.txt", "--rc-enable-metrics","-vv", "--progress"]
#result = rclone.with_config(cfg).listremotes()
#result = rcln.copy("sadedegel-aws:sadedegel-bucket", "sadedegel-minio:test/folder6", copy_dict)
rcln.listremotes()