lontara_to_latin = str.maketrans({
    "ᨀ":"ka",
    "ᨁ":"ga",
    "ᨂ":"nga",
    "ᨃ":"ngka",
    "ᨄ":"pa",
    "ᨅ":"ba",
    "ᨆ":"ma",
    "ᨇ":"mpa",
    "ᨈ":"ta",
    "ᨉ":"da",
    "ᨊ":"na",
    "ᨋ":"nra",
    "ᨌ":"ca",
    "ᨍ":"ja",
    "ᨎ":"nya",
    "ᨏ":"nca",
    "ᨐ":"ya",
    "ᨑ":"ra",
    "ᨒ":"la",
    "ᨓ":"wa",
    "ᨔ":"sa",
    "ᨕ":"a",
    "ᨖ":"ha","ᨗ":"i","ᨘ":"u","ᨙ":"é","ᨚ":"o","ᨛ":"e","᨞":",","᨟":"."
})

def remove_one_char_before_vowel(text):
    result = []
    skip_next = False

    for i, char in enumerate(text):
        if skip_next:
            skip_next = False
            continue

        if char == 'i':
            if i > 0:
                result.pop()
        if char == 'u':
            if i > 0:
                result.pop()
        if char == 'é':
            if i > 0:
                result.pop()
        if char == 'o':
            if i > 0:
                result.pop()
        if char == 'e':
            if i > 0:
                result.pop()
                result.append('e')
        else:
            result.append(char)

    return ''.join(result)

def angka_ke_kata(angka):
    # Daftar kata dalam bahasa Indonesia untuk angka 0 hingga 9
    kata = ["ᨊᨚᨒᨚ", "ᨔᨙᨉᨗ", "ᨉᨘᨕ", "ᨈᨛᨒᨘ", "ᨕᨛᨄ", "ᨒᨗᨆ", "ᨕᨛᨊᨛ", "ᨄᨗᨈᨘ", "ᨕᨑᨘᨕ", "ᨕᨔᨙᨑ"]

    # Daftar kata khusus untuk angka 10 hingga 19
    kata_khusus = ["ᨔᨛᨄᨘᨒᨚ", "ᨔᨛᨄᨘᨒᨚ ᨔᨙᨉᨗ", "ᨔᨛᨄᨘᨒᨚ ᨉᨘᨕ", "ᨔᨛᨄᨘᨒᨚ ᨈᨛᨒᨘ", "ᨔᨛᨄᨘᨒᨚ ᨕᨛᨄ", "ᨔᨛᨄᨘᨒᨚ ᨒᨗᨆ", "ᨔᨛᨄᨘᨒᨚ ᨕᨛᨊᨛ", "ᨔᨛᨄᨘᨒᨚ ᨄᨗᨈᨘ", "ᨔᨛᨄᨘᨒᨚ ᨕᨑᨘᨕ", "ᨔᨛᨄᨘᨒᨚ ᨕᨔᨙᨑ"]

    # Daftar kata untuk puluhan
    #Terjadi perubahan penyebutan Empat menjadi PATA ketika dia diawal bilangan, bukan akhiran untuk puluhan
    puluhan = ["", "ᨔᨛᨄᨘᨒᨚ", "ᨉᨘᨕᨄᨘᨒᨚ", "ᨈᨛᨒᨘᨄᨘᨒᨚ", "ᨄᨈᨄᨘᨒᨚ", "ᨒᨗᨆᨄᨘᨒᨚ", "ᨕᨛᨊᨛᨄᨘᨒᨚᨊ", "ᨄᨗᨈᨘᨄᨘᨒᨚ", "ᨕᨑᨘᨕᨄᨘᨒᨚᨊ", "ᨕᨔᨙᨑᨄᨘᨒᨚᨊ"]

    # Daftar kata untuk ratusan
    # angka ratus dalam angka 400 berubah menjadi DATU
    #Terjadi penyisipan NA di bilangan 6-8-9, di posisi bilangan Puluhan dan Ratusan, tidak pada Ribuan ke atas
    ratusan = ["", "ᨔᨗᨑᨈᨘ", "ᨉᨘᨕᨑᨈᨘ", "ᨈᨛᨒᨘᨑᨈᨘ", "ᨕᨛᨄᨉᨈᨘ", "ᨒᨗᨆᨑᨈᨘ", "ᨕᨛᨊᨛᨑᨈᨘᨊ", "ᨄᨗᨈᨘᨑᨈᨘ", "ᨕᨑᨘᨕᨑᨈᨘᨊ", "ᨕᨔᨙᨑᨑᨈᨘᨊ"]

    ribuan = ["", "ᨔᨗᨔᨛᨅᨘ", "ᨉᨘᨕᨔᨛᨅᨘ", "ᨈᨛᨒᨘᨔᨛᨅᨘ", "ᨄᨈᨔᨛᨅᨘ", "ᨒᨗᨆᨔᨛᨅᨘ", "ᨕᨛᨊᨛᨔᨛᨅᨘ", "ᨄᨗᨈᨘᨔᨛᨅᨘ", "ᨕᨑᨘᨕᨔᨛᨅᨘ", "ᨕᨔᨙᨑᨔᨛᨅᨘ"]


    # Konversi angka menjadi string
    angka_str = str(angka)

    if angka == 0:
        return kata[0]  # Angka nol

    if angka < 10:
        return kata[angka]  # Angka 1 hingga 9

    if 10 <= angka < 20:
        return kata_khusus[angka - 10]  # Angka 10 hingga 19

    if 20 <= angka < 100:
        puluhan_idx = angka // 10
        satuan_idx = angka % 10
        return puluhan[puluhan_idx] + " " + kata[satuan_idx] if satuan_idx != 0 else puluhan[puluhan_idx]  # Puluhan

    if 100 <= angka < 1000:
        ratusan_idx = angka // 100
        sisanya = angka % 100
        if sisanya == 0:
            return ratusan[ratusan_idx]  # Ratusan tanpa puluhan
        else:
            return ratusan[ratusan_idx] + " " + angka_ke_kata(sisanya)  # Ratusan dengan puluhan

    if 1000 <= angka < 1000000: # ribuan
        ribuan_idx = angka // 1000
        sisanya = angka % 1000
        if sisanya == 0 and ribuan_idx < 10:
            return ribuan[ribuan_idx]  # Ribuan tanpa ratuan
        elif sisanya == 0 and 10 <= ribuan_idx < 1000:
            return angka_ke_kata(ribuan_idx) + " " + "ᨔᨛᨅᨘ"
        else:
            return angka_ke_kata(ribuan_idx) + " " + "ᨔᨛᨅᨘ" + " " + angka_ke_kata(sisanya)  # Ribuan dengan ratusan dan puluhan

    if 1000000 <= angka < 1000000000000000: #juta, miliar, triliun
        if 1000000 <= angka < 1000000000: # jutaan
          jutaan_idx = angka // 1000000
          sisanya = angka % 1000000
          if 1 <= jutaan_idx < 1000:
              if sisanya == 0 :
                  return angka_ke_kata(jutaan_idx) + " " + "ᨍᨘᨈ"
              else:
                  return angka_ke_kata(jutaan_idx) + " " + "ᨍᨘᨈ" + " "+ angka_ke_kata(sisanya)

        elif 1000000000 <= angka < 1000000000000: # miliaran
          miliaran_idx = angka // 1000000000
          sisanya = angka % 1000000000
          if 1 <= miliaran_idx < 1000:
              if sisanya == 0 :
                  return angka_ke_kata(miliaran_idx) + " " + "ᨆᨗᨒᨗᨕᨑᨛ"
              else:
                  return angka_ke_kata(miliaran_idx) + " " + "ᨆᨗᨒᨗᨕᨑᨛ" + " "+ angka_ke_kata(sisanya)
        elif 1000000000000 <= angka < 1000000000000000:
          triliun_idx = angka // 1000000000000 # triliun
          sisanya = angka % 1000000000000
          if 1 <= triliun_idx < 1000:
              if sisanya == 0 :
                  return angka_ke_kata(triliun_idx) + " " + "ᨈᨑᨒᨗᨕᨘ"
              else:
                  return angka_ke_kata(triliun_idx) + " " + "ᨈᨑᨒᨗᨕᨘ" + " "+ angka_ke_kata(sisanya)

    return "ᨔᨛᨊ ᨆᨒᨚᨄᨚ ᨊᨚᨆᨚᨑᨚᨊ"  # Angka lebih dari 1000 (untuk contoh ini)

# Fungsi untuk mengubah angka menjadi kata dalam sebuah kalimat
def number_expand(kalimat):
    kata_kalimat = kalimat.split()
    for i, kata in enumerate(kata_kalimat):
        if kata.isdigit():
            kata_kalimat[i] = angka_ke_kata(int(kata))
    kalimat_hasil = " ".join(kata_kalimat)
    return kalimat_hasil

import re
from unidecode import unidecode

# Regular expression matching whitespace:
_whitespace_re = re.compile(r'\s+')

def lowercase(text):
  return text.lower()

#mengganti double spasi dengan spasi tunggal
def collapse_whitespace(text):
  return re.sub(_whitespace_re, ' ', text)

#mengubah teks yang mengandung karakter aksara atau karakter khusus lainnya ke dalam bentuk yang lebih umum atau standar
def convert_to_ascii(text):
  return unidecode(text)

def bugis_cleaners(text):
  '''Pipeline for lontara text, including number expansion.'''
  text = number_expand(text)
  text = text.translate(lontara_to_latin)
  text = remove_one_char_before_vowel(text)
  text = convert_to_ascii(text)
  text = lowercase(text)
  text = collapse_whitespace(text)
  return text