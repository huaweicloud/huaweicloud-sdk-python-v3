# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCoreSpaceJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'space_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'status': 'str',
        'job_name': 'str'
    }

    attribute_map = {
        'space_id': 'space_id',
        'limit': 'limit',
        'offset': 'offset',
        'status': 'status',
        'job_name': 'job_name'
    }

    def __init__(self, space_id=None, limit=None, offset=None, status=None, job_name=None):
        r"""ListCoreSpaceJobsRequest

        The model defined in huaweicloud sdk

        :param space_id: **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 
        :type space_id: str
        :param limit: **参数解释：** 每页返回的记录数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 20。 
        :type limit: int
        :param offset: **参数解释：** 偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 
        :type offset: int
        :param status: **参数解释：** 按任务执行状态过滤异步任务。 **约束限制：** 不涉及。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 **默认取值：** 不涉及。 
        :type status: str
        :param job_name: **参数解释：** 按任务名称过滤（模糊匹配）。 **约束限制：** 长度不超过128个字符，支持[待补充]字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 
        :type job_name: str
        """
        
        

        self._space_id = None
        self._limit = None
        self._offset = None
        self._status = None
        self._job_name = None
        self.discriminator = None

        self.space_id = space_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if status is not None:
            self.status = status
        if job_name is not None:
            self.job_name = job_name

    @property
    def space_id(self):
        r"""Gets the space_id of this ListCoreSpaceJobsRequest.

        **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :return: The space_id of this ListCoreSpaceJobsRequest.
        :rtype: str
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        r"""Sets the space_id of this ListCoreSpaceJobsRequest.

        **参数解释：**  记忆库 ID，唯一标识一个记忆库，可以通过AgentArts智能体记忆库控制台或者记忆库查询接口获取。 **约束限制：** 仅支持字母、数字和中划线。 **取值范围：** 匹配标准的UUID格式（8-4-4-4-12的十六进制数字串，由连字符分隔），符合正则条件^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$。 **默认取值：** 不涉及。 

        :param space_id: The space_id of this ListCoreSpaceJobsRequest.
        :type space_id: str
        """
        self._space_id = space_id

    @property
    def limit(self):
        r"""Gets the limit of this ListCoreSpaceJobsRequest.

        **参数解释：** 每页返回的记录数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 20。 

        :return: The limit of this ListCoreSpaceJobsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListCoreSpaceJobsRequest.

        **参数解释：** 每页返回的记录数量（条），用于分页查询。 **约束限制：** 不涉及。 **取值范围：** 1-100。 **默认取值：** 20。 

        :param limit: The limit of this ListCoreSpaceJobsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListCoreSpaceJobsRequest.

        **参数解释：** 偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :return: The offset of this ListCoreSpaceJobsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListCoreSpaceJobsRequest.

        **参数解释：** 偏移量（条），用于分页查询时指定起始位置，从0开始。 **约束限制：** 不涉及。 **取值范围：** 0-100000。 **默认取值：** 0。 

        :param offset: The offset of this ListCoreSpaceJobsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def status(self):
        r"""Gets the status of this ListCoreSpaceJobsRequest.

        **参数解释：** 按任务执行状态过滤异步任务。 **约束限制：** 不涉及。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 **默认取值：** 不涉及。 

        :return: The status of this ListCoreSpaceJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListCoreSpaceJobsRequest.

        **参数解释：** 按任务执行状态过滤异步任务。 **约束限制：** 不涉及。 **取值范围：** - running: 执行中 - success: 成功 - failed: 失败 **默认取值：** 不涉及。 

        :param status: The status of this ListCoreSpaceJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def job_name(self):
        r"""Gets the job_name of this ListCoreSpaceJobsRequest.

        **参数解释：** 按任务名称过滤（模糊匹配）。 **约束限制：** 长度不超过128个字符，支持[待补充]字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :return: The job_name of this ListCoreSpaceJobsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ListCoreSpaceJobsRequest.

        **参数解释：** 按任务名称过滤（模糊匹配）。 **约束限制：** 长度不超过128个字符，支持[待补充]字符。 **取值范围：** 不涉及。 **默认取值：** 不涉及。 

        :param job_name: The job_name of this ListCoreSpaceJobsRequest.
        :type job_name: str
        """
        self._job_name = job_name

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
        if not isinstance(other, ListCoreSpaceJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
