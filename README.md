![Guild Wars 2 Banner](../master/res/images/gw2-banner.jpg?raw=true)

Currently Work in Progress. Currently only APIv1 has been mapped.

----

GuildWars2 API Client
=====================

[![Build Status](https://travis-ci.org/JuxhinDB/gw2-api-interface.svg?branch=feature%2Fapi-requests)](https://travis-ci.org/JuxhinDB/gw2-api-interface)

> Library that interfaces with the Guild Wars 2 API that supports
> v1 and v2 - https://wiki.guildwars2.com/wiki/API:Main

Table of Contents
=================

- [Pre-requisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
    + [Basic Usage](#basic-usage)
    + [Advanced Usage](#advanced-usage)
        - [API Objects](#api-objects)
        - [Client Settings](#client-settings)
        - [Proxy and SSL](#proxy-and-ssl)
    + [Authenticated Endpoints](#authenticated-endpoints)
    + [Cursors and Limits](#cursors-and-limits)
- [Examples](#examples)

### Prerequisites
-----

- Python v3.4 or higher

### Installation
-----

WIP


### Usage
-----


#### Basic Usage

Initializing a default client is simple. The following default values
will be automatically set for you:

+ API URL: https://api.guildwars2.com
+ Version: 2
+    Lang: en

Thus you can create a basic client like so:

```
from client import GuildWars2Client

gw2_client = GuildWars2Client()
```

The format for accessing an object will always be `{client}.{object}.get()`.
For example:

```
gw2_client.build.get()
>>> 81583
```

#### Advanced Usage

###### API Objects

The client will automatically expose all the API objects available
depending on the API version. This can be done by calling the `dir()`
method on the client object, like so:

```
gw2_client = GuildWars2Client(version='v1')
dir(gw2_client)
>>> ['BASE_URL', 'LANG', 'VERSION',
'api_key', 'base_url', 'build', 'colors', 'continents', 'eventdetails',
'files', 'guilddetails', 'itemdetails', 'items', 'lang', 'mapfloor',
'mapnames', 'maps', 'proxy', 'recipedetails', 'recipes', 'session',
'skindetails', 'skins', 'verify_ssl', 'version', 'worldnames',
'wvwmatchdetails', 'wvwmatches', 'wvwobjectivenames']
```

All redundant protocol-methods (i.e. `__repr__`) were removed from the output,
you can ofcourse see the full output when running this in your project.

###### Client Settings

To examine the client settings at any given point, simply print the object.

```
from client import GuildWars2Client
gw2_client = GuildWars2Client()

gw2_client

>>> <GuildWars2Client https://api.guildwars2.com
Version: v2
API Key: None
Language: en
Proxy: None
Verify SSL?: True>
```

###### Proxy and SSL

If at any given point you need to pass API requests through proxy (e.g. Fiddler)
you can configure the client to pass all request through said proxy during
client initialization.

```
from client import GuildWars2Client
gw2_client = GuildWars2Client(proxy={'http': '127.0.0.1:8888', 'https': '127.0.0.1:8888'}, version='v1'})
```

Additionally if you're passing through a local proxy, you may need to set
SSL verification to false like so:

```
from client import GuildWars2Client
gw2_client = GuildWars2Client(proxy={'http': '127.0.0.1:8888', 'https': '127.0.0.1:8888'}, version='v1', verify_ssl=False)
```

#### Authenticated Endpoints

There may be cases where certain endpoints such as `Accounts` or `Guild` related endpoints may require authentication.
This is generally configured on initialization of the client, like so:

`client = GuildWars2Client(api_key='API_KEY_VALUE_HERE')`

If you want to generate your own API key, please refer to the following [link](https://account.arena.net/applications).

#### Cursors and Limits

WIP

### Examples

Below are a few examples and one-liners that may help when testing or debugging the project:

**Using [Fiddler](http://www.telerik.com/fiddler)**:

```
from client import GuildWars2Client; client = GuildWars2Client(proxy={'http': '127.0.0.1:8888', 'https': '127.0.0.1:8888'}, verify_ssl=False, api_key='API_KEY')
```

**APIv2 Searching for Guild**

```
client.guildsearch.get(name='Mythical Realms')

>>> 0CB3B1A7-4C70-E611-80D3-E4115BE8BBE8
```

**APIv2 Retrieving guild members**

```
client.guildidmembers.get('0CB3B1A7-4C70-E611-80D3-E4115BE8BBE8')

>>> {"text": "access restricted to guild leaders"}  # :-(
```