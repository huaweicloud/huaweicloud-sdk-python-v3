# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlowLog:

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
        'description': 'str',
        'project_id': 'str',
        'resource_type': 'str',
        'resource_id': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'log_store_type': 'str',
        'log_aggregation_interval': 'int',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'state': 'str',
        'enabled': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'project_id': 'project_id',
        'resource_type': 'resource_type',
        'resource_id': 'resource_id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'log_store_type': 'log_store_type',
        'log_aggregation_interval': 'log_aggregation_interval',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'state': 'state',
        'enabled': 'enabled'
    }

    def __init__(self, id=None, name=None, description=None, project_id=None, resource_type=None, resource_id=None, log_group_id=None, log_stream_id=None, log_store_type=None, log_aggregation_interval=None, created_at=None, updated_at=None, state=None, enabled=None):
        """FlowLog

        The model defined in huaweicloud sdk

        :param id: 流日志ID
        :type id: str
        :param name: 流日志名称
        :type name: str
        :param description: 流日志描述
        :type description: str
        :param project_id: 流日志任务创建者项目ID
        :type project_id: str
        :param resource_type: 采集的资源类型:attachment
        :type resource_type: str
        :param resource_id: 采集的资源ID
        :type resource_id: str
        :param log_group_id: 日志组ID
        :type log_group_id: str
        :param log_stream_id: 日志流ID
        :type log_stream_id: str
        :param log_store_type: 流日志存储类型
        :type log_store_type: str
        :param log_aggregation_interval: 日志聚合时间，单位s，取值范围：60-600
        :type log_aggregation_interval: int
        :param created_at: 创建时间
        :type created_at: datetime
        :param updated_at: 更新时间
        :type updated_at: datetime
        :param state: 日志资源状态:pending|available|modifying|deleting|deleted|failed
        :type state: str
        :param enabled: 日志开关:true|false
        :type enabled: bool
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._project_id = None
        self._resource_type = None
        self._resource_id = None
        self._log_group_id = None
        self._log_stream_id = None
        self._log_store_type = None
        self._log_aggregation_interval = None
        self._created_at = None
        self._updated_at = None
        self._state = None
        self._enabled = None
        self.discriminator = None

        self.id = id
        self.name = name
        if description is not None:
            self.description = description
        self.project_id = project_id
        self.resource_type = resource_type
        self.resource_id = resource_id
        self.log_group_id = log_group_id
        self.log_stream_id = log_stream_id
        self.log_store_type = log_store_type
        if log_aggregation_interval is not None:
            self.log_aggregation_interval = log_aggregation_interval
        self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        self.state = state
        self.enabled = enabled

    @property
    def id(self):
        """Gets the id of this FlowLog.

        流日志ID

        :return: The id of this FlowLog.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FlowLog.

        流日志ID

        :param id: The id of this FlowLog.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this FlowLog.

        流日志名称

        :return: The name of this FlowLog.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FlowLog.

        流日志名称

        :param name: The name of this FlowLog.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this FlowLog.

        流日志描述

        :return: The description of this FlowLog.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FlowLog.

        流日志描述

        :param description: The description of this FlowLog.
        :type description: str
        """
        self._description = description

    @property
    def project_id(self):
        """Gets the project_id of this FlowLog.

        流日志任务创建者项目ID

        :return: The project_id of this FlowLog.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this FlowLog.

        流日志任务创建者项目ID

        :param project_id: The project_id of this FlowLog.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def resource_type(self):
        """Gets the resource_type of this FlowLog.

        采集的资源类型:attachment

        :return: The resource_type of this FlowLog.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this FlowLog.

        采集的资源类型:attachment

        :param resource_type: The resource_type of this FlowLog.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_id(self):
        """Gets the resource_id of this FlowLog.

        采集的资源ID

        :return: The resource_id of this FlowLog.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this FlowLog.

        采集的资源ID

        :param resource_id: The resource_id of this FlowLog.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def log_group_id(self):
        """Gets the log_group_id of this FlowLog.

        日志组ID

        :return: The log_group_id of this FlowLog.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        """Sets the log_group_id of this FlowLog.

        日志组ID

        :param log_group_id: The log_group_id of this FlowLog.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        """Gets the log_stream_id of this FlowLog.

        日志流ID

        :return: The log_stream_id of this FlowLog.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        """Sets the log_stream_id of this FlowLog.

        日志流ID

        :param log_stream_id: The log_stream_id of this FlowLog.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def log_store_type(self):
        """Gets the log_store_type of this FlowLog.

        流日志存储类型

        :return: The log_store_type of this FlowLog.
        :rtype: str
        """
        return self._log_store_type

    @log_store_type.setter
    def log_store_type(self, log_store_type):
        """Sets the log_store_type of this FlowLog.

        流日志存储类型

        :param log_store_type: The log_store_type of this FlowLog.
        :type log_store_type: str
        """
        self._log_store_type = log_store_type

    @property
    def log_aggregation_interval(self):
        """Gets the log_aggregation_interval of this FlowLog.

        日志聚合时间，单位s，取值范围：60-600

        :return: The log_aggregation_interval of this FlowLog.
        :rtype: int
        """
        return self._log_aggregation_interval

    @log_aggregation_interval.setter
    def log_aggregation_interval(self, log_aggregation_interval):
        """Sets the log_aggregation_interval of this FlowLog.

        日志聚合时间，单位s，取值范围：60-600

        :param log_aggregation_interval: The log_aggregation_interval of this FlowLog.
        :type log_aggregation_interval: int
        """
        self._log_aggregation_interval = log_aggregation_interval

    @property
    def created_at(self):
        """Gets the created_at of this FlowLog.

        创建时间

        :return: The created_at of this FlowLog.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this FlowLog.

        创建时间

        :param created_at: The created_at of this FlowLog.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this FlowLog.

        更新时间

        :return: The updated_at of this FlowLog.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this FlowLog.

        更新时间

        :param updated_at: The updated_at of this FlowLog.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def state(self):
        """Gets the state of this FlowLog.

        日志资源状态:pending|available|modifying|deleting|deleted|failed

        :return: The state of this FlowLog.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this FlowLog.

        日志资源状态:pending|available|modifying|deleting|deleted|failed

        :param state: The state of this FlowLog.
        :type state: str
        """
        self._state = state

    @property
    def enabled(self):
        """Gets the enabled of this FlowLog.

        日志开关:true|false

        :return: The enabled of this FlowLog.
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this FlowLog.

        日志开关:true|false

        :param enabled: The enabled of this FlowLog.
        :type enabled: bool
        """
        self._enabled = enabled

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
        if not isinstance(other, FlowLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
