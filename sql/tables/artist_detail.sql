DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'artist_detail'
    ) THEN
        DROP TABLE artist_detail;
        RAISE NOTICE 'Table artist_detail dropped.';
    ELSE
        RAISE NOTICE 'Table artist_detail does not exist.';
    END IF;
END $$;

CREATE TABLE artist_detail (
  song_id VARCHAR(255),
  play_dt TIMESTAMP,
  PRIMARY KEY (song_id)
);

-- Artist
-- -----------------
-- Main Artist Image
-- Popularity Index
-- Total Plays (main channel)
-- Total Plays this month (main channel)
-- Average rating
-- Total ratings
-- SongsInInventory
-- Links: wikipedia website search amg

-- Albums
-- -----------
-- Album Title
-- Release Year
-- SongsInInventory
-- Info and Purchase Links

-- Songs
-- -----------
-- AlbumImage SongTitle AvgRating