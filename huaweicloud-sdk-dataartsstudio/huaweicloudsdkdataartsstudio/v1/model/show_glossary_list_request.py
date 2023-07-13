# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGlossaryListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'type': 'str',
        'name': 'str',
        'create_user': 'str',
        'start': 'str',
        'end': 'str',
        'limit': 'str',
        'offset': 'str',
        'sort_by': 'str',
        'sort_order': 'str'
    }

    attribute_map = {
        'workspace': 'workspace',
        'type': 'type',
        'name': 'name',
        'create_user': 'create_user',
        'start': 'start',
        'end': 'end',
        'limit': 'limit',
        'offset': 'offset',
        'sort_by': 'sort_by',
        'sort_order': 'sort_order'
    }

    def __init__(self, workspace=None, type=None, name=None, create_user=None, start=None, end=None, limit=None, offset=None, sort_by=None, sort_order=None):
        """ShowGlossaryListRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param type: 标签类型 缺省值：all
        :type type: str
        :param name: 标签名
        :type name: str
        :param create_user: 标签创建用户
        :type create_user: str
        :param start: 开始时间
        :type start: str
        :param end: 结束时间
        :type end: str
        :param limit: 分页参数:每页限定数量 缺省值：10
        :type limit: str
        :param offset: 分页参数：页数 缺省值：0
        :type offset: str
        :param sort_by: 排序字段 默认为createTime 缺省值：createTime
        :type sort_by: str
        :param sort_order: 排序方式 默认排序字段为降序 缺省值：desc
        :type sort_order: str
        """
        
        

        self._workspace = None
        self._type = None
        self._name = None
        self._create_user = None
        self._start = None
        self._end = None
        self._limit = None
        self._offset = None
        self._sort_by = None
        self._sort_order = None
        self.discriminator = None

        self.workspace = workspace
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
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_by is not None:
            self.sort_by = sort_by
        if sort_order is not None:
            self.sort_order = sort_order

    @property
    def workspace(self):
        """Gets the workspace of this ShowGlossaryListRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        """Sets the workspace of this ShowGlossaryListRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ShowGlossaryListRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def type(self):
        """Gets the type of this ShowGlossaryListRequest.

        标签类型 缺省值：all

        :return: The type of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowGlossaryListRequest.

        标签类型 缺省值：all

        :param type: The type of this ShowGlossaryListRequest.
        :type type: str
        """
        self._type = type

    @property
    def name(self):
        """Gets the name of this ShowGlossaryListRequest.

        标签名

        :return: The name of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowGlossaryListRequest.

        标签名

        :param name: The name of this ShowGlossaryListRequest.
        :type name: str
        """
        self._name = name

    @property
    def create_user(self):
        """Gets the create_user of this ShowGlossaryListRequest.

        标签创建用户

        :return: The create_user of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ShowGlossaryListRequest.

        标签创建用户

        :param create_user: The create_user of this ShowGlossaryListRequest.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def start(self):
        """Gets the start of this ShowGlossaryListRequest.

        开始时间

        :return: The start of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this ShowGlossaryListRequest.

        开始时间

        :param start: The start of this ShowGlossaryListRequest.
        :type start: str
        """
        self._start = start

    @property
    def end(self):
        """Gets the end of this ShowGlossaryListRequest.

        结束时间

        :return: The end of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this ShowGlossaryListRequest.

        结束时间

        :param end: The end of this ShowGlossaryListRequest.
        :type end: str
        """
        self._end = end

    @property
    def limit(self):
        """Gets the limit of this ShowGlossaryListRequest.

        分页参数:每页限定数量 缺省值：10

        :return: The limit of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowGlossaryListRequest.

        分页参数:每页限定数量 缺省值：10

        :param limit: The limit of this ShowGlossaryListRequest.
        :type limit: str
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowGlossaryListRequest.

        分页参数：页数 缺省值：0

        :return: The offset of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowGlossaryListRequest.

        分页参数：页数 缺省值：0

        :param offset: The offset of this ShowGlossaryListRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def sort_by(self):
        """Gets the sort_by of this ShowGlossaryListRequest.

        排序字段 默认为createTime 缺省值：createTime

        :return: The sort_by of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        """Sets the sort_by of this ShowGlossaryListRequest.

        排序字段 默认为createTime 缺省值：createTime

        :param sort_by: The sort_by of this ShowGlossaryListRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def sort_order(self):
        """Gets the sort_order of this ShowGlossaryListRequest.

        排序方式 默认排序字段为降序 缺省值：desc

        :return: The sort_order of this ShowGlossaryListRequest.
        :rtype: str
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this ShowGlossaryListRequest.

        排序方式 默认排序字段为降序 缺省值：desc

        :param sort_order: The sort_order of this ShowGlossaryListRequest.
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
        if not isinstance(other, ShowGlossaryListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
