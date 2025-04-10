# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCgwRequestBodyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'ca_certificate': 'CaCertificateRequest'
    }

    attribute_map = {
        'name': 'name',
        'ca_certificate': 'ca_certificate'
    }

    def __init__(self, name=None, ca_certificate=None):
        r"""UpdateCgwRequestBodyContent

        The model defined in huaweicloud sdk

        :param name: 网关名称
        :type name: str
        :param ca_certificate: 
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificateRequest`
        """
        
        

        self._name = None
        self._ca_certificate = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if ca_certificate is not None:
            self.ca_certificate = ca_certificate

    @property
    def name(self):
        r"""Gets the name of this UpdateCgwRequestBodyContent.

        网关名称

        :return: The name of this UpdateCgwRequestBodyContent.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateCgwRequestBodyContent.

        网关名称

        :param name: The name of this UpdateCgwRequestBodyContent.
        :type name: str
        """
        self._name = name

    @property
    def ca_certificate(self):
        r"""Gets the ca_certificate of this UpdateCgwRequestBodyContent.

        :return: The ca_certificate of this UpdateCgwRequestBodyContent.
        :rtype: :class:`huaweicloudsdkvpn.v5.CaCertificateRequest`
        """
        return self._ca_certificate

    @ca_certificate.setter
    def ca_certificate(self, ca_certificate):
        r"""Sets the ca_certificate of this UpdateCgwRequestBodyContent.

        :param ca_certificate: The ca_certificate of this UpdateCgwRequestBodyContent.
        :type ca_certificate: :class:`huaweicloudsdkvpn.v5.CaCertificateRequest`
        """
        self._ca_certificate = ca_certificate

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
        import simplejson as json
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateCgwRequestBodyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
