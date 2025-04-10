# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AgentPluginInfoQueryDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'plugin_name': 'str',
        'regex_name': 'str',
        'maintainer': 'str',
        'business_type': 'list[str]',
        'plugin_attribution': 'str'
    }

    attribute_map = {
        'plugin_name': 'plugin_name',
        'regex_name': 'regex_name',
        'maintainer': 'maintainer',
        'business_type': 'business_type',
        'plugin_attribution': 'plugin_attribution'
    }

    def __init__(self, plugin_name=None, regex_name=None, maintainer=None, business_type=None, plugin_attribution=None):
        r"""AgentPluginInfoQueryDTO

        The model defined in huaweicloud sdk

        :param plugin_name: 可选的查询条件-插件名
        :type plugin_name: str
        :param regex_name: 可选的查询条件-匹配名称
        :type regex_name: str
        :param maintainer: 维护者
        :type maintainer: str
        :param business_type: 业务类型,[Build,Gate,Deploy,Test,Normal]
        :type business_type: list[str]
        :param plugin_attribution: 插件属性，official/custom
        :type plugin_attribution: str
        """
        
        

        self._plugin_name = None
        self._regex_name = None
        self._maintainer = None
        self._business_type = None
        self._plugin_attribution = None
        self.discriminator = None

        if plugin_name is not None:
            self.plugin_name = plugin_name
        if regex_name is not None:
            self.regex_name = regex_name
        if maintainer is not None:
            self.maintainer = maintainer
        if business_type is not None:
            self.business_type = business_type
        if plugin_attribution is not None:
            self.plugin_attribution = plugin_attribution

    @property
    def plugin_name(self):
        r"""Gets the plugin_name of this AgentPluginInfoQueryDTO.

        可选的查询条件-插件名

        :return: The plugin_name of this AgentPluginInfoQueryDTO.
        :rtype: str
        """
        return self._plugin_name

    @plugin_name.setter
    def plugin_name(self, plugin_name):
        r"""Sets the plugin_name of this AgentPluginInfoQueryDTO.

        可选的查询条件-插件名

        :param plugin_name: The plugin_name of this AgentPluginInfoQueryDTO.
        :type plugin_name: str
        """
        self._plugin_name = plugin_name

    @property
    def regex_name(self):
        r"""Gets the regex_name of this AgentPluginInfoQueryDTO.

        可选的查询条件-匹配名称

        :return: The regex_name of this AgentPluginInfoQueryDTO.
        :rtype: str
        """
        return self._regex_name

    @regex_name.setter
    def regex_name(self, regex_name):
        r"""Sets the regex_name of this AgentPluginInfoQueryDTO.

        可选的查询条件-匹配名称

        :param regex_name: The regex_name of this AgentPluginInfoQueryDTO.
        :type regex_name: str
        """
        self._regex_name = regex_name

    @property
    def maintainer(self):
        r"""Gets the maintainer of this AgentPluginInfoQueryDTO.

        维护者

        :return: The maintainer of this AgentPluginInfoQueryDTO.
        :rtype: str
        """
        return self._maintainer

    @maintainer.setter
    def maintainer(self, maintainer):
        r"""Sets the maintainer of this AgentPluginInfoQueryDTO.

        维护者

        :param maintainer: The maintainer of this AgentPluginInfoQueryDTO.
        :type maintainer: str
        """
        self._maintainer = maintainer

    @property
    def business_type(self):
        r"""Gets the business_type of this AgentPluginInfoQueryDTO.

        业务类型,[Build,Gate,Deploy,Test,Normal]

        :return: The business_type of this AgentPluginInfoQueryDTO.
        :rtype: list[str]
        """
        return self._business_type

    @business_type.setter
    def business_type(self, business_type):
        r"""Sets the business_type of this AgentPluginInfoQueryDTO.

        业务类型,[Build,Gate,Deploy,Test,Normal]

        :param business_type: The business_type of this AgentPluginInfoQueryDTO.
        :type business_type: list[str]
        """
        self._business_type = business_type

    @property
    def plugin_attribution(self):
        r"""Gets the plugin_attribution of this AgentPluginInfoQueryDTO.

        插件属性，official/custom

        :return: The plugin_attribution of this AgentPluginInfoQueryDTO.
        :rtype: str
        """
        return self._plugin_attribution

    @plugin_attribution.setter
    def plugin_attribution(self, plugin_attribution):
        r"""Sets the plugin_attribution of this AgentPluginInfoQueryDTO.

        插件属性，official/custom

        :param plugin_attribution: The plugin_attribution of this AgentPluginInfoQueryDTO.
        :type plugin_attribution: str
        """
        self._plugin_attribution = plugin_attribution

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
        if not isinstance(other, AgentPluginInfoQueryDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
