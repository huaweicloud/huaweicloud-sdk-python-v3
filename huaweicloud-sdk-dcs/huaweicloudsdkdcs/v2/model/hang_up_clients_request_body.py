# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HangUpClientsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'client_addrs': 'list[str]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'client_addrs': 'client_addrs'
    }

    def __init__(self, node_id=None, client_addrs=None):
        r"""HangUpClientsRequestBody

        The model defined in huaweicloud sdk

        :param node_id: 节点id
        :type node_id: str
        :param client_addrs: 要kill的会话addr列表
        :type client_addrs: list[str]
        """
        
        

        self._node_id = None
        self._client_addrs = None
        self.discriminator = None

        self.node_id = node_id
        self.client_addrs = client_addrs

    @property
    def node_id(self):
        r"""Gets the node_id of this HangUpClientsRequestBody.

        节点id

        :return: The node_id of this HangUpClientsRequestBody.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this HangUpClientsRequestBody.

        节点id

        :param node_id: The node_id of this HangUpClientsRequestBody.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def client_addrs(self):
        r"""Gets the client_addrs of this HangUpClientsRequestBody.

        要kill的会话addr列表

        :return: The client_addrs of this HangUpClientsRequestBody.
        :rtype: list[str]
        """
        return self._client_addrs

    @client_addrs.setter
    def client_addrs(self, client_addrs):
        r"""Sets the client_addrs of this HangUpClientsRequestBody.

        要kill的会话addr列表

        :param client_addrs: The client_addrs of this HangUpClientsRequestBody.
        :type client_addrs: list[str]
        """
        self._client_addrs = client_addrs

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
        if not isinstance(other, HangUpClientsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
