# 應用程式設計 - 課後實作 09

## 問題描述
修改[範例程式碼](https://github.com/erhwenkuo/deep-learning-with-keras-notebooks/blob/master/2.7-mnist-recognition-cnn.ipynb)並完成表格。

|  epochs   | batch_size| loss  | accuracy  |
|  :----:  | :----:  | ----:  |----:  |
|  5 | 300|0.0680| 0.9791|
| 10 | 300|0.386 | 0.9877|
|  20 | 300|0.0216| 0.9926|
|  40 | 300|0.0123| 0.9959|


|epochs| batch_size   | loss  | accuracy  |total time  in training|
|:----:|  :----:  | ----:  |----:  |:----:  |
|1|  5 | 0.2654| 0.9184|46s|
|1| 10 | 0.3230 | 0.8994|45s|
|1|  20 | 0.4004|0.8747 |42s|
|1|  40 |0.5758 | 0.8167|39s|

|epochs|batch_size| activation   | loss  | accuracy  | total time  in training|
|:----:|:----:|  :----:  | ----:  |----:  |:----:  |
|10|300|  relu |0.0424 | 0.9869| 346s|
|10|300| sigmoid | 0.1072 | 0.9681| 351s|
|10|300|  tanh |0.0424 | 0.9866| 356s|

※ 以上數據為使用 Colab 運行後的結果