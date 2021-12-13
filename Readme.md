# 1. Employee Turnover Prediction Web App
Hasil Pengerjaan Tugas Besar II4042 Artificial Intelligence for Business 

Kelompok 2 dengan anggota:
- Vhydie Gilang C. T. – 18218016
- Akbar Rizki M. – 18218023
- Tafia Alifianty D. P. - 18218038

# 2. Table of Content
- [1. Employee Turnover Prediction Web App](#1-employee-turnover-prediction-web-app)
- [2. Table of Content](#2-table-of-content)
- [3. Deskripsi Masalah](#3-deskripsi-masalah)
- [4. Solusi](#4-solusi)
  - [4.1. Input](#41-input)
  - [4.2. Output](#42-output)
- [5. Panduan Penggunaan Employee Turnover Prediction Web App](#5-panduan-penggunaan-employee-turnover-prediction-web-app)
  - [5.1. Tata Cara Pengisian Data](#51-tata-cara-pengisian-data)
  - [5.2. Pengujian hasil "Karyawan akan meninggalkan perusahaan"](#52-pengujian-hasil-karyawan-akan-meninggalkan-perusahaan)
  - [5.3. Pengujian hasil "Karyawan tidak akan meninggalkan perusahaan"](#53-pengujian-hasil-karyawan-tidak-akan-meninggalkan-perusahaan)

# 3. Deskripsi Masalah
Employee turnover, atau keluarnya karyawan dari perusahaan, merupakan sebuah permasalahan yang seringkali dihadapi oleh sebuah perusahaan. Dampaknya bisa besar, karena semakin banyak karyawan yang keluar dari perusahaan maka semakin berkurang sumber daya manusia yang dimiliki oleh perusahaan.

Itulah permasalahan yang dihadapi PT Bank Danamon Indonesia Tbk. saat ini. Bank Danamon mengalami penyusutan jumlah karyawan yang drastis selama 3 tahun ke belakang. Tentu upaya-upaya untuk mengurangi employee turnover perlu dilakukan. Untuk dapat melakukan upaya-upaya dengan lebih tepat-sasaran, HR membutuhkan suatu cara untuk mengetahui apakah seorang karyawan memiliki kecenderungan untuk keluar atau tetap bekerja di Bank Danamon.

Untuk dapat menjawab permasalahan di atas, dibuatlah KBS Data Science untuk memprediksi apakah seorang karyawan akan meninggalkan perusahaan atau tetap bekerja di sebuah perusahaan.

# 4. Solusi
Solusi yang dibuat adalah sebuah AI yang mampu memprediksi apakah seorang karyawan akan meninggalkan perusahaan atau tetap bekerja di perusahaan berdasarkan beberapa masukan. Jenis AI yang dibuat adalah AI untuk klasifikasi, dan metode yang digunakan adalah metode Decision Tree dengan ketepatan sebesar 98%.

## 4.1. Input
Data yang dimasukkan berupa:
- 'RandD_true' = apakah karyawan bekerja di departemen RnD
- 'hr_true' = apakah karyawan bekerja di departemen HR
- 'management_true' = apakah karyawan bekerja di departemen Management
- 'satisfaction_level' = seberapa besar tingkat kepuasan karyawan bekerja di perusahaan
- 'last_evaluation' = seberapa besar nilai yang diberikan kepada karyawan pada sesi evaluasi terakhir
- 'number_project' = seberapa banyak proyek yang sudah ditangani oleh karyawan
- 'average_montly_hours' = seberapa lama rata-rata jam kerja karyawan
- 'time_spend_company' = seberapa lama karyawan telah bekerja di perusahaan
- 'Work_accident' = seberapa banyak insiden/kecelakaan pada pekerjaan yang dialami karyawan
- 'promotion_last_5years' = seberapa banyak promosi yang dialami karyawan dalam 5 tahun terakhir

## 4.2. Output
Luaran yang dihasilkan berupa angka 0 atau 1 dengan deskripsi berikut:
- 1 menyatakan bahwa karyawan sangat mungkin meninggalkan perusahaan
- 0 menyatakan bahwa karyawan sangat mungkin tetap bekerja di perusahaan

# 5. Panduan Penggunaan Employee Turnover Prediction Web App
Pengguna dapat mengakses Employee Turnover Prediction Web App menggunakan link berikut: https://share.streamlit.io/tafiaalifianty/webapp/main/deploy_streamlit.py 


## 5.1. Tata Cara Pengisian Data
Untuk menggunakannya, pengguna hanya perlu memasukkan data-data yang relevan, lalu menunggu sebentar, kemudian melihat hasil pada bagian Hasil Prediksi.
- 'RandD_true' = Diisi dengan 1 jika karyawan bekerja di departemen ini, selain itu 0.
- 'hr_true' = Diisi dengan 1 jika karyawan bekerja di departemen ini, selain itu 0.
- 'management_true' = Diisi dengan 1 jika karyawan bekerja di departemen ini, selain itu 0.
- 'satisfaction_level' = Diisi dengan level kepuasan karyawan, dari 0.50 - 1.00
- 'last_evaluation' = Diisi dengan penilaian evaluasi karyawan, dari 0.50 - 1.00
- 'number_project' = Diisi dengan jumlah proyek yang dikerjakan, minimal 1 (proyek)
- 'average_montly_hours' = Diisi dengan rata-rata rasio durasi kerja karyawan, dari 0.50 - 1.00
- 'time_spend_company' = Diisi dengan jumlah waktu yang dihabisan di perusahaan yang dikerjakan, minimal 1 (tahun)
- 'Work_accident' = Diisi dengan jumlah kecelakaan kerja yang terjadi, minimal 0 (kecelakaan)
- 'promotion_last_5years' = Diisi dengan jumlah promosi yang diberikan, minimal 1 (kali promosi)

## 5.2. Pengujian hasil "Karyawan akan meninggalkan perusahaan"
Untuk melakukan uji coba mendapatkan hasil 1 (Karyawan akan meninggalkan perusahaan), pengguna dapat memasukkan data berikut ini:
- 'RandD_true' = 1
- 'hr_true' = 0
- 'management_true' = 0
- 'satisfaction_level' = 0.64
- 'last_evaluation' = 0.75
- 'number_project' = 2
- 'average_montly_hours' = 0.55
- 'time_spend_company' = 2
- 'Work_accident' = 2
- 'promotion_last_5years' = 1

## 5.3. Pengujian hasil "Karyawan tidak akan meninggalkan perusahaan"
Untuk melakukan uji coba mendapatkan hasil 0 (Karyawan tidak akan meninggalkan perusahaan), pengguna dapat memasukkan data berikut ini:
- 'RandD_true' = 0
- 'hr_true' = 0
- 'management_true' = 1
- 'satisfaction_level' = 1.00 
- 'last_evaluation' = 1.00
- 'number_project' = 5
- 'average_montly_hours' = 1.00
- 'time_spend_company' = 6
- 'Work_accident' = 0
- 'promotion_last_5years' = 1