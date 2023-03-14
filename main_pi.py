import os
import time
import random

def estimate_pi(num_samples):
    # 在 1 x 1 的正方形內隨機生成 num_samples 個點
    num_inside = 0
    for _ in range(num_samples):
        x, y = random.random(), random.random()
        if x ** 2 + y ** 2 <= 1:
            num_inside += 1

    # 根據圓內的點和總點數的比例估計圓周率
    return 4 * num_inside / num_samples


def count_rows(filename):
    time.sleep(5)
    with open(filename) as f:
        return len(f.readlines())



if __name__ == '__main__':

    # For Test, the start time
    start_time = time.time()

    # 一個要跑很久的函示
    # 使用 1000000 個樣本估計圓周率
    total_rows = estimate_pi(10000000)

    # 在終端中打印結果
    print(f'Result: {total_rows}')

    # For Test, the execute time
    print(f"""Execute time= {time.time() - start_time}""")