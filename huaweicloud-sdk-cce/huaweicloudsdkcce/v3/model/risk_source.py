# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RiskSource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_risks': 'list[ConfigurationRisks]',
        'deprecated_api_risks': 'list[DeprecatedAPIRisks]',
        'node_risks': 'list[NodeRisks]',
        'addon_risks': 'list[AddonRisks]'
    }

    attribute_map = {
        'configuration_risks': 'configurationRisks',
        'deprecated_api_risks': 'deprecatedAPIRisks',
        'node_risks': 'nodeRisks',
        'addon_risks': 'addonRisks'
    }

    def __init__(self, configuration_risks=None, deprecated_api_risks=None, node_risks=None, addon_risks=None):
        """RiskSource

        The model defined in huaweicloud sdk

        :param configuration_risks: 配置风险项
        :type configuration_risks: list[:class:`huaweicloudsdkcce.v3.ConfigurationRisks`]
        :param deprecated_api_risks: 废弃API风险
        :type deprecated_api_risks: list[:class:`huaweicloudsdkcce.v3.DeprecatedAPIRisks`]
        :param node_risks: 节点风险
        :type node_risks: list[:class:`huaweicloudsdkcce.v3.NodeRisks`]
        :param addon_risks: 插件风险
        :type addon_risks: list[:class:`huaweicloudsdkcce.v3.AddonRisks`]
        """
        
        

        self._configuration_risks = None
        self._deprecated_api_risks = None
        self._node_risks = None
        self._addon_risks = None
        self.discriminator = None

        if configuration_risks is not None:
            self.configuration_risks = configuration_risks
        if deprecated_api_risks is not None:
            self.deprecated_api_risks = deprecated_api_risks
        if node_risks is not None:
            self.node_risks = node_risks
        if addon_risks is not None:
            self.addon_risks = addon_risks

    @property
    def configuration_risks(self):
        """Gets the configuration_risks of this RiskSource.

        配置风险项

        :return: The configuration_risks of this RiskSource.
        :rtype: list[:class:`huaweicloudsdkcce.v3.ConfigurationRisks`]
        """
        return self._configuration_risks

    @configuration_risks.setter
    def configuration_risks(self, configuration_risks):
        """Sets the configuration_risks of this RiskSource.

        配置风险项

        :param configuration_risks: The configuration_risks of this RiskSource.
        :type configuration_risks: list[:class:`huaweicloudsdkcce.v3.ConfigurationRisks`]
        """
        self._configuration_risks = configuration_risks

    @property
    def deprecated_api_risks(self):
        """Gets the deprecated_api_risks of this RiskSource.

        废弃API风险

        :return: The deprecated_api_risks of this RiskSource.
        :rtype: list[:class:`huaweicloudsdkcce.v3.DeprecatedAPIRisks`]
        """
        return self._deprecated_api_risks

    @deprecated_api_risks.setter
    def deprecated_api_risks(self, deprecated_api_risks):
        """Sets the deprecated_api_risks of this RiskSource.

        废弃API风险

        :param deprecated_api_risks: The deprecated_api_risks of this RiskSource.
        :type deprecated_api_risks: list[:class:`huaweicloudsdkcce.v3.DeprecatedAPIRisks`]
        """
        self._deprecated_api_risks = deprecated_api_risks

    @property
    def node_risks(self):
        """Gets the node_risks of this RiskSource.

        节点风险

        :return: The node_risks of this RiskSource.
        :rtype: list[:class:`huaweicloudsdkcce.v3.NodeRisks`]
        """
        return self._node_risks

    @node_risks.setter
    def node_risks(self, node_risks):
        """Sets the node_risks of this RiskSource.

        节点风险

        :param node_risks: The node_risks of this RiskSource.
        :type node_risks: list[:class:`huaweicloudsdkcce.v3.NodeRisks`]
        """
        self._node_risks = node_risks

    @property
    def addon_risks(self):
        """Gets the addon_risks of this RiskSource.

        插件风险

        :return: The addon_risks of this RiskSource.
        :rtype: list[:class:`huaweicloudsdkcce.v3.AddonRisks`]
        """
        return self._addon_risks

    @addon_risks.setter
    def addon_risks(self, addon_risks):
        """Sets the addon_risks of this RiskSource.

        插件风险

        :param addon_risks: The addon_risks of this RiskSource.
        :type addon_risks: list[:class:`huaweicloudsdkcce.v3.AddonRisks`]
        """
        self._addon_risks = addon_risks

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
        if not isinstance(other, RiskSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
