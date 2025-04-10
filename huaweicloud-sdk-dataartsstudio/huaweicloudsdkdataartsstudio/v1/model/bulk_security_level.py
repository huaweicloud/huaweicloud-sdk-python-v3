# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BulkSecurityLevel:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'guids': 'list[str]',
        'security_level': 'str'
    }

    attribute_map = {
        'guids': 'guids',
        'security_level': 'security_level'
    }

    def __init__(self, guids=None, security_level=None):
        r"""BulkSecurityLevel

        The model defined in huaweicloud sdk

        :param guids: 资产guid
        :type guids: list[str]
        :param security_level: 密级
        :type security_level: str
        """
        
        

        self._guids = None
        self._security_level = None
        self.discriminator = None

        self.guids = guids
        self.security_level = security_level

    @property
    def guids(self):
        r"""Gets the guids of this BulkSecurityLevel.

        资产guid

        :return: The guids of this BulkSecurityLevel.
        :rtype: list[str]
        """
        return self._guids

    @guids.setter
    def guids(self, guids):
        r"""Sets the guids of this BulkSecurityLevel.

        资产guid

        :param guids: The guids of this BulkSecurityLevel.
        :type guids: list[str]
        """
        self._guids = guids

    @property
    def security_level(self):
        r"""Gets the security_level of this BulkSecurityLevel.

        密级

        :return: The security_level of this BulkSecurityLevel.
        :rtype: str
        """
        return self._security_level

    @security_level.setter
    def security_level(self, security_level):
        r"""Sets the security_level of this BulkSecurityLevel.

        密级

        :param security_level: The security_level of this BulkSecurityLevel.
        :type security_level: str
        """
        self._security_level = security_level

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
        if not isinstance(other, BulkSecurityLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
