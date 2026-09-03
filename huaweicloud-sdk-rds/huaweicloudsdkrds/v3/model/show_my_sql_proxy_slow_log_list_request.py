# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMySqlProxySlowLogListRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'proxy_id': 'str',
        'x_language': 'str',
        'start_time': 'int',
        'end_time': 'int',
        'per_page': 'int',
        'line_num': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'proxy_id': 'proxy_id',
        'x_language': 'X-Language',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'per_page': 'per_page',
        'line_num': 'line_num'
    }

    def __init__(self, instance_id=None, proxy_id=None, x_language=None, start_time=None, end_time=None, per_page=None, line_num=None):
        r"""ShowMySqlProxySlowLogListRequest

        The model defined in huaweicloud sdk

        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param proxy_id: **参数解释**：  数据库代理ID，此参数是数据库代理的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。
        :type proxy_id: str
        :param x_language: **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param start_time: **参数解释**：  查询开始时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type start_time: int
        :param end_time: **参数解释**：  查询结束时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type end_time: int
        :param per_page: **参数解释**：  每页条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  10。
        :type per_page: int
        :param line_num: **参数解释**：  每次查询起始记录ID。首次查询可不传，后续传入返回值中的line_num以获取后续动态加载的数据。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type line_num: str
        """
        
        

        self._instance_id = None
        self._proxy_id = None
        self._x_language = None
        self._start_time = None
        self._end_time = None
        self._per_page = None
        self._line_num = None
        self.discriminator = None

        self.instance_id = instance_id
        self.proxy_id = proxy_id
        if x_language is not None:
            self.x_language = x_language
        self.start_time = start_time
        self.end_time = end_time
        if per_page is not None:
            self.per_page = per_page
        if line_num is not None:
            self.line_num = line_num

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowMySqlProxySlowLogListRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowMySqlProxySlowLogListRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def proxy_id(self):
        r"""Gets the proxy_id of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  数据库代理ID，此参数是数据库代理的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :return: The proxy_id of this ShowMySqlProxySlowLogListRequest.
        :rtype: str
        """
        return self._proxy_id

    @proxy_id.setter
    def proxy_id(self, proxy_id):
        r"""Sets the proxy_id of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  数据库代理ID，此参数是数据库代理的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，长度为36个字符。  **默认取值**：  不涉及。

        :param proxy_id: The proxy_id of this ShowMySqlProxySlowLogListRequest.
        :type proxy_id: str
        """
        self._proxy_id = proxy_id

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this ShowMySqlProxySlowLogListRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  请求语言类型。  **约束限制**：  不涉及。  **取值范围**：  - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowMySqlProxySlowLogListRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  查询开始时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The start_time of this ShowMySqlProxySlowLogListRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  查询开始时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param start_time: The start_time of this ShowMySqlProxySlowLogListRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  查询结束时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The end_time of this ShowMySqlProxySlowLogListRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  查询结束时间，毫秒级时间戳。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param end_time: The end_time of this ShowMySqlProxySlowLogListRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def per_page(self):
        r"""Gets the per_page of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  每页条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  10。

        :return: The per_page of this ShowMySqlProxySlowLogListRequest.
        :rtype: int
        """
        return self._per_page

    @per_page.setter
    def per_page(self, per_page):
        r"""Sets the per_page of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  每页条数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  10。

        :param per_page: The per_page of this ShowMySqlProxySlowLogListRequest.
        :type per_page: int
        """
        self._per_page = per_page

    @property
    def line_num(self):
        r"""Gets the line_num of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  每次查询起始记录ID。首次查询可不传，后续传入返回值中的line_num以获取后续动态加载的数据。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The line_num of this ShowMySqlProxySlowLogListRequest.
        :rtype: str
        """
        return self._line_num

    @line_num.setter
    def line_num(self, line_num):
        r"""Sets the line_num of this ShowMySqlProxySlowLogListRequest.

        **参数解释**：  每次查询起始记录ID。首次查询可不传，后续传入返回值中的line_num以获取后续动态加载的数据。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param line_num: The line_num of this ShowMySqlProxySlowLogListRequest.
        :type line_num: str
        """
        self._line_num = line_num

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
        if not isinstance(other, ShowMySqlProxySlowLogListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
