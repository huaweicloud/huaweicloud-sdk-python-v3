# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectWdrSnapshotRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'str',
        'end_time': 'str',
        'wdr_type': 'list[str]'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time',
        'wdr_type': 'wdr_type'
    }

    def __init__(self, start_time=None, end_time=None, wdr_type=None):
        r"""CollectWdrSnapshotRequestBody

        The model defined in huaweicloud sdk

        :param start_time: **参数解释**： 快照开始时间。 **约束限制**： 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type start_time: str
        :param end_time: **参数解释**： 快照结束时间。 **约束限制**： 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type end_time: str
        :param wdr_type: **参数解释**： 采集类型，包括实例级和组件级。 **约束限制**： 实例级则需要输入\&quot;cluster\&quot;,组件级则需要输入组件ID。实例级和组件级无法同时输入。
        :type wdr_type: list[str]
        """
        
        

        self._start_time = None
        self._end_time = None
        self._wdr_type = None
        self.discriminator = None

        self.start_time = start_time
        self.end_time = end_time
        self.wdr_type = wdr_type

    @property
    def start_time(self):
        r"""Gets the start_time of this CollectWdrSnapshotRequestBody.

        **参数解释**： 快照开始时间。 **约束限制**： 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The start_time of this CollectWdrSnapshotRequestBody.
        :rtype: str
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this CollectWdrSnapshotRequestBody.

        **参数解释**： 快照开始时间。 **约束限制**： 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param start_time: The start_time of this CollectWdrSnapshotRequestBody.
        :type start_time: str
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this CollectWdrSnapshotRequestBody.

        **参数解释**： 快照结束时间。 **约束限制**： 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The end_time of this CollectWdrSnapshotRequestBody.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this CollectWdrSnapshotRequestBody.

        **参数解释**： 快照结束时间。 **约束限制**： 格式为“yyyy-mm-ddThh:mm:ssZ”。其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param end_time: The end_time of this CollectWdrSnapshotRequestBody.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def wdr_type(self):
        r"""Gets the wdr_type of this CollectWdrSnapshotRequestBody.

        **参数解释**： 采集类型，包括实例级和组件级。 **约束限制**： 实例级则需要输入\"cluster\",组件级则需要输入组件ID。实例级和组件级无法同时输入。

        :return: The wdr_type of this CollectWdrSnapshotRequestBody.
        :rtype: list[str]
        """
        return self._wdr_type

    @wdr_type.setter
    def wdr_type(self, wdr_type):
        r"""Sets the wdr_type of this CollectWdrSnapshotRequestBody.

        **参数解释**： 采集类型，包括实例级和组件级。 **约束限制**： 实例级则需要输入\"cluster\",组件级则需要输入组件ID。实例级和组件级无法同时输入。

        :param wdr_type: The wdr_type of this CollectWdrSnapshotRequestBody.
        :type wdr_type: list[str]
        """
        self._wdr_type = wdr_type

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
        if not isinstance(other, CollectWdrSnapshotRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
