# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KMSCmk:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'grants': 'str'
    }

    attribute_map = {
        'grants': 'grants'
    }

    def __init__(self, grants=None):
        r"""KMSCmk

        The model defined in huaweicloud sdk

        :param grants: 用于加密密钥的授权。
        :type grants: str
        """
        
        

        self._grants = None
        self.discriminator = None

        self.grants = grants

    @property
    def grants(self):
        r"""Gets the grants of this KMSCmk.

        用于加密密钥的授权。

        :return: The grants of this KMSCmk.
        :rtype: str
        """
        return self._grants

    @grants.setter
    def grants(self, grants):
        r"""Sets the grants of this KMSCmk.

        用于加密密钥的授权。

        :param grants: The grants of this KMSCmk.
        :type grants: str
        """
        self._grants = grants

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
        if not isinstance(other, KMSCmk):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
