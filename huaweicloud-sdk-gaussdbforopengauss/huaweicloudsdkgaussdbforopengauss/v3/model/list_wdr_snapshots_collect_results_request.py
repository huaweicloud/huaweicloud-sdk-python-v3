# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListWdrSnapshotsCollectResultsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'start_time': 'str',
        'end_time': 'str',
        'job_id': 'str',
        'job_end_time': 'str',
        'job_start_time': 'str',
        'status': 'str',
        'wdr_type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'offset': 'offset',
        'limit': 'limit',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'job_id': 'job_id',
        'job_end_time': 'job_end_time',
        'job_start_time': 'job_start_time',
        'status': 'status',
        'wdr_type': 'wdr_type'
    }

    def __init__(self, x_language=None, instance_id=None, offset=None, limit=None, start_time=None, end_time=None, job_id=None, job_end_time=None, job_start_time=None, status=None, wdr_type=None):
        r"""ListWdrSnapshotsCollectResultsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us
        :type x_language: str
        :param instance_id: **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。
        :type instance_id: str
        :param offset: **参数解释**: 索引位置，偏移量。 **约束限制**:   不涉及。 **取值范围**:   必须为数字，不能为负数。 **默认取值**:   默认为0。
        :type offset: int
        :param limit: **参数解释**:   查询记录数。， **约束限制**:   不涉及。 **取值范围**:   不能为负数，最小值为1，最大值为100。 **默认取值**:   默认为10。
        :type limit: int
        :param start_time: **参数解释**:   查询开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。   例如北京时间偏移显示为+0800，start_time&#x3D;2024-03-15T17:20:33+0800传参时编码为start_time&#x3D;2024-03-15T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。
        :type start_time: str
        :param end_time: **参数解释**:   查询结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。   例如北京时间偏移显示为+0800，end_time&#x3D;2024-03-16T17:20:33+0800传参时编码为end_time&#x3D;2024-03-16T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。
        :type end_time: str
        :param job_id: **参数解释**:   任务ID。正确填写后，可查询指定任务对应的快照报告采集结果。不支持模糊匹配，需填写完整的任务ID。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。
        :type job_id: str
        :param job_end_time: **参数解释**:   采集任务创建时间终点。可查询任务创建时间小于等于该时间终点的任务结果。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如，北京时间偏移显示为+0800，job_end_time&#x3D;2024-03-16T17:20:33+0800，传参时编码为job_end_time&#x3D;2024-03-16T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。
        :type job_end_time: str
        :param job_start_time: **参数解释**:   采集任务创建时间起点。可查询任务创建时间大于等于该时间起点的任务结果。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如，北京时间偏移显示为+0800，job_start_time&#x3D;2024-03-15T17:20:33+0800传参时编码为job_start_time&#x3D;2024-03-15T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。
        :type job_start_time: str
        :param status: **参数解释**: 任务采集状态。填写后，可查询对应采集状态的任务结果。 **约束限制**: 不支持模糊匹配，区分大小写，请填写完整的合法状态值。 **取值范围**: - EXPORTING：采集中。 - SUCCESS：采集成功。 - FAILED：采集失败。  **默认取值**:   不涉及。
        :type status: str
        :param wdr_type: **参数解释**: 填写后，可查询对应采集类型的任务结果。 **约束限制**: 不支持模糊匹配，区分大小写，请填写完整的合法枚举值。 **取值范围**: - cluster：实例级。 - component：组件级。 - pdb：租户级。  **默认取值**:   不涉及。
        :type wdr_type: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._offset = None
        self._limit = None
        self._start_time = None
        self._end_time = None
        self._job_id = None
        self._job_end_time = None
        self._job_start_time = None
        self._status = None
        self._wdr_type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if job_id is not None:
            self.job_id = job_id
        if job_end_time is not None:
            self.job_end_time = job_end_time
        if job_start_time is not None:
            self.job_start_time = job_start_time
        if status is not None:
            self.status = status
        if wdr_type is not None:
            self.wdr_type = wdr_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us

        :return: The x_language of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**:   - zh-cn   - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListWdrSnapshotsCollectResultsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :return: The instance_id of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 实例ID，此参数是用户创建实例的唯一标识。 **约束限制**: 不涉及。 **取值范围**: 只能由英文字母、数字组成，且长度为36个字符。 **默认取值**: 不涉及。

        :param instance_id: The instance_id of this ListWdrSnapshotsCollectResultsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def offset(self):
        r"""Gets the offset of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 索引位置，偏移量。 **约束限制**:   不涉及。 **取值范围**:   必须为数字，不能为负数。 **默认取值**:   默认为0。

        :return: The offset of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 索引位置，偏移量。 **约束限制**:   不涉及。 **取值范围**:   必须为数字，不能为负数。 **默认取值**:   默认为0。

        :param offset: The offset of this ListWdrSnapshotsCollectResultsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   查询记录数。， **约束限制**:   不涉及。 **取值范围**:   不能为负数，最小值为1，最大值为100。 **默认取值**:   默认为10。

        :return: The limit of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   查询记录数。， **约束限制**:   不涉及。 **取值范围**:   不能为负数，最小值为1，最大值为100。 **默认取值**:   默认为10。

        :param limit: The limit of this ListWdrSnapshotsCollectResultsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def start_time(self):
        r"""Gets the start_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   查询开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。   例如北京时间偏移显示为+0800，start_time=2024-03-15T17:20:33+0800传参时编码为start_time=2024-03-15T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :return: The start_time of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   查询开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。   例如北京时间偏移显示为+0800，start_time=2024-03-15T17:20:33+0800传参时编码为start_time=2024-03-15T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :param start_time: The start_time of this ListWdrSnapshotsCollectResultsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   查询结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。   例如北京时间偏移显示为+0800，end_time=2024-03-16T17:20:33+0800传参时编码为end_time=2024-03-16T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :return: The end_time of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   查询结束时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始，Z指时区偏移量，时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。   例如北京时间偏移显示为+0800，end_time=2024-03-16T17:20:33+0800传参时编码为end_time=2024-03-16T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :param end_time: The end_time of this ListWdrSnapshotsCollectResultsRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def job_id(self):
        r"""Gets the job_id of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   任务ID。正确填写后，可查询指定任务对应的快照报告采集结果。不支持模糊匹配，需填写完整的任务ID。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :return: The job_id of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   任务ID。正确填写后，可查询指定任务对应的快照报告采集结果。不支持模糊匹配，需填写完整的任务ID。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :param job_id: The job_id of this ListWdrSnapshotsCollectResultsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_end_time(self):
        r"""Gets the job_end_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   采集任务创建时间终点。可查询任务创建时间小于等于该时间终点的任务结果。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如，北京时间偏移显示为+0800，job_end_time=2024-03-16T17:20:33+0800，传参时编码为job_end_time=2024-03-16T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :return: The job_end_time of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._job_end_time

    @job_end_time.setter
    def job_end_time(self, job_end_time):
        r"""Sets the job_end_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   采集任务创建时间终点。可查询任务创建时间小于等于该时间终点的任务结果。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如，北京时间偏移显示为+0800，job_end_time=2024-03-16T17:20:33+0800，传参时编码为job_end_time=2024-03-16T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :param job_end_time: The job_end_time of this ListWdrSnapshotsCollectResultsRequest.
        :type job_end_time: str
        """
        self._job_end_time = job_end_time

    @property
    def job_start_time(self):
        r"""Gets the job_start_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   采集任务创建时间起点。可查询任务创建时间大于等于该时间起点的任务结果。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如，北京时间偏移显示为+0800，job_start_time=2024-03-15T17:20:33+0800传参时编码为job_start_time=2024-03-15T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :return: The job_start_time of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._job_start_time

    @job_start_time.setter
    def job_start_time(self, job_start_time):
        r"""Sets the job_start_time of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**:   采集任务创建时间起点。可查询任务创建时间大于等于该时间起点的任务结果。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。时区中的+号需要进行URL编码，编码为%2B，时区中的-号无需编码。例如，北京时间偏移显示为+0800，job_start_time=2024-03-15T17:20:33+0800传参时编码为job_start_time=2024-03-15T17:20:33%2B0800。 **约束限制**:   不涉及。 **取值范围**:   不涉及。 **默认取值**:   不涉及。

        :param job_start_time: The job_start_time of this ListWdrSnapshotsCollectResultsRequest.
        :type job_start_time: str
        """
        self._job_start_time = job_start_time

    @property
    def status(self):
        r"""Gets the status of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 任务采集状态。填写后，可查询对应采集状态的任务结果。 **约束限制**: 不支持模糊匹配，区分大小写，请填写完整的合法状态值。 **取值范围**: - EXPORTING：采集中。 - SUCCESS：采集成功。 - FAILED：采集失败。  **默认取值**:   不涉及。

        :return: The status of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 任务采集状态。填写后，可查询对应采集状态的任务结果。 **约束限制**: 不支持模糊匹配，区分大小写，请填写完整的合法状态值。 **取值范围**: - EXPORTING：采集中。 - SUCCESS：采集成功。 - FAILED：采集失败。  **默认取值**:   不涉及。

        :param status: The status of this ListWdrSnapshotsCollectResultsRequest.
        :type status: str
        """
        self._status = status

    @property
    def wdr_type(self):
        r"""Gets the wdr_type of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 填写后，可查询对应采集类型的任务结果。 **约束限制**: 不支持模糊匹配，区分大小写，请填写完整的合法枚举值。 **取值范围**: - cluster：实例级。 - component：组件级。 - pdb：租户级。  **默认取值**:   不涉及。

        :return: The wdr_type of this ListWdrSnapshotsCollectResultsRequest.
        :rtype: str
        """
        return self._wdr_type

    @wdr_type.setter
    def wdr_type(self, wdr_type):
        r"""Sets the wdr_type of this ListWdrSnapshotsCollectResultsRequest.

        **参数解释**: 填写后，可查询对应采集类型的任务结果。 **约束限制**: 不支持模糊匹配，区分大小写，请填写完整的合法枚举值。 **取值范围**: - cluster：实例级。 - component：组件级。 - pdb：租户级。  **默认取值**:   不涉及。

        :param wdr_type: The wdr_type of this ListWdrSnapshotsCollectResultsRequest.
        :type wdr_type: str
        """
        self._wdr_type = wdr_type

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
        if not isinstance(other, ListWdrSnapshotsCollectResultsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
