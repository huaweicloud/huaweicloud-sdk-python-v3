# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_type': 'str',
        'is_build_in': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'sort': 'str',
        'asc': 'str'
    }

    attribute_map = {
        'template_type': 'template_type',
        'is_build_in': 'is_build_in',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'sort': 'sort',
        'asc': 'asc'
    }

    def __init__(self, template_type=None, is_build_in=None, offset=None, limit=None, name=None, sort=None, asc=None):
        """ListTemplatesRequest

        The model defined in huaweicloud sdk

        :param template_type: 模板类型
        :type template_type: str
        :param is_build_in: 是否内置模板
        :type is_build_in: str
        :param offset: 偏移量,表示从此偏移量开始查询,offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量
        :type limit: int
        :param name: 模板名称，匹配规则为模糊匹配
        :type name: str
        :param sort: 排序字段
        :type sort: str
        :param asc: 是否正序
        :type asc: str
        """
        
        

        self._template_type = None
        self._is_build_in = None
        self._offset = None
        self._limit = None
        self._name = None
        self._sort = None
        self._asc = None
        self.discriminator = None

        self.template_type = template_type
        self.is_build_in = is_build_in
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if sort is not None:
            self.sort = sort
        if asc is not None:
            self.asc = asc

    @property
    def template_type(self):
        """Gets the template_type of this ListTemplatesRequest.

        模板类型

        :return: The template_type of this ListTemplatesRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        """Sets the template_type of this ListTemplatesRequest.

        模板类型

        :param template_type: The template_type of this ListTemplatesRequest.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def is_build_in(self):
        """Gets the is_build_in of this ListTemplatesRequest.

        是否内置模板

        :return: The is_build_in of this ListTemplatesRequest.
        :rtype: str
        """
        return self._is_build_in

    @is_build_in.setter
    def is_build_in(self, is_build_in):
        """Sets the is_build_in of this ListTemplatesRequest.

        是否内置模板

        :param is_build_in: The is_build_in of this ListTemplatesRequest.
        :type is_build_in: str
        """
        self._is_build_in = is_build_in

    @property
    def offset(self):
        """Gets the offset of this ListTemplatesRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :return: The offset of this ListTemplatesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListTemplatesRequest.

        偏移量,表示从此偏移量开始查询,offset大于等于0

        :param offset: The offset of this ListTemplatesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListTemplatesRequest.

        每页显示的条目数量

        :return: The limit of this ListTemplatesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListTemplatesRequest.

        每页显示的条目数量

        :param limit: The limit of this ListTemplatesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListTemplatesRequest.

        模板名称，匹配规则为模糊匹配

        :return: The name of this ListTemplatesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListTemplatesRequest.

        模板名称，匹配规则为模糊匹配

        :param name: The name of this ListTemplatesRequest.
        :type name: str
        """
        self._name = name

    @property
    def sort(self):
        """Gets the sort of this ListTemplatesRequest.

        排序字段

        :return: The sort of this ListTemplatesRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListTemplatesRequest.

        排序字段

        :param sort: The sort of this ListTemplatesRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def asc(self):
        """Gets the asc of this ListTemplatesRequest.

        是否正序

        :return: The asc of this ListTemplatesRequest.
        :rtype: str
        """
        return self._asc

    @asc.setter
    def asc(self, asc):
        """Sets the asc of this ListTemplatesRequest.

        是否正序

        :param asc: The asc of this ListTemplatesRequest.
        :type asc: str
        """
        self._asc = asc

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
        if not isinstance(other, ListTemplatesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
