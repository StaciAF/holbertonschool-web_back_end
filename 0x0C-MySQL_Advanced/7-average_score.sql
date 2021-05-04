-- this script creates a stored procedure
-- computes and stores avg student score
DELIMITER $$
CREATE PROCEDURE ComputeAverageScoreForUser (IN user_id INT)
BEGIN
    SET @average = (
        SELECT AVG(score)
        FROM corrections
        WHERE corrections.user_id = user_id)

    UPDATE users
    SET average_score = @average
    WHERE id = user_id;
END$$

DELIMITER ;
