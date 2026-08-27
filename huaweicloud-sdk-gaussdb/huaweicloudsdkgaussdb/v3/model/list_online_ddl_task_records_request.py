# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOnlineDdlTaskRecordsRequest:

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
        'limit': 'int',
        'offset': 'int',
        'start_time': 'str',
        'end_time': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, x_language=None, instance_id=None, limit=None, offset=None, start_time=None, end_time=None):
        r"""ListOnlineDdlTaskRecordsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。 
        :type x_language: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。 获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。 
        :type instance_id: str
        :param limit: **参数解释**：              查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  10。
        :type limit: int
        :param offset: **参数解释**：              索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  ≥0。  **默认取值**：  0。
        :type offset: int
        :param start_time: **参数解释**：  查询的起始时间戳，格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区， 传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **约束限制**：  不涉及。  **取值范围**：  只能由数字组成，长度为13个字符。  **默认取值**：  不涉及。
        :type start_time: str
        :param end_time: **参数解释**：  查询的结束时间戳，格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区， 传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **约束限制**：  不涉及。  **取值范围**：  只能由数字组成，长度为13个字符。  **默认取值**：  不涉及。
        :type end_time: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def x_language(self):
        r"""Gets the x_language of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。 

        :return: The x_language of this ListOnlineDdlTaskRecordsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。 

        :param x_language: The x_language of this ListOnlineDdlTaskRecordsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。 获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。 

        :return: The instance_id of this ListOnlineDdlTaskRecordsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。 获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。 

        :param instance_id: The instance_id of this ListOnlineDdlTaskRecordsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        r"""Gets the limit of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：              查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  10。

        :return: The limit of this ListOnlineDdlTaskRecordsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：              查询记录数。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  1-100。  **默认取值**：  10。

        :param limit: The limit of this ListOnlineDdlTaskRecordsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：              索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  ≥0。  **默认取值**：  0。

        :return: The offset of this ListOnlineDdlTaskRecordsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：              索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。  **约束限制**：  必须为整数，不能为负数。  **取值范围**：  ≥0。  **默认取值**：  0。

        :param offset: The offset of this ListOnlineDdlTaskRecordsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def start_time(self):
        r"""Gets the start_time of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  查询的起始时间戳，格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区， 传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **约束限制**：  不涉及。  **取值范围**：  只能由数字组成，长度为13个字符。  **默认取值**：  不涉及。

        :return: The start_time of this ListOnlineDdlTaskRecordsRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  查询的起始时间戳，格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区， 传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **约束限制**：  不涉及。  **取值范围**：  只能由数字组成，长度为13个字符。  **默认取值**：  不涉及。

        :param start_time: The start_time of this ListOnlineDdlTaskRecordsRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  查询的结束时间戳，格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区， 传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **约束限制**：  不涉及。  **取值范围**：  只能由数字组成，长度为13个字符。  **默认取值**：  不涉及。

        :return: The end_time of this ListOnlineDdlTaskRecordsRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListOnlineDdlTaskRecordsRequest.

        **参数解释**：  查询的结束时间戳，格式为UNIX时间戳，单位是毫秒，时区为UTC标准时区， 传参时需要将对应时区的时间转为标准时区对应的时间戳，比如，北京时区的时间点需要-8h后再转为时间戳。  **约束限制**：  不涉及。  **取值范围**：  只能由数字组成，长度为13个字符。  **默认取值**：  不涉及。

        :param end_time: The end_time of this ListOnlineDdlTaskRecordsRequest.
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
        if not isinstance(other, ListOnlineDdlTaskRecordsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
