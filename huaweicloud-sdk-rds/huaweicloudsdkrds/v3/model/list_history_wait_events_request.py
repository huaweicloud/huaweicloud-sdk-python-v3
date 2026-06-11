# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListHistoryWaitEventsRequest:

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
        'start_time': 'int',
        'end_time': 'int',
        'offset': 'int',
        'limit': 'int',
        'x_language': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'start_time': 'start_time',
        'end_time': 'end_time',
        'offset': 'offset',
        'limit': 'limit',
        'x_language': 'X-Language'
    }

    def __init__(self, instance_id=None, start_time=None, end_time=None, offset=None, limit=None, x_language=None):
        r"""ListHistoryWaitEventsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param start_time: 参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。
        :type start_time: int
        :param end_time: 参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。
        :type end_time: int
        :param offset: 参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，值为0表示从第一条数据开始查询）。 约束限制： 必须为数字，不能为负数。 取值范围： 大于等于0的整数。 默认取值： 0
        :type offset: int
        :param limit: 参数解释： 查询记录数。 约束限制： 不涉及。 取值范围： [1, 1000] 默认取值： 100
        :type limit: int
        :param x_language: 语言。默认en-us。
        :type x_language: str
        """
        
        

        self._instance_id = None
        self._start_time = None
        self._end_time = None
        self._offset = None
        self._limit = None
        self._x_language = None
        self.discriminator = None

        self.instance_id = instance_id
        self.start_time = start_time
        self.end_time = end_time
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if x_language is not None:
            self.x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListHistoryWaitEventsRequest.

        实例ID

        :return: The instance_id of this ListHistoryWaitEventsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListHistoryWaitEventsRequest.

        实例ID

        :param instance_id: The instance_id of this ListHistoryWaitEventsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def start_time(self):
        r"""Gets the start_time of this ListHistoryWaitEventsRequest.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :return: The start_time of this ListHistoryWaitEventsRequest.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ListHistoryWaitEventsRequest.

        参数解释： 开始时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :param start_time: The start_time of this ListHistoryWaitEventsRequest.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ListHistoryWaitEventsRequest.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :return: The end_time of this ListHistoryWaitEventsRequest.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ListHistoryWaitEventsRequest.

        参数解释： 结束时间。 格式为UTC时间戳。 取值范围： 不涉及。 默认取值： 不涉及。

        :param end_time: The end_time of this ListHistoryWaitEventsRequest.
        :type end_time: int
        """
        self._end_time = end_time

    @property
    def offset(self):
        r"""Gets the offset of this ListHistoryWaitEventsRequest.

        参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，值为0表示从第一条数据开始查询）。 约束限制： 必须为数字，不能为负数。 取值范围： 大于等于0的整数。 默认取值： 0

        :return: The offset of this ListHistoryWaitEventsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListHistoryWaitEventsRequest.

        参数解释： 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询，值为0表示从第一条数据开始查询）。 约束限制： 必须为数字，不能为负数。 取值范围： 大于等于0的整数。 默认取值： 0

        :param offset: The offset of this ListHistoryWaitEventsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListHistoryWaitEventsRequest.

        参数解释： 查询记录数。 约束限制： 不涉及。 取值范围： [1, 1000] 默认取值： 100

        :return: The limit of this ListHistoryWaitEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListHistoryWaitEventsRequest.

        参数解释： 查询记录数。 约束限制： 不涉及。 取值范围： [1, 1000] 默认取值： 100

        :param limit: The limit of this ListHistoryWaitEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListHistoryWaitEventsRequest.

        语言。默认en-us。

        :return: The x_language of this ListHistoryWaitEventsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListHistoryWaitEventsRequest.

        语言。默认en-us。

        :param x_language: The x_language of this ListHistoryWaitEventsRequest.
        :type x_language: str
        """
        self._x_language = x_language

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
        if not isinstance(other, ListHistoryWaitEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
