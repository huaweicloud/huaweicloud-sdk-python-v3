# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PublicIpInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'publicip_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'publicip_address': 'publicip_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, publicip_id=None, publicip_address=None, ip_version=None):
        r"""PublicIpInfo

        The model defined in huaweicloud sdk

        :param publicip_id: 弹性公网ip配置id
        :type publicip_id: str
        :param publicip_address: IP地址
        :type publicip_address: str
        :param ip_version: IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)
        :type ip_version: int
        """
        
        

        self._publicip_id = None
        self._publicip_address = None
        self._ip_version = None
        self.discriminator = None

        self.publicip_id = publicip_id
        self.publicip_address = publicip_address
        self.ip_version = ip_version

    @property
    def publicip_id(self):
        r"""Gets the publicip_id of this PublicIpInfo.

        弹性公网ip配置id

        :return: The publicip_id of this PublicIpInfo.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        r"""Sets the publicip_id of this PublicIpInfo.

        弹性公网ip配置id

        :param publicip_id: The publicip_id of this PublicIpInfo.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def publicip_address(self):
        r"""Gets the publicip_address of this PublicIpInfo.

        IP地址

        :return: The publicip_address of this PublicIpInfo.
        :rtype: str
        """
        return self._publicip_address

    @publicip_address.setter
    def publicip_address(self, publicip_address):
        r"""Sets the publicip_address of this PublicIpInfo.

        IP地址

        :param publicip_address: The publicip_address of this PublicIpInfo.
        :type publicip_address: str
        """
        self._publicip_address = publicip_address

    @property
    def ip_version(self):
        r"""Gets the ip_version of this PublicIpInfo.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :return: The ip_version of this PublicIpInfo.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        r"""Sets the ip_version of this PublicIpInfo.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :param ip_version: The ip_version of this PublicIpInfo.
        :type ip_version: int
        """
        self._ip_version = ip_version

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
        if not isinstance(other, PublicIpInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
