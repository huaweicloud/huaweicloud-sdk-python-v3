# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportIpBlacklistRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'fw_instance_id': 'str',
        'name': 'str'
    }

    attribute_map = {
        'fw_instance_id': 'fw_instance_id',
        'name': 'name'
    }

    def __init__(self, fw_instance_id=None, name=None):
        r"""ExportIpBlacklistRequest

        The model defined in huaweicloud sdk

        :param fw_instance_id: 防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取
        :type fw_instance_id: str
        :param name: IP黑名单的名字，如果要导出生效范围为EIP的IP黑名单，就指定名字为ip-blacklist-eip.txt，如果要导出生效范围为NAT的IP黑名单，就指定名字为ip-blacklist-nat.txt。
        :type name: str
        """
        
        

        self._fw_instance_id = None
        self._name = None
        self.discriminator = None

        self.fw_instance_id = fw_instance_id
        self.name = name

    @property
    def fw_instance_id(self):
        r"""Gets the fw_instance_id of this ExportIpBlacklistRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :return: The fw_instance_id of this ExportIpBlacklistRequest.
        :rtype: str
        """
        return self._fw_instance_id

    @fw_instance_id.setter
    def fw_instance_id(self, fw_instance_id):
        r"""Sets the fw_instance_id of this ExportIpBlacklistRequest.

        防火墙ID，可通过[防火墙ID获取方式](cfw_02_0028.xml)获取

        :param fw_instance_id: The fw_instance_id of this ExportIpBlacklistRequest.
        :type fw_instance_id: str
        """
        self._fw_instance_id = fw_instance_id

    @property
    def name(self):
        r"""Gets the name of this ExportIpBlacklistRequest.

        IP黑名单的名字，如果要导出生效范围为EIP的IP黑名单，就指定名字为ip-blacklist-eip.txt，如果要导出生效范围为NAT的IP黑名单，就指定名字为ip-blacklist-nat.txt。

        :return: The name of this ExportIpBlacklistRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ExportIpBlacklistRequest.

        IP黑名单的名字，如果要导出生效范围为EIP的IP黑名单，就指定名字为ip-blacklist-eip.txt，如果要导出生效范围为NAT的IP黑名单，就指定名字为ip-blacklist-nat.txt。

        :param name: The name of this ExportIpBlacklistRequest.
        :type name: str
        """
        self._name = name

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
        if not isinstance(other, ExportIpBlacklistRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
