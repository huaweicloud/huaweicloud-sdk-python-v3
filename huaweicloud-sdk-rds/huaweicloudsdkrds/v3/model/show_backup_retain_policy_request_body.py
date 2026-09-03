# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupRetainPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instanceids': 'list[str]',
        'offset': 'int',
        'limit': 'int',
        'instance_status': 'str',
        'begin_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'instanceids': 'instanceids',
        'offset': 'offset',
        'limit': 'limit',
        'instance_status': 'instance_status',
        'begin_time': 'begin_time',
        'end_time': 'end_time'
    }

    def __init__(self, instanceids=None, offset=None, limit=None, instance_status=None, begin_time=None, end_time=None):
        r"""ShowBackupRetainPolicyRequestBody

        The model defined in huaweicloud sdk

        :param instanceids: **参数解释**：  实例ID列表，实例ID是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  实例ID只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type instanceids: list[str]
        :param offset: **参数解释**  索引位置，偏移量。  **约束限制**  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **取值范围**  大于等于0的整数。  **默认取值**  0
        :type offset: int
        :param limit: **参数解释**  查询记录数。  **约束限制**  不能为负数。  **取值范围**  最小值为1，最大值为100。  **默认取值**  10
        :type limit: int
        :param instance_status: **参数解释**：  实例状态  **约束限制**：  不涉及。  **取值范围**：  normal、deleted  **默认取值**：  不涉及。
        :type instance_status: str
        :param begin_time: **参数解释**  查询开始时间。时间指实例的删除时间。  **约束限制**  “begin_time”有值时，“end_time”必选。 “begin_time”有值时，查询实例状态为已删除的实例。  **取值范围**  格式为“yyyy-mm-ddThh:mm:ss±HH:mm”。  其中，T指某个时间的开始；±HH:mm指时区偏移量，例如北京时间偏移显示为+08:00。  **默认取值**  不涉及。
        :type begin_time: str
        :param end_time: **参数解释**  查询结束时间。时间指实例的删除时间  **约束限制**  “end_time”有值时，“begin_time”必选。 “end_time”有值时，查询实例状态为已删除的实例。  **取值范围**  格式为“yyyy-mm-ddThh:mm:ss±HH:mm”，且大于查询开始时间。  其中，T指某个时间的开始；±HH:mm指时区偏移量，例如北京时间偏移显示为+08:00。  **默认取值**  不涉及。
        :type end_time: str
        """
        
        

        self._instanceids = None
        self._offset = None
        self._limit = None
        self._instance_status = None
        self._begin_time = None
        self._end_time = None
        self.discriminator = None

        if instanceids is not None:
            self.instanceids = instanceids
        self.offset = offset
        self.limit = limit
        if instance_status is not None:
            self.instance_status = instance_status
        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def instanceids(self):
        r"""Gets the instanceids of this ShowBackupRetainPolicyRequestBody.

        **参数解释**：  实例ID列表，实例ID是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  实例ID只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instanceids of this ShowBackupRetainPolicyRequestBody.
        :rtype: list[str]
        """
        return self._instanceids

    @instanceids.setter
    def instanceids(self, instanceids):
        r"""Sets the instanceids of this ShowBackupRetainPolicyRequestBody.

        **参数解释**：  实例ID列表，实例ID是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  实例ID只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param instanceids: The instanceids of this ShowBackupRetainPolicyRequestBody.
        :type instanceids: list[str]
        """
        self._instanceids = instanceids

    @property
    def offset(self):
        r"""Gets the offset of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  索引位置，偏移量。  **约束限制**  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **取值范围**  大于等于0的整数。  **默认取值**  0

        :return: The offset of this ShowBackupRetainPolicyRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  索引位置，偏移量。  **约束限制**  从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询），必须为数字，不能为负数。  **取值范围**  大于等于0的整数。  **默认取值**  0

        :param offset: The offset of this ShowBackupRetainPolicyRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  查询记录数。  **约束限制**  不能为负数。  **取值范围**  最小值为1，最大值为100。  **默认取值**  10

        :return: The limit of this ShowBackupRetainPolicyRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  查询记录数。  **约束限制**  不能为负数。  **取值范围**  最小值为1，最大值为100。  **默认取值**  10

        :param limit: The limit of this ShowBackupRetainPolicyRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def instance_status(self):
        r"""Gets the instance_status of this ShowBackupRetainPolicyRequestBody.

        **参数解释**：  实例状态  **约束限制**：  不涉及。  **取值范围**：  normal、deleted  **默认取值**：  不涉及。

        :return: The instance_status of this ShowBackupRetainPolicyRequestBody.
        :rtype: str
        """
        return self._instance_status

    @instance_status.setter
    def instance_status(self, instance_status):
        r"""Sets the instance_status of this ShowBackupRetainPolicyRequestBody.

        **参数解释**：  实例状态  **约束限制**：  不涉及。  **取值范围**：  normal、deleted  **默认取值**：  不涉及。

        :param instance_status: The instance_status of this ShowBackupRetainPolicyRequestBody.
        :type instance_status: str
        """
        self._instance_status = instance_status

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  查询开始时间。时间指实例的删除时间。  **约束限制**  “begin_time”有值时，“end_time”必选。 “begin_time”有值时，查询实例状态为已删除的实例。  **取值范围**  格式为“yyyy-mm-ddThh:mm:ss±HH:mm”。  其中，T指某个时间的开始；±HH:mm指时区偏移量，例如北京时间偏移显示为+08:00。  **默认取值**  不涉及。

        :return: The begin_time of this ShowBackupRetainPolicyRequestBody.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  查询开始时间。时间指实例的删除时间。  **约束限制**  “begin_time”有值时，“end_time”必选。 “begin_time”有值时，查询实例状态为已删除的实例。  **取值范围**  格式为“yyyy-mm-ddThh:mm:ss±HH:mm”。  其中，T指某个时间的开始；±HH:mm指时区偏移量，例如北京时间偏移显示为+08:00。  **默认取值**  不涉及。

        :param begin_time: The begin_time of this ShowBackupRetainPolicyRequestBody.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  查询结束时间。时间指实例的删除时间  **约束限制**  “end_time”有值时，“begin_time”必选。 “end_time”有值时，查询实例状态为已删除的实例。  **取值范围**  格式为“yyyy-mm-ddThh:mm:ss±HH:mm”，且大于查询开始时间。  其中，T指某个时间的开始；±HH:mm指时区偏移量，例如北京时间偏移显示为+08:00。  **默认取值**  不涉及。

        :return: The end_time of this ShowBackupRetainPolicyRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowBackupRetainPolicyRequestBody.

        **参数解释**  查询结束时间。时间指实例的删除时间  **约束限制**  “end_time”有值时，“begin_time”必选。 “end_time”有值时，查询实例状态为已删除的实例。  **取值范围**  格式为“yyyy-mm-ddThh:mm:ss±HH:mm”，且大于查询开始时间。  其中，T指某个时间的开始；±HH:mm指时区偏移量，例如北京时间偏移显示为+08:00。  **默认取值**  不涉及。

        :param end_time: The end_time of this ShowBackupRetainPolicyRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowBackupRetainPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
