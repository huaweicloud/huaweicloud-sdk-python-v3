# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecretsRequest:

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
        'name': 'str',
        'workspace_id': 'str',
        'tags': 'str',
        'provider': 'str',
        'sort': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'tags': 'tags',
        'provider': 'provider',
        'sort': 'sort'
    }

    def __init__(self, offset=None, limit=None, name=None, workspace_id=None, tags=None, provider=None, sort=None):
        """ListSecretsRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页显示的条目数量，取值范围1~100，默认为100
        :type limit: int
        :param name: 设备名称，模糊匹配，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param workspace_id: 工作空间ID，默认为注册账号子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID
        :type workspace_id: str
        :param tags: 标签的key和value通过点连接，多个标签通过逗号连接，如：tags&#x3D;key1.value1,key2.value2
        :type tags: str
        :param provider: 服务提供者：ief或hilens。不传会查询全部服务类型的设备列表
        :type provider: str
        :param sort: 排序方式，可根据名称、创建时间、更新时间排序枚举值：name，created_at，updated_at。sort默认升序，如sort&#x3D;name，降序：sort&#x3D;name%3Adesc。不填默认为sort&#x3D;created_at%3Adesc。
        :type sort: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._workspace_id = None
        self._tags = None
        self._provider = None
        self._sort = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if tags is not None:
            self.tags = tags
        if provider is not None:
            self.provider = provider
        if sort is not None:
            self.sort = sort

    @property
    def offset(self):
        """Gets the offset of this ListSecretsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ListSecretsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListSecretsRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ListSecretsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListSecretsRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :return: The limit of this ListSecretsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListSecretsRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :param limit: The limit of this ListSecretsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ListSecretsRequest.

        设备名称，模糊匹配，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this ListSecretsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListSecretsRequest.

        设备名称，模糊匹配，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this ListSecretsRequest.
        :type name: str
        """
        self._name = name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ListSecretsRequest.

        工作空间ID，默认为注册账号子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :return: The workspace_id of this ListSecretsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ListSecretsRequest.

        工作空间ID，默认为注册账号子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :param workspace_id: The workspace_id of this ListSecretsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def tags(self):
        """Gets the tags of this ListSecretsRequest.

        标签的key和value通过点连接，多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :return: The tags of this ListSecretsRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ListSecretsRequest.

        标签的key和value通过点连接，多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :param tags: The tags of this ListSecretsRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def provider(self):
        """Gets the provider of this ListSecretsRequest.

        服务提供者：ief或hilens。不传会查询全部服务类型的设备列表

        :return: The provider of this ListSecretsRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ListSecretsRequest.

        服务提供者：ief或hilens。不传会查询全部服务类型的设备列表

        :param provider: The provider of this ListSecretsRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def sort(self):
        """Gets the sort of this ListSecretsRequest.

        排序方式，可根据名称、创建时间、更新时间排序枚举值：name，created_at，updated_at。sort默认升序，如sort=name，降序：sort=name%3Adesc。不填默认为sort=created_at%3Adesc。

        :return: The sort of this ListSecretsRequest.
        :rtype: str
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """Sets the sort of this ListSecretsRequest.

        排序方式，可根据名称、创建时间、更新时间排序枚举值：name，created_at，updated_at。sort默认升序，如sort=name，降序：sort=name%3Adesc。不填默认为sort=created_at%3Adesc。

        :param sort: The sort of this ListSecretsRequest.
        :type sort: str
        """
        self._sort = sort

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
        if not isinstance(other, ListSecretsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
