import os
from flask_restful import abort
UPLOAD_PREFIX = 'App/static/'
UPLOAD_DIR = 'uploads/'

def file_save(form):
    # 获取注册的图片对象
    f_in = form.pic.data
    # 获取该对象的文件名
    fname = f_in.filename
    # 给该文件包装到一个包里
    pic = os.path.join(UPLOAD_DIR,fname)
    # 拼接该文件的绝对路径
    file_path = os.path.join(UPLOAD_PREFIX,pic)
    # 检查目录是否存在
    f_dir = os.path.dirname(file_path)
    if not os.path.exists(f_dir):
        try:
            os.makedirs(f_dir)
        except Exception as e:
            msg = "无法创建目录{}".format(f_dir)
            abort(500, msg)
    f_in.save(file_path)
    return pic