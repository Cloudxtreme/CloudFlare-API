#!/usr/bin/python

import urllib
import json

class CloudflareApi:
  def __init__(self, host_key):
    self.host_key = host_key

  def api_request(self, method, arguments={}):
    post_data               = arguments
    post_data["act"]        = method
    post_data["host_key"]   = self.host_key

    res = urllib.urlopen("http://localhost:8080/host-gw.html", urllib.urlencode(post_data)).read()
    print res
    data = json.loads(res)
    #data = json.loads(urllib.urlopen("https://api.cloudflare.com/host-gw.html", urllib.urlencode(post_data)).read())
    return data
  
  # Auth user with CloudFlare
  def user_auth(self, cloudflare_email, cloudflare_pass, unique_id):
    result = self.api_request("user_auth", { 'cloudflare_email':cloudflare_email, 'cloudflare_pass':cloudflare_pass, 'unique_id':unique_id })
    if result["result"] == "success":
      return results["response"]["user_key"]
    else:
      return result["msg"]
  
  # Create user with CloudFlare
  def create_account(self, cloudflare_email, cloudflare_pass, unique_id):
    result = self.api_request("create_account", { 'cloudflare_email':cloudflare_email, 'cloudflare_pass':cloudflare_pass, 'unique_id':unique_id })
    if result["result"] == "success":
      return result["msg"]
    else:
      return result["msg"]
  
  # Create new zone with CloudFlare
  def zone_set(self, user_key, user_auth, zone_name, resolve_to, subdomains):
    result = self.api_request("zone_set", { 'user_key':user_key, 'user_auth':user_auth, 'zone_name':zone_name, 'resolve_to':resolve_to, 'subdomains':subdomains })
    if result["result"] == "success":
      return results["response"]
    else:
      return result["msg"]
    
  def get_balance(self):
    result = self.api_request("get_balance")
    if result["success"]:
      return result["result"]["balance"]
    else:
      return result["msg"]

cf = CloudflareApi("")
print cf.create_account("test1", "test2", "vmuser111111111")