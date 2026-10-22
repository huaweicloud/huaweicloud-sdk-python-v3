# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFlinkJobEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace_id': 'str',
        'job_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'create_time_after': 'int',
        'create_time_before': 'int'
    }

    attribute_map = {
        'workspace_id': 'workspace_id',
        'job_id': 'job_id',
        'offset': 'offset',
        'limit': 'limit',
        'create_time_after': 'create_time_after',
        'create_time_before': 'create_time_before'
    }

    def __init__(self, workspace_id=None, job_id=None, offset=None, limit=None, create_time_after=None, create_time_before=None):
        r"""ListFlinkJobEventsRequest

        The model defined in huaweicloud sdk

        :param workspace_id: **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。
        :type workspace_id: str
        :param job_id: **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。
        :type job_id: str
        :param offset: **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。
        :type offset: int
        :param limit: **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。
        :type limit: int
        :param create_time_after: **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_time_after: int
        :param create_time_before: **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type create_time_before: int
        """
        
        

        self._workspace_id = None
        self._job_id = None
        self._offset = None
        self._limit = None
        self._create_time_after = None
        self._create_time_before = None
        self.discriminator = None

        self.workspace_id = workspace_id
        self.job_id = job_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if create_time_after is not None:
            self.create_time_after = create_time_after
        if create_time_before is not None:
            self.create_time_before = create_time_before

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListFlinkJobEventsRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :return: The workspace_id of this ListFlinkJobEventsRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListFlinkJobEventsRequest.

        **参数解释**：工作空间ID，可通过[获取工作空间ID](aidatalake_02_0044.xml)获取。 **约束限制**：不涉及。 **取值范围**：长度为32~36的英文字符、数字和中划线的组合。 **默认取值**：不涉及。

        :param workspace_id: The workspace_id of this ListFlinkJobEventsRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ListFlinkJobEventsRequest.

        **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :return: The job_id of this ListFlinkJobEventsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ListFlinkJobEventsRequest.

        **参数解释**：Flink作业ID，用于唯一标识一个Flink作业，可通过[查询Flink作业列表](ListFlinkJobs.xml)接口获取。 **约束限制**：不涉及。 **取值范围**：采用UUIDv7格式，固定36个字符。 **默认取值**：不涉及。

        :param job_id: The job_id of this ListFlinkJobEventsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def offset(self):
        r"""Gets the offset of this ListFlinkJobEventsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :return: The offset of this ListFlinkJobEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFlinkJobEventsRequest.

        **参数解释**：偏移量，表示从此偏移量开始查询。 **约束限制**：不涉及。 **取值范围**：0~1000000000。 **默认取值**：0。

        :param offset: The offset of this ListFlinkJobEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFlinkJobEventsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :return: The limit of this ListFlinkJobEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFlinkJobEventsRequest.

        **参数解释**：指定每一页返回的最大条目数。 **约束限制**：不涉及。 **取值范围**：1~100。 **默认取值**：10。

        :param limit: The limit of this ListFlinkJobEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def create_time_after(self):
        r"""Gets the create_time_after of this ListFlinkJobEventsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_time_after of this ListFlinkJobEventsRequest.
        :rtype: int
        """
        return self._create_time_after

    @create_time_after.setter
    def create_time_after(self, create_time_after):
        r"""Sets the create_time_after of this ListFlinkJobEventsRequest.

        **参数解释**：用于查询创建时间在该时间点之后的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_time_after: The create_time_after of this ListFlinkJobEventsRequest.
        :type create_time_after: int
        """
        self._create_time_after = create_time_after

    @property
    def create_time_before(self):
        r"""Gets the create_time_before of this ListFlinkJobEventsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The create_time_before of this ListFlinkJobEventsRequest.
        :rtype: int
        """
        return self._create_time_before

    @create_time_before.setter
    def create_time_before(self, create_time_before):
        r"""Sets the create_time_before of this ListFlinkJobEventsRequest.

        **参数解释**：用于查询创建时间在该时间点之前的作业。unix时间戳，单位：毫秒。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param create_time_before: The create_time_before of this ListFlinkJobEventsRequest.
        :type create_time_before: int
        """
        self._create_time_before = create_time_before

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
        if not isinstance(other, ListFlinkJobEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
