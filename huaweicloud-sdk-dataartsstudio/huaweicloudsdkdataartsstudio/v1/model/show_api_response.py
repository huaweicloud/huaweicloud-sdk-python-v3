# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'group_id': 'str',
        'description': 'str',
        'protocol': 'str',
        'publish_type': 'str',
        'log_flag': 'bool',
        'path': 'str',
        'host': 'str',
        'hosts': 'InstanceHostDTO',
        'request_type': 'str',
        'create_user': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'manager': 'str',
        'status': 'str',
        'type': 'str',
        'debug_status': 'str',
        'publish_messages': 'list[ApiPublishDTO]',
        'request_paras': 'list[RequestPara]',
        'datasource_config': 'DatasourceConfig',
        'backend_config': 'BackendConfig'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'group_id': 'group_id',
        'description': 'description',
        'protocol': 'protocol',
        'publish_type': 'publish_type',
        'log_flag': 'log_flag',
        'path': 'path',
        'host': 'host',
        'hosts': 'hosts',
        'request_type': 'request_type',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'manager': 'manager',
        'status': 'status',
        'type': 'type',
        'debug_status': 'debug_status',
        'publish_messages': 'publish_messages',
        'request_paras': 'request_paras',
        'datasource_config': 'datasource_config',
        'backend_config': 'backend_config'
    }

    def __init__(self, id=None, name=None, group_id=None, description=None, protocol=None, publish_type=None, log_flag=None, path=None, host=None, hosts=None, request_type=None, create_user=None, create_time=None, update_time=None, manager=None, status=None, type=None, debug_status=None, publish_messages=None, request_paras=None, datasource_config=None, backend_config=None):
        """ShowApiResponse

        The model defined in huaweicloud sdk

        :param id: API的ID
        :type id: str
        :param name: API名称
        :type name: str
        :param group_id: API所属分组的ID（共享版）
        :type group_id: str
        :param description: API 描述
        :type description: str
        :param protocol: API 访问协议
        :type protocol: str
        :param publish_type: 发布类型，公开或者私有
        :type publish_type: str
        :param log_flag: 是否开启日志记录
        :type log_flag: bool
        :param path: API的访问路径
        :type path: str
        :param host: 共享版域名
        :type host: str
        :param hosts: 
        :type hosts: :class:`huaweicloudsdkdataartsstudio.v1.InstanceHostDTO`
        :param request_type: API访问方式
        :type request_type: str
        :param create_user: API创建者
        :type create_user: str
        :param create_time: 创建时间
        :type create_time: int
        :param update_time: 更新时间
        :type update_time: int
        :param manager: API 审核人名称
        :type manager: str
        :param status: API的状态（共享版）
        :type status: str
        :param type: API 类型
        :type type: str
        :param debug_status: API调试状态（共享版）
        :type debug_status: str
        :param publish_messages: 发布信息列表（专享版）
        :type publish_messages: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiPublishDTO`]
        :param request_paras: API请求参数
        :type request_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.RequestPara`]
        :param datasource_config: 
        :type datasource_config: :class:`huaweicloudsdkdataartsstudio.v1.DatasourceConfig`
        :param backend_config: 
        :type backend_config: :class:`huaweicloudsdkdataartsstudio.v1.BackendConfig`
        """
        
        super(ShowApiResponse, self).__init__()

        self._id = None
        self._name = None
        self._group_id = None
        self._description = None
        self._protocol = None
        self._publish_type = None
        self._log_flag = None
        self._path = None
        self._host = None
        self._hosts = None
        self._request_type = None
        self._create_user = None
        self._create_time = None
        self._update_time = None
        self._manager = None
        self._status = None
        self._type = None
        self._debug_status = None
        self._publish_messages = None
        self._request_paras = None
        self._datasource_config = None
        self._backend_config = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if group_id is not None:
            self.group_id = group_id
        if description is not None:
            self.description = description
        if protocol is not None:
            self.protocol = protocol
        if publish_type is not None:
            self.publish_type = publish_type
        if log_flag is not None:
            self.log_flag = log_flag
        if path is not None:
            self.path = path
        if host is not None:
            self.host = host
        if hosts is not None:
            self.hosts = hosts
        if request_type is not None:
            self.request_type = request_type
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if manager is not None:
            self.manager = manager
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if debug_status is not None:
            self.debug_status = debug_status
        if publish_messages is not None:
            self.publish_messages = publish_messages
        if request_paras is not None:
            self.request_paras = request_paras
        if datasource_config is not None:
            self.datasource_config = datasource_config
        if backend_config is not None:
            self.backend_config = backend_config

    @property
    def id(self):
        """Gets the id of this ShowApiResponse.

        API的ID

        :return: The id of this ShowApiResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShowApiResponse.

        API的ID

        :param id: The id of this ShowApiResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ShowApiResponse.

        API名称

        :return: The name of this ShowApiResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowApiResponse.

        API名称

        :param name: The name of this ShowApiResponse.
        :type name: str
        """
        self._name = name

    @property
    def group_id(self):
        """Gets the group_id of this ShowApiResponse.

        API所属分组的ID（共享版）

        :return: The group_id of this ShowApiResponse.
        :rtype: str
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        """Sets the group_id of this ShowApiResponse.

        API所属分组的ID（共享版）

        :param group_id: The group_id of this ShowApiResponse.
        :type group_id: str
        """
        self._group_id = group_id

    @property
    def description(self):
        """Gets the description of this ShowApiResponse.

        API 描述

        :return: The description of this ShowApiResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowApiResponse.

        API 描述

        :param description: The description of this ShowApiResponse.
        :type description: str
        """
        self._description = description

    @property
    def protocol(self):
        """Gets the protocol of this ShowApiResponse.

        API 访问协议

        :return: The protocol of this ShowApiResponse.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """Sets the protocol of this ShowApiResponse.

        API 访问协议

        :param protocol: The protocol of this ShowApiResponse.
        :type protocol: str
        """
        self._protocol = protocol

    @property
    def publish_type(self):
        """Gets the publish_type of this ShowApiResponse.

        发布类型，公开或者私有

        :return: The publish_type of this ShowApiResponse.
        :rtype: str
        """
        return self._publish_type

    @publish_type.setter
    def publish_type(self, publish_type):
        """Sets the publish_type of this ShowApiResponse.

        发布类型，公开或者私有

        :param publish_type: The publish_type of this ShowApiResponse.
        :type publish_type: str
        """
        self._publish_type = publish_type

    @property
    def log_flag(self):
        """Gets the log_flag of this ShowApiResponse.

        是否开启日志记录

        :return: The log_flag of this ShowApiResponse.
        :rtype: bool
        """
        return self._log_flag

    @log_flag.setter
    def log_flag(self, log_flag):
        """Sets the log_flag of this ShowApiResponse.

        是否开启日志记录

        :param log_flag: The log_flag of this ShowApiResponse.
        :type log_flag: bool
        """
        self._log_flag = log_flag

    @property
    def path(self):
        """Gets the path of this ShowApiResponse.

        API的访问路径

        :return: The path of this ShowApiResponse.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ShowApiResponse.

        API的访问路径

        :param path: The path of this ShowApiResponse.
        :type path: str
        """
        self._path = path

    @property
    def host(self):
        """Gets the host of this ShowApiResponse.

        共享版域名

        :return: The host of this ShowApiResponse.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """Sets the host of this ShowApiResponse.

        共享版域名

        :param host: The host of this ShowApiResponse.
        :type host: str
        """
        self._host = host

    @property
    def hosts(self):
        """Gets the hosts of this ShowApiResponse.

        :return: The hosts of this ShowApiResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.InstanceHostDTO`
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this ShowApiResponse.

        :param hosts: The hosts of this ShowApiResponse.
        :type hosts: :class:`huaweicloudsdkdataartsstudio.v1.InstanceHostDTO`
        """
        self._hosts = hosts

    @property
    def request_type(self):
        """Gets the request_type of this ShowApiResponse.

        API访问方式

        :return: The request_type of this ShowApiResponse.
        :rtype: str
        """
        return self._request_type

    @request_type.setter
    def request_type(self, request_type):
        """Sets the request_type of this ShowApiResponse.

        API访问方式

        :param request_type: The request_type of this ShowApiResponse.
        :type request_type: str
        """
        self._request_type = request_type

    @property
    def create_user(self):
        """Gets the create_user of this ShowApiResponse.

        API创建者

        :return: The create_user of this ShowApiResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        """Sets the create_user of this ShowApiResponse.

        API创建者

        :param create_user: The create_user of this ShowApiResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def create_time(self):
        """Gets the create_time of this ShowApiResponse.

        创建时间

        :return: The create_time of this ShowApiResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ShowApiResponse.

        创建时间

        :param create_time: The create_time of this ShowApiResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this ShowApiResponse.

        更新时间

        :return: The update_time of this ShowApiResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this ShowApiResponse.

        更新时间

        :param update_time: The update_time of this ShowApiResponse.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def manager(self):
        """Gets the manager of this ShowApiResponse.

        API 审核人名称

        :return: The manager of this ShowApiResponse.
        :rtype: str
        """
        return self._manager

    @manager.setter
    def manager(self, manager):
        """Sets the manager of this ShowApiResponse.

        API 审核人名称

        :param manager: The manager of this ShowApiResponse.
        :type manager: str
        """
        self._manager = manager

    @property
    def status(self):
        """Gets the status of this ShowApiResponse.

        API的状态（共享版）

        :return: The status of this ShowApiResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowApiResponse.

        API的状态（共享版）

        :param status: The status of this ShowApiResponse.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        """Gets the type of this ShowApiResponse.

        API 类型

        :return: The type of this ShowApiResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowApiResponse.

        API 类型

        :param type: The type of this ShowApiResponse.
        :type type: str
        """
        self._type = type

    @property
    def debug_status(self):
        """Gets the debug_status of this ShowApiResponse.

        API调试状态（共享版）

        :return: The debug_status of this ShowApiResponse.
        :rtype: str
        """
        return self._debug_status

    @debug_status.setter
    def debug_status(self, debug_status):
        """Sets the debug_status of this ShowApiResponse.

        API调试状态（共享版）

        :param debug_status: The debug_status of this ShowApiResponse.
        :type debug_status: str
        """
        self._debug_status = debug_status

    @property
    def publish_messages(self):
        """Gets the publish_messages of this ShowApiResponse.

        发布信息列表（专享版）

        :return: The publish_messages of this ShowApiResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiPublishDTO`]
        """
        return self._publish_messages

    @publish_messages.setter
    def publish_messages(self, publish_messages):
        """Sets the publish_messages of this ShowApiResponse.

        发布信息列表（专享版）

        :param publish_messages: The publish_messages of this ShowApiResponse.
        :type publish_messages: list[:class:`huaweicloudsdkdataartsstudio.v1.ApiPublishDTO`]
        """
        self._publish_messages = publish_messages

    @property
    def request_paras(self):
        """Gets the request_paras of this ShowApiResponse.

        API请求参数

        :return: The request_paras of this ShowApiResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.RequestPara`]
        """
        return self._request_paras

    @request_paras.setter
    def request_paras(self, request_paras):
        """Sets the request_paras of this ShowApiResponse.

        API请求参数

        :param request_paras: The request_paras of this ShowApiResponse.
        :type request_paras: list[:class:`huaweicloudsdkdataartsstudio.v1.RequestPara`]
        """
        self._request_paras = request_paras

    @property
    def datasource_config(self):
        """Gets the datasource_config of this ShowApiResponse.

        :return: The datasource_config of this ShowApiResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.DatasourceConfig`
        """
        return self._datasource_config

    @datasource_config.setter
    def datasource_config(self, datasource_config):
        """Sets the datasource_config of this ShowApiResponse.

        :param datasource_config: The datasource_config of this ShowApiResponse.
        :type datasource_config: :class:`huaweicloudsdkdataartsstudio.v1.DatasourceConfig`
        """
        self._datasource_config = datasource_config

    @property
    def backend_config(self):
        """Gets the backend_config of this ShowApiResponse.

        :return: The backend_config of this ShowApiResponse.
        :rtype: :class:`huaweicloudsdkdataartsstudio.v1.BackendConfig`
        """
        return self._backend_config

    @backend_config.setter
    def backend_config(self, backend_config):
        """Sets the backend_config of this ShowApiResponse.

        :param backend_config: The backend_config of this ShowApiResponse.
        :type backend_config: :class:`huaweicloudsdkdataartsstudio.v1.BackendConfig`
        """
        self._backend_config = backend_config

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
        if not isinstance(other, ShowApiResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
