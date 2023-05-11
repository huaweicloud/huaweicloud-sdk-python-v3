# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowNodesRequest:

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
        'app_name': 'str',
        'tags': 'str',
        'provider': 'str',
        'cluster_id': 'str',
        'status': 'str',
        'active_status': 'str'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'name': 'name',
        'workspace_id': 'workspace_id',
        'app_name': 'app_name',
        'tags': 'tags',
        'provider': 'provider',
        'cluster_id': 'cluster_id',
        'status': 'status',
        'active_status': 'active_status'
    }

    def __init__(self, offset=None, limit=None, name=None, workspace_id=None, app_name=None, tags=None, provider=None, cluster_id=None, status=None, active_status=None):
        """ShowNodesRequest

        The model defined in huaweicloud sdk

        :param offset: 查询的起始位置，取值范围为非负整数，默认为0
        :type offset: int
        :param limit: 每页显示的条目数量，取值范围1~100，默认为100
        :type limit: int
        :param name: 设备名称，模糊匹配，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64
        :type name: str
        :param workspace_id: 工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID
        :type workspace_id: str
        :param app_name: 应用名称，模糊匹配，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾
        :type app_name: str
        :param tags: 标签的key和value通过点连接，多个标签通过逗号连接，如：tags&#x3D;key1.value1,key2.value2
        :type tags: str
        :param provider: 服务提供者：ief或hilens。不传会查询全部服务类型的设备列表
        :type provider: str
        :param cluster_id: 集群ID，若值为0会过滤出不隶属任何集群的设备
        :type cluster_id: str
        :param status: 状态
        :type status: str
        :param active_status: 设备激活状态，分别是未激活（INACTIVE）、已激活（ACTIVATED）、已到期（EXPIRED）
        :type active_status: str
        """
        
        

        self._offset = None
        self._limit = None
        self._name = None
        self._workspace_id = None
        self._app_name = None
        self._tags = None
        self._provider = None
        self._cluster_id = None
        self._status = None
        self._active_status = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if name is not None:
            self.name = name
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if app_name is not None:
            self.app_name = app_name
        if tags is not None:
            self.tags = tags
        if provider is not None:
            self.provider = provider
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if status is not None:
            self.status = status
        if active_status is not None:
            self.active_status = active_status

    @property
    def offset(self):
        """Gets the offset of this ShowNodesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :return: The offset of this ShowNodesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowNodesRequest.

        查询的起始位置，取值范围为非负整数，默认为0

        :param offset: The offset of this ShowNodesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ShowNodesRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :return: The limit of this ShowNodesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowNodesRequest.

        每页显示的条目数量，取值范围1~100，默认为100

        :param limit: The limit of this ShowNodesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def name(self):
        """Gets the name of this ShowNodesRequest.

        设备名称，模糊匹配，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :return: The name of this ShowNodesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowNodesRequest.

        设备名称，模糊匹配，只允许中文字符、英文字母、数字、下划线、中划线，最大长度64

        :param name: The name of this ShowNodesRequest.
        :type name: str
        """
        self._name = name

    @property
    def workspace_id(self):
        """Gets the workspace_id of this ShowNodesRequest.

        工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :return: The workspace_id of this ShowNodesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        """Sets the workspace_id of this ShowNodesRequest.

        工作空间ID，默认为注册账号/子账号的default工作空间，可通过专业版HiLens控制台展开工作空间列表获取到工作空间ID

        :param workspace_id: The workspace_id of this ShowNodesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def app_name(self):
        """Gets the app_name of this ShowNodesRequest.

        应用名称，模糊匹配，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾

        :return: The app_name of this ShowNodesRequest.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ShowNodesRequest.

        应用名称，模糊匹配，只允许英文小写字母、数字、中划线，最大长度32, 英文小写字母或数字开头和结尾

        :param app_name: The app_name of this ShowNodesRequest.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def tags(self):
        """Gets the tags of this ShowNodesRequest.

        标签的key和value通过点连接，多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :return: The tags of this ShowNodesRequest.
        :rtype: str
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowNodesRequest.

        标签的key和value通过点连接，多个标签通过逗号连接，如：tags=key1.value1,key2.value2

        :param tags: The tags of this ShowNodesRequest.
        :type tags: str
        """
        self._tags = tags

    @property
    def provider(self):
        """Gets the provider of this ShowNodesRequest.

        服务提供者：ief或hilens。不传会查询全部服务类型的设备列表

        :return: The provider of this ShowNodesRequest.
        :rtype: str
        """
        return self._provider

    @provider.setter
    def provider(self, provider):
        """Sets the provider of this ShowNodesRequest.

        服务提供者：ief或hilens。不传会查询全部服务类型的设备列表

        :param provider: The provider of this ShowNodesRequest.
        :type provider: str
        """
        self._provider = provider

    @property
    def cluster_id(self):
        """Gets the cluster_id of this ShowNodesRequest.

        集群ID，若值为0会过滤出不隶属任何集群的设备

        :return: The cluster_id of this ShowNodesRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this ShowNodesRequest.

        集群ID，若值为0会过滤出不隶属任何集群的设备

        :param cluster_id: The cluster_id of this ShowNodesRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def status(self):
        """Gets the status of this ShowNodesRequest.

        状态

        :return: The status of this ShowNodesRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowNodesRequest.

        状态

        :param status: The status of this ShowNodesRequest.
        :type status: str
        """
        self._status = status

    @property
    def active_status(self):
        """Gets the active_status of this ShowNodesRequest.

        设备激活状态，分别是未激活（INACTIVE）、已激活（ACTIVATED）、已到期（EXPIRED）

        :return: The active_status of this ShowNodesRequest.
        :rtype: str
        """
        return self._active_status

    @active_status.setter
    def active_status(self, active_status):
        """Sets the active_status of this ShowNodesRequest.

        设备激活状态，分别是未激活（INACTIVE）、已激活（ACTIVATED）、已到期（EXPIRED）

        :param active_status: The active_status of this ShowNodesRequest.
        :type active_status: str
        """
        self._active_status = active_status

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
        if not isinstance(other, ShowNodesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
