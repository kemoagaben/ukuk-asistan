import openai

# API anahtarını buraya girin
openai.api_key = "OPENAI_API_KEYINIZI_BURAYA_YAZIN"

def gpt_gerekceli_analiz(user_text: str, mevzuatlar: list, ictihatlar: list) -> str:
    mevzuat_str = "\n".join([f"{m['tip']} {m['madde']}: {m['baslik']} – {m['metin']}" for m in mevzuatlar])
    ictihat_str = "\n".join([f"{i['esas']}/{i['karar']}: {i['ozet']}" for i in ictihatlar])
    
    prompt = f"""
Kullanıcıdan gelen olay/dilekçe metni:
{user_text}

İlgili mevzuat maddeleri:
{mevzuat_str}

Emsal içtihatlar:
{ictihat_str}

Sen bir Türk hukuk asistanısın. Yukarıdaki bilgiye göre olayla ilgili:
1. Hangi maddeler ve içtihatlar neden uygulanır?
2. Olayı hukuki açıdan madde madde, profesyonel ve gerekçeli analiz et.
3. Kısa özet ve sonuç çıkar.

Yanıtın sade, sistematik ve Türkçe olsun.
"""
    completion = openai.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "Sen Türk hukukuna ve yargı kararlarına tam hakim bir hukuk asistanısın."},
            {"role": "user", "content": prompt}
        ],
        max_tokens=900
    )
    return completion.choices[0].message.content

if __name__ == "__main__":
    # Demo
    sample_text = "Bir kişinin rızası dışında evine girilmiştir. Kişi, hem ceza hem tazminat talep etmektedir."
    mevzuatlar = [
        {"tip": "Anayasa", "madde": "21", "baslik": "Konut dokunulmazlığı", "metin": "Kimsenin konutuna dokunulamaz..."},
        {"tip": "Kanun", "madde": "TCK 116", "baslik": "Konut dokunulmazlığının ihlali", "metin": "Bir kimsenin konutuna giren kişi cezalandırılır."}
    ]
    ictihatlar = [
        {"esas": "2019/2345", "karar": "2020/1234", "ozet": "Sanığın mağdurun evine izinsiz girdiği..."}
    ]
    print(gpt_gerekceli_analiz(sample_text, mevzuatlar, ictihatlar))

