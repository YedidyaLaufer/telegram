SELECT Id,
	   DisplayName,
	   Location
FROM Users
Where Id IN (SELECT UserId FROM Badges WHERE Name = 'Guru') 