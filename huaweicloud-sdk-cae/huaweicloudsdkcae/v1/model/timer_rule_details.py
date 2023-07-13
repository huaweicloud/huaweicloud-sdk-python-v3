# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TimerRuleDetails:

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
        'type': 'str',
        'status': 'str',
        'env_id': 'str',
        'apps': 'list[AppInfo]',
        'components': 'list[ComponentInfo]',
        'component_number': 'int',
        'cron': 'str',
        'effective_range': 'str',
        'effective_policy': 'str',
        'last_execution_status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'env_id': 'env_id',
        'apps': 'apps',
        'components': 'components',
        'component_number': 'component_number',
        'cron': 'cron',
        'effective_range': 'effective_range',
        'effective_policy': 'effective_policy',
        'last_execution_status': 'last_execution_status'
    }

    def __init__(self, id=None, name=None, type=None, status=None, env_id=None, apps=None, components=None, component_number=None, cron=None, effective_range=None, effective_policy=None, last_execution_status=None):
        """TimerRuleDetails

        The model defined in huaweicloud sdk

        :param id: 定时启停规则ID，在创建定时启停规则时会忽略。
        :type id: str
        :param name: 定时启停规则名称。
        :type name: str
        :param type: 定时启停规则的类型：stop/start。
        :type type: str
        :param status: 定时启停规则状态（是否开启）：on/off。
        :type status: str
        :param env_id: 环境ID。
        :type env_id: str
        :param apps: 定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。
        :type apps: list[:class:`huaweicloudsdkcae.v1.AppInfo`]
        :param components: 在定时启停规则所包含的所有组件，只在生效范围为component的时候需要填写。
        :type components: list[:class:`huaweicloudsdkcae.v1.ComponentInfo`]
        :param component_number: 定时启停规则包含的组件个数，在创建定时启停规则时会忽略。
        :type component_number: int
        :param cron: cron表达式。
        :type cron: str
        :param effective_range: 定时启停规则生效范围: component/application/environment。
        :type effective_range: str
        :param effective_policy: 定时启停规则的定时类别: onetime/periodic。
        :type effective_policy: str
        :param last_execution_status: 上次执行的状态：abnormal/normal/executing，在创建定时启停规则时会忽略。
        :type last_execution_status: str
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._env_id = None
        self._apps = None
        self._components = None
        self._component_number = None
        self._cron = None
        self._effective_range = None
        self._effective_policy = None
        self._last_execution_status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if env_id is not None:
            self.env_id = env_id
        if apps is not None:
            self.apps = apps
        if components is not None:
            self.components = components
        if component_number is not None:
            self.component_number = component_number
        if cron is not None:
            self.cron = cron
        if effective_range is not None:
            self.effective_range = effective_range
        if effective_policy is not None:
            self.effective_policy = effective_policy
        if last_execution_status is not None:
            self.last_execution_status = last_execution_status

    @property
    def id(self):
        """Gets the id of this TimerRuleDetails.

        定时启停规则ID，在创建定时启停规则时会忽略。

        :return: The id of this TimerRuleDetails.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TimerRuleDetails.

        定时启停规则ID，在创建定时启停规则时会忽略。

        :param id: The id of this TimerRuleDetails.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this TimerRuleDetails.

        定时启停规则名称。

        :return: The name of this TimerRuleDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TimerRuleDetails.

        定时启停规则名称。

        :param name: The name of this TimerRuleDetails.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        """Gets the type of this TimerRuleDetails.

        定时启停规则的类型：stop/start。

        :return: The type of this TimerRuleDetails.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TimerRuleDetails.

        定时启停规则的类型：stop/start。

        :param type: The type of this TimerRuleDetails.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        """Gets the status of this TimerRuleDetails.

        定时启停规则状态（是否开启）：on/off。

        :return: The status of this TimerRuleDetails.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TimerRuleDetails.

        定时启停规则状态（是否开启）：on/off。

        :param status: The status of this TimerRuleDetails.
        :type status: str
        """
        self._status = status

    @property
    def env_id(self):
        """Gets the env_id of this TimerRuleDetails.

        环境ID。

        :return: The env_id of this TimerRuleDetails.
        :rtype: str
        """
        return self._env_id

    @env_id.setter
    def env_id(self, env_id):
        """Sets the env_id of this TimerRuleDetails.

        环境ID。

        :param env_id: The env_id of this TimerRuleDetails.
        :type env_id: str
        """
        self._env_id = env_id

    @property
    def apps(self):
        """Gets the apps of this TimerRuleDetails.

        定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。

        :return: The apps of this TimerRuleDetails.
        :rtype: list[:class:`huaweicloudsdkcae.v1.AppInfo`]
        """
        return self._apps

    @apps.setter
    def apps(self, apps):
        """Sets the apps of this TimerRuleDetails.

        定时启停规则所包含的所有应用，只在生效范围为application的时候需要填写。

        :param apps: The apps of this TimerRuleDetails.
        :type apps: list[:class:`huaweicloudsdkcae.v1.AppInfo`]
        """
        self._apps = apps

    @property
    def components(self):
        """Gets the components of this TimerRuleDetails.

        在定时启停规则所包含的所有组件，只在生效范围为component的时候需要填写。

        :return: The components of this TimerRuleDetails.
        :rtype: list[:class:`huaweicloudsdkcae.v1.ComponentInfo`]
        """
        return self._components

    @components.setter
    def components(self, components):
        """Sets the components of this TimerRuleDetails.

        在定时启停规则所包含的所有组件，只在生效范围为component的时候需要填写。

        :param components: The components of this TimerRuleDetails.
        :type components: list[:class:`huaweicloudsdkcae.v1.ComponentInfo`]
        """
        self._components = components

    @property
    def component_number(self):
        """Gets the component_number of this TimerRuleDetails.

        定时启停规则包含的组件个数，在创建定时启停规则时会忽略。

        :return: The component_number of this TimerRuleDetails.
        :rtype: int
        """
        return self._component_number

    @component_number.setter
    def component_number(self, component_number):
        """Sets the component_number of this TimerRuleDetails.

        定时启停规则包含的组件个数，在创建定时启停规则时会忽略。

        :param component_number: The component_number of this TimerRuleDetails.
        :type component_number: int
        """
        self._component_number = component_number

    @property
    def cron(self):
        """Gets the cron of this TimerRuleDetails.

        cron表达式。

        :return: The cron of this TimerRuleDetails.
        :rtype: str
        """
        return self._cron

    @cron.setter
    def cron(self, cron):
        """Sets the cron of this TimerRuleDetails.

        cron表达式。

        :param cron: The cron of this TimerRuleDetails.
        :type cron: str
        """
        self._cron = cron

    @property
    def effective_range(self):
        """Gets the effective_range of this TimerRuleDetails.

        定时启停规则生效范围: component/application/environment。

        :return: The effective_range of this TimerRuleDetails.
        :rtype: str
        """
        return self._effective_range

    @effective_range.setter
    def effective_range(self, effective_range):
        """Sets the effective_range of this TimerRuleDetails.

        定时启停规则生效范围: component/application/environment。

        :param effective_range: The effective_range of this TimerRuleDetails.
        :type effective_range: str
        """
        self._effective_range = effective_range

    @property
    def effective_policy(self):
        """Gets the effective_policy of this TimerRuleDetails.

        定时启停规则的定时类别: onetime/periodic。

        :return: The effective_policy of this TimerRuleDetails.
        :rtype: str
        """
        return self._effective_policy

    @effective_policy.setter
    def effective_policy(self, effective_policy):
        """Sets the effective_policy of this TimerRuleDetails.

        定时启停规则的定时类别: onetime/periodic。

        :param effective_policy: The effective_policy of this TimerRuleDetails.
        :type effective_policy: str
        """
        self._effective_policy = effective_policy

    @property
    def last_execution_status(self):
        """Gets the last_execution_status of this TimerRuleDetails.

        上次执行的状态：abnormal/normal/executing，在创建定时启停规则时会忽略。

        :return: The last_execution_status of this TimerRuleDetails.
        :rtype: str
        """
        return self._last_execution_status

    @last_execution_status.setter
    def last_execution_status(self, last_execution_status):
        """Sets the last_execution_status of this TimerRuleDetails.

        上次执行的状态：abnormal/normal/executing，在创建定时启停规则时会忽略。

        :param last_execution_status: The last_execution_status of this TimerRuleDetails.
        :type last_execution_status: str
        """
        self._last_execution_status = last_execution_status

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
        if not isinstance(other, TimerRuleDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
