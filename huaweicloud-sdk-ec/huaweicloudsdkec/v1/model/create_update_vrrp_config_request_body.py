# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateUpdateVrrpConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'virtual_ip': 'str',
        'active_equipment_id': 'str',
        'active_interface_name': 'str',
        'standby_equipment_id': 'str',
        'standby_interface_name': 'str'
    }

    attribute_map = {
        'virtual_ip': 'virtual_ip',
        'active_equipment_id': 'active_equipment_id',
        'active_interface_name': 'active_interface_name',
        'standby_equipment_id': 'standby_equipment_id',
        'standby_interface_name': 'standby_interface_name'
    }

    def __init__(self, virtual_ip=None, active_equipment_id=None, active_interface_name=None, standby_equipment_id=None, standby_interface_name=None):
        r"""CreateUpdateVrrpConfigRequestBody

        The model defined in huaweicloud sdk

        :param virtual_ip: 虚IP
        :type virtual_ip: str
        :param active_equipment_id: 主设备ID
        :type active_equipment_id: str
        :param active_interface_name: 主设备接口名字
        :type active_interface_name: str
        :param standby_equipment_id: 备设备ID
        :type standby_equipment_id: str
        :param standby_interface_name: 备设备接口名字
        :type standby_interface_name: str
        """
        
        

        self._virtual_ip = None
        self._active_equipment_id = None
        self._active_interface_name = None
        self._standby_equipment_id = None
        self._standby_interface_name = None
        self.discriminator = None

        self.virtual_ip = virtual_ip
        self.active_equipment_id = active_equipment_id
        self.active_interface_name = active_interface_name
        self.standby_equipment_id = standby_equipment_id
        self.standby_interface_name = standby_interface_name

    @property
    def virtual_ip(self):
        r"""Gets the virtual_ip of this CreateUpdateVrrpConfigRequestBody.

        虚IP

        :return: The virtual_ip of this CreateUpdateVrrpConfigRequestBody.
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        r"""Sets the virtual_ip of this CreateUpdateVrrpConfigRequestBody.

        虚IP

        :param virtual_ip: The virtual_ip of this CreateUpdateVrrpConfigRequestBody.
        :type virtual_ip: str
        """
        self._virtual_ip = virtual_ip

    @property
    def active_equipment_id(self):
        r"""Gets the active_equipment_id of this CreateUpdateVrrpConfigRequestBody.

        主设备ID

        :return: The active_equipment_id of this CreateUpdateVrrpConfigRequestBody.
        :rtype: str
        """
        return self._active_equipment_id

    @active_equipment_id.setter
    def active_equipment_id(self, active_equipment_id):
        r"""Sets the active_equipment_id of this CreateUpdateVrrpConfigRequestBody.

        主设备ID

        :param active_equipment_id: The active_equipment_id of this CreateUpdateVrrpConfigRequestBody.
        :type active_equipment_id: str
        """
        self._active_equipment_id = active_equipment_id

    @property
    def active_interface_name(self):
        r"""Gets the active_interface_name of this CreateUpdateVrrpConfigRequestBody.

        主设备接口名字

        :return: The active_interface_name of this CreateUpdateVrrpConfigRequestBody.
        :rtype: str
        """
        return self._active_interface_name

    @active_interface_name.setter
    def active_interface_name(self, active_interface_name):
        r"""Sets the active_interface_name of this CreateUpdateVrrpConfigRequestBody.

        主设备接口名字

        :param active_interface_name: The active_interface_name of this CreateUpdateVrrpConfigRequestBody.
        :type active_interface_name: str
        """
        self._active_interface_name = active_interface_name

    @property
    def standby_equipment_id(self):
        r"""Gets the standby_equipment_id of this CreateUpdateVrrpConfigRequestBody.

        备设备ID

        :return: The standby_equipment_id of this CreateUpdateVrrpConfigRequestBody.
        :rtype: str
        """
        return self._standby_equipment_id

    @standby_equipment_id.setter
    def standby_equipment_id(self, standby_equipment_id):
        r"""Sets the standby_equipment_id of this CreateUpdateVrrpConfigRequestBody.

        备设备ID

        :param standby_equipment_id: The standby_equipment_id of this CreateUpdateVrrpConfigRequestBody.
        :type standby_equipment_id: str
        """
        self._standby_equipment_id = standby_equipment_id

    @property
    def standby_interface_name(self):
        r"""Gets the standby_interface_name of this CreateUpdateVrrpConfigRequestBody.

        备设备接口名字

        :return: The standby_interface_name of this CreateUpdateVrrpConfigRequestBody.
        :rtype: str
        """
        return self._standby_interface_name

    @standby_interface_name.setter
    def standby_interface_name(self, standby_interface_name):
        r"""Sets the standby_interface_name of this CreateUpdateVrrpConfigRequestBody.

        备设备接口名字

        :param standby_interface_name: The standby_interface_name of this CreateUpdateVrrpConfigRequestBody.
        :type standby_interface_name: str
        """
        self._standby_interface_name = standby_interface_name

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
        if not isinstance(other, CreateUpdateVrrpConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
