# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchMigrateServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_ids': 'list[str]',
        'host_id': 'str'
    }

    attribute_map = {
        'server_ids': 'server_ids',
        'host_id': 'host_id'
    }

    def __init__(self, server_ids=None, host_id=None):
        """BatchMigrateServerReq

        The model defined in huaweicloud sdk

        :param server_ids: 应用服务器id集合
        :type server_ids: list[str]
        :param host_id: 目标云办公主机id
        :type host_id: str
        """
        
        

        self._server_ids = None
        self._host_id = None
        self.discriminator = None

        self.server_ids = server_ids
        self.host_id = host_id

    @property
    def server_ids(self):
        """Gets the server_ids of this BatchMigrateServerReq.

        应用服务器id集合

        :return: The server_ids of this BatchMigrateServerReq.
        :rtype: list[str]
        """
        return self._server_ids

    @server_ids.setter
    def server_ids(self, server_ids):
        """Sets the server_ids of this BatchMigrateServerReq.

        应用服务器id集合

        :param server_ids: The server_ids of this BatchMigrateServerReq.
        :type server_ids: list[str]
        """
        self._server_ids = server_ids

    @property
    def host_id(self):
        """Gets the host_id of this BatchMigrateServerReq.

        目标云办公主机id

        :return: The host_id of this BatchMigrateServerReq.
        :rtype: str
        """
        return self._host_id

    @host_id.setter
    def host_id(self, host_id):
        """Sets the host_id of this BatchMigrateServerReq.

        目标云办公主机id

        :param host_id: The host_id of this BatchMigrateServerReq.
        :type host_id: str
        """
        self._host_id = host_id

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
        if not isinstance(other, BatchMigrateServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
