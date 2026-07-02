# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKafkaLogTaskEntity:

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
        'instance_id': 'str',
        'log_group_id': 'str',
        'log_stream_id': 'str',
        'dashboard_id': 'str',
        'status': 'str',
        'log_type': 'str',
        'log_file_name': 'str',
        'created_at': 'int',
        'updated_at': 'int'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'log_group_id': 'log_group_id',
        'log_stream_id': 'log_stream_id',
        'dashboard_id': 'dashboard_id',
        'status': 'status',
        'log_type': 'log_type',
        'log_file_name': 'log_file_name',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, instance_id=None, log_group_id=None, log_stream_id=None, dashboard_id=None, status=None, log_type=None, log_file_name=None, created_at=None, updated_at=None):
        r"""ShowKafkaLogTaskEntity

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 日志记录ID。 **取值范围**： 不涉及。
        :type id: str
        :param instance_id: **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **取值范围**： 不涉及。
        :type instance_id: str
        :param log_group_id: **参数解释**： 日志组ID。 **取值范围**： 不涉及。
        :type log_group_id: str
        :param log_stream_id: **参数解释**： 日志流ID。 **取值范围**： 不涉及。
        :type log_stream_id: str
        :param dashboard_id: **参数解释**： 仪表盘ID。 **取值范围**： 不涉及。
        :type dashboard_id: str
        :param status: **参数解释**： 状态。 **取值范围**： - OPEN：开启。 - CLOSE：关闭。 - CLOSING：关闭中。 - OPENING：开启中。
        :type status: str
        :param log_type: **参数解释**： 状态。 **取值范围**： - REBALANCE：重平衡日志。 - topic_log：Topic日志。
        :type log_type: str
        :param log_file_name: **参数解释**： 日志文件名。 **取值范围**： 不涉及。
        :type log_file_name: str
        :param created_at: **参数解释**： 创建时间。 **取值范围**： 不涉及。
        :type created_at: int
        :param updated_at: **参数解释**： 更新时间。    **取值范围**： 不涉及。
        :type updated_at: int
        """
        
        

        self._id = None
        self._instance_id = None
        self._log_group_id = None
        self._log_stream_id = None
        self._dashboard_id = None
        self._status = None
        self._log_type = None
        self._log_file_name = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if log_group_id is not None:
            self.log_group_id = log_group_id
        if log_stream_id is not None:
            self.log_stream_id = log_stream_id
        if dashboard_id is not None:
            self.dashboard_id = dashboard_id
        if status is not None:
            self.status = status
        if log_type is not None:
            self.log_type = log_type
        if log_file_name is not None:
            self.log_file_name = log_file_name
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        r"""Gets the id of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志记录ID。 **取值范围**： 不涉及。

        :return: The id of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志记录ID。 **取值范围**： 不涉及。

        :param id: The id of this ShowKafkaLogTaskEntity.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **取值范围**： 不涉及。

        :return: The instance_id of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 实例ID。获取方法如下：调用“查询所有实例列表”接口，从响应体中获取实例ID。 **取值范围**： 不涉及。

        :param instance_id: The instance_id of this ShowKafkaLogTaskEntity.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def log_group_id(self):
        r"""Gets the log_group_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志组ID。 **取值范围**： 不涉及。

        :return: The log_group_id of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._log_group_id

    @log_group_id.setter
    def log_group_id(self, log_group_id):
        r"""Sets the log_group_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志组ID。 **取值范围**： 不涉及。

        :param log_group_id: The log_group_id of this ShowKafkaLogTaskEntity.
        :type log_group_id: str
        """
        self._log_group_id = log_group_id

    @property
    def log_stream_id(self):
        r"""Gets the log_stream_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志流ID。 **取值范围**： 不涉及。

        :return: The log_stream_id of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._log_stream_id

    @log_stream_id.setter
    def log_stream_id(self, log_stream_id):
        r"""Sets the log_stream_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志流ID。 **取值范围**： 不涉及。

        :param log_stream_id: The log_stream_id of this ShowKafkaLogTaskEntity.
        :type log_stream_id: str
        """
        self._log_stream_id = log_stream_id

    @property
    def dashboard_id(self):
        r"""Gets the dashboard_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 仪表盘ID。 **取值范围**： 不涉及。

        :return: The dashboard_id of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._dashboard_id

    @dashboard_id.setter
    def dashboard_id(self, dashboard_id):
        r"""Sets the dashboard_id of this ShowKafkaLogTaskEntity.

        **参数解释**： 仪表盘ID。 **取值范围**： 不涉及。

        :param dashboard_id: The dashboard_id of this ShowKafkaLogTaskEntity.
        :type dashboard_id: str
        """
        self._dashboard_id = dashboard_id

    @property
    def status(self):
        r"""Gets the status of this ShowKafkaLogTaskEntity.

        **参数解释**： 状态。 **取值范围**： - OPEN：开启。 - CLOSE：关闭。 - CLOSING：关闭中。 - OPENING：开启中。

        :return: The status of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowKafkaLogTaskEntity.

        **参数解释**： 状态。 **取值范围**： - OPEN：开启。 - CLOSE：关闭。 - CLOSING：关闭中。 - OPENING：开启中。

        :param status: The status of this ShowKafkaLogTaskEntity.
        :type status: str
        """
        self._status = status

    @property
    def log_type(self):
        r"""Gets the log_type of this ShowKafkaLogTaskEntity.

        **参数解释**： 状态。 **取值范围**： - REBALANCE：重平衡日志。 - topic_log：Topic日志。

        :return: The log_type of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        r"""Sets the log_type of this ShowKafkaLogTaskEntity.

        **参数解释**： 状态。 **取值范围**： - REBALANCE：重平衡日志。 - topic_log：Topic日志。

        :param log_type: The log_type of this ShowKafkaLogTaskEntity.
        :type log_type: str
        """
        self._log_type = log_type

    @property
    def log_file_name(self):
        r"""Gets the log_file_name of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志文件名。 **取值范围**： 不涉及。

        :return: The log_file_name of this ShowKafkaLogTaskEntity.
        :rtype: str
        """
        return self._log_file_name

    @log_file_name.setter
    def log_file_name(self, log_file_name):
        r"""Sets the log_file_name of this ShowKafkaLogTaskEntity.

        **参数解释**： 日志文件名。 **取值范围**： 不涉及。

        :param log_file_name: The log_file_name of this ShowKafkaLogTaskEntity.
        :type log_file_name: str
        """
        self._log_file_name = log_file_name

    @property
    def created_at(self):
        r"""Gets the created_at of this ShowKafkaLogTaskEntity.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :return: The created_at of this ShowKafkaLogTaskEntity.
        :rtype: int
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ShowKafkaLogTaskEntity.

        **参数解释**： 创建时间。 **取值范围**： 不涉及。

        :param created_at: The created_at of this ShowKafkaLogTaskEntity.
        :type created_at: int
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ShowKafkaLogTaskEntity.

        **参数解释**： 更新时间。    **取值范围**： 不涉及。

        :return: The updated_at of this ShowKafkaLogTaskEntity.
        :rtype: int
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ShowKafkaLogTaskEntity.

        **参数解释**： 更新时间。    **取值范围**： 不涉及。

        :param updated_at: The updated_at of this ShowKafkaLogTaskEntity.
        :type updated_at: int
        """
        self._updated_at = updated_at

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowKafkaLogTaskEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
