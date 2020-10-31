# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class UpdateCertificateResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'certificate': 'CertificateInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'certificate': 'certificate'
    }

    def __init__(self, request_id=None, certificate=None):
        """UpdateCertificateResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._request_id = None
        self._certificate = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if certificate is not None:
            self.certificate = certificate

    @property
    def request_id(self):
        """Gets the request_id of this UpdateCertificateResponse.

        请求ID。  注：自动生成 。

        :return: The request_id of this UpdateCertificateResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this UpdateCertificateResponse.

        请求ID。  注：自动生成 。

        :param request_id: The request_id of this UpdateCertificateResponse.
        :type: str
        """
        self._request_id = request_id

    @property
    def certificate(self):
        """Gets the certificate of this UpdateCertificateResponse.


        :return: The certificate of this UpdateCertificateResponse.
        :rtype: CertificateInfo
        """
        return self._certificate

    @certificate.setter
    def certificate(self, certificate):
        """Sets the certificate of this UpdateCertificateResponse.


        :param certificate: The certificate of this UpdateCertificateResponse.
        :type: CertificateInfo
        """
        self._certificate = certificate

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                if attr in self.sensitive_list:
                    result[attr] = "****"
                else:
                    result[attr] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateCertificateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
