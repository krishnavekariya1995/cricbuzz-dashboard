
-- Create Database
CREATE DATABASE IF NOT EXISTS cricket_db;

USE cricket_db;

-- Matches Table
CREATE TABLE IF NOT EXISTS matches (
    team1 VARCHAR(100),
    team2 VARCHAR(100),
    venue VARCHAR(200),
    city VARCHAR(100)
);

-- Sample Data (Optional)
INSERT INTO matches (team1, team2, venue, city) VALUES
('India', 'Australia', 'Wankhede Stadium', 'Mumbai'),
('England', 'Pakistan', 'Lords', 'London'),
('South Africa', 'New Zealand', 'Centurion Park', 'Centurion');