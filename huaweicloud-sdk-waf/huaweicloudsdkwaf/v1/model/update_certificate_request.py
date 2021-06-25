# coding: utf-8

import pprint
import re

import six





class UpdateCertificateRequest:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'certificate_id': 'str',
        'body': 'UpdateCertificateRequestBody'
    }

    attribute_map = {
        'certificate_id': 'certificate_id',
        'body': 'body'
    }

    def __init__(self, certificate_id=None, body=None):
        """UpdateCertificateRequest - a model defined in huaweicloud sdk"""
        
        

        self._certificate_id = None
        self._body = None
        self.discriminator = None

        self.certificate_id = certificate_id
        if body is not None:
            self.body = body

    @property
    def certificate_id(self):
        """Gets the certificate_id of this UpdateCertificateRequest.

        证书ID

        :return: The certificate_id of this UpdateCertificateRequest.
        :rtype: str
        """
        return self._certificate_id

    @certificate_id.setter
    def certificate_id(self, certificate_id):
        """Sets the certificate_id of this UpdateCertificateRequest.

        证书ID

        :param certificate_id: The certificate_id of this UpdateCertificateRequest.
        :type: str
        """
        self._certificate_id = certificate_id

    @property
    def body(self):
        """Gets the body of this UpdateCertificateRequest.


        :return: The body of this UpdateCertificateRequest.
        :rtype: UpdateCertificateRequestBody
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateCertificateRequest.


        :param body: The body of this UpdateCertificateRequest.
        :type: UpdateCertificateRequestBody
        """
        self._body = body

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
        if not isinstance(other, UpdateCertificateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other