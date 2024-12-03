channel_insert = "INSERT INTO Channel (channel_id,channel_name, channel_description,channel_publishedAt,playlists_id,channel_sub_count,channel_viewCount,channel_videoCount) VALUES (%s, %s,%s,%s,%s,%s,%s,%s)"


comment_insert = "INSERT INTO Comment(Comment_Id,Comment_Text,Comment_Author,Comment_PublishedAt,Channel_id,video_id) VALUES(%s, %s,%s,%s,%s,%s)"

video_insert = "INSERT INTO Video(Video_Id,Video_Name,Video_Description,Channel_id,commentCount,view_Count,like_count,dis_like_Count,durations,published_date) VALUES(%s, %s,%s,%s,%s,%s, %s,%s,%s,%s)"

question_one = "SELECT Video.Video_Name AS videoName,Channel.channel_name AS channelName FROM Video JOIN Channel ON Channel.channel_id = Video.Channel_id"

question_two = "SELECT channel_name AS channelName, channel_videoCount FROM Channel  ORDER BY channel_videoCount DESC LIMIT 3"

question_three = "SELECT Video.Video_Name AS videoName, Channel.channel_name AS channelName FROM Video JOIN Channel ON Channel.channel_id = Video.Channel_id ORDER BY Video.view_Count DESC LIMIT 10"

question_four = "SELECT commentCount AS comment_Count , Video_Name FROM Video"

question_five = "SELECT Video.like_count AS like_count, Channel.channel_name AS channel_name FROM Video JOIN Channel ON Channel.channel_id = Video.Channel_id ORDER BY Video.like_count DESC LIMIT 3"

question_six = "SELECT Video_Name,(ROUND(SUM(Video.like_count + Video.dis_like_Count), 0)) AS total_likes_dislike FROM Video GROUP BY Video_Name"

question_seven = "SELECT channel_viewCount AS Total_view_Count,channel_name FROM Channel"

question_eight = "SELECT Video.Video_Name, Channel.channel_name, Video.published_date FROM Video JOIN Channel ON Channel.channel_id = Video.Channel_id WHERE published_date BETWEEN '2022-01-01' AND '2022-12-31'"

question_nine = "SELECT Channel.channel_name AS channel_name,(AVG(IFNULL(CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(Video.durations, 'M', 1),'PT',-1) AS UNSIGNED) * 60,0) + IFNULL(CAST(SUBSTRING_INDEX(SUBSTRING_INDEX(Video.durations, 'S', 1),'M',-1) AS UNSIGNED),0))) AS Avg_duration_seconds FROM Video JOIN Channel ON Channel.channel_id = Video.Channel_id GROUP BY Channel.channel_name ORDER BY Avg_duration_seconds DESC"

question_ten = "SELECT Video.commentCount AS no_of_comments, Channel.channel_name FROM Video JOIN Channel ON Channel.channel_id = Video.Channel_id ORDER BY CAST(no_of_comments AS SIGNED) DESC LIMIT 10"