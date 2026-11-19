# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListVulHandleTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'offset': 'int',
        'limit': 'int',
        'handle_type': 'str',
        'min_start_time': 'int',
        'max_start_time': 'int',
        'status': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'offset': 'offset',
        'limit': 'limit',
        'handle_type': 'handle_type',
        'min_start_time': 'min_start_time',
        'max_start_time': 'max_start_time',
        'status': 'status'
    }

    def __init__(self, enterprise_project_id=None, offset=None, limit=None, handle_type=None, min_start_time=None, max_start_time=None, status=None):
        r"""ListVulHandleTaskRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param offset: **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 
        :type offset: int
        :param limit: **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 
        :type limit: int
        :param handle_type: **参数解释**: 处置任务类型 **约束限制**: 不涉及 **取值范围**: - immediate_repair：立即修复。 - verify：验证。  **默认取值**: 不涉及 
        :type handle_type: str
        :param min_start_time: **参数解释**: 任务开始时间的最小值，时间戳，单位毫秒 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type min_start_time: int
        :param max_start_time: **参数解释**: 任务开始时间的最大值，时间戳，单位毫秒 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 
        :type max_start_time: int
        :param status: **参数解释**: 任务状态 **约束限制**: 不涉及 **取值范围**: - running：执行中。 - finished：已完成。  **默认取值**: 不涉及 
        :type status: str
        """
        
        

        self._enterprise_project_id = None
        self._offset = None
        self._limit = None
        self._handle_type = None
        self._min_start_time = None
        self._max_start_time = None
        self._status = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if handle_type is not None:
            self.handle_type = handle_type
        if min_start_time is not None:
            self.min_start_time = min_start_time
        if max_start_time is not None:
            self.max_start_time = max_start_time
        if status is not None:
            self.status = status

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListVulHandleTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListVulHandleTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListVulHandleTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListVulHandleTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def offset(self):
        r"""Gets the offset of this ListVulHandleTaskRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :return: The offset of this ListVulHandleTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListVulHandleTaskRequest.

        **参数解释**: 偏移量：指定返回记录的开始位置 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值2000000 **默认取值**: 默认为0 

        :param offset: The offset of this ListVulHandleTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListVulHandleTaskRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :return: The limit of this ListVulHandleTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListVulHandleTaskRequest.

        **参数解释**: 每页显示个数 **约束限制**: 不涉及 **取值范围**: 取值10-200 **默认取值**: 10 

        :param limit: The limit of this ListVulHandleTaskRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def handle_type(self):
        r"""Gets the handle_type of this ListVulHandleTaskRequest.

        **参数解释**: 处置任务类型 **约束限制**: 不涉及 **取值范围**: - immediate_repair：立即修复。 - verify：验证。  **默认取值**: 不涉及 

        :return: The handle_type of this ListVulHandleTaskRequest.
        :rtype: str
        """
        return self._handle_type

    @handle_type.setter
    def handle_type(self, handle_type):
        r"""Sets the handle_type of this ListVulHandleTaskRequest.

        **参数解释**: 处置任务类型 **约束限制**: 不涉及 **取值范围**: - immediate_repair：立即修复。 - verify：验证。  **默认取值**: 不涉及 

        :param handle_type: The handle_type of this ListVulHandleTaskRequest.
        :type handle_type: str
        """
        self._handle_type = handle_type

    @property
    def min_start_time(self):
        r"""Gets the min_start_time of this ListVulHandleTaskRequest.

        **参数解释**: 任务开始时间的最小值，时间戳，单位毫秒 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The min_start_time of this ListVulHandleTaskRequest.
        :rtype: int
        """
        return self._min_start_time

    @min_start_time.setter
    def min_start_time(self, min_start_time):
        r"""Sets the min_start_time of this ListVulHandleTaskRequest.

        **参数解释**: 任务开始时间的最小值，时间戳，单位毫秒 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param min_start_time: The min_start_time of this ListVulHandleTaskRequest.
        :type min_start_time: int
        """
        self._min_start_time = min_start_time

    @property
    def max_start_time(self):
        r"""Gets the max_start_time of this ListVulHandleTaskRequest.

        **参数解释**: 任务开始时间的最大值，时间戳，单位毫秒 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :return: The max_start_time of this ListVulHandleTaskRequest.
        :rtype: int
        """
        return self._max_start_time

    @max_start_time.setter
    def max_start_time(self, max_start_time):
        r"""Sets the max_start_time of this ListVulHandleTaskRequest.

        **参数解释**: 任务开始时间的最大值，时间戳，单位毫秒 **约束限制**: 不涉及 **取值范围**: 最小值0，最大值9223372036854775807 **默认取值**: 不涉及 

        :param max_start_time: The max_start_time of this ListVulHandleTaskRequest.
        :type max_start_time: int
        """
        self._max_start_time = max_start_time

    @property
    def status(self):
        r"""Gets the status of this ListVulHandleTaskRequest.

        **参数解释**: 任务状态 **约束限制**: 不涉及 **取值范围**: - running：执行中。 - finished：已完成。  **默认取值**: 不涉及 

        :return: The status of this ListVulHandleTaskRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListVulHandleTaskRequest.

        **参数解释**: 任务状态 **约束限制**: 不涉及 **取值范围**: - running：执行中。 - finished：已完成。  **默认取值**: 不涉及 

        :param status: The status of this ListVulHandleTaskRequest.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ListVulHandleTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
