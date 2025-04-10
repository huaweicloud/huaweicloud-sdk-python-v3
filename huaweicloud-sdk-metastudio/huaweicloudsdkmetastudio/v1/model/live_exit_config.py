# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveExitConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'max_live_duration': 'int',
        'auto_stop_mode': 'str',
        'max_exception_waiting_duration': 'int'
    }

    attribute_map = {
        'max_live_duration': 'max_live_duration',
        'auto_stop_mode': 'auto_stop_mode',
        'max_exception_waiting_duration': 'max_exception_waiting_duration'
    }

    def __init__(self, max_live_duration=None, auto_stop_mode=None, max_exception_waiting_duration=None):
        r"""LiveExitConfig

        The model defined in huaweicloud sdk

        :param max_live_duration: **参数解释**： 最大直播时长。单位小时。 此数值配置为n，则标识起播后n小时后触发停止直播逻辑。 当前数值最大为168（一周），特殊的，0表示不限时。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。
        :type max_live_duration: int
        :param auto_stop_mode: **参数解释**： 自动停止直播模式。 * FORCE_EXIT：立即强制停止，不做其他逻辑处理。 * SEGMENT_END:等待段落结束停止。 * SCENE_END：等待场景结束停止。 * SCRIPT_END：等待剧本结束停止。 **约束限制**： 不涉及 **默认取值**： 不设置则表示FORCE_EXIT。
        :type auto_stop_mode: str
        :param max_exception_waiting_duration: **参数解释**： 最大异常等待时长。单位分钟。  此数值配置为n，则标识检测到异常n分钟后触发立即停止直播逻辑。 当前数值最大为60（1小时），特殊的，0表示不限时。 **约束限制**： 不涉及 **默认取值**： 不设置则为系统默认值，当前为3分钟，默认值可能会根据服务运行状态进行少许调整。
        :type max_exception_waiting_duration: int
        """
        
        

        self._max_live_duration = None
        self._auto_stop_mode = None
        self._max_exception_waiting_duration = None
        self.discriminator = None

        if max_live_duration is not None:
            self.max_live_duration = max_live_duration
        if auto_stop_mode is not None:
            self.auto_stop_mode = auto_stop_mode
        if max_exception_waiting_duration is not None:
            self.max_exception_waiting_duration = max_exception_waiting_duration

    @property
    def max_live_duration(self):
        r"""Gets the max_live_duration of this LiveExitConfig.

        **参数解释**： 最大直播时长。单位小时。 此数值配置为n，则标识起播后n小时后触发停止直播逻辑。 当前数值最大为168（一周），特殊的，0表示不限时。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。

        :return: The max_live_duration of this LiveExitConfig.
        :rtype: int
        """
        return self._max_live_duration

    @max_live_duration.setter
    def max_live_duration(self, max_live_duration):
        r"""Sets the max_live_duration of this LiveExitConfig.

        **参数解释**： 最大直播时长。单位小时。 此数值配置为n，则标识起播后n小时后触发停止直播逻辑。 当前数值最大为168（一周），特殊的，0表示不限时。 **约束限制**： 停止直播逻辑配置为立即停止则直播停止误差在5分钟之内。其他逻辑则加上处理时长。 **默认取值**： 不设置则表示不限时。

        :param max_live_duration: The max_live_duration of this LiveExitConfig.
        :type max_live_duration: int
        """
        self._max_live_duration = max_live_duration

    @property
    def auto_stop_mode(self):
        r"""Gets the auto_stop_mode of this LiveExitConfig.

        **参数解释**： 自动停止直播模式。 * FORCE_EXIT：立即强制停止，不做其他逻辑处理。 * SEGMENT_END:等待段落结束停止。 * SCENE_END：等待场景结束停止。 * SCRIPT_END：等待剧本结束停止。 **约束限制**： 不涉及 **默认取值**： 不设置则表示FORCE_EXIT。

        :return: The auto_stop_mode of this LiveExitConfig.
        :rtype: str
        """
        return self._auto_stop_mode

    @auto_stop_mode.setter
    def auto_stop_mode(self, auto_stop_mode):
        r"""Sets the auto_stop_mode of this LiveExitConfig.

        **参数解释**： 自动停止直播模式。 * FORCE_EXIT：立即强制停止，不做其他逻辑处理。 * SEGMENT_END:等待段落结束停止。 * SCENE_END：等待场景结束停止。 * SCRIPT_END：等待剧本结束停止。 **约束限制**： 不涉及 **默认取值**： 不设置则表示FORCE_EXIT。

        :param auto_stop_mode: The auto_stop_mode of this LiveExitConfig.
        :type auto_stop_mode: str
        """
        self._auto_stop_mode = auto_stop_mode

    @property
    def max_exception_waiting_duration(self):
        r"""Gets the max_exception_waiting_duration of this LiveExitConfig.

        **参数解释**： 最大异常等待时长。单位分钟。  此数值配置为n，则标识检测到异常n分钟后触发立即停止直播逻辑。 当前数值最大为60（1小时），特殊的，0表示不限时。 **约束限制**： 不涉及 **默认取值**： 不设置则为系统默认值，当前为3分钟，默认值可能会根据服务运行状态进行少许调整。

        :return: The max_exception_waiting_duration of this LiveExitConfig.
        :rtype: int
        """
        return self._max_exception_waiting_duration

    @max_exception_waiting_duration.setter
    def max_exception_waiting_duration(self, max_exception_waiting_duration):
        r"""Sets the max_exception_waiting_duration of this LiveExitConfig.

        **参数解释**： 最大异常等待时长。单位分钟。  此数值配置为n，则标识检测到异常n分钟后触发立即停止直播逻辑。 当前数值最大为60（1小时），特殊的，0表示不限时。 **约束限制**： 不涉及 **默认取值**： 不设置则为系统默认值，当前为3分钟，默认值可能会根据服务运行状态进行少许调整。

        :param max_exception_waiting_duration: The max_exception_waiting_duration of this LiveExitConfig.
        :type max_exception_waiting_duration: int
        """
        self._max_exception_waiting_duration = max_exception_waiting_duration

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
        if not isinstance(other, LiveExitConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
