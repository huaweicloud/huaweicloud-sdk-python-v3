# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EipInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'eip_id': 'str',
        'eip_address': 'str',
        'ip_version': 'int'
    }

    attribute_map = {
        'eip_id': 'eip_id',
        'eip_address': 'eip_address',
        'ip_version': 'ip_version'
    }

    def __init__(self, eip_id=None, eip_address=None, ip_version=None):
        """EipInfo

        The model defined in huaweicloud sdk

        :param eip_id: eip_id
        :type eip_id: str
        :param eip_address: eip_address
        :type eip_address: str
        :param ip_version: IP版本号。  取值：4表示IPv4,6表示IPv6。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)
        :type ip_version: int
        """
        
        

        self._eip_id = None
        self._eip_address = None
        self._ip_version = None
        self.discriminator = None

        if eip_id is not None:
            self.eip_id = eip_id
        if eip_address is not None:
            self.eip_address = eip_address
        if ip_version is not None:
            self.ip_version = ip_version

    @property
    def eip_id(self):
        """Gets the eip_id of this EipInfo.

        eip_id

        :return: The eip_id of this EipInfo.
        :rtype: str
        """
        return self._eip_id

    @eip_id.setter
    def eip_id(self, eip_id):
        """Sets the eip_id of this EipInfo.

        eip_id

        :param eip_id: The eip_id of this EipInfo.
        :type eip_id: str
        """
        self._eip_id = eip_id

    @property
    def eip_address(self):
        """Gets the eip_address of this EipInfo.

        eip_address

        :return: The eip_address of this EipInfo.
        :rtype: str
        """
        return self._eip_address

    @eip_address.setter
    def eip_address(self, eip_address):
        """Sets the eip_address of this EipInfo.

        eip_address

        :param eip_address: The eip_address of this EipInfo.
        :type eip_address: str
        """
        self._eip_address = eip_address

    @property
    def ip_version(self):
        """Gets the ip_version of this EipInfo.

        IP版本号。  取值：4表示IPv4,6表示IPv6。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :return: The ip_version of this EipInfo.
        :rtype: int
        """
        return self._ip_version

    @ip_version.setter
    def ip_version(self, ip_version):
        """Sets the ip_version of this EipInfo.

        IP版本号。  取值：4表示IPv4,6表示IPv6。  [不支持IPv6，请勿设置为6。](tag:dt,dt_test)

        :param ip_version: The ip_version of this EipInfo.
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
        if not isinstance(other, EipInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
