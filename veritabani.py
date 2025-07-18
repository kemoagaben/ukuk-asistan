import json
import numpy as np

class Mevzuat:
    def __init__(self, tip, madde, baslik, metin, gerekce="", embedding=None):
        self.tip = tip
        self.madde = madde
        self.baslik = baslik
        self.metin = metin
        self.gerekce = gerekce
        self.embedding = embedding if embedding is not None else np.random.rand(384).tolist()

    def to_dict(self):
        return {
            "tip": self.tip,
            "madde": self.madde,
            "baslik": self.baslik,
            "metin": self.metin,
            "gerekce": self.gerekce,
            "embedding": self.embedding
        }

class Ictihat:
    def __init__(self, esas, karar, ozet, tam_metin="", tarih="", embedding=None):
        self.esas = esas
        self.karar = karar
        self.ozet = ozet
        self.tam_metin = tam_metin
        self.tarih = tarih
        self.embedding = embedding if embedding is not None else np.random.rand(384).tolist()

    def to_dict(self):
        return {
            "esas": self.esas,
            "karar": self.karar,
            "ozet": self.ozet,
            "tam_metin": self.tam_metin,
            "tarih": self.tarih,
            "embedding": self.embedding
        }

# Demo dummy veri
mevzuat_db = [
    Mevzuat("Anayasa", "21", "Konut dokunulmazlığı", "Kimsenin konutuna dokunulamaz...", "Konut dokunulmazlığı Anayasal bir haktır."),
    Mevzuat("Kanun", "TCK 116", "Konut dokunulmazlığının ihlali", "Bir kimsenin konutuna rızası olmadan giren kişi cezalandırılır.", "Ceza Kanunu'nda konut dokunulmazlığı koruma altındadır."),
    Mevzuat("Kanun", "TMK 25", "Kişilik haklarının korunması", "Hukuka aykırı olarak kişilik hakkı saldırıya uğrayan kişi, saldırının önlenmesini dava edebilir.", "Kişilik hakları özel hukukta ayrıca korunur."),
]

ictihat_db = [
    Ictihat("2019/2345", "2020/1234", "Sanığın mağdurun evine izinsiz girdiği ve konut dokunulmazlığını ihlal ettiği sabittir.", tarih="20.03.2020"),
]

# Dosyaya kaydetme (ileri aşama için)
def save_json():
    with open("mevzuat_db.json", "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in mevzuat_db], f, ensure_ascii=False, indent=2)
    with open("ictihat_db.json", "w", encoding="utf-8") as f:
        json.dump([i.to_dict() for i in ictihat_db], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    save_json()
    print("mevzuat_db.json ve ictihat_db.json dosyaları oluşturuldu.")
import json
import numpy as np

class Mevzuat:
    def __init__(self, tip, madde, baslik, metin, gerekce="", embedding=None):
        self.tip = tip
        self.madde = madde
        self.baslik = baslik
        self.metin = metin
        self.gerekce = gerekce
        self.embedding = embedding if embedding is not None else np.random.rand(384).tolist()

    def to_dict(self):
        return {
            "tip": self.tip,
            "madde": self.madde,
            "baslik": self.baslik,
            "metin": self.metin,
            "gerekce": self.gerekce,
            "embedding": self.embedding
        }

class Ictihat:
    def __init__(self, esas, karar, ozet, tam_metin="", tarih="", embedding=None):
        self.esas = esas
        self.karar = karar
        self.ozet = ozet
        self.tam_metin = tam_metin
        self.tarih = tarih
        self.embedding = embedding if embedding is not None else np.random.rand(384).tolist()

    def to_dict(self):
        return {
            "esas": self.esas,
            "karar": self.karar,
            "ozet": self.ozet,
            "tam_metin": self.tam_metin,
            "tarih": self.tarih,
            "embedding": self.embedding
        }

# Demo dummy veri
mevzuat_db = [
    Mevzuat("Anayasa", "21", "Konut dokunulmazlığı", "Kimsenin konutuna dokunulamaz...", "Konut dokunulmazlığı Anayasal bir haktır."),
    Mevzuat("Kanun", "TCK 116", "Konut dokunulmazlığının ihlali", "Bir kimsenin konutuna rızası olmadan giren kişi cezalandırılır.", "Ceza Kanunu'nda konut dokunulmazlığı koruma altındadır."),
    Mevzuat("Kanun", "TMK 25", "Kişilik haklarının korunması", "Hukuka aykırı olarak kişilik hakkı saldırıya uğrayan kişi, saldırının önlenmesini dava edebilir.", "Kişilik hakları özel hukukta ayrıca korunur."),
]

ictihat_db = [
    Ictihat("2019/2345", "2020/1234", "Sanığın mağdurun evine izinsiz girdiği ve konut dokunulmazlığını ihlal ettiği sabittir.", tarih="20.03.2020"),
]

# Dosyaya kaydetme (ileri aşama için)
def save_json():
    with open("mevzuat_db.json", "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in mevzuat_db], f, ensure_ascii=False, indent=2)
    with open("ictihat_db.json", "w", encoding="utf-8") as f:
        json.dump([i.to_dict() for i in ictihat_db], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    save_json()
    print("mevzuat_db.json ve ictihat_db.json dosyaları oluşturuldu.")
import json
import numpy as np

class Mevzuat:
    def __init__(self, tip, madde, baslik, metin, gerekce="", embedding=None):
        self.tip = tip
        self.madde = madde
        self.baslik = baslik
        self.metin = metin
        self.gerekce = gerekce
        self.embedding = embedding if embedding is not None else np.random.rand(384).tolist()

    def to_dict(self):
        return {
            "tip": self.tip,
            "madde": self.madde,
            "baslik": self.baslik,
            "metin": self.metin,
            "gerekce": self.gerekce,
            "embedding": self.embedding
        }

class Ictihat:
    def __init__(self, esas, karar, ozet, tam_metin="", tarih="", embedding=None):
        self.esas = esas
        self.karar = karar
        self.ozet = ozet
        self.tam_metin = tam_metin
        self.tarih = tarih
        self.embedding = embedding if embedding is not None else np.random.rand(384).tolist()

    def to_dict(self):
        return {
            "esas": self.esas,
            "karar": self.karar,
            "ozet": self.ozet,
            "tam_metin": self.tam_metin,
            "tarih": self.tarih,
            "embedding": self.embedding
        }

# Demo dummy veri
mevzuat_db = [
    Mevzuat("Anayasa", "21", "Konut dokunulmazlığı", "Kimsenin konutuna dokunulamaz...", "Konut dokunulmazlığı Anayasal bir haktır."),
    Mevzuat("Kanun", "TCK 116", "Konut dokunulmazlığının ihlali", "Bir kimsenin konutuna rızası olmadan giren kişi cezalandırılır.", "Ceza Kanunu'nda konut dokunulmazlığı koruma altındadır."),
    Mevzuat("Kanun", "TMK 25", "Kişilik haklarının korunması", "Hukuka aykırı olarak kişilik hakkı saldırıya uğrayan kişi, saldırının önlenmesini dava edebilir.", "Kişilik hakları özel hukukta ayrıca korunur."),
]

ictihat_db = [
    Ictihat("2019/2345", "2020/1234", "Sanığın mağdurun evine izinsiz girdiği ve konut dokunulmazlığını ihlal ettiği sabittir.", tarih="20.03.2020"),
]

# Dosyaya kaydetme (ileri aşama için)
def save_json():
    with open("mevzuat_db.json", "w", encoding="utf-8") as f:
        json.dump([m.to_dict() for m in mevzuat_db], f, ensure_ascii=False, indent=2)
    with open("ictihat_db.json", "w", encoding="utf-8") as f:
        json.dump([i.to_dict() for i in ictihat_db], f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    save_json()
    print("mevzuat_db.json ve ictihat_db.json dosyaları oluşturuldu.")

