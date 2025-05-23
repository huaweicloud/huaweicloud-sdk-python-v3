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
        'equipment_id': 'str'
    }

    attribute_map = {
        'equipment_id': 'equipment_id'
    }

    def __init__(self, equipment_id=None):
        r"""ShowEquipmentSpecificConfigRequest

        The model defined in huaweicloud sdk

        :param equipment_id: 智能企业网关设备ID
        :type equipment_id: str
        """
        
        

        self._equipment_id = None
        self.discriminator = None

        self.equipment_id = equipment_id

    @property
    def equipment_id(self):
        r"""Gets the equipment_id of this ShowEquipmentSpecificConfigRequest.

        智能企业网关设备ID

        :return: The equipment_id of this ShowEquipmentSpecificConfigRequest.
        :rtype: str
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        r"""Sets the equipment_id of this ShowEquipmentSpecificConfigRequest.

        智能企业网关设备ID

        :param equipment_id: The equipment_id of this ShowEquipmentSpecificConfigRequest.
        :type equipment_id: str
        """
        self._equipment_id = equipment_id

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
