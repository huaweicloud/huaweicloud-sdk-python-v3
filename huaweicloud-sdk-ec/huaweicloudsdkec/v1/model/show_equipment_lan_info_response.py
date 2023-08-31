# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEquipmentLanInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'lan_interfaces': 'list[EquipmentLanItem]'
    }

    attribute_map = {
        'lan_interfaces': 'lan_interfaces'
    }

    def __init__(self, lan_interfaces=None):
        """ShowEquipmentLanInfoResponse

        The model defined in huaweicloud sdk

        :param lan_interfaces: 设备LAN口配置列表
        :type lan_interfaces: list[:class:`huaweicloudsdkec.v1.EquipmentLanItem`]
        """
        
        super(ShowEquipmentLanInfoResponse, self).__init__()

        self._lan_interfaces = None
        self.discriminator = None

        if lan_interfaces is not None:
            self.lan_interfaces = lan_interfaces

    @property
    def lan_interfaces(self):
        """Gets the lan_interfaces of this ShowEquipmentLanInfoResponse.

        设备LAN口配置列表

        :return: The lan_interfaces of this ShowEquipmentLanInfoResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.EquipmentLanItem`]
        """
        return self._lan_interfaces

    @lan_interfaces.setter
    def lan_interfaces(self, lan_interfaces):
        """Sets the lan_interfaces of this ShowEquipmentLanInfoResponse.

        设备LAN口配置列表

        :param lan_interfaces: The lan_interfaces of this ShowEquipmentLanInfoResponse.
        :type lan_interfaces: list[:class:`huaweicloudsdkec.v1.EquipmentLanItem`]
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
        if not isinstance(other, ShowEquipmentLanInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
