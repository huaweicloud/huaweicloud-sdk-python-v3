# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RayJobInfo:

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
        'endpoint_name': 'str',
        'config': 'RayJobConfig',
        'description': 'str',
        'id': 'str',
        'duration': 'int',
        'submission_id': 'str',
        'endpoint_type': 'str',
        'endpoint_id': 'str',
        'federation_id': 'str',
        'federation_name': 'str',
        'create_time': 'datetime',
        'update_time': 'datetime',
        'start_time': 'datetime',
        'end_time': 'datetime',
        'status': 'StatusEnum',
        'create_user': 'User',
        'error': 'ErrorMessage',
        'history_server_enabled': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'endpoint_name': 'endpoint_name',
        'config': 'config',
        'description': 'description',
        'id': 'id',
        'duration': 'duration',
        'submission_id': 'submission_id',
        'endpoint_type': 'endpoint_type',
        'endpoint_id': 'endpoint_id',
        'federation_id': 'federation_id',
        'federation_name': 'federation_name',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'status': 'status',
        'create_user': 'create_user',
        'error': 'error',
        'history_server_enabled': 'history_server_enabled'
    }

    def __init__(self, name=None, endpoint_name=None, config=None, description=None, id=None, duration=None, submission_id=None, endpoint_type=None, endpoint_id=None, federation_id=None, federation_name=None, create_time=None, update_time=None, start_time=None, end_time=None, status=None, create_user=None, error=None, history_server_enabled=None):
        r"""RayJobInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释**：Job名称。 **约束限制**：不涉及。 **取值范围**：长度为1~47的英文字母、数字、中划线的组合。 **默认取值**：不涉及。 
        :type name: str
        :param endpoint_name: **参数解释**：端点名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。包含小写字母、数字、中划线的组合。字母开头、字母或数字结尾。 **默认取值**：不涉及。
        :type endpoint_name: str
        :param config: 
        :type config: :class:`huaweicloudsdkaidatalake.v2.RayJobConfig`
        :param description: **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：0~1024。 **默认取值**：不涉及。 
        :type description: str
        :param id: **参数解释**：作业ID。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 
        :type id: str
        :param duration: **参数解释**：运行时长，单位：秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type duration: int
        :param submission_id: **参数解释**：Ray Job的唯一ID标识。 **约束限制**：不涉及。 **取值范围**：长度为0~64个字符。 **默认取值**：不涉及。
        :type submission_id: str
        :param endpoint_type: **参数解释**：作业对应的端点类型。 **约束限制**：不涉及。 **取值范围**：   - RAY_JOB: RayJob类型的端点作业；   - RAY_CLUSTER: RayCluster类型的端点作业；   - RAY_FEDERATION: Ray联邦端点作业。 **默认取值**：不涉及。 
        :type endpoint_type: str
        :param endpoint_id: **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。
        :type endpoint_id: str
        :param federation_id: **参数解释**：联邦ID。 **约束限制**：如果作业未提交到联邦端点，该字段为空字符串。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 
        :type federation_id: str
        :param federation_name: **参数解释**：联邦名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。 **默认取值**：不涉及。
        :type federation_name: str
        :param create_time: **参数解释**：创建时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type create_time: datetime
        :param update_time: **参数解释**：更新时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type update_time: datetime
        :param start_time: **参数解释**：作业开始执行的时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type start_time: datetime
        :param end_time: **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 
        :type end_time: datetime
        :param status: 
        :type status: :class:`huaweicloudsdkaidatalake.v2.StatusEnum`
        :param create_user: 
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.User`
        :param error: 
        :type error: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        :param history_server_enabled: **参数解释**：指示该作业是否启用了历史服务器（History Server）功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用History Server。   - false：禁用History Server。 **默认取值**：false。
        :type history_server_enabled: bool
        """
        
        

        self._name = None
        self._endpoint_name = None
        self._config = None
        self._description = None
        self._id = None
        self._duration = None
        self._submission_id = None
        self._endpoint_type = None
        self._endpoint_id = None
        self._federation_id = None
        self._federation_name = None
        self._create_time = None
        self._update_time = None
        self._start_time = None
        self._end_time = None
        self._status = None
        self._create_user = None
        self._error = None
        self._history_server_enabled = None
        self.discriminator = None

        self.name = name
        self.endpoint_name = endpoint_name
        self.config = config
        if description is not None:
            self.description = description
        if id is not None:
            self.id = id
        if duration is not None:
            self.duration = duration
        if submission_id is not None:
            self.submission_id = submission_id
        if endpoint_type is not None:
            self.endpoint_type = endpoint_type
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if federation_id is not None:
            self.federation_id = federation_id
        if federation_name is not None:
            self.federation_name = federation_name
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if status is not None:
            self.status = status
        if create_user is not None:
            self.create_user = create_user
        if error is not None:
            self.error = error
        if history_server_enabled is not None:
            self.history_server_enabled = history_server_enabled

    @property
    def name(self):
        r"""Gets the name of this RayJobInfo.

        **参数解释**：Job名称。 **约束限制**：不涉及。 **取值范围**：长度为1~47的英文字母、数字、中划线的组合。 **默认取值**：不涉及。 

        :return: The name of this RayJobInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RayJobInfo.

        **参数解释**：Job名称。 **约束限制**：不涉及。 **取值范围**：长度为1~47的英文字母、数字、中划线的组合。 **默认取值**：不涉及。 

        :param name: The name of this RayJobInfo.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_name(self):
        r"""Gets the endpoint_name of this RayJobInfo.

        **参数解释**：端点名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。包含小写字母、数字、中划线的组合。字母开头、字母或数字结尾。 **默认取值**：不涉及。

        :return: The endpoint_name of this RayJobInfo.
        :rtype: str
        """
        return self._endpoint_name

    @endpoint_name.setter
    def endpoint_name(self, endpoint_name):
        r"""Sets the endpoint_name of this RayJobInfo.

        **参数解释**：端点名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。包含小写字母、数字、中划线的组合。字母开头、字母或数字结尾。 **默认取值**：不涉及。

        :param endpoint_name: The endpoint_name of this RayJobInfo.
        :type endpoint_name: str
        """
        self._endpoint_name = endpoint_name

    @property
    def config(self):
        r"""Gets the config of this RayJobInfo.

        :return: The config of this RayJobInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.RayJobConfig`
        """
        return self._config

    @config.setter
    def config(self, config):
        r"""Sets the config of this RayJobInfo.

        :param config: The config of this RayJobInfo.
        :type config: :class:`huaweicloudsdkaidatalake.v2.RayJobConfig`
        """
        self._config = config

    @property
    def description(self):
        r"""Gets the description of this RayJobInfo.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：0~1024。 **默认取值**：不涉及。 

        :return: The description of this RayJobInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this RayJobInfo.

        **参数解释**：描述信息。 **约束限制**：不涉及。 **取值范围**：0~1024。 **默认取值**：不涉及。 

        :param description: The description of this RayJobInfo.
        :type description: str
        """
        self._description = description

    @property
    def id(self):
        r"""Gets the id of this RayJobInfo.

        **参数解释**：作业ID。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 

        :return: The id of this RayJobInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this RayJobInfo.

        **参数解释**：作业ID。 **取值范围**：长度为1~36的英文字符、数字和中划线的组合。 

        :param id: The id of this RayJobInfo.
        :type id: str
        """
        self._id = id

    @property
    def duration(self):
        r"""Gets the duration of this RayJobInfo.

        **参数解释**：运行时长，单位：秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The duration of this RayJobInfo.
        :rtype: int
        """
        return self._duration

    @duration.setter
    def duration(self, duration):
        r"""Sets the duration of this RayJobInfo.

        **参数解释**：运行时长，单位：秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param duration: The duration of this RayJobInfo.
        :type duration: int
        """
        self._duration = duration

    @property
    def submission_id(self):
        r"""Gets the submission_id of this RayJobInfo.

        **参数解释**：Ray Job的唯一ID标识。 **约束限制**：不涉及。 **取值范围**：长度为0~64个字符。 **默认取值**：不涉及。

        :return: The submission_id of this RayJobInfo.
        :rtype: str
        """
        return self._submission_id

    @submission_id.setter
    def submission_id(self, submission_id):
        r"""Sets the submission_id of this RayJobInfo.

        **参数解释**：Ray Job的唯一ID标识。 **约束限制**：不涉及。 **取值范围**：长度为0~64个字符。 **默认取值**：不涉及。

        :param submission_id: The submission_id of this RayJobInfo.
        :type submission_id: str
        """
        self._submission_id = submission_id

    @property
    def endpoint_type(self):
        r"""Gets the endpoint_type of this RayJobInfo.

        **参数解释**：作业对应的端点类型。 **约束限制**：不涉及。 **取值范围**：   - RAY_JOB: RayJob类型的端点作业；   - RAY_CLUSTER: RayCluster类型的端点作业；   - RAY_FEDERATION: Ray联邦端点作业。 **默认取值**：不涉及。 

        :return: The endpoint_type of this RayJobInfo.
        :rtype: str
        """
        return self._endpoint_type

    @endpoint_type.setter
    def endpoint_type(self, endpoint_type):
        r"""Sets the endpoint_type of this RayJobInfo.

        **参数解释**：作业对应的端点类型。 **约束限制**：不涉及。 **取值范围**：   - RAY_JOB: RayJob类型的端点作业；   - RAY_CLUSTER: RayCluster类型的端点作业；   - RAY_FEDERATION: Ray联邦端点作业。 **默认取值**：不涉及。 

        :param endpoint_type: The endpoint_type of this RayJobInfo.
        :type endpoint_type: str
        """
        self._endpoint_type = endpoint_type

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this RayJobInfo.

        **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :return: The endpoint_id of this RayJobInfo.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this RayJobInfo.

        **参数解释**：端点ID。 **取值范围**：长度为1~64个字符，支持大小写英文字母、数字、连字符。

        :param endpoint_id: The endpoint_id of this RayJobInfo.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def federation_id(self):
        r"""Gets the federation_id of this RayJobInfo.

        **参数解释**：联邦ID。 **约束限制**：如果作业未提交到联邦端点，该字段为空字符串。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :return: The federation_id of this RayJobInfo.
        :rtype: str
        """
        return self._federation_id

    @federation_id.setter
    def federation_id(self, federation_id):
        r"""Sets the federation_id of this RayJobInfo.

        **参数解释**：联邦ID。 **约束限制**：如果作业未提交到联邦端点，该字段为空字符串。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。 

        :param federation_id: The federation_id of this RayJobInfo.
        :type federation_id: str
        """
        self._federation_id = federation_id

    @property
    def federation_name(self):
        r"""Gets the federation_name of this RayJobInfo.

        **参数解释**：联邦名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。 **默认取值**：不涉及。

        :return: The federation_name of this RayJobInfo.
        :rtype: str
        """
        return self._federation_name

    @federation_name.setter
    def federation_name(self, federation_name):
        r"""Sets the federation_name of this RayJobInfo.

        **参数解释**：联邦名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符。 **默认取值**：不涉及。

        :param federation_name: The federation_name of this RayJobInfo.
        :type federation_name: str
        """
        self._federation_name = federation_name

    @property
    def create_time(self):
        r"""Gets the create_time of this RayJobInfo.

        **参数解释**：创建时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The create_time of this RayJobInfo.
        :rtype: datetime
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this RayJobInfo.

        **参数解释**：创建时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param create_time: The create_time of this RayJobInfo.
        :type create_time: datetime
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this RayJobInfo.

        **参数解释**：更新时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The update_time of this RayJobInfo.
        :rtype: datetime
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this RayJobInfo.

        **参数解释**：更新时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param update_time: The update_time of this RayJobInfo.
        :type update_time: datetime
        """
        self._update_time = update_time

    @property
    def start_time(self):
        r"""Gets the start_time of this RayJobInfo.

        **参数解释**：作业开始执行的时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The start_time of this RayJobInfo.
        :rtype: datetime
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this RayJobInfo.

        **参数解释**：作业开始执行的时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param start_time: The start_time of this RayJobInfo.
        :type start_time: datetime
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this RayJobInfo.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :return: The end_time of this RayJobInfo.
        :rtype: datetime
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this RayJobInfo.

        **参数解释**：结束时间。使用UTC时间格式，格式为yyyy-MM-ddTHH:mm:ssZ，例如2023-05-30T12:24:30.401Z。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。 

        :param end_time: The end_time of this RayJobInfo.
        :type end_time: datetime
        """
        self._end_time = end_time

    @property
    def status(self):
        r"""Gets the status of this RayJobInfo.

        :return: The status of this RayJobInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.StatusEnum`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this RayJobInfo.

        :param status: The status of this RayJobInfo.
        :type status: :class:`huaweicloudsdkaidatalake.v2.StatusEnum`
        """
        self._status = status

    @property
    def create_user(self):
        r"""Gets the create_user of this RayJobInfo.

        :return: The create_user of this RayJobInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this RayJobInfo.

        :param create_user: The create_user of this RayJobInfo.
        :type create_user: :class:`huaweicloudsdkaidatalake.v2.User`
        """
        self._create_user = create_user

    @property
    def error(self):
        r"""Gets the error of this RayJobInfo.

        :return: The error of this RayJobInfo.
        :rtype: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        """
        return self._error

    @error.setter
    def error(self, error):
        r"""Sets the error of this RayJobInfo.

        :param error: The error of this RayJobInfo.
        :type error: :class:`huaweicloudsdkaidatalake.v2.ErrorMessage`
        """
        self._error = error

    @property
    def history_server_enabled(self):
        r"""Gets the history_server_enabled of this RayJobInfo.

        **参数解释**：指示该作业是否启用了历史服务器（History Server）功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用History Server。   - false：禁用History Server。 **默认取值**：false。

        :return: The history_server_enabled of this RayJobInfo.
        :rtype: bool
        """
        return self._history_server_enabled

    @history_server_enabled.setter
    def history_server_enabled(self, history_server_enabled):
        r"""Sets the history_server_enabled of this RayJobInfo.

        **参数解释**：指示该作业是否启用了历史服务器（History Server）功能。 **约束限制**：不涉及。 **取值范围**：   - true：启用History Server。   - false：禁用History Server。 **默认取值**：false。

        :param history_server_enabled: The history_server_enabled of this RayJobInfo.
        :type history_server_enabled: bool
        """
        self._history_server_enabled = history_server_enabled

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
        if not isinstance(other, RayJobInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
