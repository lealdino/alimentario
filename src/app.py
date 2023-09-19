import requests

url = "https://pb.utfpr.edu.br/geppadem/alimentario/index.php/admin/remotecontrol"

payload = {
    "method": "get_session_key",
    "params": ["ppgdr-pb@utfpr.edu.br", "5MnVpxad273a"],
    "id": 1
}
headers = {
    "cookie": "LS-BFZSAEVMKCPRBIUK=ehvcotsuvgjkoff0n91nn2m3um",
    "Content-Type": "application/json",
    "User-Agent": "Apache-HttpClient/4.2.2 (java 1.5)"
}

response = requests.request("POST", url, json=payload, headers=headers, verify=False)

print(response.text)