# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ProtectableReplicationCapabilitiesRespRegion:

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
        'replication_destinations': 'list[str]'
    }

    attribute_map = {
        'name': 'name',
        'replication_destinations': 'replication_destinations'
    }

    def __init__(self, name=None, replication_destinations=None):
        """ProtectableReplicationCapabilitiesRespRegion

        The model defined in huaweicloud sdk

        :param name: 云服务所在的区域
        :type name: str
        :param replication_destinations: 支持复制的目标区域列表
        :type replication_destinations: list[str]
        """
        
        

        self._name = None
        self._replication_destinations = None
        self.discriminator = None

        self.name = name
        self.replication_destinations = replication_destinations

    @property
    def name(self):
        """Gets the name of this ProtectableReplicationCapabilitiesRespRegion.

        云服务所在的区域

        :return: The name of this ProtectableReplicationCapabilitiesRespRegion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProtectableReplicationCapabilitiesRespRegion.

        云服务所在的区域

        :param name: The name of this ProtectableReplicationCapabilitiesRespRegion.
        :type name: str
        """
        self._name = name

    @property
    def replication_destinations(self):
        """Gets the replication_destinations of this ProtectableReplicationCapabilitiesRespRegion.

        支持复制的目标区域列表

        :return: The replication_destinations of this ProtectableReplicationCapabilitiesRespRegion.
        :rtype: list[str]
        """
        return self._replication_destinations

    @replication_destinations.setter
    def replication_destinations(self, replication_destinations):
        """Sets the replication_destinations of this ProtectableReplicationCapabilitiesRespRegion.

        支持复制的目标区域列表

        :param replication_destinations: The replication_destinations of this ProtectableReplicationCapabilitiesRespRegion.
        :type replication_destinations: list[str]
        """
        self._replication_destinations = replication_destinations

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
        if not isinstance(other, ProtectableReplicationCapabilitiesRespRegion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
