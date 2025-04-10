# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAliasesRequest:

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
        'limit': 'str',
        'marker': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, key_id=None, limit=None, marker=None):
        r"""ListAliasesRequest

        The model defined in huaweicloud sdk

        :param key_id: 密钥ID
        :type key_id: str
        :param limit: 指定查询返回记录条数
        :type limit: str
        :param marker: 分页查询起始位置标识
        :type marker: str
        """
        
        

        self._key_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def key_id(self):
        r"""Gets the key_id of this ListAliasesRequest.

        密钥ID

        :return: The key_id of this ListAliasesRequest.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        r"""Sets the key_id of this ListAliasesRequest.

        密钥ID

        :param key_id: The key_id of this ListAliasesRequest.
        :type key_id: str
        """
        self._key_id = key_id

    @property
    def limit(self):
        r"""Gets the limit of this ListAliasesRequest.

        指定查询返回记录条数

        :return: The limit of this ListAliasesRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAliasesRequest.

        指定查询返回记录条数

        :param limit: The limit of this ListAliasesRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListAliasesRequest.

        分页查询起始位置标识

        :return: The marker of this ListAliasesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListAliasesRequest.

        分页查询起始位置标识

        :param marker: The marker of this ListAliasesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListAliasesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
