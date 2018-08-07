import urllib.request
import json
token="EAAORlveqKDkBAJixD6c3s1B77ypPzvmrqGtlLjZBjqQZBWZCbilZBR2yFCJ9k7Pf2pjRj3V8fb2j8iecum6cikxmnYvhAFiGedDqLLn0GKUuUbRXu23vGhj5r1XyZAul9bhT961nF4TSkKKAq8xyfzSpAUWqan9ZBNpTaGYn7n1pk3OWZCAOxXi2Seq00BJYyMZD"
contents =json.loads( urllib.request.urlopen("https://graph.facebook.com/v3.1/10155705849232361?fields=events&access_token="+token).read())
print (contents)