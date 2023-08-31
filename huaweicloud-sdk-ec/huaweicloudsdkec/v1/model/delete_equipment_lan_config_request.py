# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEquipmentLanConfigRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ieg_id': 'str',
        'equipment_id': 'str',
        'interface_name': 'str',
        'vlan_id': 'str'
    }

    attribute_map = {
        'ieg_id': 'ieg_id',
        'equipment_id': 'equipment_id',
        'interface_name': 'interface_name',
        'vlan_id': 'vlan_id'
    }

    def __init__(self, ieg_id=None, equipment_id=None, interface_name=None, vlan_id=None):
        """DeleteEquipmentLanConfigRequest

        The model defined in huaweicloud sdk

        :param ieg_id: 智能企业网关ID
        :type ieg_id: str
        :param equipment_id: 智能企业网关设备ID
        :type equipment_id: str
        :param interface_name: 接口名字
        :type interface_name: str
        :param vlan_id: VlanID
        :type vlan_id: str
        """
        
        

        self._ieg_id = None
        self._equipment_id = None
        self._interface_name = None
        self._vlan_id = None
        self.discriminator = None

        self.ieg_id = ieg_id
        self.equipment_id = equipment_id
        self.interface_name = interface_name
        if vlan_id is not None:
            self.vlan_id = vlan_id

    @property
    def ieg_id(self):
        """Gets the ieg_id of this DeleteEquipmentLanConfigRequest.

        智能企业网关ID

        :return: The ieg_id of this DeleteEquipmentLanConfigRequest.
        :rtype: str
        """
        return self._ieg_id

    @ieg_id.setter
    def ieg_id(self, ieg_id):
        """Sets the ieg_id of this DeleteEquipmentLanConfigRequest.

        智能企业网关ID

        :param ieg_id: The ieg_id of this DeleteEquipmentLanConfigRequest.
        :type ieg_id: str
        """
        self._ieg_id = ieg_id

    @property
    def equipment_id(self):
        """Gets the equipment_id of this DeleteEquipmentLanConfigRequest.

        智能企业网关设备ID

        :return: The equipment_id of this DeleteEquipmentLanConfigRequest.
        :rtype: str
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        """Sets the equipment_id of this DeleteEquipmentLanConfigRequest.

        智能企业网关设备ID

        :param equipment_id: The equipment_id of this DeleteEquipmentLanConfigRequest.
        :type equipment_id: str
        """
        self._equipment_id = equipment_id

    @property
    def interface_name(self):
        """Gets the interface_name of this DeleteEquipmentLanConfigRequest.

        接口名字

        :return: The interface_name of this DeleteEquipmentLanConfigRequest.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """Sets the interface_name of this DeleteEquipmentLanConfigRequest.

        接口名字

        :param interface_name: The interface_name of this DeleteEquipmentLanConfigRequest.
        :type interface_name: str
        """
        self._interface_name = interface_name

    @property
    def vlan_id(self):
        """Gets the vlan_id of this DeleteEquipmentLanConfigRequest.

        VlanID

        :return: The vlan_id of this DeleteEquipmentLanConfigRequest.
        :rtype: str
        """
        return self._vlan_id

    @vlan_id.setter
    def vlan_id(self, vlan_id):
        """Sets the vlan_id of this DeleteEquipmentLanConfigRequest.

        VlanID

        :param vlan_id: The vlan_id of this DeleteEquipmentLanConfigRequest.
        :type vlan_id: str
        """
        self._vlan_id = vlan_id

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
        if not isinstance(other, DeleteEquipmentLanConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
