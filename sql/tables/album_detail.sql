DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'album_detail'
    ) THEN
        DROP TABLE album_detail;
        RAISE NOTICE 'Table album_detail dropped.';
    ELSE
        RAISE NOTICE 'Table album_detail does not exist.';
    END IF;
END $$;

CREATE TABLE album_detail (
  song_id VARCHAR(255),
  play_dt TIMESTAMP,
  PRIMARY KEY (song_id)
);

-- AlbumImage
-- AlbumName
-- ArtistName

-- AmazonLinks
-- iTunesLinks

-- ReleaseDate
-- Links: WikiSearch WebSearch AmgSearch

-- Songs
-- ----------------
-- SongsInInventory
-- SongName(Title) 
-- AvgRating 
