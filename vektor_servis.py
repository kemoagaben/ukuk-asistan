import openai
import numpy as np
import json

# OpenAI API key'inizi ekleyin
openai.api_key = "OPENAI_API_KEYINIZI_BURAYA_YAZIN"

def get_embedding(text: str) -> list:
    """OpenAI üzerinden metnin embedding vektörünü alır."""
    emb = openai.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return emb.data[0].embedding

def cosine_sim(a: list, b: list) -> float:
    a_arr, b_arr = np.array(a), np.array(b)
    return float(np.dot(a_arr, b_arr) / (np.linalg.norm(a_arr) * np.linalg.norm(b_arr)))

def en_benzer_madde(metin: str, mevzuat_json_path="mevzuat_db.json", topn=5) -> list:
    with open(mevzuat_json_path, "r", encoding="utf-8") as f:
        mevzuat_db = json.load(f)
    query_emb = get_embedding(metin)
    skorlar = [(cosine_sim(query_emb, m["embedding"]), m) for m in mevzuat_db]
    skorlar.sort(key=lambda x: x[0], reverse=True)
    return [m for _, m in skorlar[:topn]]

def en_benzer_ictihat(metin: str, ictihat_json_path="ictihat_db.json", topn=3) -> list:
    with open(ictihat_json_path, "r", encoding="utf-8") as f:
        ictihat_db = json.load(f)
    query_emb = get_embedding(metin)
    skorlar = [(cosine_sim(query_emb, i["embedding"]), i) for i in ictihat_db]
    skorlar.sort(key=lambda x: x[0], reverse=True)
    return [i for _, i in skorlar[:topn]]

if __name__ == "__main__":
    # Basit test
    test_metin = "Bir kişinin rızası dışında evine girilmiştir."
    print("En yakın mevzuat maddeleri:")
    for m in en_benzer_madde(test_metin):
        print(f"{m['tip']} {m['madde']}: {m['baslik']}")
    print("\nEn yakın içtihatlar:")
    for i in en_benzer_ictihat(test_metin):
        print(f"{i['esas']}/{i['karar']}: {i['ozet']}")

