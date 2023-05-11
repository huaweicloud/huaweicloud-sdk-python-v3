# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDictionaryRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'offset': 'str',
        'limit': 'str',
        'parent_code': 'str',
        'code': 'str',
        'name': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'parent_code': 'parent_code',
        'code': 'code',
        'name': 'name'
    }

    def __init__(self, instance_id=None, offset=None, limit=None, parent_code=None, code=None, name=None):
        """ListDictionaryRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param offset: 偏移量，大于等于0
        :type offset: str
        :param limit: 每页显示的条目数量
        :type limit: str
        :param parent_code: 指定父字典编码，返回子字典列表信息，未指定时查询顶级字典列表信息
        :type parent_code: str
        :param code: 通过code进行模糊匹配查询
        :type code: str
        :param name: 通过name进行模糊匹配查询
        :type name: str
        """
        
        

        self._instance_id = None
        self._offset = None
        self._limit = None
        self._parent_code = None
        self._code = None
        self._name = None
        self.discriminator = None

        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if parent_code is not None:
            self.parent_code = parent_code
        if code is not None:
            self.code = code
        if name is not None:
            self.name = name

    @property
    def instance_id(self):
        """Gets the instance_id of this ListDictionaryRequest.

        实例ID

        :return: The instance_id of this ListDictionaryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListDictionaryRequest.

        实例ID

        :param instance_id: The instance_id of this ListDictionaryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        """Gets the offset of this ListDictionaryRequest.

        偏移量，大于等于0

        :return: The offset of this ListDictionaryRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListDictionaryRequest.

        偏移量，大于等于0

        :param offset: The offset of this ListDictionaryRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListDictionaryRequest.

        每页显示的条目数量

        :return: The limit of this ListDictionaryRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListDictionaryRequest.

        每页显示的条目数量

        :param limit: The limit of this ListDictionaryRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def parent_code(self):
        """Gets the parent_code of this ListDictionaryRequest.

        指定父字典编码，返回子字典列表信息，未指定时查询顶级字典列表信息

        :return: The parent_code of this ListDictionaryRequest.
        :rtype: str
        """
        return self._parent_code

    @parent_code.setter
    def parent_code(self, parent_code):
        """Sets the parent_code of this ListDictionaryRequest.

        指定父字典编码，返回子字典列表信息，未指定时查询顶级字典列表信息

        :param parent_code: The parent_code of this ListDictionaryRequest.
        :type parent_code: str
        """
        self._parent_code = parent_code

    @property
    def code(self):
        """Gets the code of this ListDictionaryRequest.

        通过code进行模糊匹配查询

        :return: The code of this ListDictionaryRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this ListDictionaryRequest.

        通过code进行模糊匹配查询

        :param code: The code of this ListDictionaryRequest.
        :type code: str
        """
        self._code = code

    @property
    def name(self):
        """Gets the name of this ListDictionaryRequest.

        通过name进行模糊匹配查询

        :return: The name of this ListDictionaryRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListDictionaryRequest.

        通过name进行模糊匹配查询

        :param name: The name of this ListDictionaryRequest.
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
        if not isinstance(other, ListDictionaryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
