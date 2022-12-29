# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'public_ip': 'str',
        'status': 'int',
        'public_ipv6': 'str',
        'enterprise_project_id': 'str',
        'device_id': 'str',
        'device_name': 'str',
        'device_owner': 'str',
        'associate_instance_type': 'str',
        'fw_instance_name': 'str',
        'fw_instance_id': 'str',
        'fw_enterprise_project_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'public_ip': 'public_ip',
        'status': 'status',
        'public_ipv6': 'public_ipv6',
        'enterprise_project_id': 'enterprise_project_id',
        'device_id': 'device_id',
        'device_name': 'device_name',
        'device_owner': 'device_owner',
        'associate_instance_type': 'associate_instance_type',
        'fw_instance_name': 'fw_instance_name',
        'fw_instance_id': 'fw_instance_id',
        'fw_enterprise_project_id': 'fw_enterprise_project_id'
    }

    def __init__(self, id=None, public_ip=None, status=None, public_ipv6=None, enterprise_project_id=None, device_id=None, device_name=None, device_owner=None, associate_instance_type=None, fw_instance_name=None, fw_instance_id=None, fw_enterprise_project_id=None):
        """EipResource

        The model defined in huaweicloud sdk

        :param id: 弹性公网ID
        :type id: str
        :param public_ip: 弹性公网IP
        :type public_ip: str
        :param status: EIP防护状态
        :type status: int
        :param public_ipv6: 弹性公网IP,IPV6
        :type public_ipv6: str
        :param enterprise_project_id: 企业项目id
        :type enterprise_project_id: str
        :param device_id: 设备id
        :type device_id: str
        :param device_name: 设备名称
        :type device_name: str
        :param device_owner: 设备拥有者
        :type device_owner: str
        :param associate_instance_type: 关联实例类型
        :type associate_instance_type: str
        :param fw_instance_name: 防火墙名称
        :type fw_instance_name: str
        :param fw_instance_id: 防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。
        :type fw_instance_id: str
        :param fw_enterprise_project_id: Eip绑定的防火墙企业项目id
        :type fw_enterprise_project_id: str
        """
        
        

        self._id = None
        self._public_ip = None
        self._status = None
        self._public_ipv6 = None
        self._enterprise_project_id = None
        self._device_id = None
        self._device_name = None
        self._device_owner = None
        self._associate_instance_type = None
        self._fw_instance_name = None
        self._fw_instance_id = None
        self._fw_enterprise_project_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if public_ip is not None:
            self.public_ip = public_ip
        if status is not None:
            self.status = status
        if public_ipv6 is not None:
            self.public_ipv6 = public_ipv6
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if device_id is not None:
            self.device_id = device_id
        if device_name is not None:
            self.device_name = device_name
        if device_owner is not None:
            self.device_owner = device_owner
        if associate_instance_type is not None:
            self.associate_instance_type = associate_instance_type
        if fw_instance_name is not None:
            self.fw_instance_name = fw_instance_name
        if fw_instance_id is not None:
            self.fw_instance_id = fw_instance_id
        if fw_enterprise_project_id is not None:
            self.fw_enterprise_project_id = fw_enterprise_project_id

    @property
    def id(self):
        """Gets the id of this EipResource.

        弹性公网ID

        :return: The id of this EipResource.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EipResource.

        弹性公网ID

        :param id: The id of this EipResource.
        :type id: str
        """
        self._id = id

    @property
    def public_ip(self):
        """Gets the public_ip of this EipResource.

        弹性公网IP

        :return: The public_ip of this EipResource.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this EipResource.

        弹性公网IP

        :param public_ip: The public_ip of this EipResource.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def status(self):
        """Gets the status of this EipResource.

        EIP防护状态

        :return: The status of this EipResource.
        :rtype: int
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this EipResource.

        EIP防护状态

        :param status: The status of this EipResource.
        :type status: int
        """
        self._status = status

    @property
    def public_ipv6(self):
        """Gets the public_ipv6 of this EipResource.

        弹性公网IP,IPV6

        :return: The public_ipv6 of this EipResource.
        :rtype: str
        """
        return self._public_ipv6

    @public_ipv6.setter
    def public_ipv6(self, public_ipv6):
        """Sets the public_ipv6 of this EipResource.

        弹性公网IP,IPV6

        :param public_ipv6: The public_ipv6 of this EipResource.
        :type public_ipv6: str
        """
        self._public_ipv6 = public_ipv6

    @property
    def enterprise_project_id(self):
        """Gets the enterprise_project_id of this EipResource.

        企业项目id

        :return: The enterprise_project_id of this EipResource.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        """Sets the enterprise_project_id of this EipResource.

        企业项目id

        :param enterprise_project_id: The enterprise_project_id of this EipResource.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def device_id(self):
        """Gets the device_id of this EipResource.

        设备id

        :return: The device_id of this EipResource.
        :rtype: str
        """
        return self._device_id

    @device_id.setter
    def device_id(self, device_id):
        """Sets the device_id of this EipResource.

        设备id

        :param device_id: The device_id of this EipResource.
        :type device_id: str
        """
        self._device_id = device_id

    @property
    def device_name(self):
        """Gets the device_name of this EipResource.

        设备名称

        :return: The device_name of this EipResource.
        :rtype: str
        """
        return self._device_name

    @device_name.setter
    def device_name(self, device_name):
        """Sets the device_name of this EipResource.

        设备名称

        :param device_name: The device_name of this EipResource.
        :type device_name: str
        """
        self._device_name = device_name

    @property
    def device_owner(self):
        """Gets the device_owner of this EipResource.

        设备拥有者

        :return: The device_owner of this EipResource.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this EipResource.

        设备拥有者

        :param device_owner: The device_owner of this EipResource.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def associate_instance_type(self):
        """Gets the associate_instance_type of this EipResource.

        关联实例类型

        :return: The associate_instance_type of this EipResource.
        :rtype: str
        """
        return self._associate_instance_type

    @associate_instance_type.setter
    def associate_instance_type(self, associate_instance_type):
        """Sets the associate_instance_type of this EipResource.

        关联实例类型

        :param associate_instance_type: The associate_instance_type of this EipResource.
        :type associate_instance_type: str
        """
        self._associate_instance_type = associate_instance_type

    @property
    def fw_instance_name(self):
        """Gets the fw_instance_name of this EipResource.

        防火墙名称

        :return: The fw_instance_name of this EipResource.
        :rtype: str
        """
        return self._fw_instance_name

    @fw_instance_name.setter
    def fw_instance_name(self, fw_instance_name):
        """Sets the fw_instance_name of this EipResource.

        防火墙名称

        :param fw_instance_name: The fw_instance_name of this EipResource.
        :type fw_instance_name: str
        """
        self._fw_instance_name = fw_instance_name

    @property
    def fw_instance_id(self):
        """Gets the fw_instance_id of this EipResource.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。

        :return: The fw_instance_id of this EipResource.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        """Sets the fw_instance_id of this EipResource.

        防火墙实例id，创建云防火墙后用于标志防火墙由系统自动生成的标志id，可通过调用查询防火墙实例接口获得。具体可参考APIExlorer和帮助中心FAQ。

        :param fw_instance_id: The fw_instance_id of this EipResource.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def fw_enterprise_project_id(self):
        """Gets the fw_enterprise_project_id of this EipResource.

        Eip绑定的防火墙企业项目id

        :return: The fw_enterprise_project_id of this EipResource.
        :rtype: str
        """
        return self._fw_enterprise_project_id

    @fw_enterprise_project_id.setter
    def fw_enterprise_project_id(self, fw_enterprise_project_id):
        """Sets the fw_enterprise_project_id of this EipResource.

        Eip绑定的防火墙企业项目id

        :param fw_enterprise_project_id: The fw_enterprise_project_id of this EipResource.
        :type fw_enterprise_project_id: str
        """
        self._fw_enterprise_project_id = fw_enterprise_project_id

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
        if not isinstance(other, EipResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
