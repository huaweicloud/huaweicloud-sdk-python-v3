# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePolicyResponse(SdkResponse):

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
        'robot_action': 'Action',
        'action': 'PolicyAction',
        'options': 'PolicyOption',
        'modulex_options': 'dict(str, object)',
        'hosts': 'list[str]',
        'bind_host': 'list[BindHost]',
        'extend': 'dict(str, str)',
        'timestamp': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'level': 'level',
        'full_detection': 'full_detection',
        'robot_action': 'robot_action',
        'action': 'action',
        'options': 'options',
        'modulex_options': 'modulex_options',
        'hosts': 'hosts',
        'bind_host': 'bind_host',
        'extend': 'extend',
        'timestamp': 'timestamp'
    }

    def __init__(self, id=None, name=None, level=None, full_detection=None, robot_action=None, action=None, options=None, modulex_options=None, hosts=None, bind_host=None, extend=None, timestamp=None):
        """UpdatePolicyResponse

        The model defined in huaweicloud sdk

        :param id: 防护策略id
        :type id: str
        :param name: 防护策略名
        :type name: str
        :param level: Web基础防护等级   - 1 : 宽松，防护粒度较粗，只拦截攻击特征比较明显的请求。当误报情况较多的场景下，建议选择“宽松”模式。   - 2：中等，默认为“中等”防护模式，满足大多数场景下的Web防护需求。   - 3：严格，防护粒度最精细，可以拦截具有复杂的绕过特征的攻击请求，例如jolokia网络攻击、探测CGI漏洞、探测 Druid SQL注入攻击
        :type level: int
        :param full_detection: 精准防护中的检测模式。   - false：短路检测，当用户的请求符合精准防护中的拦截条件时，便立刻终止检测，进行拦截   - true ：全检测，请求符合精准防护中的拦截条件时，全检测不会立即拦截，会继续执行其他防护的检测，最后进行拦截。
        :type full_detection: bool
        :param robot_action: 
        :type robot_action: :class:`huaweicloudsdkwaf.v1.Action`
        :param action: 
        :type action: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        :param options: 
        :type options: :class:`huaweicloudsdkwaf.v1.PolicyOption`
        :param modulex_options: 智能访问控制防护项相关配置信息，目前该特性还处于公测阶段，只有部分局点支持该特性
        :type modulex_options: dict(str, object)
        :param hosts: 与防护策略绑定的防护的域名id数组
        :type hosts: list[str]
        :param bind_host: 与防护策略绑定的防护的域名信息数组，相对于hosts字段，包含更详细的域名信息
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        :param extend: 扩展字段，用于存放Web基础防护中一些开关配置等信息
        :type extend: dict(str, str)
        :param timestamp: 创建防护策略的时间
        :type timestamp: int
        """
        
        super(UpdatePolicyResponse, self).__init__()

        self._id = None
        self._name = None
        self._level = None
        self._full_detection = None
        self._robot_action = None
        self._action = None
        self._options = None
        self._modulex_options = None
        self._hosts = None
        self._bind_host = None
        self._extend = None
        self._timestamp = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if level is not None:
            self.level = level
        if full_detection is not None:
            self.full_detection = full_detection
        if robot_action is not None:
            self.robot_action = robot_action
        if action is not None:
            self.action = action
        if options is not None:
            self.options = options
        if modulex_options is not None:
            self.modulex_options = modulex_options
        if hosts is not None:
            self.hosts = hosts
        if bind_host is not None:
            self.bind_host = bind_host
        if extend is not None:
            self.extend = extend
        if timestamp is not None:
            self.timestamp = timestamp

    @property
    def id(self):
        """Gets the id of this UpdatePolicyResponse.

        防护策略id

        :return: The id of this UpdatePolicyResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UpdatePolicyResponse.

        防护策略id

        :param id: The id of this UpdatePolicyResponse.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this UpdatePolicyResponse.

        防护策略名

        :return: The name of this UpdatePolicyResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePolicyResponse.

        防护策略名

        :param name: The name of this UpdatePolicyResponse.
        :type name: str
        """
        self._name = name

    @property
    def level(self):
        """Gets the level of this UpdatePolicyResponse.

        Web基础防护等级   - 1 : 宽松，防护粒度较粗，只拦截攻击特征比较明显的请求。当误报情况较多的场景下，建议选择“宽松”模式。   - 2：中等，默认为“中等”防护模式，满足大多数场景下的Web防护需求。   - 3：严格，防护粒度最精细，可以拦截具有复杂的绕过特征的攻击请求，例如jolokia网络攻击、探测CGI漏洞、探测 Druid SQL注入攻击

        :return: The level of this UpdatePolicyResponse.
        :rtype: int
        """
        return self._level

    @level.setter
    def level(self, level):
        """Sets the level of this UpdatePolicyResponse.

        Web基础防护等级   - 1 : 宽松，防护粒度较粗，只拦截攻击特征比较明显的请求。当误报情况较多的场景下，建议选择“宽松”模式。   - 2：中等，默认为“中等”防护模式，满足大多数场景下的Web防护需求。   - 3：严格，防护粒度最精细，可以拦截具有复杂的绕过特征的攻击请求，例如jolokia网络攻击、探测CGI漏洞、探测 Druid SQL注入攻击

        :param level: The level of this UpdatePolicyResponse.
        :type level: int
        """
        self._level = level

    @property
    def full_detection(self):
        """Gets the full_detection of this UpdatePolicyResponse.

        精准防护中的检测模式。   - false：短路检测，当用户的请求符合精准防护中的拦截条件时，便立刻终止检测，进行拦截   - true ：全检测，请求符合精准防护中的拦截条件时，全检测不会立即拦截，会继续执行其他防护的检测，最后进行拦截。

        :return: The full_detection of this UpdatePolicyResponse.
        :rtype: bool
        """
        return self._full_detection

    @full_detection.setter
    def full_detection(self, full_detection):
        """Sets the full_detection of this UpdatePolicyResponse.

        精准防护中的检测模式。   - false：短路检测，当用户的请求符合精准防护中的拦截条件时，便立刻终止检测，进行拦截   - true ：全检测，请求符合精准防护中的拦截条件时，全检测不会立即拦截，会继续执行其他防护的检测，最后进行拦截。

        :param full_detection: The full_detection of this UpdatePolicyResponse.
        :type full_detection: bool
        """
        self._full_detection = full_detection

    @property
    def robot_action(self):
        """Gets the robot_action of this UpdatePolicyResponse.

        :return: The robot_action of this UpdatePolicyResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.Action`
        """
        return self._robot_action

    @robot_action.setter
    def robot_action(self, robot_action):
        """Sets the robot_action of this UpdatePolicyResponse.

        :param robot_action: The robot_action of this UpdatePolicyResponse.
        :type robot_action: :class:`huaweicloudsdkwaf.v1.Action`
        """
        self._robot_action = robot_action

    @property
    def action(self):
        """Gets the action of this UpdatePolicyResponse.

        :return: The action of this UpdatePolicyResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        """
        return self._action

    @action.setter
    def action(self, action):
        """Sets the action of this UpdatePolicyResponse.

        :param action: The action of this UpdatePolicyResponse.
        :type action: :class:`huaweicloudsdkwaf.v1.PolicyAction`
        """
        self._action = action

    @property
    def options(self):
        """Gets the options of this UpdatePolicyResponse.

        :return: The options of this UpdatePolicyResponse.
        :rtype: :class:`huaweicloudsdkwaf.v1.PolicyOption`
        """
        return self._options

    @options.setter
    def options(self, options):
        """Sets the options of this UpdatePolicyResponse.

        :param options: The options of this UpdatePolicyResponse.
        :type options: :class:`huaweicloudsdkwaf.v1.PolicyOption`
        """
        self._options = options

    @property
    def modulex_options(self):
        """Gets the modulex_options of this UpdatePolicyResponse.

        智能访问控制防护项相关配置信息，目前该特性还处于公测阶段，只有部分局点支持该特性

        :return: The modulex_options of this UpdatePolicyResponse.
        :rtype: dict(str, object)
        """
        return self._modulex_options

    @modulex_options.setter
    def modulex_options(self, modulex_options):
        """Sets the modulex_options of this UpdatePolicyResponse.

        智能访问控制防护项相关配置信息，目前该特性还处于公测阶段，只有部分局点支持该特性

        :param modulex_options: The modulex_options of this UpdatePolicyResponse.
        :type modulex_options: dict(str, object)
        """
        self._modulex_options = modulex_options

    @property
    def hosts(self):
        """Gets the hosts of this UpdatePolicyResponse.

        与防护策略绑定的防护的域名id数组

        :return: The hosts of this UpdatePolicyResponse.
        :rtype: list[str]
        """
        return self._hosts

    @hosts.setter
    def hosts(self, hosts):
        """Sets the hosts of this UpdatePolicyResponse.

        与防护策略绑定的防护的域名id数组

        :param hosts: The hosts of this UpdatePolicyResponse.
        :type hosts: list[str]
        """
        self._hosts = hosts

    @property
    def bind_host(self):
        """Gets the bind_host of this UpdatePolicyResponse.

        与防护策略绑定的防护的域名信息数组，相对于hosts字段，包含更详细的域名信息

        :return: The bind_host of this UpdatePolicyResponse.
        :rtype: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        return self._bind_host

    @bind_host.setter
    def bind_host(self, bind_host):
        """Sets the bind_host of this UpdatePolicyResponse.

        与防护策略绑定的防护的域名信息数组，相对于hosts字段，包含更详细的域名信息

        :param bind_host: The bind_host of this UpdatePolicyResponse.
        :type bind_host: list[:class:`huaweicloudsdkwaf.v1.BindHost`]
        """
        self._bind_host = bind_host

    @property
    def extend(self):
        """Gets the extend of this UpdatePolicyResponse.

        扩展字段，用于存放Web基础防护中一些开关配置等信息

        :return: The extend of this UpdatePolicyResponse.
        :rtype: dict(str, str)
        """
        return self._extend

    @extend.setter
    def extend(self, extend):
        """Sets the extend of this UpdatePolicyResponse.

        扩展字段，用于存放Web基础防护中一些开关配置等信息

        :param extend: The extend of this UpdatePolicyResponse.
        :type extend: dict(str, str)
        """
        self._extend = extend

    @property
    def timestamp(self):
        """Gets the timestamp of this UpdatePolicyResponse.

        创建防护策略的时间

        :return: The timestamp of this UpdatePolicyResponse.
        :rtype: int
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this UpdatePolicyResponse.

        创建防护策略的时间

        :param timestamp: The timestamp of this UpdatePolicyResponse.
        :type timestamp: int
        """
        self._timestamp = timestamp

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
        if not isinstance(other, UpdatePolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
