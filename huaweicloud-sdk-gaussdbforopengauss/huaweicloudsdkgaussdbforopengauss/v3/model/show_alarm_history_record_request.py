# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlarmHistoryRecordRequest:

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
        'start_time': 'str',
        'offset': 'int',
        'limit': 'int',
        'level': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'start_time': 'start_time',
        'offset': 'offset',
        'limit': 'limit',
        'level': 'level'
    }

    def __init__(self, x_language=None, start_time=None, offset=None, limit=None, level=None):
        r"""ShowAlarmHistoryRecordRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param start_time: **参数解释**: 查询开始时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。最多可以获取最近7天的数据。 **默认取值**: 不涉及。
        :type start_time: str
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2-11条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 2^31-1] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param limit: **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 50] **默认取值**: 50
        :type limit: int
        :param level: **参数解释**: 实例告警等级。 **约束限制**: 不涉及。 **取值范围**: - 1：紧急。 - 2：重要。 - 3：次要。 - 4：提示。  **默认取值**: 1
        :type level: int
        """
        
        

        self._x_language = None
        self._start_time = None
        self._offset = None
        self._limit = None
        self._level = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.start_time = start_time
        self.offset = offset
        self.limit = limit
        if level is not None:
            self.level = level

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ShowAlarmHistoryRecordRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ShowAlarmHistoryRecordRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 查询开始时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。最多可以获取最近7天的数据。 **默认取值**: 不涉及。

        :return: The start_time of this ShowAlarmHistoryRecordRequest.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 查询开始时间。 **约束限制**: 不涉及。 **取值范围**: 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。最多可以获取最近7天的数据。 **默认取值**: 不涉及。

        :param start_time: The start_time of this ShowAlarmHistoryRecordRequest.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def offset(self):
        r"""Gets the offset of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2-11条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 2^31-1] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ShowAlarmHistoryRecordRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。例如：该参数指定为1，limit指定为10，则只展示第2-11条数据。 **约束限制**: 不涉及。 **取值范围**: [0, 2^31-1] **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ShowAlarmHistoryRecordRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 50] **默认取值**: 50

        :return: The limit of this ShowAlarmHistoryRecordRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 查询记录数。例如该参数设定为10，则查询结果最多只显示10条记录。 **约束限制**: 不涉及。 **取值范围**: [1, 50] **默认取值**: 50

        :param limit: The limit of this ShowAlarmHistoryRecordRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def level(self):
        r"""Gets the level of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 实例告警等级。 **约束限制**: 不涉及。 **取值范围**: - 1：紧急。 - 2：重要。 - 3：次要。 - 4：提示。  **默认取值**: 1

        :return: The level of this ShowAlarmHistoryRecordRequest.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this ShowAlarmHistoryRecordRequest.

        **参数解释**: 实例告警等级。 **约束限制**: 不涉及。 **取值范围**: - 1：紧急。 - 2：重要。 - 3：次要。 - 4：提示。  **默认取值**: 1

        :param level: The level of this ShowAlarmHistoryRecordRequest.
        :type level: int
        """
        self._level = level

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowAlarmHistoryRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
