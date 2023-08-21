# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApplyWafPolicyResponse(SdkResponse):

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
        'action': 'WafPolicyAction',
        'options': 'WafPolicyOption',
        'level': 'int',
        'full_detection': 'bool',
        'robot_action': 'WafPolicyAction',
        'bind_host': 'list[WafPolicyBindHost]',
        'timestamp': 'int',
        'extend': 'dict(str, str)'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'action': 'action',
        'options': 'options',
        'level': 'level',
        'full_detection': 'full_detection',
        'robot_action': 'robot_action',
        'bind_host': 'bind_host',
        'timestamp': 'timestamp',
        'extend': 'extend'
    }

    def __init__(self, id=None, name=None, action=None, options=None, level=None, full_detection=None, robot_action=None, bind_host=None, timestamp=None, extend=None):
        """ApplyWafPolicyResponse

        The model defined in huaweicloud sdk

        :param id: 防护策略id
        :type id: str
        :param name: 防护策略名
        :type name: str
        :param action: 
        :type action: :class:`huaweicloudsdkedgesec.v1.WafPolicyAction`
        :param options: 
        :type options: :class:`huaweicloudsdkedgesec.v1.WafPolicyOption`
        :param level: 防护等级
        :type level: int
        :param full_detection: 精准防护中的检测模式
        :type full_detection: bool
        :param robot_action: 
        :type robot_action: :class:`huaweicloudsdkedgesec.v1.WafPolicyAction`
        :param bind_host: 防护域名的信息
        :type bind_host: list[:class:`huaweicloudsdkedgesec.v1.WafPolicyBindHost`]
        :param timestamp: 创建防护策略的时间
        :type timestamp: int
        :param extend: 扩展字段
        :type extend: dict(str, str)
        """
        
        super(ApplyWafPolicyResponse, self).__init__()

        self._id = None
        self._name = None
        self._action = None
        self._options = None
        self._level = None
        self._full_detection = None
        self._robot_action = None
        self._bind_host = None
        self._timestamp = None
        self._extend = None
        self.discriminator = None

        if id is not None:
            self.id = id
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
        if bind_host is not None:
            self.bind_host = bind_host
        if timestamp is not None:
            self.timestamp = timestamp
        if extend is not None:
            self.extend = extend

    @property
    def id(self):
        """Gets the id of this ApplyWafPolicyResponse.

        防护策略id

        :return: The id of this ApplyWafPolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ApplyWafPolicyResponse.

        防护策略id

        :param id: The id of this ApplyWafPolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ApplyWafPolicyResponse.

        防护策略名

        :return: The name of this ApplyWafPolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplyWafPolicyResponse.

        防护策略名

        :param name: The name of this ApplyWafPolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def action(self):
        """Gets the action of this ApplyWafPolicyResponse.

        :return: The action of this ApplyWafPolicyResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafPolicyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this ApplyWafPolicyResponse.

        :param action: The action of this ApplyWafPolicyResponse.
        :type action: :class:`huaweicloudsdkedgesec.v1.WafPolicyAction`
        """
        self._action = action

    @property
    def options(self):
        """Gets the options of this ApplyWafPolicyResponse.

        :return: The options of this ApplyWafPolicyResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafPolicyOption`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this ApplyWafPolicyResponse.

        :param options: The options of this ApplyWafPolicyResponse.
        :type options: :class:`huaweicloudsdkedgesec.v1.WafPolicyOption`
        """
        self._options = options

    @property
    def level(self):
        """Gets the level of this ApplyWafPolicyResponse.

        防护等级

        :return: The level of this ApplyWafPolicyResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this ApplyWafPolicyResponse.

        防护等级

        :param level: The level of this ApplyWafPolicyResponse.
        :type level: int
        """
        self._level = level

    @property
    def full_detection(self):
        """Gets the full_detection of this ApplyWafPolicyResponse.

        精准防护中的检测模式

        :return: The full_detection of this ApplyWafPolicyResponse.
        :rtype: bool
        """
        return self._full_detection

    @full_detection.setter
    def full_detection(self, full_detection):
        """Sets the full_detection of this ApplyWafPolicyResponse.

        精准防护中的检测模式

        :param full_detection: The full_detection of this ApplyWafPolicyResponse.
        :type full_detection: bool
        """
        self._full_detection = full_detection

    @property
    def robot_action(self):
        """Gets the robot_action of this ApplyWafPolicyResponse.

        :return: The robot_action of this ApplyWafPolicyResponse.
        :rtype: :class:`huaweicloudsdkedgesec.v1.WafPolicyAction`
        """
        return self._robot_action

    @robot_action.setter
    def robot_action(self, robot_action):
        """Sets the robot_action of this ApplyWafPolicyResponse.

        :param robot_action: The robot_action of this ApplyWafPolicyResponse.
        :type robot_action: :class:`huaweicloudsdkedgesec.v1.WafPolicyAction`
        """
        self._robot_action = robot_action

    @property
    def bind_host(self):
        """Gets the bind_host of this ApplyWafPolicyResponse.

        防护域名的信息

        :return: The bind_host of this ApplyWafPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkedgesec.v1.WafPolicyBindHost`]
        """
        return self._bind_host

    @bind_host.setter
    def bind_host(self, bind_host):
        """Sets the bind_host of this ApplyWafPolicyResponse.

        防护域名的信息

        :param bind_host: The bind_host of this ApplyWafPolicyResponse.
        :type bind_host: list[:class:`huaweicloudsdkedgesec.v1.WafPolicyBindHost`]
        """
        self._bind_host = bind_host

    @property
    def timestamp(self):
        """Gets the timestamp of this ApplyWafPolicyResponse.

        创建防护策略的时间

        :return: The timestamp of this ApplyWafPolicyResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this ApplyWafPolicyResponse.

        创建防护策略的时间

        :param timestamp: The timestamp of this ApplyWafPolicyResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

    @property
    def extend(self):
        """Gets the extend of this ApplyWafPolicyResponse.

        扩展字段

        :return: The extend of this ApplyWafPolicyResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this ApplyWafPolicyResponse.

        扩展字段

        :param extend: The extend of this ApplyWafPolicyResponse.
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
        if not isinstance(other, ApplyWafPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
