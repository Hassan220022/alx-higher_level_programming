-- Convert the database character set and collation
ALTER DATABASE hbtn_0c_0
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Convert the table character set and collation
ALTER TABLE first_table
    CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Specifically convert the 'name' field in 'first_table' to use UTF8
ALTER TABLE first_table
    MODIFY name VARCHAR(256)
    CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
