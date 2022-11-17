# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteVirtualInterfaceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_interface_id': 'str'
    }

    attribute_map = {
        'virtual_interface_id': 'virtual_interface_id'
    }

    def __init__(self, virtual_interface_id=None):
        """DeleteVirtualInterfaceRequest

        The model defined in huaweicloud sdk

        :param virtual_interface_id: 虚拟接口ID。
        :type virtual_interface_id: str
        """
        
        

        self._virtual_interface_id = None
        self.discriminator = None

        self.virtual_interface_id = virtual_interface_id

    @property
    def virtual_interface_id(self):
        """Gets the virtual_interface_id of this DeleteVirtualInterfaceRequest.

        虚拟接口ID。

        :return: The virtual_interface_id of this DeleteVirtualInterfaceRequest.
        :rtype: str
        """
        return self._virtual_interface_id

    @virtual_interface_id.setter
    def virtual_interface_id(self, virtual_interface_id):
        """Sets the virtual_interface_id of this DeleteVirtualInterfaceRequest.

        虚拟接口ID。

        :param virtual_interface_id: The virtual_interface_id of this DeleteVirtualInterfaceRequest.
        :type virtual_interface_id: str
        """
        self._virtual_interface_id = virtual_interface_id

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
        if not isinstance(other, DeleteVirtualInterfaceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
