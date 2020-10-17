Divergence Meter
=====
PICの勉強のために作りました。
言語はMPASMです。

![image.png](./pictures/image.png)

[実際に動いているところ（ブレッドボード上ですが）](https://twitter.com/makutamoto/status/1317350844782632962?s=20)

divergence_meter.X/
-----
MPLABのプロジェクトです。
PICのコードが入っています。

pcb/
-----
KICADのプロジェクトです。
基盤データが入っています。

scripts/
-----
ダイバージェンスメータに様々な情報を書き込むためのスクリプトを置いています。

### add.py
世界戦変動率を追加します。

### calibrate.py
現在時刻と同期します。

### clock.py
忘れた、不明。

### preview.py
世界戦変動率をプレビューします。

### remove.py
世界戦変動率を削除します。
