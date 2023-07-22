DO $$
BEGIN
    IF EXISTS (
        SELECT 1
        FROM information_schema.tables
        WHERE table_schema = 'public'
        AND table_name = 'hacker_news'
    ) THEN
        DROP TABLE hacker_news;
        RAISE NOTICE 'Table hacker_news dropped.';
    ELSE
        RAISE NOTICE 'Table hacker_news does not exist.';
    END IF;
END $$;

CREATE TABLE hacker_news (
  song_id VARCHAR(255),
  play_dt TIMESTAMP,
  PRIMARY KEY (song_id)
);

/*

  id            SERIAL PRIMARY KEY,
  line_content  VARCHAR(255),
  line_num      NUMERIC,
  line_url      VARCHAR(255),
  first_dt      TIMESTAMP,
  latest_dt     TIMESTAMP,
  duration_secs NUMERIC,
  duration_txt  VARCHAR(30),
  site_name_txt VARCHAR(100),
  perm_link     BOOLEAN DEFAULT FALSE,
  departed      BOOLEAN DEFAULT FALSE
  num_points    INTEGER,
  num_comments  INTEGER  

*/