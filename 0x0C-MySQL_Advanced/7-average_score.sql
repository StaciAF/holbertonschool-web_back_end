-- this script creates a stored procedure
-- computes and stores avg student score
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    UPDATE users
    SET @average = (SELECT AVG(score)
    FROM corrections
    WHERE corrections.user_id = user_id)
    WHERE id = user_id;
END$$
DELIMITER $$;
