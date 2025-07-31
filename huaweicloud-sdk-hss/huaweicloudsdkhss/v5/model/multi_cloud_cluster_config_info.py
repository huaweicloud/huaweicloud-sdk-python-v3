# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MultiCloudClusterConfigInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'address': 'str',
        'certificate_expiration_date': 'int'
    }

    attribute_map = {
        'address': 'address',
        'certificate_expiration_date': 'certificate_expiration_date'
    }

    def __init__(self, address=None, certificate_expiration_date=None):
        r"""MultiCloudClusterConfigInfo

        The model defined in huaweicloud sdk

        :param address: apiserver的地址
        :type address: str
        :param certificate_expiration_date: 证书有效期结束时间
        :type certificate_expiration_date: int
        """
        
        

        self._address = None
        self._certificate_expiration_date = None
        self.discriminator = None

        if address is not None:
            self.address = address
        if certificate_expiration_date is not None:
            self.certificate_expiration_date = certificate_expiration_date

    @property
    def address(self):
        r"""Gets the address of this MultiCloudClusterConfigInfo.

        apiserver的地址

        :return: The address of this MultiCloudClusterConfigInfo.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        r"""Sets the address of this MultiCloudClusterConfigInfo.

        apiserver的地址

        :param address: The address of this MultiCloudClusterConfigInfo.
        :type address: str
        """
        self._address = address

    @property
    def certificate_expiration_date(self):
        r"""Gets the certificate_expiration_date of this MultiCloudClusterConfigInfo.

        证书有效期结束时间

        :return: The certificate_expiration_date of this MultiCloudClusterConfigInfo.
        :rtype: int
        """
        return self._certificate_expiration_date

    @certificate_expiration_date.setter
    def certificate_expiration_date(self, certificate_expiration_date):
        r"""Sets the certificate_expiration_date of this MultiCloudClusterConfigInfo.

        证书有效期结束时间

        :param certificate_expiration_date: The certificate_expiration_date of this MultiCloudClusterConfigInfo.
        :type certificate_expiration_date: int
        """
        self._certificate_expiration_date = certificate_expiration_date

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
        if not isinstance(other, MultiCloudClusterConfigInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
