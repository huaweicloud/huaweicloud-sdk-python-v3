# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEquipmentWanInfoResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'wan_interfaces': 'list[EquipmentWanItem]'
    }

    attribute_map = {
        'wan_interfaces': 'wan_interfaces'
    }

    def __init__(self, wan_interfaces=None):
        """ShowEquipmentWanInfoResponse

        The model defined in huaweicloud sdk

        :param wan_interfaces: 设备WAN口配置列表
        :type wan_interfaces: list[:class:`huaweicloudsdkec.v1.EquipmentWanItem`]
        """
        
        super(ShowEquipmentWanInfoResponse, self).__init__()

        self._wan_interfaces = None
        self.discriminator = None

        if wan_interfaces is not None:
            self.wan_interfaces = wan_interfaces

    @property
    def wan_interfaces(self):
        """Gets the wan_interfaces of this ShowEquipmentWanInfoResponse.

        设备WAN口配置列表

        :return: The wan_interfaces of this ShowEquipmentWanInfoResponse.
        :rtype: list[:class:`huaweicloudsdkec.v1.EquipmentWanItem`]
        """
        return self._wan_interfaces

    @wan_interfaces.setter
    def wan_interfaces(self, wan_interfaces):
        """Sets the wan_interfaces of this ShowEquipmentWanInfoResponse.

        设备WAN口配置列表

        :param wan_interfaces: The wan_interfaces of this ShowEquipmentWanInfoResponse.
        :type wan_interfaces: list[:class:`huaweicloudsdkec.v1.EquipmentWanItem`]
        """
        self._wan_interfaces = wan_interfaces

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
        if not isinstance(other, ShowEquipmentWanInfoResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
