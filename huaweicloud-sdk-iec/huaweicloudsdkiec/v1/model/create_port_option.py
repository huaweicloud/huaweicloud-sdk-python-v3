# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePortOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'device_owner': 'str',
        'network_id': 'str',
        'fixed_ips': 'list[FixedIp]'
    }

    attribute_map = {
        'device_owner': 'device_owner',
        'network_id': 'network_id',
        'fixed_ips': 'fixed_ips'
    }

    def __init__(self, device_owner=None, network_id=None, fixed_ips=None):
        """CreatePortOption

        The model defined in huaweicloud sdk

        :param device_owner: 端口设备所属。  取值范围：目前只支持指定\&quot;neutron:VIP_PORT\&quot;，neutron:VIP_PORT表示创建的是VIP
        :type device_owner: str
        :param network_id: 端口所属网络的ID。  约束：必须是存在的网络ID。
        :type network_id: str
        :param fixed_ips: 端口IP  约束：一个端口只支持一个fixed_ip，且不支持更新。
        :type fixed_ips: list[:class:`huaweicloudsdkiec.v1.FixedIp`]
        """
        
        

        self._device_owner = None
        self._network_id = None
        self._fixed_ips = None
        self.discriminator = None

        self.device_owner = device_owner
        self.network_id = network_id
        if fixed_ips is not None:
            self.fixed_ips = fixed_ips

    @property
    def device_owner(self):
        """Gets the device_owner of this CreatePortOption.

        端口设备所属。  取值范围：目前只支持指定\"neutron:VIP_PORT\"，neutron:VIP_PORT表示创建的是VIP

        :return: The device_owner of this CreatePortOption.
        :rtype: str
        """
        return self._device_owner

    @device_owner.setter
    def device_owner(self, device_owner):
        """Sets the device_owner of this CreatePortOption.

        端口设备所属。  取值范围：目前只支持指定\"neutron:VIP_PORT\"，neutron:VIP_PORT表示创建的是VIP

        :param device_owner: The device_owner of this CreatePortOption.
        :type device_owner: str
        """
        self._device_owner = device_owner

    @property
    def network_id(self):
        """Gets the network_id of this CreatePortOption.

        端口所属网络的ID。  约束：必须是存在的网络ID。

        :return: The network_id of this CreatePortOption.
        :rtype: str
        """
        return self._network_id

    @network_id.setter
    def network_id(self, network_id):
        """Sets the network_id of this CreatePortOption.

        端口所属网络的ID。  约束：必须是存在的网络ID。

        :param network_id: The network_id of this CreatePortOption.
        :type network_id: str
        """
        self._network_id = network_id

    @property
    def fixed_ips(self):
        """Gets the fixed_ips of this CreatePortOption.

        端口IP  约束：一个端口只支持一个fixed_ip，且不支持更新。

        :return: The fixed_ips of this CreatePortOption.
        :rtype: list[:class:`huaweicloudsdkiec.v1.FixedIp`]
        """
        return self._fixed_ips

    @fixed_ips.setter
    def fixed_ips(self, fixed_ips):
        """Sets the fixed_ips of this CreatePortOption.

        端口IP  约束：一个端口只支持一个fixed_ip，且不支持更新。

        :param fixed_ips: The fixed_ips of this CreatePortOption.
        :type fixed_ips: list[:class:`huaweicloudsdkiec.v1.FixedIp`]
        """
        self._fixed_ips = fixed_ips

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
        if not isinstance(other, CreatePortOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
