# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListModelsRequest:

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
        'visibility': 'str',
        'sort_by': 'str',
        'order_by': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'visibility': 'visibility',
        'sort_by': 'sort_by',
        'order_by': 'order_by'
    }

    def __init__(self, workspace_id=None, offset=None, limit=None, name=None, id=None, type=None, visibility=None, sort_by=None, order_by=None):
        r"""ListModelsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: 工作空间ID
        :type workspace_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param name: 通过名字搜索Model，支持模糊查询
        :type name: str
        :param id: 通过模型ID检索，32~36位的英文、数字、短横组合
        :type id: str
        :param type: 通过模型类型检索
        :type type: str
        :param visibility: 可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - ALL: 所有的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。
        :type visibility: str
        :param sort_by: 指定排序字段，可选值为： CREATE_TIME：创建时间，默认值 UPDATE_TIME：更新时间 NAME: 服务名称
        :type sort_by: str
        :param order_by: 排序方式，可选值如下： ASC : 递增排序 DESC: 递减排序，默认值
        :type order_by: str
        """
        
        

        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._name = None
        self._id = None
        self._type = None
        self._visibility = None
        self._sort_by = None
        self._order_by = None
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
        if visibility is not None:
            self.visibility = visibility
        if sort_by is not None:
            self.sort_by = sort_by
        if order_by is not None:
            self.order_by = order_by

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListModelsRequest.

        工作空间ID

        :return: The workspace_id of this ListModelsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListModelsRequest.

        工作空间ID

        :param workspace_id: The workspace_id of this ListModelsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListModelsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListModelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListModelsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListModelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListModelsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListModelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListModelsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListModelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        r"""Gets the name of this ListModelsRequest.

        通过名字搜索Model，支持模糊查询

        :return: The name of this ListModelsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListModelsRequest.

        通过名字搜索Model，支持模糊查询

        :param name: The name of this ListModelsRequest.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this ListModelsRequest.

        通过模型ID检索，32~36位的英文、数字、短横组合

        :return: The id of this ListModelsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListModelsRequest.

        通过模型ID检索，32~36位的英文、数字、短横组合

        :param id: The id of this ListModelsRequest.
        :type id: str
        """
        self._id = id

    @property
    def type(self):
        r"""Gets the type of this ListModelsRequest.

        通过模型类型检索

        :return: The type of this ListModelsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListModelsRequest.

        通过模型类型检索

        :param type: The type of this ListModelsRequest.
        :type type: str
        """
        self._type = type

    @property
    def visibility(self):
        r"""Gets the visibility of this ListModelsRequest.

        可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - ALL: 所有的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。

        :return: The visibility of this ListModelsRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ListModelsRequest.

        可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - ALL: 所有的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。

        :param visibility: The visibility of this ListModelsRequest.
        :type visibility: str
        """
        self._visibility = visibility

    @property
    def sort_by(self):
        r"""Gets the sort_by of this ListModelsRequest.

        指定排序字段，可选值为： CREATE_TIME：创建时间，默认值 UPDATE_TIME：更新时间 NAME: 服务名称

        :return: The sort_by of this ListModelsRequest.
        :rtype: str
        """
        return self._sort_by

    @sort_by.setter
    def sort_by(self, sort_by):
        r"""Sets the sort_by of this ListModelsRequest.

        指定排序字段，可选值为： CREATE_TIME：创建时间，默认值 UPDATE_TIME：更新时间 NAME: 服务名称

        :param sort_by: The sort_by of this ListModelsRequest.
        :type sort_by: str
        """
        self._sort_by = sort_by

    @property
    def order_by(self):
        r"""Gets the order_by of this ListModelsRequest.

        排序方式，可选值如下： ASC : 递增排序 DESC: 递减排序，默认值

        :return: The order_by of this ListModelsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListModelsRequest.

        排序方式，可选值如下： ASC : 递增排序 DESC: 递减排序，默认值

        :param order_by: The order_by of this ListModelsRequest.
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
        if not isinstance(other, ListModelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
