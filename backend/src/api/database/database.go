package database

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	"github.com/go-sql-driver/mysql"
)

var db *sql.DB

type InfoRaw struct {
	Id        int64
	Path      string
	Title     string
	Album     sql.NullString
	Artist    sql.NullString
	ArtworkId sql.NullInt64
}

type Info struct {
	Id        int64
	Path      string
	Title     string
	Album     string
	Artist    string
	ArtworkId int64
}

func connectDb() {
	cfg := mysql.Config{
		User:   "root",
		Passwd: os.Getenv("MYSQL_ROOT_PASSWORD"),
		Net:    "tcp",
		Addr:   "music:3306",
		DBName: "music_player",
	}

	var err error
	db, err = sql.Open("mysql", cfg.FormatDSN())
	if err != nil {
		log.Fatal(err)
	}

	pingErr := db.Ping()
	if pingErr != nil {
		log.Fatal(pingErr)
	}
	fmt.Println("Connected!")
}

func GetInfoAll() ([]Info, error) {
	connectDb()
	defer db.Close()

	var infoList []Info
	rows, err := db.Query("SELECT * FROM info")
	if err != nil {
		return nil, fmt.Errorf("getInfoAll %v", err)
	}
	defer rows.Close()

	for rows.Next() {
		var infoRaw InfoRaw
		var info Info

		if err := rows.Scan(&infoRaw.Id, &infoRaw.Path, &infoRaw.Title, &infoRaw.Album, &infoRaw.Artist, &infoRaw.ArtworkId); err != nil {
			return nil, fmt.Errorf("getInfoAll %v", err)
		}

		info = convertInfo(infoRaw)
		infoList = append(infoList, info)
	}
	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("getInfoAll %v", err)
	}

	return infoList, nil
}

func convertInfo(infoRaw InfoRaw) (info Info) {
	info.Id, info.Path, info.Title = infoRaw.Id, infoRaw.Path, infoRaw.Title

	if infoRaw.Album.Valid {
		info.Album = infoRaw.Album.String
	} else {
		info.Album = ""
	}

	if infoRaw.Artist.Valid {
		info.Artist = infoRaw.Artist.String
	} else {
		info.Artist = ""
	}

	if infoRaw.ArtworkId.Valid {
		info.ArtworkId = infoRaw.ArtworkId.Int64
	} else {
		info.ArtworkId = 0
	}

	return info
}
