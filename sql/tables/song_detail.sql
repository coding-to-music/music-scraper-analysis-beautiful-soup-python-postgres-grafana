DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'song_detail'
    ) THEN
        DROP TABLE song_detail;
        RAISE NOTICE 'Table song_detail dropped.';
    ELSE
        RAISE NOTICE 'Table song_detail does not exist.';
    END IF;
END $$;

CREATE TABLE song_detail (
  song_id VARCHAR(255),
  play_dt TIMESTAMP,
  PRIMARY KEY (song_id)
);

-- ArtistName -- SongName
-- AlbumImage
-- Album
-- Avg Rating
-- Total ratings
-- Rating Distribution
-- Release Year
-- Length
-- Plays (last 30 days)
-- Lyrics

-- Links: ShareFB, Tweet, wiki, website, search, amg
-- Links: Amazon
-- Links: iTunes

-- Comments