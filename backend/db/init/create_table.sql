-- MusicPlayerデータベースの作成
CREATE DATABASE IF NOT EXISTS MusicPlayer;

-- MusicPlayerデータベースを使用
USE MusicPlayer;

-- Infoテーブルの作成
CREATE TABLE IF NOT EXISTS Info (
    id INT AUTO_INCREMENT PRIMARY KEY,
    path NVARCHAR(255) NOT NULL,
    title NVARCHAR(255) NOT NULL,
    album NVARCHAR(255),
    artist NVARCHAR(255),
    artwork_id INT
);

-- Artworkテーブルの作成
CREATE TABLE IF NOT EXISTS Artwork (
    id INT AUTO_INCREMENT PRIMARY KEY,
    path NVARCHAR(255) NOT NULL
)