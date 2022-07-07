# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GlobalEipInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'global_eip_id': 'str',
        'global_eip_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'global_eip_id': 'global_eip_id',
        'global_eip_address': 'global_eip_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, global_eip_id=None, global_eip_address=None, ip_version=None):
        """GlobalEipInfo

        The model defined in huaweicloud sdk

        :param global_eip_id: global eip的id
        :type global_eip_id: str
        :param global_eip_address: global eip的ip地址
        :type global_eip_address: str
        :param ip_version: IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6 [不支持IPv6，请勿设置为6。]
        :type ip_version: int
        """
        
        

        self._global_eip_id = None
        self._global_eip_address = None
        self._ip_version = None
        self.discriminator = None

        if global_eip_id is not None:
            self.global_eip_id = global_eip_id
        if global_eip_address is not None:
            self.global_eip_address = global_eip_address
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def global_eip_id(self):
        """Gets the global_eip_id of this GlobalEipInfo.

        global eip的id

        :return: The global_eip_id of this GlobalEipInfo.
        :rtype: str
        """
        return self._global_eip_id

    @global_eip_id.setter
    def global_eip_id(self, global_eip_id):
        """Sets the global_eip_id of this GlobalEipInfo.

        global eip的id

        :param global_eip_id: The global_eip_id of this GlobalEipInfo.
        :type global_eip_id: str
        """
        self._global_eip_id = global_eip_id

    @property
    def global_eip_address(self):
        """Gets the global_eip_address of this GlobalEipInfo.

        global eip的ip地址

        :return: The global_eip_address of this GlobalEipInfo.
        :rtype: str
        """
        return self._global_eip_address

    @global_eip_address.setter
    def global_eip_address(self, global_eip_address):
        """Sets the global_eip_address of this GlobalEipInfo.

        global eip的ip地址

        :param global_eip_address: The global_eip_address of this GlobalEipInfo.
        :type global_eip_address: str
        """
        self._global_eip_address = global_eip_address

    @property
    def ip_version(self):
        """Gets the ip_version of this GlobalEipInfo.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6 [不支持IPv6，请勿设置为6。]

        :return: The ip_version of this GlobalEipInfo.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this GlobalEipInfo.

        IP版本信息。 取值范围：4和6 4：IPv4 6：IPv6 [不支持IPv6，请勿设置为6。]

        :param ip_version: The ip_version of this GlobalEipInfo.
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
        if not isinstance(other, GlobalEipInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
