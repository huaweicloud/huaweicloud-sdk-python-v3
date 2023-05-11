# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigMapsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'provider': 'str',
        'name': 'str',
        'workspace_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'sort': 'str',
        'tag_key': 'str'
    }

    attribute_map = {
        'provider': 'provider',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'limit': 'limit',
        'offset': 'offset',
        'sort': 'sort',
        'tag_key': 'tag_key'
    }

    def __init__(self, provider=None, name=None, workspace_id=None, limit=None, offset=None, sort=None, tag_key=None):
        """ListConfigMapsRequest

        The model defined in huaweicloud sdk

        :param provider: 服务提供者：ief或hilens，默认为hilens。
        :type provider: str
        :param name: 配置项名称，模糊匹配。
        :type name: str
        :param workspace_id: 工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID
        :type workspace_id: str
        :param limit: 每页显示的条目数量，取值范围1~1000，默认值为1000。
        :type limit: int
        :param offset: 查询的起始位置，取值范围为非负整数，默认为0。
        :type offset: int
        :param sort: 排序方式，可根据名称、创建时间、更新时间排序枚举值：name，created_at，updated_at。sort默认升序，如sort&#x3D;name，降序：sort&#x3D;name%3Adesc。不填默认为sort&#x3D;created_at%3Adesc。
        :type sort: str
        :param tag_key: 格式为{tag_key}&#x3D;{tag_value}，支持多对tag或查询。
        :type tag_key: str
        """
        
        

        self._provider = None
        self._name = None
        self._workspace_id = None
        self._limit = None
        self._offset = None
        self._sort = None
        self._tag_key = None
        self.discriminator = None

        if provider is not None:
            self.provider = provider
        if name is not None:
            self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort is not None:
            self.sort = sort
        if tag_key is not None:
            self.tag_key = tag_key

    @property
    def provider(self):
        """Gets the provider of this ListConfigMapsRequest.

        服务提供者：ief或hilens，默认为hilens。

        :return: The provider of this ListConfigMapsRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ListConfigMapsRequest.

        服务提供者：ief或hilens，默认为hilens。

        :param provider: The provider of this ListConfigMapsRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def name(self):
        """Gets the name of this ListConfigMapsRequest.

        配置项名称，模糊匹配。

        :return: The name of this ListConfigMapsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListConfigMapsRequest.

        配置项名称，模糊匹配。

        :param name: The name of this ListConfigMapsRequest.
        :type name: str
        """
        self._name = name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListConfigMapsRequest.

        工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :return: The workspace_id of this ListConfigMapsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListConfigMapsRequest.

        工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :param workspace_id: The workspace_id of this ListConfigMapsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def limit(self):
        """Gets the limit of this ListConfigMapsRequest.

        每页显示的条目数量，取值范围1~1000，默认值为1000。

        :return: The limit of this ListConfigMapsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListConfigMapsRequest.

        每页显示的条目数量，取值范围1~1000，默认值为1000。

        :param limit: The limit of this ListConfigMapsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListConfigMapsRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :return: The offset of this ListConfigMapsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListConfigMapsRequest.

        查询的起始位置，取值范围为非负整数，默认为0。

        :param offset: The offset of this ListConfigMapsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort(self):
        """Gets the sort of this ListConfigMapsRequest.

        排序方式，可根据名称、创建时间、更新时间排序枚举值：name，created_at，updated_at。sort默认升序，如sort=name，降序：sort=name%3Adesc。不填默认为sort=created_at%3Adesc。

        :return: The sort of this ListConfigMapsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListConfigMapsRequest.

        排序方式，可根据名称、创建时间、更新时间排序枚举值：name，created_at，updated_at。sort默认升序，如sort=name，降序：sort=name%3Adesc。不填默认为sort=created_at%3Adesc。

        :param sort: The sort of this ListConfigMapsRequest.
        :type sort: str
        """
        self._sort = sort

    @property
    def tag_key(self):
        """Gets the tag_key of this ListConfigMapsRequest.

        格式为{tag_key}={tag_value}，支持多对tag或查询。

        :return: The tag_key of this ListConfigMapsRequest.
        :rtype: str
        """
        return self._tag_key

    @tag_key.setter
    def tag_key(self, tag_key):
        """Sets the tag_key of this ListConfigMapsRequest.

        格式为{tag_key}={tag_value}，支持多对tag或查询。

        :param tag_key: The tag_key of this ListConfigMapsRequest.
        :type tag_key: str
        """
        self._tag_key = tag_key

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
        if not isinstance(other, ListConfigMapsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
