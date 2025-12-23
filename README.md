# 概要

青森の方言を文字起こしするデモ


# 準備

```
$ python -m venv .transcribe
$ source .transcribe/bin/activate
$ pip install -U faster-whisper
```

# 実行

## GPT-4o-transcribe

かの有名なOpenAIのWhisperの後継である `GPT-4o-Transcribe` を使ったやつ

```
$ python gpt-4o-transcribe.py
```

## Kotoba-Whisper-v2.2

日本語特化の音声認識モデルである `Kotoba-Whisper` の最新の v2.2 を使ったやつ。
参考: https://huggingface.co/kotoba-tech/kotoba-whisper-v2.2

```
$ python kotoba-whisper.py
```