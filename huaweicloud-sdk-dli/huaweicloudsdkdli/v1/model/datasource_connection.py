# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatasourceConnection:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_success': 'bool',
        'message': 'str',
        'connection_id': 'str',
        'destination': 'str',
        'state': 'str',
        'process': 'float',
        'name': 'str',
        'connection_url': 'str',
        'cluster_name': 'str',
        'service': 'str',
        'create_time': 'int',
        'queue_list': 'list[str]'
    }

    attribute_map = {
        'is_success': 'is_success',
        'message': 'message',
        'connection_id': 'connection_id',
        'destination': 'destination',
        'state': 'state',
        'process': 'process',
        'name': 'name',
        'connection_url': 'connection_url',
        'cluster_name': 'cluster_name',
        'service': 'service',
        'create_time': 'create_time',
        'queue_list': 'queue_list'
    }

    def __init__(self, is_success=None, message=None, connection_id=None, destination=None, state=None, process=None, name=None, connection_url=None, cluster_name=None, service=None, create_time=None, queue_list=None):
        """DatasourceConnection

        The model defined in huaweicloud sdk

        :param is_success: 执行请求是否成功。“true”表示请求执行成功。
        :type is_success: bool
        :param message: 系统提示信息，执行成功时，信息为空。
        :type message: str
        :param connection_id: 连接ID，用于标识跨源连接的UUID。
        :type connection_id: str
        :param destination: 创建连接时，用户填写的队列的访问地址。
        :type destination: str
        :param state: 连接状态。CREATING：跨源连接正在创建中；ACTIVE：跨源连接创建成功，与目的地址连接正常；FAILED：跨源连接创建失败；DELETED：跨源连接已被删除。
        :type state: str
        :param process: 正在创建的跨源连接进度，显示0.0至1.0代表0%至100%。
        :type process: float
        :param name: 创建连接时，用户自定义的连接名称。
        :type name: str
        :param connection_url: 用于建立跨源关联表时，需要使用到的连接url。
        :type connection_url: str
        :param cluster_name: Serverless Spark队列名称。SQL队列模式下建立的跨源连接，该字段为空。
        :type cluster_name: str
        :param service: 创建连接时，用户指定的对端服务（CloudTable/CloudTable.OpenTSDB/MRS.OpenTSDB/DWS/RDS/CSS）。
        :type service: str
        :param create_time: 创建连接的时间。为UTC的时间戳。
        :type create_time: int
        :param queue_list: 当前跨源已绑定的队列名
        :type queue_list: list[str]
        """
        
        

        self._is_success = None
        self._message = None
        self._connection_id = None
        self._destination = None
        self._state = None
        self._process = None
        self._name = None
        self._connection_url = None
        self._cluster_name = None
        self._service = None
        self._create_time = None
        self._queue_list = None
        self.discriminator = None

        if is_success is not None:
            self.is_success = is_success
        if message is not None:
            self.message = message
        if connection_id is not None:
            self.connection_id = connection_id
        if destination is not None:
            self.destination = destination
        if state is not None:
            self.state = state
        if process is not None:
            self.process = process
        if name is not None:
            self.name = name
        if connection_url is not None:
            self.connection_url = connection_url
        if cluster_name is not None:
            self.cluster_name = cluster_name
        if service is not None:
            self.service = service
        if create_time is not None:
            self.create_time = create_time
        if queue_list is not None:
            self.queue_list = queue_list

    @property
    def is_success(self):
        """Gets the is_success of this DatasourceConnection.

        执行请求是否成功。“true”表示请求执行成功。

        :return: The is_success of this DatasourceConnection.
        :rtype: bool
        """
        return self._is_success

    @is_success.setter
    def is_success(self, is_success):
        """Sets the is_success of this DatasourceConnection.

        执行请求是否成功。“true”表示请求执行成功。

        :param is_success: The is_success of this DatasourceConnection.
        :type is_success: bool
        """
        self._is_success = is_success

    @property
    def message(self):
        """Gets the message of this DatasourceConnection.

        系统提示信息，执行成功时，信息为空。

        :return: The message of this DatasourceConnection.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this DatasourceConnection.

        系统提示信息，执行成功时，信息为空。

        :param message: The message of this DatasourceConnection.
        :type message: str
        """
        self._message = message

    @property
    def connection_id(self):
        """Gets the connection_id of this DatasourceConnection.

        连接ID，用于标识跨源连接的UUID。

        :return: The connection_id of this DatasourceConnection.
        :rtype: str
        """
        return self._connection_id

    @connection_id.setter
    def connection_id(self, connection_id):
        """Sets the connection_id of this DatasourceConnection.

        连接ID，用于标识跨源连接的UUID。

        :param connection_id: The connection_id of this DatasourceConnection.
        :type connection_id: str
        """
        self._connection_id = connection_id

    @property
    def destination(self):
        """Gets the destination of this DatasourceConnection.

        创建连接时，用户填写的队列的访问地址。

        :return: The destination of this DatasourceConnection.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        """Sets the destination of this DatasourceConnection.

        创建连接时，用户填写的队列的访问地址。

        :param destination: The destination of this DatasourceConnection.
        :type destination: str
        """
        self._destination = destination

    @property
    def state(self):
        """Gets the state of this DatasourceConnection.

        连接状态。CREATING：跨源连接正在创建中；ACTIVE：跨源连接创建成功，与目的地址连接正常；FAILED：跨源连接创建失败；DELETED：跨源连接已被删除。

        :return: The state of this DatasourceConnection.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DatasourceConnection.

        连接状态。CREATING：跨源连接正在创建中；ACTIVE：跨源连接创建成功，与目的地址连接正常；FAILED：跨源连接创建失败；DELETED：跨源连接已被删除。

        :param state: The state of this DatasourceConnection.
        :type state: str
        """
        self._state = state

    @property
    def process(self):
        """Gets the process of this DatasourceConnection.

        正在创建的跨源连接进度，显示0.0至1.0代表0%至100%。

        :return: The process of this DatasourceConnection.
        :rtype: float
        """
        return self._process

    @process.setter
    def process(self, process):
        """Sets the process of this DatasourceConnection.

        正在创建的跨源连接进度，显示0.0至1.0代表0%至100%。

        :param process: The process of this DatasourceConnection.
        :type process: float
        """
        self._process = process

    @property
    def name(self):
        """Gets the name of this DatasourceConnection.

        创建连接时，用户自定义的连接名称。

        :return: The name of this DatasourceConnection.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DatasourceConnection.

        创建连接时，用户自定义的连接名称。

        :param name: The name of this DatasourceConnection.
        :type name: str
        """
        self._name = name

    @property
    def connection_url(self):
        """Gets the connection_url of this DatasourceConnection.

        用于建立跨源关联表时，需要使用到的连接url。

        :return: The connection_url of this DatasourceConnection.
        :rtype: str
        """
        return self._connection_url

    @connection_url.setter
    def connection_url(self, connection_url):
        """Sets the connection_url of this DatasourceConnection.

        用于建立跨源关联表时，需要使用到的连接url。

        :param connection_url: The connection_url of this DatasourceConnection.
        :type connection_url: str
        """
        self._connection_url = connection_url

    @property
    def cluster_name(self):
        """Gets the cluster_name of this DatasourceConnection.

        Serverless Spark队列名称。SQL队列模式下建立的跨源连接，该字段为空。

        :return: The cluster_name of this DatasourceConnection.
        :rtype: str
        """
        return self._cluster_name

    @cluster_name.setter
    def cluster_name(self, cluster_name):
        """Sets the cluster_name of this DatasourceConnection.

        Serverless Spark队列名称。SQL队列模式下建立的跨源连接，该字段为空。

        :param cluster_name: The cluster_name of this DatasourceConnection.
        :type cluster_name: str
        """
        self._cluster_name = cluster_name

    @property
    def service(self):
        """Gets the service of this DatasourceConnection.

        创建连接时，用户指定的对端服务（CloudTable/CloudTable.OpenTSDB/MRS.OpenTSDB/DWS/RDS/CSS）。

        :return: The service of this DatasourceConnection.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """Sets the service of this DatasourceConnection.

        创建连接时，用户指定的对端服务（CloudTable/CloudTable.OpenTSDB/MRS.OpenTSDB/DWS/RDS/CSS）。

        :param service: The service of this DatasourceConnection.
        :type service: str
        """
        self._service = service

    @property
    def create_time(self):
        """Gets the create_time of this DatasourceConnection.

        创建连接的时间。为UTC的时间戳。

        :return: The create_time of this DatasourceConnection.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this DatasourceConnection.

        创建连接的时间。为UTC的时间戳。

        :param create_time: The create_time of this DatasourceConnection.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def queue_list(self):
        """Gets the queue_list of this DatasourceConnection.

        当前跨源已绑定的队列名

        :return: The queue_list of this DatasourceConnection.
        :rtype: list[str]
        """
        return self._queue_list

    @queue_list.setter
    def queue_list(self, queue_list):
        """Sets the queue_list of this DatasourceConnection.

        当前跨源已绑定的队列名

        :param queue_list: The queue_list of this DatasourceConnection.
        :type queue_list: list[str]
        """
        self._queue_list = queue_list

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
        if not isinstance(other, DatasourceConnection):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
