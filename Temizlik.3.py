file_path = "Günlük_Adım_Sayısı_Cleaned.xml"  # Orijinal XML dosya yolu
output_path = "Günlük_Adım_Sayısı_Final.xml"  # Düzeltilmiş dosya kaydedilecek yol

# Dosyayı oku
with open(file_path, "r", encoding="utf-8") as file:
    xml_content = file.read()

# Hatalı `<` ve `>` sembollerini düzeltme
# Geçersiz olanlar kaçış dizgelerine çevriliyor
xml_content_fixed = xml_content.replace("<<", "&lt;").replace(">>", "&gt;")

# Temizlenmiş dosyayı kaydet
with open(output_path, "w", encoding="utf-8") as file:
    file.write(xml_content_fixed)

print(f"Düzeltilmiş XML dosyası kaydedildi: {output_path}")
