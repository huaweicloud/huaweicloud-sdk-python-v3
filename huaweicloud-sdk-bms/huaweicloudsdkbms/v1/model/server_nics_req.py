# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerNicsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'subnet_id': 'str',
        'ip_address': 'str',
        'security_groups': 'list[SecurityGroupInfo]'
    }

    attribute_map = {
        'subnet_id': 'subnet_id',
        'ip_address': 'ip_address',
        'security_groups': 'security_groups'
    }

    def __init__(self, subnet_id=None, ip_address=None, security_groups=None):
        r"""ServerNicsReq

        The model defined in huaweicloud sdk

        :param subnet_id: 网卡的子网ID
        :type subnet_id: str
        :param ip_address: 
        :type ip_address: str
        :param security_groups: 
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroupInfo`]
        """
        
        

        self._subnet_id = None
        self._ip_address = None
        self._security_groups = None
        self.discriminator = None

        self.subnet_id = subnet_id
        if ip_address is not None:
            self.ip_address = ip_address
        if security_groups is not None:
            self.security_groups = security_groups

    @property
    def subnet_id(self):
        r"""Gets the subnet_id of this ServerNicsReq.

        网卡的子网ID

        :return: The subnet_id of this ServerNicsReq.
        :rtype: str
        """
        return self._subnet_id

    @subnet_id.setter
    def subnet_id(self, subnet_id):
        r"""Sets the subnet_id of this ServerNicsReq.

        网卡的子网ID

        :param subnet_id: The subnet_id of this ServerNicsReq.
        :type subnet_id: str
        """
        self._subnet_id = subnet_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ServerNicsReq.

        

        :return: The ip_address of this ServerNicsReq.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ServerNicsReq.

        

        :param ip_address: The ip_address of this ServerNicsReq.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def security_groups(self):
        r"""Gets the security_groups of this ServerNicsReq.

        

        :return: The security_groups of this ServerNicsReq.
        :rtype: list[:class:`huaweicloudsdkbms.v1.SecurityGroupInfo`]
        """
        return self._security_groups

    @security_groups.setter
    def security_groups(self, security_groups):
        r"""Sets the security_groups of this ServerNicsReq.

        

        :param security_groups: The security_groups of this ServerNicsReq.
        :type security_groups: list[:class:`huaweicloudsdkbms.v1.SecurityGroupInfo`]
        """
        self._security_groups = security_groups

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
        if not isinstance(other, ServerNicsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
