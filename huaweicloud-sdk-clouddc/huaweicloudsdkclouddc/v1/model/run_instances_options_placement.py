# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RunInstancesOptionsPlacement:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id_set': 'list[str]'
    }

    attribute_map = {
        'server_id_set': 'server_id_set'
    }

    def __init__(self, server_id_set=None):
        r"""RunInstancesOptionsPlacement

        The model defined in huaweicloud sdk

        :param server_id_set: 指定服务器
        :type server_id_set: list[str]
        """
        
        

        self._server_id_set = None
        self.discriminator = None

        if server_id_set is not None:
            self.server_id_set = server_id_set

    @property
    def server_id_set(self):
        r"""Gets the server_id_set of this RunInstancesOptionsPlacement.

        指定服务器

        :return: The server_id_set of this RunInstancesOptionsPlacement.
        :rtype: list[str]
        """
        return self._server_id_set

    @server_id_set.setter
    def server_id_set(self, server_id_set):
        r"""Sets the server_id_set of this RunInstancesOptionsPlacement.

        指定服务器

        :param server_id_set: The server_id_set of this RunInstancesOptionsPlacement.
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
        if not isinstance(other, RunInstancesOptionsPlacement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
