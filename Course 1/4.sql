SELECT DisplayName,
	   AboutMe,
	   LEN(AboutMe),
	   IsBio = CASE 
					WHEN AboutMe IS NULL OR AboutMe = '' THEN DisplayName + ' kept mystery'
					WHEN LEN(AboutMe) <= (SELECT AVG(LEN(AboutMe)) FROM Users WHERE AboutMe IS NOT NULL AND AboutMe != '') THEN DisplayName + ' is not autobiograph'
					ELSE DisplayName + ' is autobiograph'
				END
FROM Users
WHERE DATEPART(YEAR, CreationDate) > 2016 OR (DATEPART(YEAR, CreationDate) = 2016 AND DATEPART(MONTH, CreationDate) > 6)
ORDER BY Id DESC