# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEquipmentInterfaceNameResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interface_names': 'list[str]'
    }

    attribute_map = {
        'interface_names': 'interface_names'
    }

    def __init__(self, interface_names=None):
        r"""ListEquipmentInterfaceNameResponse

        The model defined in huaweicloud sdk

        :param interface_names: 设备接口名字列表
        :type interface_names: list[str]
        """
        
        super(ListEquipmentInterfaceNameResponse, self).__init__()

        self._interface_names = None
        self.discriminator = None

        if interface_names is not None:
            self.interface_names = interface_names

    @property
    def interface_names(self):
        r"""Gets the interface_names of this ListEquipmentInterfaceNameResponse.

        设备接口名字列表

        :return: The interface_names of this ListEquipmentInterfaceNameResponse.
        :rtype: list[str]
        """
        return self._interface_names

    @interface_names.setter
    def interface_names(self, interface_names):
        r"""Sets the interface_names of this ListEquipmentInterfaceNameResponse.

        设备接口名字列表

        :param interface_names: The interface_names of this ListEquipmentInterfaceNameResponse.
        :type interface_names: list[str]
        """
        self._interface_names = interface_names

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
        if not isinstance(other, ListEquipmentInterfaceNameResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
