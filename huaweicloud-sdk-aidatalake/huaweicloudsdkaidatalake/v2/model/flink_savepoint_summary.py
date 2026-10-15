# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FlinkSavepointSummary:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'savepoint_id': 'str',
        'job_id': 'str',
        'trigger_type': 'FlinkSavepointTriggerType',
        'status': 'FlinkSavepointStatus',
        'created_time': 'int',
        'location': 'str',
        'description': 'str'
    }

    attribute_map = {
        'savepoint_id': 'savepoint_id',
        'job_id': 'job_id',
        'trigger_type': 'trigger_type',
        'status': 'status',
        'created_time': 'created_time',
        'location': 'location',
        'description': 'description'
    }

    def __init__(self, savepoint_id=None, job_id=None, trigger_type=None, status=None, created_time=None, location=None, description=None):
        r"""FlinkSavepointSummary

        The model defined in huaweicloud sdk

        :param savepoint_id: **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type savepoint_id: str
        :param job_id: **参数解释**：关联的Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type job_id: str
        :param trigger_type: 
        :type trigger_type: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointTriggerType`
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointStatus`
        :param created_time: **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type created_time: int
        :param location: **参数解释**：快照存储路径。 **取值范围**：1~512个字符，需以obs://开头。 
        :type location: str
        :param description: **参数解释**：作业快照描述。 **取值范围**：0~512个字符。 
        :type description: str
        """
        
        

        self._savepoint_id = None
        self._job_id = None
        self._trigger_type = None
        self._status = None
        self._created_time = None
        self._location = None
        self._description = None
        self.discriminator = None

        if savepoint_id is not None:
            self.savepoint_id = savepoint_id
        if job_id is not None:
            self.job_id = job_id
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if status is not None:
            self.status = status
        if created_time is not None:
            self.created_time = created_time
        if location is not None:
            self.location = location
        if description is not None:
            self.description = description

    @property
    def savepoint_id(self):
        r"""Gets the savepoint_id of this FlinkSavepointSummary.

        **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The savepoint_id of this FlinkSavepointSummary.
        :rtype: str
        """
        return self._savepoint_id

    @savepoint_id.setter
    def savepoint_id(self, savepoint_id):
        r"""Sets the savepoint_id of this FlinkSavepointSummary.

        **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param savepoint_id: The savepoint_id of this FlinkSavepointSummary.
        :type savepoint_id: str
        """
        self._savepoint_id = savepoint_id

    @property
    def job_id(self):
        r"""Gets the job_id of this FlinkSavepointSummary.

        **参数解释**：关联的Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The job_id of this FlinkSavepointSummary.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this FlinkSavepointSummary.

        **参数解释**：关联的Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param job_id: The job_id of this FlinkSavepointSummary.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this FlinkSavepointSummary.

        :return: The trigger_type of this FlinkSavepointSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointTriggerType`
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this FlinkSavepointSummary.

        :param trigger_type: The trigger_type of this FlinkSavepointSummary.
        :type trigger_type: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointTriggerType`
        """
        self._trigger_type = trigger_type

    @property
    def status(self):
        r"""Gets the status of this FlinkSavepointSummary.

        :return: The status of this FlinkSavepointSummary.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this FlinkSavepointSummary.

        :param status: The status of this FlinkSavepointSummary.
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointStatus`
        """
        self._status = status

    @property
    def created_time(self):
        r"""Gets the created_time of this FlinkSavepointSummary.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The created_time of this FlinkSavepointSummary.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this FlinkSavepointSummary.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param created_time: The created_time of this FlinkSavepointSummary.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def location(self):
        r"""Gets the location of this FlinkSavepointSummary.

        **参数解释**：快照存储路径。 **取值范围**：1~512个字符，需以obs://开头。 

        :return: The location of this FlinkSavepointSummary.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this FlinkSavepointSummary.

        **参数解释**：快照存储路径。 **取值范围**：1~512个字符，需以obs://开头。 

        :param location: The location of this FlinkSavepointSummary.
        :type location: str
        """
        self._location = location

    @property
    def description(self):
        r"""Gets the description of this FlinkSavepointSummary.

        **参数解释**：作业快照描述。 **取值范围**：0~512个字符。 

        :return: The description of this FlinkSavepointSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this FlinkSavepointSummary.

        **参数解释**：作业快照描述。 **取值范围**：0~512个字符。 

        :param description: The description of this FlinkSavepointSummary.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, FlinkSavepointSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
