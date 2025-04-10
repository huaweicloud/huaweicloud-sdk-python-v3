# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOmUrlRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'ip_address': 'str',
        'host_account_name': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'ip_address': 'ip_address',
        'host_account_name': 'host_account_name'
    }

    def __init__(self, server_id=None, ip_address=None, host_account_name=None):
        r"""ShowOmUrlRequest

        The model defined in huaweicloud sdk

        :param server_id: 云堡垒机服务器ID
        :type server_id: str
        :param ip_address: 被纳管主机IP
        :type ip_address: str
        :param host_account_name: 被纳管主机的账户
        :type host_account_name: str
        """
        
        

        self._server_id = None
        self._ip_address = None
        self._host_account_name = None
        self.discriminator = None

        self.server_id = server_id
        self.ip_address = ip_address
        self.host_account_name = host_account_name

    @property
    def server_id(self):
        r"""Gets the server_id of this ShowOmUrlRequest.

        云堡垒机服务器ID

        :return: The server_id of this ShowOmUrlRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ShowOmUrlRequest.

        云堡垒机服务器ID

        :param server_id: The server_id of this ShowOmUrlRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def ip_address(self):
        r"""Gets the ip_address of this ShowOmUrlRequest.

        被纳管主机IP

        :return: The ip_address of this ShowOmUrlRequest.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        r"""Sets the ip_address of this ShowOmUrlRequest.

        被纳管主机IP

        :param ip_address: The ip_address of this ShowOmUrlRequest.
        :type ip_address: str
        """
        self._ip_address = ip_address

    @property
    def host_account_name(self):
        r"""Gets the host_account_name of this ShowOmUrlRequest.

        被纳管主机的账户

        :return: The host_account_name of this ShowOmUrlRequest.
        :rtype: str
        """
        return self._host_account_name

    @host_account_name.setter
    def host_account_name(self, host_account_name):
        r"""Sets the host_account_name of this ShowOmUrlRequest.

        被纳管主机的账户

        :param host_account_name: The host_account_name of this ShowOmUrlRequest.
        :type host_account_name: str
        """
        self._host_account_name = host_account_name

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
        if not isinstance(other, ShowOmUrlRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
