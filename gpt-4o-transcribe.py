from openai import OpenAI

client = OpenAI()

hint = """\
あなたは日本語およびその方言体系に精通した専門家です。
与えられた音声データは日本の青森県の方言をお年寄りが話しています。この方言を正確に書き起こしてください。また、話し言葉をなるべく尊重してください。"""

with open("sample.m4a", "rb") as audio_file:
    transcription = client.audio.transcriptions.create(
        file=audio_file,
        model="gpt-4o-transcribe",
        language="ja",
        prompt=hint
    )

print(transcription.text)
