# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProxyUpgradeProxyVersionRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'source_version': 'str',
        'target_version': 'str'
    }

    attribute_map = {
        'source_version': 'source_version',
        'target_version': 'target_version'
    }

    def __init__(self, source_version=None, target_version=None):
        r"""ProxyUpgradeProxyVersionRequest

        The model defined in huaweicloud sdk

        :param source_version: 升级前源内核版本号
        :type source_version: str
        :param target_version: 目标升级内核版本号
        :type target_version: str
        """
        
        

        self._source_version = None
        self._target_version = None
        self.discriminator = None

        self.source_version = source_version
        self.target_version = target_version

    @property
    def source_version(self):
        r"""Gets the source_version of this ProxyUpgradeProxyVersionRequest.

        升级前源内核版本号

        :return: The source_version of this ProxyUpgradeProxyVersionRequest.
        :rtype: str
        """
        return self._source_version

    @source_version.setter
    def source_version(self, source_version):
        r"""Sets the source_version of this ProxyUpgradeProxyVersionRequest.

        升级前源内核版本号

        :param source_version: The source_version of this ProxyUpgradeProxyVersionRequest.
        :type source_version: str
        """
        self._source_version = source_version

    @property
    def target_version(self):
        r"""Gets the target_version of this ProxyUpgradeProxyVersionRequest.

        目标升级内核版本号

        :return: The target_version of this ProxyUpgradeProxyVersionRequest.
        :rtype: str
        """
        return self._target_version

    @target_version.setter
    def target_version(self, target_version):
        r"""Sets the target_version of this ProxyUpgradeProxyVersionRequest.

        目标升级内核版本号

        :param target_version: The target_version of this ProxyUpgradeProxyVersionRequest.
        :type target_version: str
        """
        self._target_version = target_version

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
        if not isinstance(other, ProxyUpgradeProxyVersionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
