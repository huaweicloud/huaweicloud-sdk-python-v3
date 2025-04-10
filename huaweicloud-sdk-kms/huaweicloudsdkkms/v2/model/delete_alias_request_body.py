# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteAliasRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aliases': 'list[str]',
        'key_id': 'str'
    }

    attribute_map = {
        'aliases': 'aliases',
        'key_id': 'key_id'
    }

    def __init__(self, aliases=None, key_id=None):
        r"""DeleteAliasRequestBody

        The model defined in huaweicloud sdk

        :param aliases: 待删除的别名
        :type aliases: list[str]
        :param key_id: 别名关联的密钥ID
        :type key_id: str
        """
        
        

        self._aliases = None
        self._key_id = None
        self.discriminator = None

        self.aliases = aliases
        self.key_id = key_id

    @property
    def aliases(self):
        r"""Gets the aliases of this DeleteAliasRequestBody.

        待删除的别名

        :return: The aliases of this DeleteAliasRequestBody.
        :rtype: list[str]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        r"""Sets the aliases of this DeleteAliasRequestBody.

        待删除的别名

        :param aliases: The aliases of this DeleteAliasRequestBody.
        :type aliases: list[str]
        """
        self._aliases = aliases

    @property
    def key_id(self):
        r"""Gets the key_id of this DeleteAliasRequestBody.

        别名关联的密钥ID

        :return: The key_id of this DeleteAliasRequestBody.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this DeleteAliasRequestBody.

        别名关联的密钥ID

        :param key_id: The key_id of this DeleteAliasRequestBody.
        :type key_id: str
        """
        self._key_id = key_id

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
        if not isinstance(other, DeleteAliasRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
