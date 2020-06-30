# coding: utf-8
from huaweicloudsdkcore.http.http_config import HttpConfig
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdkiotda.v5 import *


def getCertificates(client):
    try:
        request = ListCertificatesRequest()
        response = client.list_certificates(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def deleteCertificate(client):
    try:
        request = DeleteCertificateRequest(certificate_id="5e25d39a3b7c24fa3638804b_gf")
        response = client.delete_certificate(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def addCertificate(client):
    try:
        content = "-----BEGIN CERTIFICATE-----MIID2TCCAsGgAwIBAgIJAOEDEgVdVMn9MA0GCSqGSIb3DQEBCwUAMIGCMQswCQYDVQQGEwJDTjERMA8GA1UECAwIR3VhbmRvbmcxETAPBgNVBAcMCFNoZW56aGVuMQ8wDQYDVQQKDAZIdWF3ZWkxDDAKBgNVBAsMA2lvdDESMBAGA1UEAwwJMTIzNDU2Nzg5MRowGAYJKoZIhvcNAQkBFgtkamthQHFxLmNvbTAeFw0xOTEyMTkxMzE1MjZaFw0yMjEwMDgxMzE1MjZaMIGCMQswCQYDVQQGEwJDTjERMA8GA1UECAwIR3VhbmRvbmcxETAPBgNVBAcMCFNoZW56aGVuMQ8wDQYDVQQKDAZIdWF3ZWkxDDAKBgNVBAsMA2lvdDESMBAGA1UEAwwJMTIzNDU2Nzg5MRowGAYJKoZIhvcNAQkBFgtkamthQHFxLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM72QUzoadvLfxGjt3UFoZ4MJbblqnRbouO4KpOVHBXyS2yQVl4CWWMhLh4pp2efNUSqKuXHjY3r68PquyNnYk8zO59zVc7JHvjGkBvo7DgPRAhEKPLJIpRzkmlCBbxwTNCjc3FovGb/sHHNlpGncCKUzMfPGNZuBiuemskuEXL/eMHxDPbXYWn4Wq0wt+28PKUL5jybY7nsXSNnmAPFTO0CAmq0meUukubT/jHDCQ78ihQ/iqw1RNq88aCqRleoHiGg5nWkjL+05GXqUrqVVnZNL+YqcXzuVMs5XgyhNM2AsuH2g3D8ZuF6Dj9qY1n/v/Cp/DGpxP3A74SlplnFD/0CAwEAAaNQME4wHQYDVR0OBBYEFAVPWVtpTdO6KQnmVrrNlMguWNR7MB8GA1UdIwQYMBaAFAVPWVtpTdO6KQnmVrrNlMguWNR7MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAE40ViqK+UaEn++Xq6f4Cmeg3JqYHu47v9RIAASNihYRBQ/r3RE7Af3GqjIO5nMJJuCMzdcoAU8N9KwkgXD+GLR9fYLEoEmq5CrhgaGDsCi85vCsmWhj5z8r5TG207xpmvH2KT447dnG+chMBE594ma85dCv+0mCDrqNToElipgT8+rYAYVClnIt3kbsTg1vSRNHadd+TpgRVxJZBF0fHcCAyc/2f3UJgPYNWShIetHM6BdI3fZ4H+eeHPjagm5kzmffli1cUv2/N+1hKUvcI4uFCqEwZRFtp90RyIbxUfQwi+CsXVnwV+BZS5qD9bTcfxZMXhuVRwO/5xWYMYPN1uY=-----END CERTIFICATE-----"
        body = CreateCertificateDTO(content=content)
        request = AddCertificateRequest(body=body)
        response = client.add_certificate(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


def verifyCertificate(client):
    try:
        certificate_id = "13f9dc18-8c5f-47f7-9b22-0d570d67703f"
        action_id = "verify"
        verify_content = "-----BEGIN CERTIFICATE-----MIID2TCCAsGgAwIBAgIJAOEDEgVdVMn9MA0GCSqGSIb3DQEBCwUAMIGCMQswCQYDVQQGEwJDTjERMA8GA1UECAwIR3VhbmRvbmcxETAPBgNVBAcMCFNoZW56aGVuMQ8wDQYDVQQKDAZIdWF3ZWkxDDAKBgNVBAsMA2lvdDESMBAGA1UEAwwJMTIzNDU2Nzg5MRowGAYJKoZIhvcNAQkBFgtkamthQHFxLmNvbTAeFw0xOTEyMTkxMzE1MjZaFw0yMjEwMDgxMzE1MjZaMIGCMQswCQYDVQQGEwJDTjERMA8GA1UECAwIR3VhbmRvbmcxETAPBgNVBAcMCFNoZW56aGVuMQ8wDQYDVQQKDAZIdWF3ZWkxDDAKBgNVBAsMA2lvdDESMBAGA1UEAwwJMTIzNDU2Nzg5MRowGAYJKoZIhvcNAQkBFgtkamthQHFxLmNvbTCCASIwDQYJKoZIhvcNAQEBBQADggEPADCCAQoCggEBAM72QUzoadvLfxGjt3UFoZ4MJbblqnRbouO4KpOVHBXyS2yQVl4CWWMhLh4pp2efNUSqKuXHjY3r68PquyNnYk8zO59zVc7JHvjGkBvo7DgPRAhEKPLJIpRzkmlCBbxwTNCjc3FovGb/sHHNlpGncCKUzMfPGNZuBiuemskuEXL/eMHxDPbXYWn4Wq0wt+28PKUL5jybY7nsXSNnmAPFTO0CAmq0meUukubT/jHDCQ78ihQ/iqw1RNq88aCqRleoHiGg5nWkjL+05GXqUrqVVnZNL+YqcXzuVMs5XgyhNM2AsuH2g3D8ZuF6Dj9qY1n/v/Cp/DGpxP3A74SlplnFD/0CAwEAAaNQME4wHQYDVR0OBBYEFAVPWVtpTdO6KQnmVrrNlMguWNR7MB8GA1UdIwQYMBaAFAVPWVtpTdO6KQnmVrrNlMguWNR7MAwGA1UdEwQFMAMBAf8wDQYJKoZIhvcNAQELBQADggEBAE40ViqK+UaEn++Xq6f4Cmeg3JqYHu47v9RIAASNihYRBQ/r3RE7Af3GqjIO5nMJJuCMzdcoAU8N9KwkgXD+GLR9fYLEoEmq5CrhgaGDsCi85vCsmWhj5z8r5TG207xpmvH2KT447dnG+chMBE594ma85dCv+0mCDrqNToElipgT8+rYAYVClnIt3kbsTg1vSRNHadd+TpgRVxJZBF0fHcCAyc/2f3UJgPYNWShIetHM6BdI3fZ4H+eeHPjagm5kzmffli1cUv2/N+1hKUvcI4uFCqEwZRFtp90RyIbxUfQwi+CsXVnwV+BZS5qD9bTcfxZMXhuVRwO/5xWYMYPN1uY=-----END CERTIFICATE-----"
        body = VerifyCertificateDTO(verify_content=verify_content)
        request = CheckCertificateRequest(certificate_id=certificate_id, action_id=action_id, body=body)
        response = client.check_certificate(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)


if __name__ == '__main__':
    ak = "{your ak string}"
    sk = "{your sk string}"
    endpoint = "{your endpoint}"
    project_id = "{your project id}"

    config = HttpConfig.get_default_config()
    config.ignore_ssl_verification = True
    credentials = BasicCredentials(ak, sk, project_id)

    iotda_client = IoTDAClient().new_builder(IoTDAClient) \
        .with_http_config(config) \
        .with_credentials(credentials) \
        .with_endpoint(endpoint) \
        .build()

    getCertificates(iotda_client)
    deleteCertificate(iotda_client)
    addCertificate(iotda_client)
    verifyCertificate(iotda_client)
