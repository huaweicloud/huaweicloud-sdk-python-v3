# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UrlDomainModify:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'min_ssl_version': 'str'
    }

    attribute_map = {
        'min_ssl_version': 'min_ssl_version'
    }

    def __init__(self, min_ssl_version=None):
        """UrlDomainModify

        The model defined in huaweicloud sdk

        :param min_ssl_version: 最小ssl协议版本号。支持TLSv1.1或TLSv1.2
        :type min_ssl_version: str
        """
        
        

        self._min_ssl_version = None
        self.discriminator = None

        self.min_ssl_version = min_ssl_version

    @property
    def min_ssl_version(self):
        """Gets the min_ssl_version of this UrlDomainModify.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :return: The min_ssl_version of this UrlDomainModify.
        :rtype: str
        """
        return self._min_ssl_version

    @min_ssl_version.setter
    def min_ssl_version(self, min_ssl_version):
        """Sets the min_ssl_version of this UrlDomainModify.

        最小ssl协议版本号。支持TLSv1.1或TLSv1.2

        :param min_ssl_version: The min_ssl_version of this UrlDomainModify.
        :type min_ssl_version: str
        """
        self._min_ssl_version = min_ssl_version

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
        if not isinstance(other, UrlDomainModify):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
