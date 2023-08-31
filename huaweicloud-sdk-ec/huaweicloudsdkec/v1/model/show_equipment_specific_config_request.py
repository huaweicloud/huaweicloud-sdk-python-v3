# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEquipmentSpecificConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'equipment_type': 'str'
    }

    attribute_map = {
        'equipment_type': 'equipment_type'
    }

    def __init__(self, equipment_type=None):
        """ShowEquipmentSpecificConfigRequest

        The model defined in huaweicloud sdk

        :param equipment_type: 设备类型
        :type equipment_type: str
        """
        
        

        self._equipment_type = None
        self.discriminator = None

        self.equipment_type = equipment_type

    @property
    def equipment_type(self):
        """Gets the equipment_type of this ShowEquipmentSpecificConfigRequest.

        设备类型

        :return: The equipment_type of this ShowEquipmentSpecificConfigRequest.
        :rtype: str
        """
        return self._equipment_type

    @equipment_type.setter
    def equipment_type(self, equipment_type):
        """Sets the equipment_type of this ShowEquipmentSpecificConfigRequest.

        设备类型

        :param equipment_type: The equipment_type of this ShowEquipmentSpecificConfigRequest.
        :type equipment_type: str
        """
        self._equipment_type = equipment_type

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
        if not isinstance(other, ShowEquipmentSpecificConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
