import numpy as np
import pandas as pd
from keras.utils import np_utils

# 用來後續將 label 標籤轉為 one-hot-encoding
np.random.seed(10)

# 2.下載 mnist data
from keras.datasets import mnist

# 3.讀取與查看 mnist data
(X_train_image, y_train_label), (X_test_image, y_test_label) = mnist.load_data()
print("\t[Info] train data={:7,}".format(len(X_train_image)))
print("\t[Info] test  data={:7,}".format(len(X_test_image)))
# 1.訓練資料是由 images 與 labels 所組成
print("\t[Info] Shape of train data=%s" % (str(X_train_image.shape)))
print("\t[Info] Shape of train label=%s" % (str(y_train_label.shape)))
# 得:訓練資料是由 images 與 labels 所組成共有 60,000 筆, 每一筆代表某個數字的影像為 28x28 pixels.

# 2.建立 plot_image 函數顯示數字影像
import matplotlib.pyplot as plt


def plot_image(image):
    fig = plt.gcf()
    fig.set_size_inches(2, 2)
    plt.imshow(image, cmap="binary")  # cmap='binary' 參數設定以黑白灰階顯示.
    plt.show()


# 3.執行 plot_image 函數查看第 0 筆數字影像與 label 資料
plot_image(X_train_image[0])
print(y_train_label[0])
# 得:呼叫 plot_image 函數, 傳入 X_train_image[0], 也就是順練資料集的第 0 筆資料, 顯示結果可以看到這是一個數字 5 的圖形
# 1.建立 plot_images_labels_predict() 函數
# 為了後續能很方便查看數字圖形, 真實的數字與預測結果
def plot_images_labels_predict(images, labels, prediction, idx, num=10):
    fig = plt.gcf()
    fig.set_size_inches(12, 14)
    if num > 25:
        num = 25
    for i in range(0, num):
        ax = plt.subplot(5, 5, 1 + i)
        ax.imshow(images[idx], cmap="binary")
        title = "l=" + str(labels[idx])
        if len(prediction) > 0:
            title = "l={},p={}".format(str(labels[idx]), str(prediction[idx]))
        else:
            title = "l={}".format(str(labels[idx]))
        ax.set_title(title, fontsize=10)
        ax.set_xticks([])
        ax.set_yticks([])
        idx += 1
    plt.show()


plot_images_labels_predict(X_train_image, y_train_label, [], 0, 10)
# 1.features (數字影像的特徵值) 資料前處理
# 先將 image 以 reshape 轉換為二維 ndarray 並進行 normalization (Feature scaling):
x_Train = X_train_image.reshape(60000, 28 * 28).astype("float32")
x_Test = X_test_image.reshape(10000, 28 * 28).astype("float32")
print("\t[Info] xTrain: %s" % (str(x_Train.shape)))
print("\t[Info] xTest: %s" % (str(x_Test.shape)))
# Normalization
x_Train_norm = x_Train / 255
x_Test_norm = x_Test / 255
# 2.labels (影像數字真實的值) 資料前處理
y_TrainOneHot = np_utils.to_categorical(y_train_label)
# 將 training 的 label 進行 one-hot encoding
y_TestOneHot = np_utils.to_categorical(y_test_label)
# 將測試的 labels 進行 one-hot encoding
# 檢視 training labels 第一個 label 的值
print(y_train_label[0])
# 檢視第一個 label 在 one-hot encoding 後的結果, 會在第六個位置上為 1, 其他位置上為 0
print(y_TrainOneHot[:1])
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()  # Build Linear Model
model.add(Dense(units=256, input_dim=784, kernel_initializer="normal", activation="relu"))  # Add Input/hidden layer
model.add(Dense(units=10, kernel_initializer="normal", activation="softmax"))  # Add Hidden/output layer
print("\t[Info] Model summary:")
model.summary()
print("")

# 1.定義訓練方式
# 在訓練模型之前, 我們必須先使用 compile 方法, 對訓練模型進行設定
model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

# 2.開始訓練
train_history = model.fit(
    x=x_Train_norm,
    y=y_TrainOneHot,
    validation_split=0.2,
    epochs=10,
    batch_size=2000,
    verbose=2,
)

# 3.建立 show_train_history 顯示訓練過程
# 訓練步驟會將每一個訓練週期的 accuracy 與 loss 記錄在 train_history 變數
# 讀取 train_history 以圖表顯示訓練過程:
import matplotlib.pyplot as plt


def show_train_history(train_history, train, validation):

    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title("Train history")
    plt.ylabel("train")
    plt.xlabel("epoch")
    # 設置圖例在左上角
    plt.legend(["train", "validation"], loc="upper left")
    plt.show()


show_train_history(train_history, "accuracy", "val_accuracy")
show_train_history(train_history, "loss", "val_loss")

# 1.評估模型準確率
# 使用下面代碼評估模型準確率:
scores = model.evaluate(x_Test_norm, y_TestOneHot)
print()
print("\t[Info] Accuracy of testing data = {:2.1f}%".format(scores[1] * 100.0))

# 2.進行預測
print("\t[Info] Making prediction to x_Test_norm")
prediction = model.predict(x_Test_norm)
prediction = np.argmax(prediction, axis=1)
print()
print("\t[Info] Show 10 prediction result (From 240):")
print("%s\n" % (prediction[240:250]))
plot_images_labels_predict(X_test_image, y_test_label, prediction, idx=240)

# 1.使用 pandas crosstab 建立混淆矩陣 (Confusion matrix)
print("\t[Info] Display Confusion Matrix:")
import pandas as pd

print("%s\n"% pd.crosstab(y_test_label, prediction, rownames=["label"], colnames=["predict"]))

# 2.建立真實與預測的 dataframe
# 如找出那些 label 結果為 "5" 的結果被預測成 "3" 的資料, 所以建立的下面的 dataframe:
df = pd.DataFrame({"label": y_test_label, "predict": prediction})
df[:2]  # 顯示前兩筆資料

# 3.查詢 label=5; prediction=3 的資料
# Pandas Dataframe 可以讓你很方便的查詢資料:
out = df[(df.label == 5) & (df.predict == 3)]  # 查詢 label=5; predict=3 的 records
out.__class__  # 輸出是另一個 DataFrame
print(out)

# 4.查看第 340 筆資料
plot_images_labels_predict(X_test_image, y_test_label, prediction, idx=340, num=1)