# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsTaskBaseInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'created_at': 'str',
        'start_at': 'str',
        'updated_at': 'str',
        'completed_at': 'str',
        'duration_seconds': 'int',
        'created_by': 'UserInfoObj',
        'started_by': 'UserInfoObj'
    }

    attribute_map = {
        'created_at': 'created_at',
        'start_at': 'start_at',
        'updated_at': 'updated_at',
        'completed_at': 'completed_at',
        'duration_seconds': 'duration_seconds',
        'created_by': 'created_by',
        'started_by': 'started_by'
    }

    def __init__(self, created_at=None, start_at=None, updated_at=None, completed_at=None, duration_seconds=None, created_by=None, started_by=None):
        r"""EvaluationOpsTaskBaseInfo

        The model defined in huaweicloud sdk

        :param created_at: **参数解释：** 任务在系统中创建的时间戳。 **取值范围：** 日期时间字符串。 
        :type created_at: str
        :param start_at: **参数解释：** 任务正式开始执行的精确时刻。 **取值范围：** 日期时间字符串。 
        :type start_at: str
        :param updated_at: **参数解释：** 任务状态或元数据最后一次变更的时间。 **取值范围：** 日期时间字符串。 
        :type updated_at: str
        :param completed_at: **参数解释：** 任务执行完毕（无论成败）的时间。 **取值范围：** 日期时间字符串。 
        :type completed_at: str
        :param duration_seconds: **参数解释：** 任务的有效运行总时长（秒）。 **取值范围：** 非负整数。 
        :type duration_seconds: int
        :param created_by: 
        :type created_by: :class:`huaweicloudsdkagentarts.v1.UserInfoObj`
        :param started_by: 
        :type started_by: :class:`huaweicloudsdkagentarts.v1.UserInfoObj`
        """
        
        

        self._created_at = None
        self._start_at = None
        self._updated_at = None
        self._completed_at = None
        self._duration_seconds = None
        self._created_by = None
        self._started_by = None
        self.discriminator = None

        if created_at is not None:
            self.created_at = created_at
        if start_at is not None:
            self.start_at = start_at
        if updated_at is not None:
            self.updated_at = updated_at
        if completed_at is not None:
            self.completed_at = completed_at
        if duration_seconds is not None:
            self.duration_seconds = duration_seconds
        if created_by is not None:
            self.created_by = created_by
        if started_by is not None:
            self.started_by = started_by

    @property
    def created_at(self):
        r"""Gets the created_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务在系统中创建的时间戳。 **取值范围：** 日期时间字符串。 

        :return: The created_at of this EvaluationOpsTaskBaseInfo.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务在系统中创建的时间戳。 **取值范围：** 日期时间字符串。 

        :param created_at: The created_at of this EvaluationOpsTaskBaseInfo.
        :type created_at: str
        """
        self._created_at = created_at

    @property
    def start_at(self):
        r"""Gets the start_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务正式开始执行的精确时刻。 **取值范围：** 日期时间字符串。 

        :return: The start_at of this EvaluationOpsTaskBaseInfo.
        :rtype: str
        """
        return self._start_at

    @start_at.setter
    def start_at(self, start_at):
        r"""Sets the start_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务正式开始执行的精确时刻。 **取值范围：** 日期时间字符串。 

        :param start_at: The start_at of this EvaluationOpsTaskBaseInfo.
        :type start_at: str
        """
        self._start_at = start_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务状态或元数据最后一次变更的时间。 **取值范围：** 日期时间字符串。 

        :return: The updated_at of this EvaluationOpsTaskBaseInfo.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务状态或元数据最后一次变更的时间。 **取值范围：** 日期时间字符串。 

        :param updated_at: The updated_at of this EvaluationOpsTaskBaseInfo.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def completed_at(self):
        r"""Gets the completed_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务执行完毕（无论成败）的时间。 **取值范围：** 日期时间字符串。 

        :return: The completed_at of this EvaluationOpsTaskBaseInfo.
        :rtype: str
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        r"""Sets the completed_at of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务执行完毕（无论成败）的时间。 **取值范围：** 日期时间字符串。 

        :param completed_at: The completed_at of this EvaluationOpsTaskBaseInfo.
        :type completed_at: str
        """
        self._completed_at = completed_at

    @property
    def duration_seconds(self):
        r"""Gets the duration_seconds of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务的有效运行总时长（秒）。 **取值范围：** 非负整数。 

        :return: The duration_seconds of this EvaluationOpsTaskBaseInfo.
        :rtype: int
        """
        return self._duration_seconds

    @duration_seconds.setter
    def duration_seconds(self, duration_seconds):
        r"""Sets the duration_seconds of this EvaluationOpsTaskBaseInfo.

        **参数解释：** 任务的有效运行总时长（秒）。 **取值范围：** 非负整数。 

        :param duration_seconds: The duration_seconds of this EvaluationOpsTaskBaseInfo.
        :type duration_seconds: int
        """
        self._duration_seconds = duration_seconds

    @property
    def created_by(self):
        r"""Gets the created_by of this EvaluationOpsTaskBaseInfo.

        :return: The created_by of this EvaluationOpsTaskBaseInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UserInfoObj`
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        r"""Sets the created_by of this EvaluationOpsTaskBaseInfo.

        :param created_by: The created_by of this EvaluationOpsTaskBaseInfo.
        :type created_by: :class:`huaweicloudsdkagentarts.v1.UserInfoObj`
        """
        self._created_by = created_by

    @property
    def started_by(self):
        r"""Gets the started_by of this EvaluationOpsTaskBaseInfo.

        :return: The started_by of this EvaluationOpsTaskBaseInfo.
        :rtype: :class:`huaweicloudsdkagentarts.v1.UserInfoObj`
        """
        return self._started_by

    @started_by.setter
    def started_by(self, started_by):
        r"""Sets the started_by of this EvaluationOpsTaskBaseInfo.

        :param started_by: The started_by of this EvaluationOpsTaskBaseInfo.
        :type started_by: :class:`huaweicloudsdkagentarts.v1.UserInfoObj`
        """
        self._started_by = started_by

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
        if not isinstance(other, EvaluationOpsTaskBaseInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
