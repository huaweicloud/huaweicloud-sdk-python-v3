# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeyDescriptionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'key_description': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key_description': 'key_description'
    }

    def __init__(self, key_id=None, key_description=None):
        """KeyDescriptionInfo

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID。
        :type key_id: str
        :param key_description: 密钥描述。
        :type key_description: str
        """
        
        

        self._key_id = None
        self._key_description = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if key_description is not None:
            self.key_description = key_description

    @property
    def key_id(self):
        """Gets the key_id of this KeyDescriptionInfo.

        密钥ID。

        :return: The key_id of this KeyDescriptionInfo.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this KeyDescriptionInfo.

        密钥ID。

        :param key_id: The key_id of this KeyDescriptionInfo.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key_description(self):
        """Gets the key_description of this KeyDescriptionInfo.

        密钥描述。

        :return: The key_description of this KeyDescriptionInfo.
        :rtype: str
        """
        return self._key_description

    @key_description.setter
    def key_description(self, key_description):
        """Sets the key_description of this KeyDescriptionInfo.

        密钥描述。

        :param key_description: The key_description of this KeyDescriptionInfo.
        :type key_description: str
        """
        self._key_description = key_description

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
        if not isinstance(other, KeyDescriptionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
