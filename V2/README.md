## Web UI client

It contains 2 pages. The landing page(index.html) contains a field to insert the local IP of the Arduino HTTP server. After inserting the IP, the user is redirected to the control page

Create a file named **WiFiCredentials.h** following this scheme:

``` C
#ifndef CONFIG_H
#define CONFIG_H

const char* ssid = "your_SSID";
const char* password = "your_PASSWORD";

#endif

```