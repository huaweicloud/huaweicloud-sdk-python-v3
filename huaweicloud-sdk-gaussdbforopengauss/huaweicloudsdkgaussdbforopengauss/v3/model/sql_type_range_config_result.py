# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SqlTypeRangeConfigResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_open': 'bool',
        'begin_time': 'str'
    }

    attribute_map = {
        'is_open': 'is_open',
        'begin_time': 'begin_time'
    }

    def __init__(self, is_open=None, begin_time=None):
        r"""SqlTypeRangeConfigResult

        The model defined in huaweicloud sdk

        :param is_open: **参数解释**: 是否开启全量SQL。 **取值范围**: - true：已开启。 - false：已关闭。
        :type is_open: bool
        :param begin_time: **参数解释**: 开关状态持续的开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 不涉及。
        :type begin_time: str
        """
        
        

        self._is_open = None
        self._begin_time = None
        self.discriminator = None

        if is_open is not None:
            self.is_open = is_open
        if begin_time is not None:
            self.begin_time = begin_time

    @property
    def is_open(self):
        r"""Gets the is_open of this SqlTypeRangeConfigResult.

        **参数解释**: 是否开启全量SQL。 **取值范围**: - true：已开启。 - false：已关闭。

        :return: The is_open of this SqlTypeRangeConfigResult.
        :rtype: bool
        """
        return self._is_open

    @is_open.setter
    def is_open(self, is_open):
        r"""Sets the is_open of this SqlTypeRangeConfigResult.

        **参数解释**: 是否开启全量SQL。 **取值范围**: - true：已开启。 - false：已关闭。

        :param is_open: The is_open of this SqlTypeRangeConfigResult.
        :type is_open: bool
        """
        self._is_open = is_open

    @property
    def begin_time(self):
        r"""Gets the begin_time of this SqlTypeRangeConfigResult.

        **参数解释**: 开关状态持续的开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 不涉及。

        :return: The begin_time of this SqlTypeRangeConfigResult.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this SqlTypeRangeConfigResult.

        **参数解释**: 开关状态持续的开始时间。格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量。 **取值范围**: 不涉及。

        :param begin_time: The begin_time of this SqlTypeRangeConfigResult.
        :type begin_time: str
        """
        self._begin_time = begin_time

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
        if not isinstance(other, SqlTypeRangeConfigResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
