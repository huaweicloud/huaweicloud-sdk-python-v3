# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BotRequestTimeline:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datetime': 'int',
        'normal_request_count': 'int',
        'known_bot_matched_count': 'int',
        'transparent_matched_count': 'int',
        'behavior_matched_count': 'int'
    }

    attribute_map = {
        'datetime': 'datetime',
        'normal_request_count': 'normal_request_count',
        'known_bot_matched_count': 'known_bot_matched_count',
        'transparent_matched_count': 'transparent_matched_count',
        'behavior_matched_count': 'behavior_matched_count'
    }

    def __init__(self, datetime=None, normal_request_count=None, known_bot_matched_count=None, transparent_matched_count=None, behavior_matched_count=None):
        r"""BotRequestTimeline

        The model defined in huaweicloud sdk

        :param datetime: **参数解释：** 时间点（如2023-10-01 00:00:00） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type datetime: int
        :param normal_request_count: **参数解释：** 该时间点的正常请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type normal_request_count: int
        :param known_bot_matched_count: **参数解释：** 该时间点匹配已知bot的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type known_bot_matched_count: int
        :param transparent_matched_count: **参数解释：** 该时间点透明检测的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type transparent_matched_count: int
        :param behavior_matched_count: **参数解释：** 该时间点行为检测的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0
        :type behavior_matched_count: int
        """
        
        

        self._datetime = None
        self._normal_request_count = None
        self._known_bot_matched_count = None
        self._transparent_matched_count = None
        self._behavior_matched_count = None
        self.discriminator = None

        if datetime is not None:
            self.datetime = datetime
        if normal_request_count is not None:
            self.normal_request_count = normal_request_count
        if known_bot_matched_count is not None:
            self.known_bot_matched_count = known_bot_matched_count
        if transparent_matched_count is not None:
            self.transparent_matched_count = transparent_matched_count
        if behavior_matched_count is not None:
            self.behavior_matched_count = behavior_matched_count

    @property
    def datetime(self):
        r"""Gets the datetime of this BotRequestTimeline.

        **参数解释：** 时间点（如2023-10-01 00:00:00） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The datetime of this BotRequestTimeline.
        :rtype: int
        """
        return self._datetime

    @datetime.setter
    def datetime(self, datetime):
        r"""Sets the datetime of this BotRequestTimeline.

        **参数解释：** 时间点（如2023-10-01 00:00:00） **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param datetime: The datetime of this BotRequestTimeline.
        :type datetime: int
        """
        self._datetime = datetime

    @property
    def normal_request_count(self):
        r"""Gets the normal_request_count of this BotRequestTimeline.

        **参数解释：** 该时间点的正常请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The normal_request_count of this BotRequestTimeline.
        :rtype: int
        """
        return self._normal_request_count

    @normal_request_count.setter
    def normal_request_count(self, normal_request_count):
        r"""Sets the normal_request_count of this BotRequestTimeline.

        **参数解释：** 该时间点的正常请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param normal_request_count: The normal_request_count of this BotRequestTimeline.
        :type normal_request_count: int
        """
        self._normal_request_count = normal_request_count

    @property
    def known_bot_matched_count(self):
        r"""Gets the known_bot_matched_count of this BotRequestTimeline.

        **参数解释：** 该时间点匹配已知bot的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The known_bot_matched_count of this BotRequestTimeline.
        :rtype: int
        """
        return self._known_bot_matched_count

    @known_bot_matched_count.setter
    def known_bot_matched_count(self, known_bot_matched_count):
        r"""Sets the known_bot_matched_count of this BotRequestTimeline.

        **参数解释：** 该时间点匹配已知bot的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param known_bot_matched_count: The known_bot_matched_count of this BotRequestTimeline.
        :type known_bot_matched_count: int
        """
        self._known_bot_matched_count = known_bot_matched_count

    @property
    def transparent_matched_count(self):
        r"""Gets the transparent_matched_count of this BotRequestTimeline.

        **参数解释：** 该时间点透明检测的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The transparent_matched_count of this BotRequestTimeline.
        :rtype: int
        """
        return self._transparent_matched_count

    @transparent_matched_count.setter
    def transparent_matched_count(self, transparent_matched_count):
        r"""Sets the transparent_matched_count of this BotRequestTimeline.

        **参数解释：** 该时间点透明检测的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param transparent_matched_count: The transparent_matched_count of this BotRequestTimeline.
        :type transparent_matched_count: int
        """
        self._transparent_matched_count = transparent_matched_count

    @property
    def behavior_matched_count(self):
        r"""Gets the behavior_matched_count of this BotRequestTimeline.

        **参数解释：** 该时间点行为检测的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :return: The behavior_matched_count of this BotRequestTimeline.
        :rtype: int
        """
        return self._behavior_matched_count

    @behavior_matched_count.setter
    def behavior_matched_count(self, behavior_matched_count):
        r"""Sets the behavior_matched_count of this BotRequestTimeline.

        **参数解释：** 该时间点行为检测的请求数量 **约束限制：** 不涉及 **取值范围：** ≥0 **默认取值：** 0

        :param behavior_matched_count: The behavior_matched_count of this BotRequestTimeline.
        :type behavior_matched_count: int
        """
        self._behavior_matched_count = behavior_matched_count

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
        if not isinstance(other, BotRequestTimeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
