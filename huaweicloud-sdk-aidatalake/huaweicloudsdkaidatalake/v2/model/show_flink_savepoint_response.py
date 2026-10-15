# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowFlinkSavepointResponse(SdkResponse):

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
        'format': 'FlinkSavepointFormat',
        'status': 'FlinkSavepointStatus',
        'drain_mode_enabled': 'bool',
        'location': 'str',
        'created_time': 'int',
        'completed_time': 'int',
        'create_user': 'FlinkCreateUser',
        'description': 'str'
    }

    attribute_map = {
        'savepoint_id': 'savepoint_id',
        'job_id': 'job_id',
        'trigger_type': 'trigger_type',
        'format': 'format',
        'status': 'status',
        'drain_mode_enabled': 'drain_mode_enabled',
        'location': 'location',
        'created_time': 'created_time',
        'completed_time': 'completed_time',
        'create_user': 'create_user',
        'description': 'description'
    }

    def __init__(self, savepoint_id=None, job_id=None, trigger_type=None, format=None, status=None, drain_mode_enabled=None, location=None, created_time=None, completed_time=None, create_user=None, description=None):
        r"""ShowFlinkSavepointResponse

        The model defined in huaweicloud sdk

        :param savepoint_id: **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type savepoint_id: str
        :param job_id: **参数解释**：关联的Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 
        :type job_id: str
        :param trigger_type: 
        :type trigger_type: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointTriggerType`
        :param format: 
        :type format: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointFormat`
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointStatus`
        :param drain_mode_enabled: **参数解释**：是否启用了Drain模式。启用后，触发Savepoint前将先发送Watermark到所有算子以触发窗口计算完成，然后再保存状态快照。 **取值范围**：   - true：已启用Drain模式。   - false：未启用Drain模式。 
        :type drain_mode_enabled: bool
        :param location: **参数解释**：Savepoint存储路径。 **取值范围**：1~512个字符，需以obs://开头。 
        :type location: str
        :param created_time: **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type created_time: int
        :param completed_time: **参数解释**：完成时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 
        :type completed_time: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        :param description: **参数解释**：作业快照描述。 **取值范围**：0~512个字符。 
        :type description: str
        """
        
        super().__init__()

        self._savepoint_id = None
        self._job_id = None
        self._trigger_type = None
        self._format = None
        self._status = None
        self._drain_mode_enabled = None
        self._location = None
        self._created_time = None
        self._completed_time = None
        self._create_user = None
        self._description = None
        self.discriminator = None

        if savepoint_id is not None:
            self.savepoint_id = savepoint_id
        if job_id is not None:
            self.job_id = job_id
        if trigger_type is not None:
            self.trigger_type = trigger_type
        if format is not None:
            self.format = format
        if status is not None:
            self.status = status
        if drain_mode_enabled is not None:
            self.drain_mode_enabled = drain_mode_enabled
        if location is not None:
            self.location = location
        if created_time is not None:
            self.created_time = created_time
        if completed_time is not None:
            self.completed_time = completed_time
        if create_user is not None:
            self.create_user = create_user
        if description is not None:
            self.description = description

    @property
    def savepoint_id(self):
        r"""Gets the savepoint_id of this ShowFlinkSavepointResponse.

        **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The savepoint_id of this ShowFlinkSavepointResponse.
        :rtype: str
        """
        return self._savepoint_id

    @savepoint_id.setter
    def savepoint_id(self, savepoint_id):
        r"""Sets the savepoint_id of this ShowFlinkSavepointResponse.

        **参数解释**：Savepoint唯一标识。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param savepoint_id: The savepoint_id of this ShowFlinkSavepointResponse.
        :type savepoint_id: str
        """
        self._savepoint_id = savepoint_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowFlinkSavepointResponse.

        **参数解释**：关联的Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :return: The job_id of this ShowFlinkSavepointResponse.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowFlinkSavepointResponse.

        **参数解释**：关联的Flink作业ID。 **取值范围**：UUIDv7格式，固定36位，由英文小写字母、数字及中划线组成。 

        :param job_id: The job_id of this ShowFlinkSavepointResponse.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def trigger_type(self):
        r"""Gets the trigger_type of this ShowFlinkSavepointResponse.

        :return: The trigger_type of this ShowFlinkSavepointResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointTriggerType`
        """
        return self._trigger_type

    @trigger_type.setter
    def trigger_type(self, trigger_type):
        r"""Sets the trigger_type of this ShowFlinkSavepointResponse.

        :param trigger_type: The trigger_type of this ShowFlinkSavepointResponse.
        :type trigger_type: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointTriggerType`
        """
        self._trigger_type = trigger_type

    @property
    def format(self):
        r"""Gets the format of this ShowFlinkSavepointResponse.

        :return: The format of this ShowFlinkSavepointResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointFormat`
        """
        return self._format

    @format.setter
    def format(self, format):
        r"""Sets the format of this ShowFlinkSavepointResponse.

        :param format: The format of this ShowFlinkSavepointResponse.
        :type format: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointFormat`
        """
        self._format = format

    @property
    def status(self):
        r"""Gets the status of this ShowFlinkSavepointResponse.

        :return: The status of this ShowFlinkSavepointResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowFlinkSavepointResponse.

        :param status: The status of this ShowFlinkSavepointResponse.
        :type status: :class:`huaweicloudsdkaidatalake.v2.FlinkSavepointStatus`
        """
        self._status = status

    @property
    def drain_mode_enabled(self):
        r"""Gets the drain_mode_enabled of this ShowFlinkSavepointResponse.

        **参数解释**：是否启用了Drain模式。启用后，触发Savepoint前将先发送Watermark到所有算子以触发窗口计算完成，然后再保存状态快照。 **取值范围**：   - true：已启用Drain模式。   - false：未启用Drain模式。 

        :return: The drain_mode_enabled of this ShowFlinkSavepointResponse.
        :rtype: bool
        """
        return self._drain_mode_enabled

    @drain_mode_enabled.setter
    def drain_mode_enabled(self, drain_mode_enabled):
        r"""Sets the drain_mode_enabled of this ShowFlinkSavepointResponse.

        **参数解释**：是否启用了Drain模式。启用后，触发Savepoint前将先发送Watermark到所有算子以触发窗口计算完成，然后再保存状态快照。 **取值范围**：   - true：已启用Drain模式。   - false：未启用Drain模式。 

        :param drain_mode_enabled: The drain_mode_enabled of this ShowFlinkSavepointResponse.
        :type drain_mode_enabled: bool
        """
        self._drain_mode_enabled = drain_mode_enabled

    @property
    def location(self):
        r"""Gets the location of this ShowFlinkSavepointResponse.

        **参数解释**：Savepoint存储路径。 **取值范围**：1~512个字符，需以obs://开头。 

        :return: The location of this ShowFlinkSavepointResponse.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this ShowFlinkSavepointResponse.

        **参数解释**：Savepoint存储路径。 **取值范围**：1~512个字符，需以obs://开头。 

        :param location: The location of this ShowFlinkSavepointResponse.
        :type location: str
        """
        self._location = location

    @property
    def created_time(self):
        r"""Gets the created_time of this ShowFlinkSavepointResponse.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The created_time of this ShowFlinkSavepointResponse.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this ShowFlinkSavepointResponse.

        **参数解释**：创建时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param created_time: The created_time of this ShowFlinkSavepointResponse.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def completed_time(self):
        r"""Gets the completed_time of this ShowFlinkSavepointResponse.

        **参数解释**：完成时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :return: The completed_time of this ShowFlinkSavepointResponse.
        :rtype: int
        """
        return self._completed_time

    @completed_time.setter
    def completed_time(self, completed_time):
        r"""Sets the completed_time of this ShowFlinkSavepointResponse.

        **参数解释**：完成时间戳。 **取值范围**：0~4102416000000，13位毫秒时间戳。 

        :param completed_time: The completed_time of this ShowFlinkSavepointResponse.
        :type completed_time: int
        """
        self._completed_time = completed_time

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowFlinkSavepointResponse.

        :return: The create_user of this ShowFlinkSavepointResponse.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowFlinkSavepointResponse.

        :param create_user: The create_user of this ShowFlinkSavepointResponse.
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.FlinkCreateUser`
        """
        self._create_user = create_user

    @property
    def description(self):
        r"""Gets the description of this ShowFlinkSavepointResponse.

        **参数解释**：作业快照描述。 **取值范围**：0~512个字符。 

        :return: The description of this ShowFlinkSavepointResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowFlinkSavepointResponse.

        **参数解释**：作业快照描述。 **取值范围**：0~512个字符。 

        :param description: The description of this ShowFlinkSavepointResponse.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        import warnings
        warnings.warn("ShowFlinkSavepointResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowFlinkSavepointResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
