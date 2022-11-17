# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Privateip:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'id': 'str',
        'subnet_id': 'str',
        'tenant_id': 'str',
        'device_owner': 'str',
        'ip_address': 'str'
    }

    attribute_map = {
        'status': 'status',
        'id': 'id',
        'subnet_id': 'subnet_id',
        'tenant_id': 'tenant_id',
        'device_owner': 'device_owner',
        'ip_address': 'ip_address'
    }

    def __init__(self, status=None, id=None, subnet_id=None, tenant_id=None, device_owner=None, ip_address=None):
        """Privateip

        The model defined in huaweicloud sdk

        :param status: 私有IP的状态  - ACTIVE：活动的  - DOWN：不可用
        :type status: str
        :param id: 私有IP ID
        :type id: str
        :param subnet_id: 分配IP的子网标识
        :type subnet_id: str
        :param tenant_id: 项目ID
        :type tenant_id: str
        :param device_owner: 私有IP的使用者，空表示未使用 取值范围：network:dhcp，network:router_interface_distributed，compute:xxx(xxx对应具体的az名称，例如compute:aa-bb-cc表示是被aa-bb-cc上的虚拟机使用) 约束：此处的取值范围只是本服务支持的类型，其他类型未做标注
        :type device_owner: str
        :param ip_address: 申请到的私有IP
        :type ip_address: str
        """
        
        

        self._status = None
        self._id = None
        self._subnet_id = None
        self._tenant_id = None
        self._device_owner = None
        self._ip_address = None
        self.discriminator = None

        self.status = status
        self.id = id
        self.subnet_id = subnet_id
        self.tenant_id = tenant_id
        self.device_owner = device_owner
        self.ip_address = ip_address

    @property
    def status(self):
        """Gets the status of this Privateip.

        私有IP的状态  - ACTIVE：活动的  - DOWN：不可用

        :return: The status of this Privateip.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Privateip.

        私有IP的状态  - ACTIVE：活动的  - DOWN：不可用

        :param status: The status of this Privateip.
        :type status: str
        """
        self._status = status

    @property
    def id(self):
        """Gets the id of this Privateip.

        私有IP ID

        :return: The id of this Privateip.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Privateip.

        私有IP ID

        :param id: The id of this Privateip.
        :type id: str
        """
        self._id = id

    @property
    def subnet_id(self):
        """Gets the subnet_id of this Privateip.

        分配IP的子网标识

        :return: The subnet_id of this Privateip.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        """Sets the subnet_id of this Privateip.

        分配IP的子网标识

        :param subnet_id: The subnet_id of this Privateip.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def tenant_id(self):
        """Gets the tenant_id of this Privateip.

        项目ID

        :return: The tenant_id of this Privateip.
        :rtype: str
        """
        return self._tenant_id

    @tenant_id.setter
    def tenant_id(self, tenant_id):
        """Sets the tenant_id of this Privateip.

        项目ID

        :param tenant_id: The tenant_id of this Privateip.
        :type tenant_id: str
        """
        self._tenant_id = tenant_id

    @property
    def device_owner(self):
        """Gets the device_owner of this Privateip.

        私有IP的使用者，空表示未使用 取值范围：network:dhcp，network:router_interface_distributed，compute:xxx(xxx对应具体的az名称，例如compute:aa-bb-cc表示是被aa-bb-cc上的虚拟机使用) 约束：此处的取值范围只是本服务支持的类型，其他类型未做标注

        :return: The device_owner of this Privateip.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this Privateip.

        私有IP的使用者，空表示未使用 取值范围：network:dhcp，network:router_interface_distributed，compute:xxx(xxx对应具体的az名称，例如compute:aa-bb-cc表示是被aa-bb-cc上的虚拟机使用) 约束：此处的取值范围只是本服务支持的类型，其他类型未做标注

        :param device_owner: The device_owner of this Privateip.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def ip_address(self):
        """Gets the ip_address of this Privateip.

        申请到的私有IP

        :return: The ip_address of this Privateip.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """Sets the ip_address of this Privateip.

        申请到的私有IP

        :param ip_address: The ip_address of this Privateip.
        :type ip_address: str
        """
        self._ip_address = ip_address

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
        if not isinstance(other, Privateip):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
