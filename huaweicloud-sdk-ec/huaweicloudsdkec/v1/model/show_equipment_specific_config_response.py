# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEquipmentSpecificConfigResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'type': 'str',
        'wan_interfaces': 'list[str]',
        'lte_interfaces': 'list[str]',
        'lan_interfaces': 'list[str]'
    }

    attribute_map = {
        'type': 'type',
        'wan_interfaces': 'wan_interfaces',
        'lte_interfaces': 'lte_interfaces',
        'lan_interfaces': 'lan_interfaces'
    }

    def __init__(self, type=None, wan_interfaces=None, lte_interfaces=None, lan_interfaces=None):
        """ShowEquipmentSpecificConfigResponse

        The model defined in huaweicloud sdk

        :param type: 设备类型
        :type type: str
        :param wan_interfaces: WAN口列表
        :type wan_interfaces: list[str]
        :param lte_interfaces: LTE口列表
        :type lte_interfaces: list[str]
        :param lan_interfaces: LAN口列表
        :type lan_interfaces: list[str]
        """
        
        super(ShowEquipmentSpecificConfigResponse, self).__init__()

        self._type = None
        self._wan_interfaces = None
        self._lte_interfaces = None
        self._lan_interfaces = None
        self.discriminator = None

        if type is not None:
            self.type = type
        if wan_interfaces is not None:
            self.wan_interfaces = wan_interfaces
        if lte_interfaces is not None:
            self.lte_interfaces = lte_interfaces
        if lan_interfaces is not None:
            self.lan_interfaces = lan_interfaces

    @property
    def type(self):
        """Gets the type of this ShowEquipmentSpecificConfigResponse.

        设备类型

        :return: The type of this ShowEquipmentSpecificConfigResponse.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEquipmentSpecificConfigResponse.

        设备类型

        :param type: The type of this ShowEquipmentSpecificConfigResponse.
        :type type: str
        """
        self._type = type

    @property
    def wan_interfaces(self):
        """Gets the wan_interfaces of this ShowEquipmentSpecificConfigResponse.

        WAN口列表

        :return: The wan_interfaces of this ShowEquipmentSpecificConfigResponse.
        :rtype: list[str]
        """
        return self._wan_interfaces

    @wan_interfaces.setter
    def wan_interfaces(self, wan_interfaces):
        """Sets the wan_interfaces of this ShowEquipmentSpecificConfigResponse.

        WAN口列表

        :param wan_interfaces: The wan_interfaces of this ShowEquipmentSpecificConfigResponse.
        :type wan_interfaces: list[str]
        """
        self._wan_interfaces = wan_interfaces

    @property
    def lte_interfaces(self):
        """Gets the lte_interfaces of this ShowEquipmentSpecificConfigResponse.

        LTE口列表

        :return: The lte_interfaces of this ShowEquipmentSpecificConfigResponse.
        :rtype: list[str]
        """
        return self._lte_interfaces

    @lte_interfaces.setter
    def lte_interfaces(self, lte_interfaces):
        """Sets the lte_interfaces of this ShowEquipmentSpecificConfigResponse.

        LTE口列表

        :param lte_interfaces: The lte_interfaces of this ShowEquipmentSpecificConfigResponse.
        :type lte_interfaces: list[str]
        """
        self._lte_interfaces = lte_interfaces

    @property
    def lan_interfaces(self):
        """Gets the lan_interfaces of this ShowEquipmentSpecificConfigResponse.

        LAN口列表

        :return: The lan_interfaces of this ShowEquipmentSpecificConfigResponse.
        :rtype: list[str]
        """
        return self._lan_interfaces

    @lan_interfaces.setter
    def lan_interfaces(self, lan_interfaces):
        """Sets the lan_interfaces of this ShowEquipmentSpecificConfigResponse.

        LAN口列表

        :param lan_interfaces: The lan_interfaces of this ShowEquipmentSpecificConfigResponse.
        :type lan_interfaces: list[str]
        """
        self._lan_interfaces = lan_interfaces

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
        if not isinstance(other, ShowEquipmentSpecificConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
