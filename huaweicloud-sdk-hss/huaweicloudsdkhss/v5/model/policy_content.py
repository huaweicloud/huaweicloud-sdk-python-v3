# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyContent:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_image_startup': 'bool',
        'policy_type': 'str',
        'severity': 'int',
        'risky_item': 'list[str]',
        'action': 'int'
    }

    attribute_map = {
        'enable_image_startup': 'enable_image_startup',
        'policy_type': 'policy_type',
        'severity': 'severity',
        'risky_item': 'risky_item',
        'action': 'action'
    }

    def __init__(self, enable_image_startup=None, policy_type=None, severity=None, risky_item=None, action=None):
        r"""PolicyContent

        The model defined in huaweicloud sdk

        :param enable_image_startup: 是否允许未扫描镜像启动
        :type enable_image_startup: bool
        :param policy_type: 告警策略: - vuls: 漏洞 - baselines: 基线  - malwares: 恶意脚本 
        :type policy_type: str
        :param severity: 风险等级
        :type severity: int
        :param risky_item: 危险项
        :type risky_item: list[str]
        :param action: 防护动作   - 0: 告警   - 1: 阻断   - 2: 放行 
        :type action: int
        """
        
        

        self._enable_image_startup = None
        self._policy_type = None
        self._severity = None
        self._risky_item = None
        self._action = None
        self.discriminator = None

        self.enable_image_startup = enable_image_startup
        self.policy_type = policy_type
        self.severity = severity
        self.risky_item = risky_item
        self.action = action

    @property
    def enable_image_startup(self):
        r"""Gets the enable_image_startup of this PolicyContent.

        是否允许未扫描镜像启动

        :return: The enable_image_startup of this PolicyContent.
        :rtype: bool
        """
        return self._enable_image_startup

    @enable_image_startup.setter
    def enable_image_startup(self, enable_image_startup):
        r"""Sets the enable_image_startup of this PolicyContent.

        是否允许未扫描镜像启动

        :param enable_image_startup: The enable_image_startup of this PolicyContent.
        :type enable_image_startup: bool
        """
        self._enable_image_startup = enable_image_startup

    @property
    def policy_type(self):
        r"""Gets the policy_type of this PolicyContent.

        告警策略: - vuls: 漏洞 - baselines: 基线  - malwares: 恶意脚本 

        :return: The policy_type of this PolicyContent.
        :rtype: str
        """
        return self._policy_type

    @policy_type.setter
    def policy_type(self, policy_type):
        r"""Sets the policy_type of this PolicyContent.

        告警策略: - vuls: 漏洞 - baselines: 基线  - malwares: 恶意脚本 

        :param policy_type: The policy_type of this PolicyContent.
        :type policy_type: str
        """
        self._policy_type = policy_type

    @property
    def severity(self):
        r"""Gets the severity of this PolicyContent.

        风险等级

        :return: The severity of this PolicyContent.
        :rtype: int
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this PolicyContent.

        风险等级

        :param severity: The severity of this PolicyContent.
        :type severity: int
        """
        self._severity = severity

    @property
    def risky_item(self):
        r"""Gets the risky_item of this PolicyContent.

        危险项

        :return: The risky_item of this PolicyContent.
        :rtype: list[str]
        """
        return self._risky_item

    @risky_item.setter
    def risky_item(self, risky_item):
        r"""Sets the risky_item of this PolicyContent.

        危险项

        :param risky_item: The risky_item of this PolicyContent.
        :type risky_item: list[str]
        """
        self._risky_item = risky_item

    @property
    def action(self):
        r"""Gets the action of this PolicyContent.

        防护动作   - 0: 告警   - 1: 阻断   - 2: 放行 

        :return: The action of this PolicyContent.
        :rtype: int
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this PolicyContent.

        防护动作   - 0: 告警   - 1: 阻断   - 2: 放行 

        :param action: The action of this PolicyContent.
        :type action: int
        """
        self._action = action

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
        if not isinstance(other, PolicyContent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
