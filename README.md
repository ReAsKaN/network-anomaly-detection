# Network Traffic Anomaly Detection 🛡️📊

Bu proje, ağ trafiğindeki anormallikleri ve olası siber saldırı girişimlerini tespit etmek amacıyla geliştirilmiş bir makine öğrenmesi (Machine Learning) çözümüdür. Kapsamlı bir siber güvenlik analizi için **UNSW-NB15** veri seti kullanılarak eğitilmiş bir **Random Forest (Rastgele Orman)** sınıflandırıcısı içermektedir.

## 🚀 Proje Özellikleri

* **Makine Öğrenmesi ile Tehdit Tespiti:** Ağ paketlerindeki normal ve anormal (malicious) davranışları ayırt edebilen yüksek doğruluklu model.
* **Kapsamlı Veri Analizi:** UNSW-NB15 veri seti üzerinde gerçekleştirilen veri ön işleme, özellik mühendisliği (feature engineering) ve boyut indirgeme adımları.
* **Kullanıcı Dostu Arayüz:** Ağ durumu ve analiz sonuçlarını görselleştirmek için `dashboard.py` üzerinden çalışan interaktif kontrol paneli.
* **Performans Optimizasyonu:** Hızlı tahminleme ve düşük kaynak tüketimi ile verimli çalışma altyapısı.

## 🛠️ Kullanılan Teknolojiler

* **Programlama Dili:** Python 3.12
* **Veri İşleme & Analizi:** Pandas, NumPy
* **Makine Öğrenmesi:** Scikit-Learn (Random Forest Classifier)
* **Görselleştirme & Arayüz:** Matplotlib / Seaborn (Dashboard bileşenleri)

## 📂 Veri Seti Hakkında (UNSW-NB15)

Dosya boyutu kısıtlamaları ve GitHub politikaları gereği (`.gitignore` yapılandırması ile) eğitim ve test veri setleri (`.csv` dosyaları) bu depoya **dahil edilmemiştir**. Projeyi yerel ortamınızda çalıştırmak için orijinal veri setini indirmeniz gerekmektedir:

1. [UNSW-NB15 Dataset](https://research.unsw.edu.au/projects/unsw-nb15-dataset) adresine gidin.
2. İlgili CSV dosyalarını (`UNSW_NB15_testing-set.csv` ve `UNSW_NB15_training-set.csv`) indirin.
3. Dosyaları projenin ana dizinine yerleştirin.

## ⚙️ Kurulum ve Çalıştırma

Projeyi kendi bilgisayarınızda çalıştırmak için aşağıdaki adımları izleyin:

**1. Depoyu Klonlayın:**
```bash
git clone [https://github.com/ReAsKaN/network-anomaly-detection.git](https://github.com/ReAsKaN/network-anomaly-detection.git)
cd network-anomaly-detection
