-- Records are ordered by descending scores.
SELECT `score`, `name`
FROM `second_table` WHERE `name` != "" ORDER BY `score` DESC;
