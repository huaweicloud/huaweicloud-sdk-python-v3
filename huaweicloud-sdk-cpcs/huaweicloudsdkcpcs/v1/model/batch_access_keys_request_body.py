# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAccessKeysRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key_ids': 'list[str]'
    }

    attribute_map = {
        'access_key_ids': 'access_key_ids'
    }

    def __init__(self, access_key_ids=None):
        r"""BatchAccessKeysRequestBody

        The model defined in huaweicloud sdk

        :param access_key_ids: 所需要绑定的访问密钥ID
        :type access_key_ids: list[str]
        """
        
        

        self._access_key_ids = None
        self.discriminator = None

        self.access_key_ids = access_key_ids

    @property
    def access_key_ids(self):
        r"""Gets the access_key_ids of this BatchAccessKeysRequestBody.

        所需要绑定的访问密钥ID

        :return: The access_key_ids of this BatchAccessKeysRequestBody.
        :rtype: list[str]
        """
        return self._access_key_ids

    @access_key_ids.setter
    def access_key_ids(self, access_key_ids):
        r"""Sets the access_key_ids of this BatchAccessKeysRequestBody.

        所需要绑定的访问密钥ID

        :param access_key_ids: The access_key_ids of this BatchAccessKeysRequestBody.
        :type access_key_ids: list[str]
        """
        self._access_key_ids = access_key_ids

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
        if not isinstance(other, BatchAccessKeysRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
