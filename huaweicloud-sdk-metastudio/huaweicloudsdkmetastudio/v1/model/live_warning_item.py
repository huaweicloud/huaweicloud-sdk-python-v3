# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveWarningItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'warning_type': 'str'
    }

    attribute_map = {
        'warning_type': 'warning_type'
    }

    def __init__(self, warning_type=None):
        r"""LiveWarningItem

        The model defined in huaweicloud sdk

        :param warning_type: 告警类型。 - TOO_LESSS_SCRIPT_ITEMS：段落（话术）数量太少。 - TOO_SHORT_SCRIPT_TIME：段落（话术）总时长太短。 - TOO_LESS_DANMAKU_RULES： 弹幕互动规则太少。 - RANDOM_PLAY_CLOSED: 随机播放开关关闭。 - ROTATION_MODEL_CLOSED: 主播轮转未配置。
        :type warning_type: str
        """
        
        

        self._warning_type = None
        self.discriminator = None

        if warning_type is not None:
            self.warning_type = warning_type

    @property
    def warning_type(self):
        r"""Gets the warning_type of this LiveWarningItem.

        告警类型。 - TOO_LESSS_SCRIPT_ITEMS：段落（话术）数量太少。 - TOO_SHORT_SCRIPT_TIME：段落（话术）总时长太短。 - TOO_LESS_DANMAKU_RULES： 弹幕互动规则太少。 - RANDOM_PLAY_CLOSED: 随机播放开关关闭。 - ROTATION_MODEL_CLOSED: 主播轮转未配置。

        :return: The warning_type of this LiveWarningItem.
        :rtype: str
        """
        return self._warning_type

    @warning_type.setter
    def warning_type(self, warning_type):
        r"""Sets the warning_type of this LiveWarningItem.

        告警类型。 - TOO_LESSS_SCRIPT_ITEMS：段落（话术）数量太少。 - TOO_SHORT_SCRIPT_TIME：段落（话术）总时长太短。 - TOO_LESS_DANMAKU_RULES： 弹幕互动规则太少。 - RANDOM_PLAY_CLOSED: 随机播放开关关闭。 - ROTATION_MODEL_CLOSED: 主播轮转未配置。

        :param warning_type: The warning_type of this LiveWarningItem.
        :type warning_type: str
        """
        self._warning_type = warning_type

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
        if not isinstance(other, LiveWarningItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
