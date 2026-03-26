# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'name': 'str',
        'id': 'str',
        'type': 'str',
        'endpoint_id': 'str',
        'sort_by': 'str',
        'order_by': 'str',
        'create_by_me': 'bool'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'endpoint_id': 'endpoint_id',
        'sort_by': 'sort_by',
        'order_by': 'order_by',
        'create_by_me': 'create_by_me'
    }

    def __init__(self, workspace_id=None, offset=None, limit=None, name=None, id=None, type=None, endpoint_id=None, sort_by=None, order_by=None, create_by_me=None):
        r"""ListJobsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param name: 通过名字搜索作业
        :type name: str
        :param id: 通过作业id检索
        :type id: str
        :param type: 通过类型检索
        :type type: str
        :param endpoint_id: 通过id检索Endpoint的参数
        :type endpoint_id: str
        :param sort_by: 指定排序字段，可选值为： CREATE_TIME：创建时间，默认值 UPDATE_TIME：更新时间 NAME: 服务名称
        :type sort_by: str
        :param order_by: 排序方式，可选值如下： ASC : 递增排序 DESC: 递减排序，默认值
        :type order_by: str
        :param create_by_me: 是否由我创建的作业。 默认为null，即返回租户下所有子用户的作业； True: 只返回当前子用户的作业； False: 返回租户下所有子用户的作业；
        :type create_by_me: bool
        """
        
        

        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._id = None
        self._type = None
        self._endpoint_id = None
        self._sort_by = None
        self._order_by = None
        self._create_by_me = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if sort_by is not None:
            self.sort_by = sort_by
        if order_by is not None:
            self.order_by = order_by
        if create_by_me is not None:
            self.create_by_me = create_by_me

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListJobsRequest.

        工作空间ID

        :return: The workspace_id of this ListJobsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListJobsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListJobsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListJobsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListJobsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListJobsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListJobsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListJobsRequest.

        通过名字搜索作业

        :return: The name of this ListJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListJobsRequest.

        通过名字搜索作业

        :param name: The name of this ListJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListJobsRequest.

        通过作业id检索

        :return: The id of this ListJobsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListJobsRequest.

        通过作业id检索

        :param id: The id of this ListJobsRequest.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ListJobsRequest.

        通过类型检索

        :return: The type of this ListJobsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListJobsRequest.

        通过类型检索

        :param type: The type of this ListJobsRequest.
        :type type: str
        """
        self._type = type

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListJobsRequest.

        通过id检索Endpoint的参数

        :return: The endpoint_id of this ListJobsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListJobsRequest.

        通过id检索Endpoint的参数

        :param endpoint_id: The endpoint_id of this ListJobsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListJobsRequest.

        指定排序字段，可选值为： CREATE_TIME：创建时间，默认值 UPDATE_TIME：更新时间 NAME: 服务名称

        :return: The sort_by of this ListJobsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListJobsRequest.

        指定排序字段，可选值为： CREATE_TIME：创建时间，默认值 UPDATE_TIME：更新时间 NAME: 服务名称

        :param sort_by: The sort_by of this ListJobsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order_by(self):
        r"""Gets the order_by of this ListJobsRequest.

        排序方式，可选值如下： ASC : 递增排序 DESC: 递减排序，默认值

        :return: The order_by of this ListJobsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListJobsRequest.

        排序方式，可选值如下： ASC : 递增排序 DESC: 递减排序，默认值

        :param order_by: The order_by of this ListJobsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def create_by_me(self):
        r"""Gets the create_by_me of this ListJobsRequest.

        是否由我创建的作业。 默认为null，即返回租户下所有子用户的作业； True: 只返回当前子用户的作业； False: 返回租户下所有子用户的作业；

        :return: The create_by_me of this ListJobsRequest.
        :rtype: bool
        """
        return self._create_by_me

    @create_by_me.setter
    def create_by_me(self, create_by_me):
        r"""Sets the create_by_me of this ListJobsRequest.

        是否由我创建的作业。 默认为null，即返回租户下所有子用户的作业； True: 只返回当前子用户的作业； False: 返回租户下所有子用户的作业；

        :param create_by_me: The create_by_me of this ListJobsRequest.
        :type create_by_me: bool
        """
        self._create_by_me = create_by_me

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
