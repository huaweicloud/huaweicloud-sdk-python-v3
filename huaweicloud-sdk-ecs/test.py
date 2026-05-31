# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkecs.v2.region.ecs_region import EcsRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkecs.v2 import *
from huaweicloudsdkecs.v2.ecs_client import EcsClient

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = os.environ["CLOUD_SDK_AK"]
    sk = os.environ["CLOUD_SDK_SK"]

    credentials = BasicCredentials(ak, sk)

    client = EcsClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(EcsRegion.value_of("af-north-1")) \
        .build()

    try:
        request = BatchRebootServersRequest()
        listServersReboot = [
            ServerId(
                id="c64f299a-638a-4e5a-8420-985b65d9a2a8"
            )
        ]
        rebootbody = BatchRebootSeversOption(
            servers=listServersReboot,
            type="SOFT"
        )
        request.body = BatchRebootServersRequestBody(
            reboot=rebootbody
        )
        response = client.batch_reboot_servers(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
