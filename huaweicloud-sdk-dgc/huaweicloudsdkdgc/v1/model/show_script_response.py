# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowScriptResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'type': 'str',
        'directory': 'str',
        'content': 'str',
        'connection_name': 'str',
        'database': 'str',
        'queue_name': 'str',
        'configuration': 'str',
        'description': 'str',
        'target_status': 'str',
        'approvers': 'list[JobApprover]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'directory': 'directory',
        'content': 'content',
        'connection_name': 'connectionName',
        'database': 'database',
        'queue_name': 'queueName',
        'configuration': 'configuration',
        'description': 'description',
        'target_status': 'targetStatus',
        'approvers': 'approvers'
    }

    def __init__(self, name=None, type=None, directory=None, content=None, connection_name=None, database=None, queue_name=None, configuration=None, description=None, target_status=None, approvers=None):
        """ShowScriptResponse

        The model defined in huaweicloud sdk

        :param name: 
        :type name: str
        :param type: 脚本类型
        :type type: str
        :param directory: 脚本关联的目录
        :type directory: str
        :param content: 脚本内容
        :type content: str
        :param connection_name: 脚本关联的连接名称
        :type connection_name: str
        :param database: 脚本执行所在的数据库
        :type database: str
        :param queue_name: 脚本关联的DLI队列名称
        :type queue_name: str
        :param configuration: 脚本的配置项参数
        :type configuration: str
        :param description: 脚本描述，长度不能超过255个字符
        :type description: str
        :param target_status: 在开启审批开关后，需要填写该字段。表示创建脚本的目标状态，有三种状态：SAVED、SUBMITTED和PRODUCTION，分别表示脚本创建后是保存态，提交态，生产态。
        :type target_status: str
        :param approvers: 在开启审批开关后，需要填写该字段，表示脚本审批人
        :type approvers: list[:class:`huaweicloudsdkdgc.v1.JobApprover`]
        """
        
        super(ShowScriptResponse, self).__init__()

        self._name = None
        self._type = None
        self._directory = None
        self._content = None
        self._connection_name = None
        self._database = None
        self._queue_name = None
        self._configuration = None
        self._description = None
        self._target_status = None
        self._approvers = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if directory is not None:
            self.directory = directory
        if content is not None:
            self.content = content
        if connection_name is not None:
            self.connection_name = connection_name
        if database is not None:
            self.database = database
        if queue_name is not None:
            self.queue_name = queue_name
        if configuration is not None:
            self.configuration = configuration
        if description is not None:
            self.description = description
        if target_status is not None:
            self.target_status = target_status
        if approvers is not None:
            self.approvers = approvers

    @property
    def name(self):
        """Gets the name of this ShowScriptResponse.

        :return: The name of this ShowScriptResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowScriptResponse.

        :param name: The name of this ShowScriptResponse.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this ShowScriptResponse.

        脚本类型

        :return: The type of this ShowScriptResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowScriptResponse.

        脚本类型

        :param type: The type of this ShowScriptResponse.
        :type type: str
        """
        self._type = type

    @property
    def directory(self):
        """Gets the directory of this ShowScriptResponse.

        脚本关联的目录

        :return: The directory of this ShowScriptResponse.
        :rtype: str
        """
        return self._directory

    @directory.setter
    def directory(self, directory):
        """Sets the directory of this ShowScriptResponse.

        脚本关联的目录

        :param directory: The directory of this ShowScriptResponse.
        :type directory: str
        """
        self._directory = directory

    @property
    def content(self):
        """Gets the content of this ShowScriptResponse.

        脚本内容

        :return: The content of this ShowScriptResponse.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this ShowScriptResponse.

        脚本内容

        :param content: The content of this ShowScriptResponse.
        :type content: str
        """
        self._content = content

    @property
    def connection_name(self):
        """Gets the connection_name of this ShowScriptResponse.

        脚本关联的连接名称

        :return: The connection_name of this ShowScriptResponse.
        :rtype: str
        """
        return self._connection_name

    @connection_name.setter
    def connection_name(self, connection_name):
        """Sets the connection_name of this ShowScriptResponse.

        脚本关联的连接名称

        :param connection_name: The connection_name of this ShowScriptResponse.
        :type connection_name: str
        """
        self._connection_name = connection_name

    @property
    def database(self):
        """Gets the database of this ShowScriptResponse.

        脚本执行所在的数据库

        :return: The database of this ShowScriptResponse.
        :rtype: str
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this ShowScriptResponse.

        脚本执行所在的数据库

        :param database: The database of this ShowScriptResponse.
        :type database: str
        """
        self._database = database

    @property
    def queue_name(self):
        """Gets the queue_name of this ShowScriptResponse.

        脚本关联的DLI队列名称

        :return: The queue_name of this ShowScriptResponse.
        :rtype: str
        """
        return self._queue_name

    @queue_name.setter
    def queue_name(self, queue_name):
        """Sets the queue_name of this ShowScriptResponse.

        脚本关联的DLI队列名称

        :param queue_name: The queue_name of this ShowScriptResponse.
        :type queue_name: str
        """
        self._queue_name = queue_name

    @property
    def configuration(self):
        """Gets the configuration of this ShowScriptResponse.

        脚本的配置项参数

        :return: The configuration of this ShowScriptResponse.
        :rtype: str
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ShowScriptResponse.

        脚本的配置项参数

        :param configuration: The configuration of this ShowScriptResponse.
        :type configuration: str
        """
        self._configuration = configuration

    @property
    def description(self):
        """Gets the description of this ShowScriptResponse.

        脚本描述，长度不能超过255个字符

        :return: The description of this ShowScriptResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ShowScriptResponse.

        脚本描述，长度不能超过255个字符

        :param description: The description of this ShowScriptResponse.
        :type description: str
        """
        self._description = description

    @property
    def target_status(self):
        """Gets the target_status of this ShowScriptResponse.

        在开启审批开关后，需要填写该字段。表示创建脚本的目标状态，有三种状态：SAVED、SUBMITTED和PRODUCTION，分别表示脚本创建后是保存态，提交态，生产态。

        :return: The target_status of this ShowScriptResponse.
        :rtype: str
        """
        return self._target_status

    @target_status.setter
    def target_status(self, target_status):
        """Sets the target_status of this ShowScriptResponse.

        在开启审批开关后，需要填写该字段。表示创建脚本的目标状态，有三种状态：SAVED、SUBMITTED和PRODUCTION，分别表示脚本创建后是保存态，提交态，生产态。

        :param target_status: The target_status of this ShowScriptResponse.
        :type target_status: str
        """
        self._target_status = target_status

    @property
    def approvers(self):
        """Gets the approvers of this ShowScriptResponse.

        在开启审批开关后，需要填写该字段，表示脚本审批人

        :return: The approvers of this ShowScriptResponse.
        :rtype: list[:class:`huaweicloudsdkdgc.v1.JobApprover`]
        """
        return self._approvers

    @approvers.setter
    def approvers(self, approvers):
        """Sets the approvers of this ShowScriptResponse.

        在开启审批开关后，需要填写该字段，表示脚本审批人

        :param approvers: The approvers of this ShowScriptResponse.
        :type approvers: list[:class:`huaweicloudsdkdgc.v1.JobApprover`]
        """
        self._approvers = approvers

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
        if not isinstance(other, ShowScriptResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
