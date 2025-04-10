# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EquipmentActivate:

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
        'type': 'str',
        'esn': 'str',
        'ha_type': 'str'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'esn': 'esn',
        'ha_type': 'ha_type'
    }

    def __init__(self, name=None, type=None, esn=None, ha_type=None):
        r"""EquipmentActivate

        The model defined in huaweicloud sdk

        :param name: 设备名称
        :type name: str
        :param type: 设备类型
        :type type: str
        :param esn: esn
        :type esn: str
        :param ha_type: 高可用类型
        :type ha_type: str
        """
        
        

        self._name = None
        self._type = None
        self._esn = None
        self._ha_type = None
        self.discriminator = None

        self.name = name
        self.type = type
        self.esn = esn
        self.ha_type = ha_type

    @property
    def name(self):
        r"""Gets the name of this EquipmentActivate.

        设备名称

        :return: The name of this EquipmentActivate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EquipmentActivate.

        设备名称

        :param name: The name of this EquipmentActivate.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this EquipmentActivate.

        设备类型

        :return: The type of this EquipmentActivate.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this EquipmentActivate.

        设备类型

        :param type: The type of this EquipmentActivate.
        :type type: str
        """
        self._type = type

    @property
    def esn(self):
        r"""Gets the esn of this EquipmentActivate.

        esn

        :return: The esn of this EquipmentActivate.
        :rtype: str
        """
        return self._esn

    @esn.setter
    def esn(self, esn):
        r"""Sets the esn of this EquipmentActivate.

        esn

        :param esn: The esn of this EquipmentActivate.
        :type esn: str
        """
        self._esn = esn

    @property
    def ha_type(self):
        r"""Gets the ha_type of this EquipmentActivate.

        高可用类型

        :return: The ha_type of this EquipmentActivate.
        :rtype: str
        """
        return self._ha_type

    @ha_type.setter
    def ha_type(self, ha_type):
        r"""Sets the ha_type of this EquipmentActivate.

        高可用类型

        :param ha_type: The ha_type of this EquipmentActivate.
        :type ha_type: str
        """
        self._ha_type = ha_type

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
        if not isinstance(other, EquipmentActivate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
