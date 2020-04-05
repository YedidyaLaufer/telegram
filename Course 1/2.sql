SELECT *
FROM Users
WHERE LEN(DisplayName) = (SELECT AVG(LEN(DisplayName)) FROM Users)