SELECT TOP (100) Title,
	   ViewCount,
	   HasMoreCommentsThanAVG = CASE WHEN CommentCount > (SELECT AVG(CommentCount) FROM Posts WHERE PostTypeId = 1) THEN 1 ELSE 0 END
FROM Posts
WHERE PostTypeId = 1 AND Title LIKE '%SQL%'
ORDER BY ViewCount DESC