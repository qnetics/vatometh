# what is VATOMETH?

<p align="center">
    <img src="img/vatometh_icon.jpg"></img>
</p>
 
 **_VATOMETH_** is a simple configuration management tool, It handles
configuration management, application deployment, cloud provisioning, and network automation.
 
 <hr>
 
 # USAGE
 
## Requirement's install

```
$ pip install -r requirements.txt
```
 
 ## how to use

```
 ~ [ <-+=-+=-+=-+=- VATOMETH -+=-+=-+=-+=-> ] ~
 ~ [ <-+=-+=-+=-+=-+ V1.0.0 +-+=-+=-+=-+=-> ] ~


usage => python vatometh.py [ TYPE ] [ FILE ] [ FILENAME ]
--------------------------------------------------------
[ TYPE ] +==> [ -c | --crowded ] | [ -s | --single ]
[ FILE ] +==> [ -f | --file ]
[ FILENAME ] +==> [ whatever ].json
 
```

 ## Configuration
 
 ### Single Command configuration for single Machine / VPS

```
{
    "service" : {

        "host"     :  "192.168.137.1",
        "port"     :   22,
        "user"     :  "qywok",
        "password" :  "qywok"

    },

    "commands" : {

        "message" : "[ installing docker ]",
        "cmd"     : "apt install docker.io"

    }
}
 
```

 ### Multi command configuration for single Machine / VPS

```
{
    "service" : {

        "host"     :  "192.168.137.1",
        "port"     :   22,
        "user"     :  "qywok",
        "password" :  "qywok"

    },

    "commands" : [

        {

            "message" : "[ updating ]",
            "cmd"     : "apt update"

        },

        {

            "message" : "[ installing docker ]",
            "cmd"     : [

                "ls",
                "ls /",
                "apt install docker.io"

            ]

        }

    ]
}
 
```

 ### Multi and single command configuration for multi machine / VPS

```
{
    "services" : [

        {

            "host"     :  "192.168.43.177",
            "port"     :   22,
            "user"     :  "qywok",
            "password" :  "qywok",
            "commands" :  [

                {

                    "message" : "installing ssh & docker",
                    "cmd"     : [
        
                        "apt-get install openssh",
                        "apt-get install docker.io",
                        "service docker start"
        
                    ]
        
                }


            ]

        },
        
        {

            "host"     :  "192.168.137.9",
            "port"     :   22,
            "user"     :  "qywok",
            "password" :  "qywok",
            "commands" :  {

                "message" : "installing ssh & docker",
                "cmd"     : "apt-get install openssh"
    
            }

        },

        {

            "host"     :  "192.168.137.70",
            "port"     :   22,
            "user"     :  "qywok",
            "password" :  "qywok",
            "commands" :  [

                {

                    "message" : "installing ssh & docker",
                    "cmd"     : "apt-get install openssh"
    
                }

            ]

        }
        

    ]
}
 
```
