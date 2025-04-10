# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTimerRuleDetails:

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
        'type': 'str',
        'status': 'str',
        'apps': 'list[AppInfo]',
        'components': 'list[ComponentInfo]',
        'cron': 'str',
        'effective_range': 'str',
        'effective_policy': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'apps': 'apps',
        'components': 'components',
        'cron': 'cron',
        'effective_range': 'effective_range',
        'effective_policy': 'effective_policy'
    }

    def __init__(self, name=None, type=None, status=None, apps=None, components=None, cron=None, effective_range=None, effective_policy=None):
        r"""UpdateTimerRuleDetails

        The model defined in huaweicloud sdk

        :param name: 定时启停规则名称。
        :type name: str
        :param type: 定时启停规则的类型：stop/start。
        :type type: str
        :param status: 定时启停规则状态（是否开启）：on/off。
        :type status: str
        :param apps: 定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。
        :type apps: list[:class:`huaweicloudsdkcae.v1.AppInfo`]
        :param components: 在定时启停规则所包含的所有组件，只在生效范围为component的时候需要填写。
        :type components: list[:class:`huaweicloudsdkcae.v1.ComponentInfo`]
        :param cron: cron表达式。
        :type cron: str
        :param effective_range: 定时启停规则生效范围: component/application/environment。
        :type effective_range: str
        :param effective_policy: 定时启停规则的定时类别: onetime/periodic。
        :type effective_policy: str
        """
        
        

        self._name = None
        self._type = None
        self._status = None
        self._apps = None
        self._components = None
        self._cron = None
        self._effective_range = None
        self._effective_policy = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.status = status
        if apps is not None:
            self.apps = apps
        if components is not None:
            self.components = components
        self.cron = cron
        self.effective_range = effective_range
        self.effective_policy = effective_policy

    @property
    def name(self):
        r"""Gets the name of this UpdateTimerRuleDetails.

        定时启停规则名称。

        :return: The name of this UpdateTimerRuleDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateTimerRuleDetails.

        定时启停规则名称。

        :param name: The name of this UpdateTimerRuleDetails.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this UpdateTimerRuleDetails.

        定时启停规则的类型：stop/start。

        :return: The type of this UpdateTimerRuleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this UpdateTimerRuleDetails.

        定时启停规则的类型：stop/start。

        :param type: The type of this UpdateTimerRuleDetails.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this UpdateTimerRuleDetails.

        定时启停规则状态（是否开启）：on/off。

        :return: The status of this UpdateTimerRuleDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateTimerRuleDetails.

        定时启停规则状态（是否开启）：on/off。

        :param status: The status of this UpdateTimerRuleDetails.
        :type status: str
        """
        self._status = status

    @property
    def apps(self):
        r"""Gets the apps of this UpdateTimerRuleDetails.

        定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。

        :return: The apps of this UpdateTimerRuleDetails.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AppInfo`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        r"""Sets the apps of this UpdateTimerRuleDetails.

        定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。

        :param apps: The apps of this UpdateTimerRuleDetails.
        :type apps: list[:class:`huaweicloudsdkcae.v1.AppInfo`]
        """
        self._apps = apps

    @property
    def components(self):
        r"""Gets the components of this UpdateTimerRuleDetails.

        在定时启停规则所包含的所有组件，只在生效范围为component的时候需要填写。

        :return: The components of this UpdateTimerRuleDetails.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ComponentInfo`]
        """
        return self._components

    @components.setter
    def components(self, components):
        r"""Sets the components of this UpdateTimerRuleDetails.

        在定时启停规则所包含的所有组件，只在生效范围为component的时候需要填写。

        :param components: The components of this UpdateTimerRuleDetails.
        :type components: list[:class:`huaweicloudsdkcae.v1.ComponentInfo`]
        """
        self._components = components

    @property
    def cron(self):
        r"""Gets the cron of this UpdateTimerRuleDetails.

        cron表达式。

        :return: The cron of this UpdateTimerRuleDetails.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        r"""Sets the cron of this UpdateTimerRuleDetails.

        cron表达式。

        :param cron: The cron of this UpdateTimerRuleDetails.
        :type cron: str
        """
        self._cron = cron

    @property
    def effective_range(self):
        r"""Gets the effective_range of this UpdateTimerRuleDetails.

        定时启停规则生效范围: component/application/environment。

        :return: The effective_range of this UpdateTimerRuleDetails.
        :rtype: str
        """
        return self._effective_range

    @effective_range.setter
    def effective_range(self, effective_range):
        r"""Sets the effective_range of this UpdateTimerRuleDetails.

        定时启停规则生效范围: component/application/environment。

        :param effective_range: The effective_range of this UpdateTimerRuleDetails.
        :type effective_range: str
        """
        self._effective_range = effective_range

    @property
    def effective_policy(self):
        r"""Gets the effective_policy of this UpdateTimerRuleDetails.

        定时启停规则的定时类别: onetime/periodic。

        :return: The effective_policy of this UpdateTimerRuleDetails.
        :rtype: str
        """
        return self._effective_policy

    @effective_policy.setter
    def effective_policy(self, effective_policy):
        r"""Sets the effective_policy of this UpdateTimerRuleDetails.

        定时启停规则的定时类别: onetime/periodic。

        :param effective_policy: The effective_policy of this UpdateTimerRuleDetails.
        :type effective_policy: str
        """
        self._effective_policy = effective_policy

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
        if not isinstance(other, UpdateTimerRuleDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
