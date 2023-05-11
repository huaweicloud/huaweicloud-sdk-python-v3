# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NetworkControlConfig:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disable_public_network': 'bool',
        'trigger_access_vpcs': 'list[VpcConfig]'
    }

    attribute_map = {
        'disable_public_network': 'disable_public_network',
        'trigger_access_vpcs': 'trigger_access_vpcs'
    }

    def __init__(self, disable_public_network=None, trigger_access_vpcs=None):
        """NetworkControlConfig

        The model defined in huaweicloud sdk

        :param disable_public_network: 禁止公网访问开关。
        :type disable_public_network: bool
        :param trigger_access_vpcs: 指定触发函数vpc配置。
        :type trigger_access_vpcs: list[:class:`huaweicloudsdkfunctiongraph.v2.VpcConfig`]
        """
        
        

        self._disable_public_network = None
        self._trigger_access_vpcs = None
        self.discriminator = None

        if disable_public_network is not None:
            self.disable_public_network = disable_public_network
        if trigger_access_vpcs is not None:
            self.trigger_access_vpcs = trigger_access_vpcs

    @property
    def disable_public_network(self):
        """Gets the disable_public_network of this NetworkControlConfig.

        禁止公网访问开关。

        :return: The disable_public_network of this NetworkControlConfig.
        :rtype: bool
        """
        return self._disable_public_network

    @disable_public_network.setter
    def disable_public_network(self, disable_public_network):
        """Sets the disable_public_network of this NetworkControlConfig.

        禁止公网访问开关。

        :param disable_public_network: The disable_public_network of this NetworkControlConfig.
        :type disable_public_network: bool
        """
        self._disable_public_network = disable_public_network

    @property
    def trigger_access_vpcs(self):
        """Gets the trigger_access_vpcs of this NetworkControlConfig.

        指定触发函数vpc配置。

        :return: The trigger_access_vpcs of this NetworkControlConfig.
        :rtype: list[:class:`huaweicloudsdkfunctiongraph.v2.VpcConfig`]
        """
        return self._trigger_access_vpcs

    @trigger_access_vpcs.setter
    def trigger_access_vpcs(self, trigger_access_vpcs):
        """Sets the trigger_access_vpcs of this NetworkControlConfig.

        指定触发函数vpc配置。

        :param trigger_access_vpcs: The trigger_access_vpcs of this NetworkControlConfig.
        :type trigger_access_vpcs: list[:class:`huaweicloudsdkfunctiongraph.v2.VpcConfig`]
        """
        self._trigger_access_vpcs = trigger_access_vpcs

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
        if not isinstance(other, NetworkControlConfig):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
