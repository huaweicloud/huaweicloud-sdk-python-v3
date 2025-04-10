# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServicesInstancesRequest:

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
        'id': 'str',
        'name': 'str',
        'limit': 'int',
        'offset': 'int',
        'endpoint_id': 'str',
        'source_id': 'str',
        'version_id': 'str',
        'type': 'str',
        'visibility': 'str',
        'sort_by': 'str',
        'order_by': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'id': 'id',
        'name': 'name',
        'limit': 'limit',
        'offset': 'offset',
        'endpoint_id': 'endpoint_id',
        'source_id': 'source_id',
        'version_id': 'version_id',
        'type': 'type',
        'visibility': 'visibility',
        'sort_by': 'sort_by',
        'order_by': 'order_by'
    }

    def __init__(self, workspace_id=None, id=None, name=None, limit=None, offset=None, endpoint_id=None, source_id=None, version_id=None, type=None, visibility=None, sort_by=None, order_by=None):
        r"""ListServicesInstancesRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param id: 通过service Instance id检索，32~36位的英文、数字、短横组合
        :type id: str
        :param name: 通过名字搜索Service Instance，支持模糊查询
        :type name: str
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param endpoint_id: 通过id检索Endpoint的参数
        :type endpoint_id: str
        :param source_id: Service ID或者Model ID
        :type source_id: str
        :param version_id: Service version ID或者Model version ID
        :type version_id: str
        :param type: Service的类型，可选值： - PGSQL_SERVICE：DWS Pay-By-Query - LLM_MODEL：大语言模型
        :type type: str
        :param visibility: 可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。
        :type visibility: str
        :param sort_by: 根据字段排序，可选值： - CREATE_TIME：创建时间 - DURATION: 运行时间
        :type sort_by: str
        :param order_by: 排序方式，可选值： - ASC：正序排序 - DESC: 倒序排序
        :type order_by: str
        """
        
        

        self._workspace_id = None
        self._id = None
        self._name = None
        self._limit = None
        self._offset = None
        self._endpoint_id = None
        self._source_id = None
        self._version_id = None
        self._type = None
        self._visibility = None
        self._sort_by = None
        self._order_by = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if source_id is not None:
            self.source_id = source_id
        if version_id is not None:
            self.version_id = version_id
        if type is not None:
            self.type = type
        if visibility is not None:
            self.visibility = visibility
        if sort_by is not None:
            self.sort_by = sort_by
        if order_by is not None:
            self.order_by = order_by

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListServicesInstancesRequest.

        Workspace的ID

        :return: The workspace_id of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListServicesInstancesRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this ListServicesInstancesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def id(self):
        r"""Gets the id of this ListServicesInstancesRequest.

        通过service Instance id检索，32~36位的英文、数字、短横组合

        :return: The id of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListServicesInstancesRequest.

        通过service Instance id检索，32~36位的英文、数字、短横组合

        :param id: The id of this ListServicesInstancesRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListServicesInstancesRequest.

        通过名字搜索Service Instance，支持模糊查询

        :return: The name of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListServicesInstancesRequest.

        通过名字搜索Service Instance，支持模糊查询

        :param name: The name of this ListServicesInstancesRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListServicesInstancesRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListServicesInstancesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListServicesInstancesRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListServicesInstancesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListServicesInstancesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListServicesInstancesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListServicesInstancesRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListServicesInstancesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListServicesInstancesRequest.

        通过id检索Endpoint的参数

        :return: The endpoint_id of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListServicesInstancesRequest.

        通过id检索Endpoint的参数

        :param endpoint_id: The endpoint_id of this ListServicesInstancesRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def source_id(self):
        r"""Gets the source_id of this ListServicesInstancesRequest.

        Service ID或者Model ID

        :return: The source_id of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._source_id

    @source_id.setter
    def source_id(self, source_id):
        r"""Sets the source_id of this ListServicesInstancesRequest.

        Service ID或者Model ID

        :param source_id: The source_id of this ListServicesInstancesRequest.
        :type source_id: str
        """
        self._source_id = source_id

    @property
    def version_id(self):
        r"""Gets the version_id of this ListServicesInstancesRequest.

        Service version ID或者Model version ID

        :return: The version_id of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._version_id

    @version_id.setter
    def version_id(self, version_id):
        r"""Sets the version_id of this ListServicesInstancesRequest.

        Service version ID或者Model version ID

        :param version_id: The version_id of this ListServicesInstancesRequest.
        :type version_id: str
        """
        self._version_id = version_id

    @property
    def type(self):
        r"""Gets the type of this ListServicesInstancesRequest.

        Service的类型，可选值： - PGSQL_SERVICE：DWS Pay-By-Query - LLM_MODEL：大语言模型

        :return: The type of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListServicesInstancesRequest.

        Service的类型，可选值： - PGSQL_SERVICE：DWS Pay-By-Query - LLM_MODEL：大语言模型

        :param type: The type of this ListServicesInstancesRequest.
        :type type: str
        """
        self._type = type

    @property
    def visibility(self):
        r"""Gets the visibility of this ListServicesInstancesRequest.

        可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。

        :return: The visibility of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ListServicesInstancesRequest.

        可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。

        :param visibility: The visibility of this ListServicesInstancesRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListServicesInstancesRequest.

        根据字段排序，可选值： - CREATE_TIME：创建时间 - DURATION: 运行时间

        :return: The sort_by of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListServicesInstancesRequest.

        根据字段排序，可选值： - CREATE_TIME：创建时间 - DURATION: 运行时间

        :param sort_by: The sort_by of this ListServicesInstancesRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order_by(self):
        r"""Gets the order_by of this ListServicesInstancesRequest.

        排序方式，可选值： - ASC：正序排序 - DESC: 倒序排序

        :return: The order_by of this ListServicesInstancesRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListServicesInstancesRequest.

        排序方式，可选值： - ASC：正序排序 - DESC: 倒序排序

        :param order_by: The order_by of this ListServicesInstancesRequest.
        :type order_by: str
        """
        self._order_by = order_by

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
        if not isinstance(other, ListServicesInstancesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
