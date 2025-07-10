# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListScriptsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'id': 'str',
        'name': 'str',
        'type': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'id': 'id',
        'name': 'name',
        'type': 'type'
    }

    def __init__(self, offset=None, limit=None, id=None, name=None, type=None):
        r"""ListScriptsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的偏移量，默认值0。
        :type offset: int
        :param limit: 单次查询的大小[1-100]，默认值10。
        :type limit: int
        :param id: 脚本ID。
        :type id: str
        :param name: 脚本名称。
        :type name: str
        :param type: 脚本类型。
        :type type: str
        """
        
        

        self._offset = None
        self._limit = None
        self._id = None
        self._name = None
        self._type = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type

    @property
    def offset(self):
        r"""Gets the offset of this ListScriptsRequest.

        查询的偏移量，默认值0。

        :return: The offset of this ListScriptsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListScriptsRequest.

        查询的偏移量，默认值0。

        :param offset: The offset of this ListScriptsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListScriptsRequest.

        单次查询的大小[1-100]，默认值10。

        :return: The limit of this ListScriptsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListScriptsRequest.

        单次查询的大小[1-100]，默认值10。

        :param limit: The limit of this ListScriptsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def id(self):
        r"""Gets the id of this ListScriptsRequest.

        脚本ID。

        :return: The id of this ListScriptsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListScriptsRequest.

        脚本ID。

        :param id: The id of this ListScriptsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListScriptsRequest.

        脚本名称。

        :return: The name of this ListScriptsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListScriptsRequest.

        脚本名称。

        :param name: The name of this ListScriptsRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListScriptsRequest.

        脚本类型。

        :return: The type of this ListScriptsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListScriptsRequest.

        脚本类型。

        :param type: The type of this ListScriptsRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListScriptsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
