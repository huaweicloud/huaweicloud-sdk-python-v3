# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDataframeJobResp:

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
        'status': 'str',
        'entrypoint': 'str',
        'duration': 'int',
        'create_user': 'User',
        'create_time': 'datetime',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'execution_result': 'ExecutionResult'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'description': 'description',
        'status': 'status',
        'entrypoint': 'entrypoint',
        'duration': 'duration',
        'create_user': 'create_user',
        'create_time': 'create_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'execution_result': 'execution_result'
    }

    def __init__(self, id=None, name=None, description=None, status=None, entrypoint=None, duration=None, create_user=None, create_time=None, start_time=None, end_time=None, execution_result=None):
        r"""ShowDataframeJobResp

        The model defined in huaweicloud sdk

        :param id: **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type id: str
        :param name: **参数解释**：作业名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type name: str
        :param description: **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：长度为0-1024的任意字符组合，不包含“!”、“&lt;”、“&gt;”、“&#x3D;”、“&amp;”、“\&quot;”、“&#39;”。 **默认取值**：不涉及。 
        :type description: str
        :param status: **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。
        :type status: str
        :param entrypoint: **参数解释**：作业启动命令。 **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。
        :type entrypoint: str
        :param duration: **参数解释**：运行时长，单位：秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type duration: int
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.User`
        :param create_time: **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd&#39;T&#39;HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 
        :type create_time: datetime
        :param start_time: **参数解释**：作业开始执行的时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type start_time: datetime
        :param end_time: **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type end_time: datetime
        :param execution_result: 
        :type execution_result: :class:`huaweicloudsdkaidatalake.v2.ExecutionResult`
        """
        
        

        self._id = None
        self._name = None
        self._description = None
        self._status = None
        self._entrypoint = None
        self._duration = None
        self._create_user = None
        self._create_time = None
        self._start_time = None
        self._end_time = None
        self._execution_result = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if status is not None:
            self.status = status
        if entrypoint is not None:
            self.entrypoint = entrypoint
        if duration is not None:
            self.duration = duration
        if create_user is not None:
            self.create_user = create_user
        if create_time is not None:
            self.create_time = create_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if execution_result is not None:
            self.execution_result = execution_result

    @property
    def id(self):
        r"""Gets the id of this ShowDataframeJobResp.

        **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The id of this ShowDataframeJobResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ShowDataframeJobResp.

        **参数解释**：作业ID。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param id: The id of this ShowDataframeJobResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ShowDataframeJobResp.

        **参数解释**：作业名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The name of this ShowDataframeJobResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowDataframeJobResp.

        **参数解释**：作业名称。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param name: The name of this ShowDataframeJobResp.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowDataframeJobResp.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：长度为0-1024的任意字符组合，不包含“!”、“<”、“>”、“=”、“&”、“\"”、“'”。 **默认取值**：不涉及。 

        :return: The description of this ShowDataframeJobResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowDataframeJobResp.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：长度为0-1024的任意字符组合，不包含“!”、“<”、“>”、“=”、“&”、“\"”、“'”。 **默认取值**：不涉及。 

        :param description: The description of this ShowDataframeJobResp.
        :type description: str
        """
        self._description = description

    @property
    def status(self):
        r"""Gets the status of this ShowDataframeJobResp.

        **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :return: The status of this ShowDataframeJobResp.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowDataframeJobResp.

        **参数解释**：作业状态。 **约束限制**：不涉及。 **取值范围**：长度为1~128的任意字符组合。 **默认取值**：不涉及。

        :param status: The status of this ShowDataframeJobResp.
        :type status: str
        """
        self._status = status

    @property
    def entrypoint(self):
        r"""Gets the entrypoint of this ShowDataframeJobResp.

        **参数解释**：作业启动命令。 **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :return: The entrypoint of this ShowDataframeJobResp.
        :rtype: str
        """
        return self._entrypoint

    @entrypoint.setter
    def entrypoint(self, entrypoint):
        r"""Sets the entrypoint of this ShowDataframeJobResp.

        **参数解释**：作业启动命令。 **约束限制**：不涉及。 **取值范围**：长度为1~1024的任意字符组合。 **默认取值**：不涉及。

        :param entrypoint: The entrypoint of this ShowDataframeJobResp.
        :type entrypoint: str
        """
        self._entrypoint = entrypoint

    @property
    def duration(self):
        r"""Gets the duration of this ShowDataframeJobResp.

        **参数解释**：运行时长，单位：秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The duration of this ShowDataframeJobResp.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this ShowDataframeJobResp.

        **参数解释**：运行时长，单位：秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param duration: The duration of this ShowDataframeJobResp.
        :type duration: int
        """
        self._duration = duration

    @property
    def create_user(self):
        r"""Gets the create_user of this ShowDataframeJobResp.

        :return: The create_user of this ShowDataframeJobResp.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this ShowDataframeJobResp.

        :param create_user: The create_user of this ShowDataframeJobResp.
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        self._create_user = create_user

    @property
    def create_time(self):
        r"""Gets the create_time of this ShowDataframeJobResp.

        **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :return: The create_time of this ShowDataframeJobResp.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this ShowDataframeJobResp.

        **参数解释**：资源创建时间，使用UTC时间，ISO 8601格式，yyyy-MM-dd'T'HH:mm:ss.SSSXXX，例如：2025-01-10T03:37:12.000+00:00。 **取值范围**：不涉及。 

        :param create_time: The create_time of this ShowDataframeJobResp.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowDataframeJobResp.

        **参数解释**：作业开始执行的时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The start_time of this ShowDataframeJobResp.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowDataframeJobResp.

        **参数解释**：作业开始执行的时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param start_time: The start_time of this ShowDataframeJobResp.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowDataframeJobResp.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The end_time of this ShowDataframeJobResp.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowDataframeJobResp.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param end_time: The end_time of this ShowDataframeJobResp.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def execution_result(self):
        r"""Gets the execution_result of this ShowDataframeJobResp.

        :return: The execution_result of this ShowDataframeJobResp.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ExecutionResult`
        """
        return self._execution_result

    @execution_result.setter
    def execution_result(self, execution_result):
        r"""Sets the execution_result of this ShowDataframeJobResp.

        :param execution_result: The execution_result of this ShowDataframeJobResp.
        :type execution_result: :class:`huaweicloudsdkaidatalake.v2.ExecutionResult`
        """
        self._execution_result = execution_result

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
        if not isinstance(other, ShowDataframeJobResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
