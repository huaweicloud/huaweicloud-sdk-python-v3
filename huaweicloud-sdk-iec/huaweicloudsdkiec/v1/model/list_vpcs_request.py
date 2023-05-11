# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVpcsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'id': 'id',
        'name': 'name'
    }

    def __init__(self, limit=None, offset=None, id=None, name=None):
        """ListVpcsRequest

        The model defined in huaweicloud sdk

        :param limit: 查询返回虚拟私有云列表数量。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param id: 通过ID查询
        :type id: str
        :param name: 通过name查询
        :type name: str
        """
        
        

        self._limit = None
        self._offset = None
        self._id = None
        self._name = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name

    @property
    def limit(self):
        """Gets the limit of this ListVpcsRequest.

        查询返回虚拟私有云列表数量。

        :return: The limit of this ListVpcsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListVpcsRequest.

        查询返回虚拟私有云列表数量。

        :param limit: The limit of this ListVpcsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListVpcsRequest.

        查询的偏移量。

        :return: The offset of this ListVpcsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListVpcsRequest.

        查询的偏移量。

        :param offset: The offset of this ListVpcsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def id(self):
        """Gets the id of this ListVpcsRequest.

        通过ID查询

        :return: The id of this ListVpcsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListVpcsRequest.

        通过ID查询

        :param id: The id of this ListVpcsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListVpcsRequest.

        通过name查询

        :return: The name of this ListVpcsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListVpcsRequest.

        通过name查询

        :param name: The name of this ListVpcsRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ListVpcsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
