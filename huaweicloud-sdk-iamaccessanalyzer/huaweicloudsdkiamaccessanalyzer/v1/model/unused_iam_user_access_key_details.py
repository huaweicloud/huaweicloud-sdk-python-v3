# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UnusedIamUserAccessKeyDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_id': 'str',
        'last_accessed': 'datetime'
    }

    attribute_map = {
        'access_key_id': 'access_key_id',
        'last_accessed': 'last_accessed'
    }

    def __init__(self, access_key_id=None, last_accessed=None):
        r"""UnusedIamUserAccessKeyDetails

        The model defined in huaweicloud sdk

        :param access_key_id: 用户访问密钥唯一标识符（ID）。
        :type access_key_id: str
        :param last_accessed: 用户访问密钥的最后访问时间。
        :type last_accessed: datetime
        """
        
        

        self._access_key_id = None
        self._last_accessed = None
        self.discriminator = None

        self.access_key_id = access_key_id
        if last_accessed is not None:
            self.last_accessed = last_accessed

    @property
    def access_key_id(self):
        r"""Gets the access_key_id of this UnusedIamUserAccessKeyDetails.

        用户访问密钥唯一标识符（ID）。

        :return: The access_key_id of this UnusedIamUserAccessKeyDetails.
        :rtype: str
        """
        return self._access_key_id

    @access_key_id.setter
    def access_key_id(self, access_key_id):
        r"""Sets the access_key_id of this UnusedIamUserAccessKeyDetails.

        用户访问密钥唯一标识符（ID）。

        :param access_key_id: The access_key_id of this UnusedIamUserAccessKeyDetails.
        :type access_key_id: str
        """
        self._access_key_id = access_key_id

    @property
    def last_accessed(self):
        r"""Gets the last_accessed of this UnusedIamUserAccessKeyDetails.

        用户访问密钥的最后访问时间。

        :return: The last_accessed of this UnusedIamUserAccessKeyDetails.
        :rtype: datetime
        """
        return self._last_accessed

    @last_accessed.setter
    def last_accessed(self, last_accessed):
        r"""Sets the last_accessed of this UnusedIamUserAccessKeyDetails.

        用户访问密钥的最后访问时间。

        :param last_accessed: The last_accessed of this UnusedIamUserAccessKeyDetails.
        :type last_accessed: datetime
        """
        self._last_accessed = last_accessed

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
        if not isinstance(other, UnusedIamUserAccessKeyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
