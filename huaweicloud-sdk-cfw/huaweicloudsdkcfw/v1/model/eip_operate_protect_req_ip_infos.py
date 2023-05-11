# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipOperateProtectReqIpInfos:

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
        'public_ipv6': 'str'
    }

    attribute_map = {
        'id': 'id',
        'public_ip': 'public_ip',
        'public_ipv6': 'public_ipv6'
    }

    def __init__(self, id=None, public_ip=None, public_ipv6=None):
        """EipOperateProtectReqIpInfos

        The model defined in huaweicloud sdk

        :param id: 弹性公网IP数据ID
        :type id: str
        :param public_ip: 弹性公网IP地址
        :type public_ip: str
        :param public_ipv6: 弹性公网IP地址IPV6
        :type public_ipv6: str
        """
        
        

        self._id = None
        self._public_ip = None
        self._public_ipv6 = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if public_ip is not None:
            self.public_ip = public_ip
        if public_ipv6 is not None:
            self.public_ipv6 = public_ipv6

    @property
    def id(self):
        """Gets the id of this EipOperateProtectReqIpInfos.

        弹性公网IP数据ID

        :return: The id of this EipOperateProtectReqIpInfos.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this EipOperateProtectReqIpInfos.

        弹性公网IP数据ID

        :param id: The id of this EipOperateProtectReqIpInfos.
        :type id: str
        """
        self._id = id

    @property
    def public_ip(self):
        """Gets the public_ip of this EipOperateProtectReqIpInfos.

        弹性公网IP地址

        :return: The public_ip of this EipOperateProtectReqIpInfos.
        :rtype: str
        """
        return self._public_ip

    @public_ip.setter
    def public_ip(self, public_ip):
        """Sets the public_ip of this EipOperateProtectReqIpInfos.

        弹性公网IP地址

        :param public_ip: The public_ip of this EipOperateProtectReqIpInfos.
        :type public_ip: str
        """
        self._public_ip = public_ip

    @property
    def public_ipv6(self):
        """Gets the public_ipv6 of this EipOperateProtectReqIpInfos.

        弹性公网IP地址IPV6

        :return: The public_ipv6 of this EipOperateProtectReqIpInfos.
        :rtype: str
        """
        return self._public_ipv6

    @public_ipv6.setter
    def public_ipv6(self, public_ipv6):
        """Sets the public_ipv6 of this EipOperateProtectReqIpInfos.

        弹性公网IP地址IPV6

        :param public_ipv6: The public_ipv6 of this EipOperateProtectReqIpInfos.
        :type public_ipv6: str
        """
        self._public_ipv6 = public_ipv6

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
        if not isinstance(other, EipOperateProtectReqIpInfos):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
