# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionActionReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'endpoints': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'endpoints': 'endpoints'
    }

    def __init__(self, action=None, endpoints=None):
        r"""ConnectionActionReq

        The model defined in huaweicloud sdk

        :param action: 允许或拒绝连接 - receive 接受 - reject 拒绝
        :type action: str
        :param endpoints: 终端节点列表
        :type endpoints: list[str]
        """
        
        

        self._action = None
        self._endpoints = None
        self.discriminator = None

        self.action = action
        self.endpoints = endpoints

    @property
    def action(self):
        r"""Gets the action of this ConnectionActionReq.

        允许或拒绝连接 - receive 接受 - reject 拒绝

        :return: The action of this ConnectionActionReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this ConnectionActionReq.

        允许或拒绝连接 - receive 接受 - reject 拒绝

        :param action: The action of this ConnectionActionReq.
        :type action: str
        """
        self._action = action

    @property
    def endpoints(self):
        r"""Gets the endpoints of this ConnectionActionReq.

        终端节点列表

        :return: The endpoints of this ConnectionActionReq.
        :rtype: list[str]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this ConnectionActionReq.

        终端节点列表

        :param endpoints: The endpoints of this ConnectionActionReq.
        :type endpoints: list[str]
        """
        self._endpoints = endpoints

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
        if not isinstance(other, ConnectionActionReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
