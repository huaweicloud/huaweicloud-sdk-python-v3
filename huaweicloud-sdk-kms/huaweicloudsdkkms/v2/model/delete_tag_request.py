# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteTagRequest:

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
        'key': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'key': 'key'
    }

    def __init__(self, key_id=None, key=None):
        """DeleteTagRequest

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param key: 标签键的值
        :type key: str
        """
        
        

        self._key_id = None
        self._key = None
        self.discriminator = None

        self.key_id = key_id
        self.key = key

    @property
    def key_id(self):
        """Gets the key_id of this DeleteTagRequest.

        密钥ID

        :return: The key_id of this DeleteTagRequest.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this DeleteTagRequest.

        密钥ID

        :param key_id: The key_id of this DeleteTagRequest.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def key(self):
        """Gets the key of this DeleteTagRequest.

        标签键的值

        :return: The key of this DeleteTagRequest.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this DeleteTagRequest.

        标签键的值

        :param key: The key of this DeleteTagRequest.
        :type key: str
        """
        self._key = key

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
        if not isinstance(other, DeleteTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
