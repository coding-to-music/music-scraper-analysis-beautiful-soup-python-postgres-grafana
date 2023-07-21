DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'play_history'
    ) THEN
        DROP TABLE play_history;
        RAISE NOTICE 'Table play_history dropped.';
    ELSE
        RAISE NOTICE 'Table play_history does not exist.';
    END IF;
END $$;

CREATE TABLE play_history (
  id                SERIAL PRIMARY KEY,
  play_dt           TIMESTAMP,
  song_id           NUMERIC,
  artist_and_song   VARCHAR(70),
  release_year      INTEGER,
  song_rating       NUMERIC(2,1),
  image_url         VARCHAR(70),
  song_url          VARCHAR(70)

--   PRIMARY KEY (line_content, site_name)
);

-- CREATE UNIQUE INDEX idx_unique_line_content_url ON scraper_history (line_content, line_url)
