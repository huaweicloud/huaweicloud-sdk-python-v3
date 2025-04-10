# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'action': 'HttpPolicyAction',
        'options': 'HttpPolicyOption',
        'level': 'int',
        'full_detection': 'bool',
        'robot_action': 'HttpPolicyAction',
        'third_bot_options': 'HttpThirdBotOptions',
        'extend': 'dict(str, str)'
    }

    attribute_map = {
        'name': 'name',
        'action': 'action',
        'options': 'options',
        'level': 'level',
        'full_detection': 'full_detection',
        'robot_action': 'robot_action',
        'third_bot_options': 'third_bot_options',
        'extend': 'extend'
    }

    def __init__(self, name=None, action=None, options=None, level=None, full_detection=None, robot_action=None, third_bot_options=None, extend=None):
        r"""UpdateHttpPolicyRequestBody

        The model defined in huaweicloud sdk

        :param name: 防护策略名
        :type name: str
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        :param options: 
        :type options: :class:`huaweicloudsdkedgesec.v2.HttpPolicyOption`
        :param level: 防护等级
        :type level: int
        :param full_detection: 精准防护中的检测模式
        :type full_detection: bool
        :param robot_action: 
        :type robot_action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        :param third_bot_options: 
        :type third_bot_options: :class:`huaweicloudsdkedgesec.v2.HttpThirdBotOptions`
        :param extend: 扩展字段
        :type extend: dict(str, str)
        """
        
        

        self._name = None
        self._action = None
        self._options = None
        self._level = None
        self._full_detection = None
        self._robot_action = None
        self._third_bot_options = None
        self._extend = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if action is not None:
            self.action = action
        if options is not None:
            self.options = options
        if level is not None:
            self.level = level
        if full_detection is not None:
            self.full_detection = full_detection
        if robot_action is not None:
            self.robot_action = robot_action
        if third_bot_options is not None:
            self.third_bot_options = third_bot_options
        if extend is not None:
            self.extend = extend

    @property
    def name(self):
        r"""Gets the name of this UpdateHttpPolicyRequestBody.

        防护策略名

        :return: The name of this UpdateHttpPolicyRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateHttpPolicyRequestBody.

        防护策略名

        :param name: The name of this UpdateHttpPolicyRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        r"""Gets the action of this UpdateHttpPolicyRequestBody.

        :return: The action of this UpdateHttpPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this UpdateHttpPolicyRequestBody.

        :param action: The action of this UpdateHttpPolicyRequestBody.
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        self._action = action

    @property
    def options(self):
        r"""Gets the options of this UpdateHttpPolicyRequestBody.

        :return: The options of this UpdateHttpPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpPolicyOption`
        """
        return self._options

    @options.setter
    def options(self, options):
        r"""Sets the options of this UpdateHttpPolicyRequestBody.

        :param options: The options of this UpdateHttpPolicyRequestBody.
        :type options: :class:`huaweicloudsdkedgesec.v2.HttpPolicyOption`
        """
        self._options = options

    @property
    def level(self):
        r"""Gets the level of this UpdateHttpPolicyRequestBody.

        防护等级

        :return: The level of this UpdateHttpPolicyRequestBody.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this UpdateHttpPolicyRequestBody.

        防护等级

        :param level: The level of this UpdateHttpPolicyRequestBody.
        :type level: int
        """
        self._level = level

    @property
    def full_detection(self):
        r"""Gets the full_detection of this UpdateHttpPolicyRequestBody.

        精准防护中的检测模式

        :return: The full_detection of this UpdateHttpPolicyRequestBody.
        :rtype: bool
        """
        return self._full_detection

    @full_detection.setter
    def full_detection(self, full_detection):
        r"""Sets the full_detection of this UpdateHttpPolicyRequestBody.

        精准防护中的检测模式

        :param full_detection: The full_detection of this UpdateHttpPolicyRequestBody.
        :type full_detection: bool
        """
        self._full_detection = full_detection

    @property
    def robot_action(self):
        r"""Gets the robot_action of this UpdateHttpPolicyRequestBody.

        :return: The robot_action of this UpdateHttpPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        return self._robot_action

    @robot_action.setter
    def robot_action(self, robot_action):
        r"""Sets the robot_action of this UpdateHttpPolicyRequestBody.

        :param robot_action: The robot_action of this UpdateHttpPolicyRequestBody.
        :type robot_action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        self._robot_action = robot_action

    @property
    def third_bot_options(self):
        r"""Gets the third_bot_options of this UpdateHttpPolicyRequestBody.

        :return: The third_bot_options of this UpdateHttpPolicyRequestBody.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpThirdBotOptions`
        """
        return self._third_bot_options

    @third_bot_options.setter
    def third_bot_options(self, third_bot_options):
        r"""Sets the third_bot_options of this UpdateHttpPolicyRequestBody.

        :param third_bot_options: The third_bot_options of this UpdateHttpPolicyRequestBody.
        :type third_bot_options: :class:`huaweicloudsdkedgesec.v2.HttpThirdBotOptions`
        """
        self._third_bot_options = third_bot_options

    @property
    def extend(self):
        r"""Gets the extend of this UpdateHttpPolicyRequestBody.

        扩展字段

        :return: The extend of this UpdateHttpPolicyRequestBody.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        r"""Sets the extend of this UpdateHttpPolicyRequestBody.

        扩展字段

        :param extend: The extend of this UpdateHttpPolicyRequestBody.
        :type extend: dict(str, str)
        """
        self._extend = extend

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
        if not isinstance(other, UpdateHttpPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
