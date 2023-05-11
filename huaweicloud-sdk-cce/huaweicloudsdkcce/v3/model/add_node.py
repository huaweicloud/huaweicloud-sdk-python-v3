# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddNode:

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
        'spec': 'ReinstallNodeSpec'
    }

    attribute_map = {
        'server_id': 'serverID',
        'spec': 'spec'
    }

    def __init__(self, server_id=None, spec=None):
        """AddNode

        The model defined in huaweicloud sdk

        :param server_id: 服务器ID，获取方式请参见ECS/BMS相关资料。
        :type server_id: str
        :param spec: 
        :type spec: :class:`huaweicloudsdkcce.v3.ReinstallNodeSpec`
        """
        
        

        self._server_id = None
        self._spec = None
        self.discriminator = None

        self.server_id = server_id
        self.spec = spec

    @property
    def server_id(self):
        """Gets the server_id of this AddNode.

        服务器ID，获取方式请参见ECS/BMS相关资料。

        :return: The server_id of this AddNode.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this AddNode.

        服务器ID，获取方式请参见ECS/BMS相关资料。

        :param server_id: The server_id of this AddNode.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def spec(self):
        """Gets the spec of this AddNode.

        :return: The spec of this AddNode.
        :rtype: :class:`huaweicloudsdkcce.v3.ReinstallNodeSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this AddNode.

        :param spec: The spec of this AddNode.
        :type spec: :class:`huaweicloudsdkcce.v3.ReinstallNodeSpec`
        """
        self._spec = spec

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
        if not isinstance(other, AddNode):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
