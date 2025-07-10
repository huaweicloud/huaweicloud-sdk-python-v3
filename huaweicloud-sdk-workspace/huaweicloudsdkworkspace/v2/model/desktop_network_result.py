# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DesktopNetworkResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'computer_name': 'str',
        'computer_id': 'str',
        'computer_ip': 'str',
        'network_infos': 'list[NetworkInfo]'
    }

    attribute_map = {
        'computer_name': 'computer_name',
        'computer_id': 'computer_id',
        'computer_ip': 'computer_ip',
        'network_infos': 'network_infos'
    }

    def __init__(self, computer_name=None, computer_id=None, computer_ip=None, network_infos=None):
        r"""DesktopNetworkResult

        The model defined in huaweicloud sdk

        :param computer_name: 桌面名称。
        :type computer_name: str
        :param computer_id: 桌面ID。
        :type computer_id: str
        :param computer_ip: 桌面IP。
        :type computer_ip: str
        :param network_infos: 桌面网络信息。
        :type network_infos: list[:class:`huaweicloudsdkworkspace.v2.NetworkInfo`]
        """
        
        

        self._computer_name = None
        self._computer_id = None
        self._computer_ip = None
        self._network_infos = None
        self.discriminator = None

        if computer_name is not None:
            self.computer_name = computer_name
        if computer_id is not None:
            self.computer_id = computer_id
        if computer_ip is not None:
            self.computer_ip = computer_ip
        if network_infos is not None:
            self.network_infos = network_infos

    @property
    def computer_name(self):
        r"""Gets the computer_name of this DesktopNetworkResult.

        桌面名称。

        :return: The computer_name of this DesktopNetworkResult.
        :rtype: str
        """
        return self._computer_name

    @computer_name.setter
    def computer_name(self, computer_name):
        r"""Sets the computer_name of this DesktopNetworkResult.

        桌面名称。

        :param computer_name: The computer_name of this DesktopNetworkResult.
        :type computer_name: str
        """
        self._computer_name = computer_name

    @property
    def computer_id(self):
        r"""Gets the computer_id of this DesktopNetworkResult.

        桌面ID。

        :return: The computer_id of this DesktopNetworkResult.
        :rtype: str
        """
        return self._computer_id

    @computer_id.setter
    def computer_id(self, computer_id):
        r"""Sets the computer_id of this DesktopNetworkResult.

        桌面ID。

        :param computer_id: The computer_id of this DesktopNetworkResult.
        :type computer_id: str
        """
        self._computer_id = computer_id

    @property
    def computer_ip(self):
        r"""Gets the computer_ip of this DesktopNetworkResult.

        桌面IP。

        :return: The computer_ip of this DesktopNetworkResult.
        :rtype: str
        """
        return self._computer_ip

    @computer_ip.setter
    def computer_ip(self, computer_ip):
        r"""Sets the computer_ip of this DesktopNetworkResult.

        桌面IP。

        :param computer_ip: The computer_ip of this DesktopNetworkResult.
        :type computer_ip: str
        """
        self._computer_ip = computer_ip

    @property
    def network_infos(self):
        r"""Gets the network_infos of this DesktopNetworkResult.

        桌面网络信息。

        :return: The network_infos of this DesktopNetworkResult.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.NetworkInfo`]
        """
        return self._network_infos

    @network_infos.setter
    def network_infos(self, network_infos):
        r"""Sets the network_infos of this DesktopNetworkResult.

        桌面网络信息。

        :param network_infos: The network_infos of this DesktopNetworkResult.
        :type network_infos: list[:class:`huaweicloudsdkworkspace.v2.NetworkInfo`]
        """
        self._network_infos = network_infos

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
        if not isinstance(other, DesktopNetworkResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
