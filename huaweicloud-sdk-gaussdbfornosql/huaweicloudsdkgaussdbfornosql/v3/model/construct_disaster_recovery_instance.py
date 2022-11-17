# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConstructDisasterRecoveryInstance:

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
        'region_code': 'str',
        'subnet_cidrs': 'list[str]',
        'node_ips': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'region_code': 'region_code',
        'subnet_cidrs': 'subnet_cidrs',
        'node_ips': 'node_ips'
    }

    def __init__(self, id=None, region_code=None, subnet_cidrs=None, node_ips=None):
        """ConstructDisasterRecoveryInstance

        The model defined in huaweicloud sdk

        :param id: 容灾实例的ID。
        :type id: str
        :param region_code: 容灾实例所在Region的code。
        :type region_code: str
        :param subnet_cidrs: 与当前实例建立容灾关系实例所在子网的CIDR列表。
        :type subnet_cidrs: list[str]
        :param node_ips: 与当前实例建立容灾关系实例的所有节点的IP列表。
        :type node_ips: list[str]
        """
        
        

        self._id = None
        self._region_code = None
        self._subnet_cidrs = None
        self._node_ips = None
        self.discriminator = None

        self.id = id
        self.region_code = region_code
        self.subnet_cidrs = subnet_cidrs
        self.node_ips = node_ips

    @property
    def id(self):
        """Gets the id of this ConstructDisasterRecoveryInstance.

        容灾实例的ID。

        :return: The id of this ConstructDisasterRecoveryInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ConstructDisasterRecoveryInstance.

        容灾实例的ID。

        :param id: The id of this ConstructDisasterRecoveryInstance.
        :type id: str
        """
        self._id = id

    @property
    def region_code(self):
        """Gets the region_code of this ConstructDisasterRecoveryInstance.

        容灾实例所在Region的code。

        :return: The region_code of this ConstructDisasterRecoveryInstance.
        :rtype: str
        """
        return self._region_code

    @region_code.setter
    def region_code(self, region_code):
        """Sets the region_code of this ConstructDisasterRecoveryInstance.

        容灾实例所在Region的code。

        :param region_code: The region_code of this ConstructDisasterRecoveryInstance.
        :type region_code: str
        """
        self._region_code = region_code

    @property
    def subnet_cidrs(self):
        """Gets the subnet_cidrs of this ConstructDisasterRecoveryInstance.

        与当前实例建立容灾关系实例所在子网的CIDR列表。

        :return: The subnet_cidrs of this ConstructDisasterRecoveryInstance.
        :rtype: list[str]
        """
        return self._subnet_cidrs

    @subnet_cidrs.setter
    def subnet_cidrs(self, subnet_cidrs):
        """Sets the subnet_cidrs of this ConstructDisasterRecoveryInstance.

        与当前实例建立容灾关系实例所在子网的CIDR列表。

        :param subnet_cidrs: The subnet_cidrs of this ConstructDisasterRecoveryInstance.
        :type subnet_cidrs: list[str]
        """
        self._subnet_cidrs = subnet_cidrs

    @property
    def node_ips(self):
        """Gets the node_ips of this ConstructDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的所有节点的IP列表。

        :return: The node_ips of this ConstructDisasterRecoveryInstance.
        :rtype: list[str]
        """
        return self._node_ips

    @node_ips.setter
    def node_ips(self, node_ips):
        """Sets the node_ips of this ConstructDisasterRecoveryInstance.

        与当前实例建立容灾关系实例的所有节点的IP列表。

        :param node_ips: The node_ips of this ConstructDisasterRecoveryInstance.
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
        if not isinstance(other, ConstructDisasterRecoveryInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
