from faster_whisper import WhisperModel

AUDIO_FILE = "sample.m4a"

def main():
    # kotoba-whisper-v2.2-faster を指定
    model = WhisperModel(
        "RoachLin/kotoba-whisper-v2.2-faster",
        device="cpu",        # "cuda" も可
        compute_type="float32", # CPUなら int8 / GPUなら float16 推奨
    )

    segments, info = model.transcribe(
        AUDIO_FILE,
        language="ja",       # 日本語固定
        beam_size=10,
        vad_filter=True,     # 無音区間を自動除去
    )

    print("=== Transcription ===")
    for segment in segments:
        start = segment.start
        end = segment.end
        text = segment.text
        print(f"[{start:6.2f}s -> {end:6.2f}s] {text}")
        print(segment.text)

    print("\n=== Metadata ===")
    print(info)

if __name__ == "__main__":
    main()
