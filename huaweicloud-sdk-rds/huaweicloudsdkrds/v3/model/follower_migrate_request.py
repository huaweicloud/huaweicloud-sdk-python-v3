# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FollowerMigrateRequest:

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
        'az_code': 'str'
    }

    attribute_map = {
        'node_id': 'nodeId',
        'az_code': 'azCode'
    }

    def __init__(self, node_id=None, az_code=None):
        """FollowerMigrateRequest

        The model defined in huaweicloud sdk

        :param node_id: 备机节点Id
        :type node_id: str
        :param az_code: 要迁入的可用区code
        :type az_code: str
        """
        
        

        self._node_id = None
        self._az_code = None
        self.discriminator = None

        self.node_id = node_id
        self.az_code = az_code

    @property
    def node_id(self):
        """Gets the node_id of this FollowerMigrateRequest.

        备机节点Id

        :return: The node_id of this FollowerMigrateRequest.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this FollowerMigrateRequest.

        备机节点Id

        :param node_id: The node_id of this FollowerMigrateRequest.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def az_code(self):
        """Gets the az_code of this FollowerMigrateRequest.

        要迁入的可用区code

        :return: The az_code of this FollowerMigrateRequest.
        :rtype: str
        """
        return self._az_code

    @az_code.setter
    def az_code(self, az_code):
        """Sets the az_code of this FollowerMigrateRequest.

        要迁入的可用区code

        :param az_code: The az_code of this FollowerMigrateRequest.
        :type az_code: str
        """
        self._az_code = az_code

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
        if not isinstance(other, FollowerMigrateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
