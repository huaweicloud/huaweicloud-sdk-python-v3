# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowKillProcessHistoryRequest:

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
        'start_time': 'int',
        'end_time': 'int',
        'page_num': 'int',
        'page_size': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'page_num': 'page_num',
        'page_size': 'page_size'
    }

    def __init__(self, x_language=None, instance_id=None, start_time=None, end_time=None, page_num=None, page_size=None):
        r"""ShowKillProcessHistoryRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。
        :type x_language: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param start_time: **参数解释**：  Kill会话的开始时间。  **约束限制**：  - 格式为UNIX时间戳，单位是毫秒。 - start_time要小于end_time。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type start_time: int
        :param end_time: **参数解释**：    Kill会话的结束时间。    **约束限制**：    - 格式为UNIX时间戳，单位是毫秒。 - end_time要大于start_time。   **取值范围**：    不涉及。  **默认取值**：    不涉及。
        :type end_time: int
        :param page_num: **参数解释**：    当前页数。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    1。
        :type page_num: int
        :param page_size: **参数解释**：    每页大小。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    1-100。  **默认取值**：    10。
        :type page_size: int
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._page_num = None
        self._page_size = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time
        if page_num is not None:
            self.page_num = page_num
        if page_size is not None:
            self.page_size = page_size

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowKillProcessHistoryRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。

        :return: The x_language of this ShowKillProcessHistoryRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowKillProcessHistoryRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us：英文。 - zh-cn：中文。  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowKillProcessHistoryRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowKillProcessHistoryRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowKillProcessHistoryRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowKillProcessHistoryRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  获取方法请参见[查询实例列表](https://support.huaweicloud.com/api-taurusdb/ListGaussMySqlInstancesUnifyStatus.html)。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowKillProcessHistoryRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowKillProcessHistoryRequest.

        **参数解释**：  Kill会话的开始时间。  **约束限制**：  - 格式为UNIX时间戳，单位是毫秒。 - start_time要小于end_time。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The start_time of this ShowKillProcessHistoryRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowKillProcessHistoryRequest.

        **参数解释**：  Kill会话的开始时间。  **约束限制**：  - 格式为UNIX时间戳，单位是毫秒。 - start_time要小于end_time。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param start_time: The start_time of this ShowKillProcessHistoryRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowKillProcessHistoryRequest.

        **参数解释**：    Kill会话的结束时间。    **约束限制**：    - 格式为UNIX时间戳，单位是毫秒。 - end_time要大于start_time。   **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :return: The end_time of this ShowKillProcessHistoryRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowKillProcessHistoryRequest.

        **参数解释**：    Kill会话的结束时间。    **约束限制**：    - 格式为UNIX时间戳，单位是毫秒。 - end_time要大于start_time。   **取值范围**：    不涉及。  **默认取值**：    不涉及。

        :param end_time: The end_time of this ShowKillProcessHistoryRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def page_num(self):
        r"""Gets the page_num of this ShowKillProcessHistoryRequest.

        **参数解释**：    当前页数。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    1。

        :return: The page_num of this ShowKillProcessHistoryRequest.
        :rtype: int
        """
        return self._page_num

    @page_num.setter
    def page_num(self, page_num):
        r"""Sets the page_num of this ShowKillProcessHistoryRequest.

        **参数解释**：    当前页数。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    ≥0。  **默认取值**：    1。

        :param page_num: The page_num of this ShowKillProcessHistoryRequest.
        :type page_num: int
        """
        self._page_num = page_num

    @property
    def page_size(self):
        r"""Gets the page_size of this ShowKillProcessHistoryRequest.

        **参数解释**：    每页大小。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    1-100。  **默认取值**：    10。

        :return: The page_size of this ShowKillProcessHistoryRequest.
        :rtype: int
        """
        return self._page_size

    @page_size.setter
    def page_size(self, page_size):
        r"""Sets the page_size of this ShowKillProcessHistoryRequest.

        **参数解释**：    每页大小。    **约束限制**：    必须为整数，不能为负数。    **取值范围**：    1-100。  **默认取值**：    10。

        :param page_size: The page_size of this ShowKillProcessHistoryRequest.
        :type page_size: int
        """
        self._page_size = page_size

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
        if not isinstance(other, ShowKillProcessHistoryRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
