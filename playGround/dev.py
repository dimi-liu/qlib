import qlib
# region in [REG_CN, REG_US]
from qlib.constant import REG_CN


if __name__ == '__main__':

    # 下载数据 路径在 ~/.qlib，然后初始化数据
    provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir

    # Initialize Qlib before calling other APIs: run following code in python.
    qlib.init(provider_uri=provider_uri, region=REG_CN)

