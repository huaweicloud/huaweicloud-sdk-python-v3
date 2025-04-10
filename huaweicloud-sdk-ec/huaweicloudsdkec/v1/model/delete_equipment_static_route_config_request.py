# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteEquipmentStaticRouteConfigRequest:

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
        'prefix': 'str',
        'next_hop': 'str',
        'interface_name': 'str'
    }

    attribute_map = {
        'ieg_id': 'ieg_id',
        'equipment_id': 'equipment_id',
        'prefix': 'prefix',
        'next_hop': 'next_hop',
        'interface_name': 'interface_name'
    }

    def __init__(self, ieg_id=None, equipment_id=None, prefix=None, next_hop=None, interface_name=None):
        r"""DeleteEquipmentStaticRouteConfigRequest

        The model defined in huaweicloud sdk

        :param ieg_id: 智能企业网关ID
        :type ieg_id: str
        :param equipment_id: 智能企业网关设备ID
        :type equipment_id: str
        :param prefix: 目标网络
        :type prefix: str
        :param next_hop: 下一跳地址
        :type next_hop: str
        :param interface_name: 接口名字
        :type interface_name: str
        """
        
        

        self._ieg_id = None
        self._equipment_id = None
        self._prefix = None
        self._next_hop = None
        self._interface_name = None
        self.discriminator = None

        self.ieg_id = ieg_id
        self.equipment_id = equipment_id
        self.prefix = prefix
        self.next_hop = next_hop
        self.interface_name = interface_name

    @property
    def ieg_id(self):
        r"""Gets the ieg_id of this DeleteEquipmentStaticRouteConfigRequest.

        智能企业网关ID

        :return: The ieg_id of this DeleteEquipmentStaticRouteConfigRequest.
        :rtype: str
        """
        return self._ieg_id

    @ieg_id.setter
    def ieg_id(self, ieg_id):
        r"""Sets the ieg_id of this DeleteEquipmentStaticRouteConfigRequest.

        智能企业网关ID

        :param ieg_id: The ieg_id of this DeleteEquipmentStaticRouteConfigRequest.
        :type ieg_id: str
        """
        self._ieg_id = ieg_id

    @property
    def equipment_id(self):
        r"""Gets the equipment_id of this DeleteEquipmentStaticRouteConfigRequest.

        智能企业网关设备ID

        :return: The equipment_id of this DeleteEquipmentStaticRouteConfigRequest.
        :rtype: str
        """
        return self._equipment_id

    @equipment_id.setter
    def equipment_id(self, equipment_id):
        r"""Sets the equipment_id of this DeleteEquipmentStaticRouteConfigRequest.

        智能企业网关设备ID

        :param equipment_id: The equipment_id of this DeleteEquipmentStaticRouteConfigRequest.
        :type equipment_id: str
        """
        self._equipment_id = equipment_id

    @property
    def prefix(self):
        r"""Gets the prefix of this DeleteEquipmentStaticRouteConfigRequest.

        目标网络

        :return: The prefix of this DeleteEquipmentStaticRouteConfigRequest.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this DeleteEquipmentStaticRouteConfigRequest.

        目标网络

        :param prefix: The prefix of this DeleteEquipmentStaticRouteConfigRequest.
        :type prefix: str
        """
        self._prefix = prefix

    @property
    def next_hop(self):
        r"""Gets the next_hop of this DeleteEquipmentStaticRouteConfigRequest.

        下一跳地址

        :return: The next_hop of this DeleteEquipmentStaticRouteConfigRequest.
        :rtype: str
        """
        return self._next_hop

    @next_hop.setter
    def next_hop(self, next_hop):
        r"""Sets the next_hop of this DeleteEquipmentStaticRouteConfigRequest.

        下一跳地址

        :param next_hop: The next_hop of this DeleteEquipmentStaticRouteConfigRequest.
        :type next_hop: str
        """
        self._next_hop = next_hop

    @property
    def interface_name(self):
        r"""Gets the interface_name of this DeleteEquipmentStaticRouteConfigRequest.

        接口名字

        :return: The interface_name of this DeleteEquipmentStaticRouteConfigRequest.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        r"""Sets the interface_name of this DeleteEquipmentStaticRouteConfigRequest.

        接口名字

        :param interface_name: The interface_name of this DeleteEquipmentStaticRouteConfigRequest.
        :type interface_name: str
        """
        self._interface_name = interface_name

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
        if not isinstance(other, DeleteEquipmentStaticRouteConfigRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
