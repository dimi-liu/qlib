import pandas as pd
from Crypto.Hash import SM3Hash

# 读取 CSV 文件
df = pd.read_csv('data.csv')

# 待加密数据所在的列
column_name = 'column_name'

# 对每个数据进行加密
for i, value in enumerate(df[column_name]):
    # 将数据转换为字节数组
    data = bytes(str(value), 'utf-8')

    # 计算 SM3 哈希值
    hash_object = SM3Hash.new(data)
    sm3_hash = hash_object.digest().hex()

    # 将加密后的值写回到 DataFrame 中
    df.at[i, column_name] = sm3_hash

# 输出加密后的 DataFrame
print(df)
# import qlib
# from pathlib import Path
# # region in [REG_CN, REG_US]
# from qlib.constant import REG_CN
#
#
# if __name__ == '__main__':
#     print(qlib.__version__)
#     # 下载数据 路径在 ~/.qlib，然后初始化数据
#     provider_uri = "~/.qlib/qlib_data/cn_data"  # target_dir
#     #
#     # # Initialize Qlib before calling other APIs: run following code in python.
#     qlib.init(provider_uri=provider_uri, region=REG_CN)
#
#     path_cur = Path.cwd()
