# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHttpPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'level': 'int',
        'full_detection': 'bool',
        'action': 'HttpPolicyAction',
        'robot_action': 'HttpPolicyAction',
        'options': 'HttpPolicyOption',
        'bind_host': 'list[HttpPolicyBindHost]',
        'extend': 'dict(str, str)',
        'third_bot_options': 'dict(str, object)',
        'wap_managed_ruleset_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'level': 'level',
        'full_detection': 'full_detection',
        'action': 'action',
        'robot_action': 'robot_action',
        'options': 'options',
        'bind_host': 'bind_host',
        'extend': 'extend',
        'third_bot_options': 'third_bot_options',
        'wap_managed_ruleset_id': 'wap_managed_ruleset_id'
    }

    def __init__(self, id=None, name=None, level=None, full_detection=None, action=None, robot_action=None, options=None, bind_host=None, extend=None, third_bot_options=None, wap_managed_ruleset_id=None):
        """UpdateHttpPolicyResponse

        The model defined in huaweicloud sdk

        :param id: 防护策略id
        :type id: str
        :param name: 防护策略名
        :type name: str
        :param level: 防护等级
        :type level: int
        :param full_detection: 精准防护中的检测模式
        :type full_detection: bool
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        :param robot_action: 
        :type robot_action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        :param options: 
        :type options: :class:`huaweicloudsdkedgesec.v2.HttpPolicyOption`
        :param bind_host: 防护域名的信息
        :type bind_host: list[:class:`huaweicloudsdkedgesec.v2.HttpPolicyBindHost`]
        :param extend: 扩展字段
        :type extend: dict(str, str)
        :param third_bot_options: 三方BOT操作
        :type third_bot_options: dict(str, object)
        :param wap_managed_ruleset_id: web基础防护托管规则集id
        :type wap_managed_ruleset_id: str
        """
        
        super(UpdateHttpPolicyResponse, self).__init__()

        self._id = None
        self._name = None
        self._level = None
        self._full_detection = None
        self._action = None
        self._robot_action = None
        self._options = None
        self._bind_host = None
        self._extend = None
        self._third_bot_options = None
        self._wap_managed_ruleset_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if level is not None:
            self.level = level
        if full_detection is not None:
            self.full_detection = full_detection
        if action is not None:
            self.action = action
        if robot_action is not None:
            self.robot_action = robot_action
        if options is not None:
            self.options = options
        if bind_host is not None:
            self.bind_host = bind_host
        if extend is not None:
            self.extend = extend
        if third_bot_options is not None:
            self.third_bot_options = third_bot_options
        if wap_managed_ruleset_id is not None:
            self.wap_managed_ruleset_id = wap_managed_ruleset_id

    @property
    def id(self):
        """Gets the id of this UpdateHttpPolicyResponse.

        防护策略id

        :return: The id of this UpdateHttpPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdateHttpPolicyResponse.

        防护策略id

        :param id: The id of this UpdateHttpPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdateHttpPolicyResponse.

        防护策略名

        :return: The name of this UpdateHttpPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateHttpPolicyResponse.

        防护策略名

        :param name: The name of this UpdateHttpPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def level(self):
        """Gets the level of this UpdateHttpPolicyResponse.

        防护等级

        :return: The level of this UpdateHttpPolicyResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdateHttpPolicyResponse.

        防护等级

        :param level: The level of this UpdateHttpPolicyResponse.
        :type level: int
        """
        self._level = level

    @property
    def full_detection(self):
        """Gets the full_detection of this UpdateHttpPolicyResponse.

        精准防护中的检测模式

        :return: The full_detection of this UpdateHttpPolicyResponse.
        :rtype: bool
        """
        return self._full_detection

    @full_detection.setter
    def full_detection(self, full_detection):
        """Sets the full_detection of this UpdateHttpPolicyResponse.

        精准防护中的检测模式

        :param full_detection: The full_detection of this UpdateHttpPolicyResponse.
        :type full_detection: bool
        """
        self._full_detection = full_detection

    @property
    def action(self):
        """Gets the action of this UpdateHttpPolicyResponse.

        :return: The action of this UpdateHttpPolicyResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdateHttpPolicyResponse.

        :param action: The action of this UpdateHttpPolicyResponse.
        :type action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        self._action = action

    @property
    def robot_action(self):
        """Gets the robot_action of this UpdateHttpPolicyResponse.

        :return: The robot_action of this UpdateHttpPolicyResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        return self._robot_action

    @robot_action.setter
    def robot_action(self, robot_action):
        """Sets the robot_action of this UpdateHttpPolicyResponse.

        :param robot_action: The robot_action of this UpdateHttpPolicyResponse.
        :type robot_action: :class:`huaweicloudsdkedgesec.v2.HttpPolicyAction`
        """
        self._robot_action = robot_action

    @property
    def options(self):
        """Gets the options of this UpdateHttpPolicyResponse.

        :return: The options of this UpdateHttpPolicyResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpPolicyOption`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this UpdateHttpPolicyResponse.

        :param options: The options of this UpdateHttpPolicyResponse.
        :type options: :class:`huaweicloudsdkedgesec.v2.HttpPolicyOption`
        """
        self._options = options

    @property
    def bind_host(self):
        """Gets the bind_host of this UpdateHttpPolicyResponse.

        防护域名的信息

        :return: The bind_host of this UpdateHttpPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v2.HttpPolicyBindHost`]
        """
        return self._bind_host

    @bind_host.setter
    def bind_host(self, bind_host):
        """Sets the bind_host of this UpdateHttpPolicyResponse.

        防护域名的信息

        :param bind_host: The bind_host of this UpdateHttpPolicyResponse.
        :type bind_host: list[:class:`huaweicloudsdkedgesec.v2.HttpPolicyBindHost`]
        """
        self._bind_host = bind_host

    @property
    def extend(self):
        """Gets the extend of this UpdateHttpPolicyResponse.

        扩展字段

        :return: The extend of this UpdateHttpPolicyResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdateHttpPolicyResponse.

        扩展字段

        :param extend: The extend of this UpdateHttpPolicyResponse.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def third_bot_options(self):
        """Gets the third_bot_options of this UpdateHttpPolicyResponse.

        三方BOT操作

        :return: The third_bot_options of this UpdateHttpPolicyResponse.
        :rtype: dict(str, object)
        """
        return self._third_bot_options

    @third_bot_options.setter
    def third_bot_options(self, third_bot_options):
        """Sets the third_bot_options of this UpdateHttpPolicyResponse.

        三方BOT操作

        :param third_bot_options: The third_bot_options of this UpdateHttpPolicyResponse.
        :type third_bot_options: dict(str, object)
        """
        self._third_bot_options = third_bot_options

    @property
    def wap_managed_ruleset_id(self):
        """Gets the wap_managed_ruleset_id of this UpdateHttpPolicyResponse.

        web基础防护托管规则集id

        :return: The wap_managed_ruleset_id of this UpdateHttpPolicyResponse.
        :rtype: str
        """
        return self._wap_managed_ruleset_id

    @wap_managed_ruleset_id.setter
    def wap_managed_ruleset_id(self, wap_managed_ruleset_id):
        """Sets the wap_managed_ruleset_id of this UpdateHttpPolicyResponse.

        web基础防护托管规则集id

        :param wap_managed_ruleset_id: The wap_managed_ruleset_id of this UpdateHttpPolicyResponse.
        :type wap_managed_ruleset_id: str
        """
        self._wap_managed_ruleset_id = wap_managed_ruleset_id

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
        if not isinstance(other, UpdateHttpPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
