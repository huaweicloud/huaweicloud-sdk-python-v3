# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PrecheckDisasterRecoveryInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'vpc_cidr': 'str',
        'spec_code': 'str',
        'node_ips': 'list[str]'
    }

    attribute_map = {
        'vpc_cidr': 'vpc_cidr',
        'spec_code': 'spec_code',
        'node_ips': 'node_ips'
    }

    def __init__(self, vpc_cidr=None, spec_code=None, node_ips=None):
        """PrecheckDisasterRecoveryInstance

        The model defined in huaweicloud sdk

        :param vpc_cidr: 与当前实例建立容灾关系实例的vpc网段。
        :type vpc_cidr: str
        :param spec_code: 与当前实例建立容灾关系实例的规格码。
        :type spec_code: str
        :param node_ips: 与当前实例建立容灾关系实例的节点IP列表。
        :type node_ips: list[str]
        """
        
        

        self._vpc_cidr = None
        self._spec_code = None
        self._node_ips = None
        self.discriminator = None

        self.vpc_cidr = vpc_cidr
        self.spec_code = spec_code
        self.node_ips = node_ips

    @property
    def vpc_cidr(self):
        """Gets the vpc_cidr of this PrecheckDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的vpc网段。

        :return: The vpc_cidr of this PrecheckDisasterRecoveryInstance.
        :rtype: str
        """
        return self._vpc_cidr

    @vpc_cidr.setter
    def vpc_cidr(self, vpc_cidr):
        """Sets the vpc_cidr of this PrecheckDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的vpc网段。

        :param vpc_cidr: The vpc_cidr of this PrecheckDisasterRecoveryInstance.
        :type vpc_cidr: str
        """
        self._vpc_cidr = vpc_cidr

    @property
    def spec_code(self):
        """Gets the spec_code of this PrecheckDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的规格码。

        :return: The spec_code of this PrecheckDisasterRecoveryInstance.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        """Sets the spec_code of this PrecheckDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的规格码。

        :param spec_code: The spec_code of this PrecheckDisasterRecoveryInstance.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def node_ips(self):
        """Gets the node_ips of this PrecheckDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的节点IP列表。

        :return: The node_ips of this PrecheckDisasterRecoveryInstance.
        :rtype: list[str]
        """
        return self._node_ips

    @node_ips.setter
    def node_ips(self, node_ips):
        """Sets the node_ips of this PrecheckDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的节点IP列表。

        :param node_ips: The node_ips of this PrecheckDisasterRecoveryInstance.
        :type node_ips: list[str]
        """
        self._node_ips = node_ips

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
        if not isinstance(other, PrecheckDisasterRecoveryInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
