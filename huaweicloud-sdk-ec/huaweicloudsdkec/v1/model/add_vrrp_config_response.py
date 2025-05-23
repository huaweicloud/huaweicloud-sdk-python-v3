# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddVrrpConfigResponse(SdkResponse):

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
        'virtual_router_id': 'int',
        'virtual_ip': 'str',
        'active_equipment_id': 'str',
        'active_interface_name': 'str',
        'standby_equipment_id': 'str',
        'standby_interface_name': 'str'
    }

    attribute_map = {
        'ieg_id': 'ieg_id',
        'virtual_router_id': 'virtual_router_id',
        'virtual_ip': 'virtual_ip',
        'active_equipment_id': 'active_equipment_id',
        'active_interface_name': 'active_interface_name',
        'standby_equipment_id': 'standby_equipment_id',
        'standby_interface_name': 'standby_interface_name'
    }

    def __init__(self, ieg_id=None, virtual_router_id=None, virtual_ip=None, active_equipment_id=None, active_interface_name=None, standby_equipment_id=None, standby_interface_name=None):
        r"""AddVrrpConfigResponse

        The model defined in huaweicloud sdk

        :param ieg_id: 智能企业网关ID
        :type ieg_id: str
        :param virtual_router_id: 虚路由ID
        :type virtual_router_id: int
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
        
        super(AddVrrpConfigResponse, self).__init__()

        self._ieg_id = None
        self._virtual_router_id = None
        self._virtual_ip = None
        self._active_equipment_id = None
        self._active_interface_name = None
        self._standby_equipment_id = None
        self._standby_interface_name = None
        self.discriminator = None

        if ieg_id is not None:
            self.ieg_id = ieg_id
        if virtual_router_id is not None:
            self.virtual_router_id = virtual_router_id
        if virtual_ip is not None:
            self.virtual_ip = virtual_ip
        if active_equipment_id is not None:
            self.active_equipment_id = active_equipment_id
        if active_interface_name is not None:
            self.active_interface_name = active_interface_name
        if standby_equipment_id is not None:
            self.standby_equipment_id = standby_equipment_id
        if standby_interface_name is not None:
            self.standby_interface_name = standby_interface_name

    @property
    def ieg_id(self):
        r"""Gets the ieg_id of this AddVrrpConfigResponse.

        智能企业网关ID

        :return: The ieg_id of this AddVrrpConfigResponse.
        :rtype: str
        """
        return self._ieg_id

    @ieg_id.setter
    def ieg_id(self, ieg_id):
        r"""Sets the ieg_id of this AddVrrpConfigResponse.

        智能企业网关ID

        :param ieg_id: The ieg_id of this AddVrrpConfigResponse.
        :type ieg_id: str
        """
        self._ieg_id = ieg_id

    @property
    def virtual_router_id(self):
        r"""Gets the virtual_router_id of this AddVrrpConfigResponse.

        虚路由ID

        :return: The virtual_router_id of this AddVrrpConfigResponse.
        :rtype: int
        """
        return self._virtual_router_id

    @virtual_router_id.setter
    def virtual_router_id(self, virtual_router_id):
        r"""Sets the virtual_router_id of this AddVrrpConfigResponse.

        虚路由ID

        :param virtual_router_id: The virtual_router_id of this AddVrrpConfigResponse.
        :type virtual_router_id: int
        """
        self._virtual_router_id = virtual_router_id

    @property
    def virtual_ip(self):
        r"""Gets the virtual_ip of this AddVrrpConfigResponse.

        虚IP

        :return: The virtual_ip of this AddVrrpConfigResponse.
        :rtype: str
        """
        return self._virtual_ip

    @virtual_ip.setter
    def virtual_ip(self, virtual_ip):
        r"""Sets the virtual_ip of this AddVrrpConfigResponse.

        虚IP

        :param virtual_ip: The virtual_ip of this AddVrrpConfigResponse.
        :type virtual_ip: str
        """
        self._virtual_ip = virtual_ip

    @property
    def active_equipment_id(self):
        r"""Gets the active_equipment_id of this AddVrrpConfigResponse.

        主设备ID

        :return: The active_equipment_id of this AddVrrpConfigResponse.
        :rtype: str
        """
        return self._active_equipment_id

    @active_equipment_id.setter
    def active_equipment_id(self, active_equipment_id):
        r"""Sets the active_equipment_id of this AddVrrpConfigResponse.

        主设备ID

        :param active_equipment_id: The active_equipment_id of this AddVrrpConfigResponse.
        :type active_equipment_id: str
        """
        self._active_equipment_id = active_equipment_id

    @property
    def active_interface_name(self):
        r"""Gets the active_interface_name of this AddVrrpConfigResponse.

        主设备接口名字

        :return: The active_interface_name of this AddVrrpConfigResponse.
        :rtype: str
        """
        return self._active_interface_name

    @active_interface_name.setter
    def active_interface_name(self, active_interface_name):
        r"""Sets the active_interface_name of this AddVrrpConfigResponse.

        主设备接口名字

        :param active_interface_name: The active_interface_name of this AddVrrpConfigResponse.
        :type active_interface_name: str
        """
        self._active_interface_name = active_interface_name

    @property
    def standby_equipment_id(self):
        r"""Gets the standby_equipment_id of this AddVrrpConfigResponse.

        备设备ID

        :return: The standby_equipment_id of this AddVrrpConfigResponse.
        :rtype: str
        """
        return self._standby_equipment_id

    @standby_equipment_id.setter
    def standby_equipment_id(self, standby_equipment_id):
        r"""Sets the standby_equipment_id of this AddVrrpConfigResponse.

        备设备ID

        :param standby_equipment_id: The standby_equipment_id of this AddVrrpConfigResponse.
        :type standby_equipment_id: str
        """
        self._standby_equipment_id = standby_equipment_id

    @property
    def standby_interface_name(self):
        r"""Gets the standby_interface_name of this AddVrrpConfigResponse.

        备设备接口名字

        :return: The standby_interface_name of this AddVrrpConfigResponse.
        :rtype: str
        """
        return self._standby_interface_name

    @standby_interface_name.setter
    def standby_interface_name(self, standby_interface_name):
        r"""Sets the standby_interface_name of this AddVrrpConfigResponse.

        备设备接口名字

        :param standby_interface_name: The standby_interface_name of this AddVrrpConfigResponse.
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
        if not isinstance(other, AddVrrpConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
