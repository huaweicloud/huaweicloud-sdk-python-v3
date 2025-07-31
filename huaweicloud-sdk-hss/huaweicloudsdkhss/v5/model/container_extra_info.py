# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ContainerExtraInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'openvpn': 'ContainerExtraOpenvpnInfo',
        'linux': 'ContainerExtraLinuxInfo',
        'rdp': 'ContainerExtraRdpInfo',
        'mysql': 'ContainerExtraMysqlInfo'
    }

    attribute_map = {
        'openvpn': 'openvpn',
        'linux': 'linux',
        'rdp': 'rdp',
        'mysql': 'mysql'
    }

    def __init__(self, openvpn=None, linux=None, rdp=None, mysql=None):
        r"""ContainerExtraInfo

        The model defined in huaweicloud sdk

        :param openvpn: 
        :type openvpn: :class:`huaweicloudsdkhss.v5.ContainerExtraOpenvpnInfo`
        :param linux: 
        :type linux: :class:`huaweicloudsdkhss.v5.ContainerExtraLinuxInfo`
        :param rdp: 
        :type rdp: :class:`huaweicloudsdkhss.v5.ContainerExtraRdpInfo`
        :param mysql: 
        :type mysql: :class:`huaweicloudsdkhss.v5.ContainerExtraMysqlInfo`
        """
        
        

        self._openvpn = None
        self._linux = None
        self._rdp = None
        self._mysql = None
        self.discriminator = None

        if openvpn is not None:
            self.openvpn = openvpn
        if linux is not None:
            self.linux = linux
        if rdp is not None:
            self.rdp = rdp
        if mysql is not None:
            self.mysql = mysql

    @property
    def openvpn(self):
        r"""Gets the openvpn of this ContainerExtraInfo.

        :return: The openvpn of this ContainerExtraInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ContainerExtraOpenvpnInfo`
        """
        return self._openvpn

    @openvpn.setter
    def openvpn(self, openvpn):
        r"""Sets the openvpn of this ContainerExtraInfo.

        :param openvpn: The openvpn of this ContainerExtraInfo.
        :type openvpn: :class:`huaweicloudsdkhss.v5.ContainerExtraOpenvpnInfo`
        """
        self._openvpn = openvpn

    @property
    def linux(self):
        r"""Gets the linux of this ContainerExtraInfo.

        :return: The linux of this ContainerExtraInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ContainerExtraLinuxInfo`
        """
        return self._linux

    @linux.setter
    def linux(self, linux):
        r"""Sets the linux of this ContainerExtraInfo.

        :param linux: The linux of this ContainerExtraInfo.
        :type linux: :class:`huaweicloudsdkhss.v5.ContainerExtraLinuxInfo`
        """
        self._linux = linux

    @property
    def rdp(self):
        r"""Gets the rdp of this ContainerExtraInfo.

        :return: The rdp of this ContainerExtraInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ContainerExtraRdpInfo`
        """
        return self._rdp

    @rdp.setter
    def rdp(self, rdp):
        r"""Sets the rdp of this ContainerExtraInfo.

        :param rdp: The rdp of this ContainerExtraInfo.
        :type rdp: :class:`huaweicloudsdkhss.v5.ContainerExtraRdpInfo`
        """
        self._rdp = rdp

    @property
    def mysql(self):
        r"""Gets the mysql of this ContainerExtraInfo.

        :return: The mysql of this ContainerExtraInfo.
        :rtype: :class:`huaweicloudsdkhss.v5.ContainerExtraMysqlInfo`
        """
        return self._mysql

    @mysql.setter
    def mysql(self, mysql):
        r"""Sets the mysql of this ContainerExtraInfo.

        :param mysql: The mysql of this ContainerExtraInfo.
        :type mysql: :class:`huaweicloudsdkhss.v5.ContainerExtraMysqlInfo`
        """
        self._mysql = mysql

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
        if not isinstance(other, ContainerExtraInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
