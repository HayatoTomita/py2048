# py2048
pythonで作った2048

# install
```
git clone $THIS_REPO
cd $THIS_REPO
poetry install
poetry run python py2048/main.py
```

# 操作説明
w : 上
a : 左
s : 下
d : 右

# プレイ後の生成物
プレイ後にgamelogsディレクトリが生成され、中に以下のファイルが生成されます  
* controll_log.json : {入力した方向, 数字がスポーンした場所, スポーンした数字}, {最終的なスコア}
* initial_board.csv : ゲーム開始時の盤面
* last_board.csv : ゲーム終了時の盤面
