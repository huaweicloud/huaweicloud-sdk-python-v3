# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ServerGroupItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'server_group_name': 'str',
        'host_num': 'int'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'server_group_name': 'server_group_name',
        'host_num': 'host_num'
    }

    def __init__(self, server_group_id=None, server_group_name=None, host_num=None):
        r"""ServerGroupItem

        The model defined in huaweicloud sdk

        :param server_group_id: 服务器组ID
        :type server_group_id: str
        :param server_group_name: 服务器组名称
        :type server_group_name: str
        :param host_num: 服务器组分配的主机数量
        :type host_num: int
        """
        
        

        self._server_group_id = None
        self._server_group_name = None
        self._host_num = None
        self.discriminator = None

        if server_group_id is not None:
            self.server_group_id = server_group_id
        if server_group_name is not None:
            self.server_group_name = server_group_name
        if host_num is not None:
            self.host_num = host_num

    @property
    def server_group_id(self):
        r"""Gets the server_group_id of this ServerGroupItem.

        服务器组ID

        :return: The server_group_id of this ServerGroupItem.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        r"""Sets the server_group_id of this ServerGroupItem.

        服务器组ID

        :param server_group_id: The server_group_id of this ServerGroupItem.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def server_group_name(self):
        r"""Gets the server_group_name of this ServerGroupItem.

        服务器组名称

        :return: The server_group_name of this ServerGroupItem.
        :rtype: str
        """
        return self._server_group_name

    @server_group_name.setter
    def server_group_name(self, server_group_name):
        r"""Sets the server_group_name of this ServerGroupItem.

        服务器组名称

        :param server_group_name: The server_group_name of this ServerGroupItem.
        :type server_group_name: str
        """
        self._server_group_name = server_group_name

    @property
    def host_num(self):
        r"""Gets the host_num of this ServerGroupItem.

        服务器组分配的主机数量

        :return: The host_num of this ServerGroupItem.
        :rtype: int
        """
        return self._host_num

    @host_num.setter
    def host_num(self, host_num):
        r"""Sets the host_num of this ServerGroupItem.

        服务器组分配的主机数量

        :param host_num: The host_num of this ServerGroupItem.
        :type host_num: int
        """
        self._host_num = host_num

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
        if not isinstance(other, ServerGroupItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
