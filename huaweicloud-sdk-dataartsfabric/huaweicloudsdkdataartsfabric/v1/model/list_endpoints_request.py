# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEndpointsRequest:

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
        'model_id': 'str',
        'name': 'str',
        'endpoint_id': 'str',
        'type': 'EndpointType',
        'visibility': 'str'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit',
        'model_id': 'model_id',
        'name': 'name',
        'endpoint_id': 'endpoint_id',
        'type': 'type',
        'visibility': 'visibility'
    }

    def __init__(self, workspace_id=None, offset=None, limit=None, model_id=None, name=None, endpoint_id=None, type=None, visibility=None):
        r"""ListEndpointsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: Workspace的ID
        :type workspace_id: str
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 指定每一页返回的最大条目数，取值范围[1,100]，默认为10。
        :type limit: int
        :param model_id: 通过模型ID检索，32~36位的英文、数字、短横组合
        :type model_id: str
        :param name: 通过名字搜索Endpoint的参数，一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线，支持模糊查询
        :type name: str
        :param endpoint_id: 通过id检索Endpoint的参数
        :type endpoint_id: str
        :param type: 通过类型检索Endpoint的参数
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        :param visibility: 可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - ALL: 所有的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。
        :type visibility: str
        """
        
        

        self._workspace_id = None
        self._offset = None
        self._limit = None
        self._model_id = None
        self._name = None
        self._endpoint_id = None
        self._type = None
        self._visibility = None
        self.discriminator = None

        self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if model_id is not None:
            self.model_id = model_id
        if name is not None:
            self.name = name
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if type is not None:
            self.type = type
        if visibility is not None:
            self.visibility = visibility

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListEndpointsRequest.

        Workspace的ID

        :return: The workspace_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListEndpointsRequest.

        Workspace的ID

        :param workspace_id: The workspace_id of this ListEndpointsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListEndpointsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListEndpointsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEndpointsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListEndpointsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEndpointsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :return: The limit of this ListEndpointsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEndpointsRequest.

        指定每一页返回的最大条目数，取值范围[1,100]，默认为10。

        :param limit: The limit of this ListEndpointsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def model_id(self):
        r"""Gets the model_id of this ListEndpointsRequest.

        通过模型ID检索，32~36位的英文、数字、短横组合

        :return: The model_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this ListEndpointsRequest.

        通过模型ID检索，32~36位的英文、数字、短横组合

        :param model_id: The model_id of this ListEndpointsRequest.
        :type model_id: str
        """
        self._model_id = model_id

    @property
    def name(self):
        r"""Gets the name of this ListEndpointsRequest.

        通过名字搜索Endpoint的参数，一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线，支持模糊查询

        :return: The name of this ListEndpointsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListEndpointsRequest.

        通过名字搜索Endpoint的参数，一个Endpoint名称，只能包含中文、字母、数字、下划线、中划线，支持模糊查询

        :param name: The name of this ListEndpointsRequest.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListEndpointsRequest.

        通过id检索Endpoint的参数

        :return: The endpoint_id of this ListEndpointsRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListEndpointsRequest.

        通过id检索Endpoint的参数

        :param endpoint_id: The endpoint_id of this ListEndpointsRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def type(self):
        r"""Gets the type of this ListEndpointsRequest.

        通过类型检索Endpoint的参数

        :return: The type of this ListEndpointsRequest.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListEndpointsRequest.

        通过类型检索Endpoint的参数

        :param type: The type of this ListEndpointsRequest.
        :type type: :class:`huaweicloudsdkdataartsfabric.v1.EndpointType`
        """
        self._type = type

    @property
    def visibility(self):
        r"""Gets the visibility of this ListEndpointsRequest.

        可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - ALL: 所有的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。

        :return: The visibility of this ListEndpointsRequest.
        :rtype: str
        """
        return self._visibility

    @visibility.setter
    def visibility(self, visibility):
        r"""Sets the visibility of this ListEndpointsRequest.

        可见性检索的参数，可选值为： - PRIVATE: 私有，用户自己创建的； - PUBLIC:公共，查询所有公共的，包括其他用户创建的； - ALL: 所有的； - 默认为空，不填表示不限制，则查出当前用户下的，包括PRIVATE和PUBLIC，不包括其他用户创建的。

        :param visibility: The visibility of this ListEndpointsRequest.
        :type visibility: str
        """
        self._visibility = visibility

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
        if not isinstance(other, ListEndpointsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
