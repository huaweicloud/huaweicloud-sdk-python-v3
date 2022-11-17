# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MigrateSubNetworkInterfaceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_id': 'str',
        'sub_network_interfaces': 'list[dict(str, str)]'
    }

    attribute_map = {
        'parent_id': 'parent_id',
        'sub_network_interfaces': 'sub_network_interfaces'
    }

    def __init__(self, parent_id=None, sub_network_interfaces=None):
        """MigrateSubNetworkInterfaceOption

        The model defined in huaweicloud sdk

        :param parent_id: 目的宿主网卡ID
        :type parent_id: str
        :param sub_network_interfaces: 待迁移辅助弹性网卡列表
        :type sub_network_interfaces: list[dict(str, str)]
        """
        
        

        self._parent_id = None
        self._sub_network_interfaces = None
        self.discriminator = None

        self.parent_id = parent_id
        self.sub_network_interfaces = sub_network_interfaces

    @property
    def parent_id(self):
        """Gets the parent_id of this MigrateSubNetworkInterfaceOption.

        目的宿主网卡ID

        :return: The parent_id of this MigrateSubNetworkInterfaceOption.
        :rtype: str
        """
        return self._parent_id

    @parent_id.setter
    def parent_id(self, parent_id):
        """Sets the parent_id of this MigrateSubNetworkInterfaceOption.

        目的宿主网卡ID

        :param parent_id: The parent_id of this MigrateSubNetworkInterfaceOption.
        :type parent_id: str
        """
        self._parent_id = parent_id

    @property
    def sub_network_interfaces(self):
        """Gets the sub_network_interfaces of this MigrateSubNetworkInterfaceOption.

        待迁移辅助弹性网卡列表

        :return: The sub_network_interfaces of this MigrateSubNetworkInterfaceOption.
        :rtype: list[dict(str, str)]
        """
        return self._sub_network_interfaces

    @sub_network_interfaces.setter
    def sub_network_interfaces(self, sub_network_interfaces):
        """Sets the sub_network_interfaces of this MigrateSubNetworkInterfaceOption.

        待迁移辅助弹性网卡列表

        :param sub_network_interfaces: The sub_network_interfaces of this MigrateSubNetworkInterfaceOption.
        :type sub_network_interfaces: list[dict(str, str)]
        """
        self._sub_network_interfaces = sub_network_interfaces

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
        if not isinstance(other, MigrateSubNetworkInterfaceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
