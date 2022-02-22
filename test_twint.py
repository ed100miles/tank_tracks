import twint
c = twint.Config()
print(dir(c))

c.Images = True
c.Geo = "48.330668, 38.410169,50km"
c.Filter_retweets = True

# c.Store_csv = True
# c.User_full = True
# c.Output = "users.csv"

# print(dir(twint.run))
twint.run.Search(c)
