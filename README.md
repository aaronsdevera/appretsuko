# appretsuko
Android AppID <> Hash Resolver

<img src="https://repository-images.githubusercontent.com/257831950/a1782380-8440-11ea-9a7a-8a1a7a96e1ff" width=200>


*named after [aggretsuko the red fox panda](https://www.youtube.com/watch?v=1n3xXuEyr40) who loves looking at malicious apps*

# Read The Foxing Manual
```
----------------------------------------------------------------
appretsuko v0.1
----------------------------------------------------------------
resolve android appids to sha256 (and more)
Options:
appid         use the appid api endpoint to submit android appid
sha256        use the sha256 api endpoint to submit sha256 hash

Usage: ./appretsuko <appid | sha256> <appid or sha256 indicator>
e.g. appretsuko appid com.facebook.katana
e.g. appretsuko sha256 04709090134ca217db5b4190f6c5d30d60164a5a565de45a0ed3e3a6fc2d9f76
```

# The parts
This repo contains the API server that wraps arouond the Koodous endpoints, as well as a CLI script for hitting the API.

## server.py
This runs the appretsuko API server.
Note that Koodous key should be exported to an environment variable named `koodous_key`.
This can be done by running `export koodous_key=<your koodous API key>` in your terminal.

## appretsuko
Shell script for using the appretsuko API.
Doesn't do much other than *the thing*.

# Thank you human
This is free and open source software, but was made with [love and support from White Ops](https://whiteops.com)

And thanks to Koodous. >:)
