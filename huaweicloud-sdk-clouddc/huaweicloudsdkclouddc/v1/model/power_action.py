# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PowerAction:

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
        'server_id_set': 'list[str]'
    }

    attribute_map = {
        'action': 'action',
        'server_id_set': 'server_id_set'
    }

    def __init__(self, action=None, server_id_set=None):
        r"""PowerAction

        The model defined in huaweicloud sdk

        :param action: 电源操作
        :type action: str
        :param server_id_set: server id set
        :type server_id_set: list[str]
        """
        
        

        self._action = None
        self._server_id_set = None
        self.discriminator = None

        self.action = action
        if server_id_set is not None:
            self.server_id_set = server_id_set

    @property
    def action(self):
        r"""Gets the action of this PowerAction.

        电源操作

        :return: The action of this PowerAction.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this PowerAction.

        电源操作

        :param action: The action of this PowerAction.
        :type action: str
        """
        self._action = action

    @property
    def server_id_set(self):
        r"""Gets the server_id_set of this PowerAction.

        server id set

        :return: The server_id_set of this PowerAction.
        :rtype: list[str]
        """
        return self._server_id_set

    @server_id_set.setter
    def server_id_set(self, server_id_set):
        r"""Sets the server_id_set of this PowerAction.

        server id set

        :param server_id_set: The server_id_set of this PowerAction.
        :type server_id_set: list[str]
        """
        self._server_id_set = server_id_set

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
        if not isinstance(other, PowerAction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
