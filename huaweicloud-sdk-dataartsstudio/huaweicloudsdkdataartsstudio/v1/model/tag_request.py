# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TagRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tag_ids': 'list[str]',
        'type': 'str',
        'name': 'str',
        'create_user': 'str',
        'start': 'str',
        'end': 'str',
        'offset': 'int',
        'limit': 'int',
        'sort_by': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'tag_ids': 'tag_ids',
        'type': 'type',
        'name': 'name',
        'create_user': 'create_user',
        'start': 'start',
        'end': 'end',
        'offset': 'offset',
        'limit': 'limit',
        'sort_by': 'sort_by',
        'sort_order': 'sort_order'
    }

    def __init__(self, tag_ids=None, type=None, name=None, create_user=None, start=None, end=None, offset=None, limit=None, sort_by=None, sort_order=None):
        """TagRequest

        The model defined in huaweicloud sdk

        :param tag_ids: 标签id
        :type tag_ids: list[str]
        :param type: 类型
        :type type: str
        :param name: 标签名称，用作搜索框筛选
        :type name: str
        :param create_user: 创建者，用作搜索框筛选
        :type create_user: str
        :param start: 开始时间
        :type start: str
        :param end: 结束时间
        :type end: str
        :param offset: 页码
        :type offset: int
        :param limit: 每页大小
        :type limit: int
        :param sort_by: 根据xx排序
        :type sort_by: str
        :param sort_order: 升序/降序
        :type sort_order: str
        """
        
        

        self._tag_ids = None
        self._type = None
        self._name = None
        self._create_user = None
        self._start = None
        self._end = None
        self._offset = None
        self._limit = None
        self._sort_by = None
        self._sort_order = None
        self.discriminator = None

        if tag_ids is not None:
            self.tag_ids = tag_ids
        if type is not None:
            self.type = type
        if name is not None:
            self.name = name
        if create_user is not None:
            self.create_user = create_user
        if start is not None:
            self.start = start
        if end is not None:
            self.end = end
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def tag_ids(self):
        """Gets the tag_ids of this TagRequest.

        标签id

        :return: The tag_ids of this TagRequest.
        :rtype: list[str]
        """
        return self._tag_ids

    @tag_ids.setter
    def tag_ids(self, tag_ids):
        """Sets the tag_ids of this TagRequest.

        标签id

        :param tag_ids: The tag_ids of this TagRequest.
        :type tag_ids: list[str]
        """
        self._tag_ids = tag_ids

    @property
    def type(self):
        """Gets the type of this TagRequest.

        类型

        :return: The type of this TagRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TagRequest.

        类型

        :param type: The type of this TagRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this TagRequest.

        标签名称，用作搜索框筛选

        :return: The name of this TagRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TagRequest.

        标签名称，用作搜索框筛选

        :param name: The name of this TagRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_user(self):
        """Gets the create_user of this TagRequest.

        创建者，用作搜索框筛选

        :return: The create_user of this TagRequest.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this TagRequest.

        创建者，用作搜索框筛选

        :param create_user: The create_user of this TagRequest.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def start(self):
        """Gets the start of this TagRequest.

        开始时间

        :return: The start of this TagRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this TagRequest.

        开始时间

        :param start: The start of this TagRequest.
        :type start: str
        """
        self._start = start

    @property
    def end(self):
        """Gets the end of this TagRequest.

        结束时间

        :return: The end of this TagRequest.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this TagRequest.

        结束时间

        :param end: The end of this TagRequest.
        :type end: str
        """
        self._end = end

    @property
    def offset(self):
        """Gets the offset of this TagRequest.

        页码

        :return: The offset of this TagRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this TagRequest.

        页码

        :param offset: The offset of this TagRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this TagRequest.

        每页大小

        :return: The limit of this TagRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this TagRequest.

        每页大小

        :param limit: The limit of this TagRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_by(self):
        """Gets the sort_by of this TagRequest.

        根据xx排序

        :return: The sort_by of this TagRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this TagRequest.

        根据xx排序

        :param sort_by: The sort_by of this TagRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this TagRequest.

        升序/降序

        :return: The sort_order of this TagRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this TagRequest.

        升序/降序

        :param sort_order: The sort_order of this TagRequest.
        :type sort_order: str
        """
        self._sort_order = sort_order

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
        if not isinstance(other, TagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
