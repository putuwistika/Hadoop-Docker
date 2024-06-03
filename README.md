# Proyek Docker-Hadoop dan PostgreSQL dengan API Pokemon

Proyek ini mencakup beberapa layanan yang dikonfigurasi menggunakan Docker. Proyek ini bertujuan untuk mengambil data dari API Pokemon, menyimpannya ke dalam database PostgreSQL, dan kemudian mengunggah data tersebut ke Hadoop HDFS dalam bentuk file CSV.

## Struktur Proyek

- `Dockerfile.api`
- `Dockerfile.postgres`
- `docker-compose.yaml`
- `config`
- `src/init.sql`
- `src/poke_api.py`
- `src/requirements.txt`
- `request/post-pokemon_ability_id.py`
- `request/post-upload_file_csv.py`

## Langkah-Langkah Membangun dan Menjalankan Proyek

1. **Build dan Jalankan Layanan dengan Docker Compose**

    Jalankan perintah berikut untuk membangun dan menjalankan layanan yang didefinisikan dalam `docker-compose.yaml`:

    ```sh
    docker-compose up --build
    ```

2. **Memasukkan Data `pokemon_ability_id` ke PostgreSQL**

    Untuk memasukkan data `pokemon_ability_id` ke PostgreSQL menggunakan script Python `request/post-pokemon_ability_id.py`, jalankan perintah berikut:

    ```sh
    python3 request/post-pokemon_ability_id.py
    ```

    Script ini akan mengambil data dari API "https://pokeapi.co/api/v2/ability/" + pokemon_ability_id untuk ability id dari 1 hingga 999 dan akan menambahkannya ke database PostgreSQL.

3. **Upload Data dari PostgreSQL ke HDFS**

    Untuk meng-upload data dari PostgreSQL ke HDFS menggunakan API ke HDFS, jalankan script Python `request/post-upload_file_csv.py`:

    ```sh
    python3 request/post-upload_file_csv.py
    ```

    **Catatan:** Pastikan untuk mengganti URL sesuai dengan IP publik Anda pada script yang relevan.

## Penjelasan Port Layanan

Berikut adalah port-port yang terbuka dan fungsinya:

- **PostgreSQL**: 
  - Port `2102:5432` digunakan untuk mengakses database PostgreSQL. Database ini menyimpan data `pokemon_ability_id`.

- **API Pokemon**: 
  - Port `8000:8000` digunakan untuk mengakses API Pokemon. API ini memungkinkan interaksi dengan data Pokemon yang disimpan di PostgreSQL.

- **Hadoop HDFS Namenode**:
  - Port `9870:9870` digunakan untuk mengakses UI Hadoop HDFS Namenode. UI ini memungkinkan Anda untuk mengelola dan memonitor sistem file terdistribusi HDFS.

- **Hadoop YARN Resource Manager**:
  - Port `8088:8088` digunakan untuk mengakses UI YARN Resource Manager. UI ini memungkinkan Anda untuk mengelola dan memonitor sumber daya dalam cluster Hadoop.

## Menghubungkan ke PostgreSQL dengan DBeaver

1. **Buka DBeaver** dan buat koneksi baru.
2. Pilih **PostgreSQL** sebagai database.
3. Masukkan detail koneksi sebagai berikut:
    - **Host:** `localhost`
    - **Port:** `2102`
    - **Database:** `pokemon_db`
    - **Username:** `pokemon`
    - **Password:** `Dev1!`
4. Klik **Test Connection** untuk memastikan koneksi berhasil, lalu klik **Finish**.

## Menghentikan Layanan
Untuk menghentikan semua layanan, jalankan perintah berikut:

```sh
docker-compose down
```






