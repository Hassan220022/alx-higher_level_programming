-- Select the score and name columns where score >= 10, ordered by score (top first)
SELECT
    score,
    name
FROM
    second_table
WHERE
    score >= 10
ORDER BY
    score DESC;