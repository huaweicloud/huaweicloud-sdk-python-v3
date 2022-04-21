# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryAuthorizedNodeDTO:

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
        'authorized_time': 'str'
    }

    attribute_map = {
        'node_id': 'node_id',
        'authorized_time': 'authorized_time'
    }

    def __init__(self, node_id=None, authorized_time=None):
        """QueryAuthorizedNodeDTO

        The model defined in huaweicloud sdk

        :param node_id: 边缘节点ID
        :type node_id: str
        :param authorized_time: 授权时间
        :type authorized_time: str
        """
        
        

        self._node_id = None
        self._authorized_time = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if authorized_time is not None:
            self.authorized_time = authorized_time

    @property
    def node_id(self):
        """Gets the node_id of this QueryAuthorizedNodeDTO.

        边缘节点ID

        :return: The node_id of this QueryAuthorizedNodeDTO.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        """Sets the node_id of this QueryAuthorizedNodeDTO.

        边缘节点ID

        :param node_id: The node_id of this QueryAuthorizedNodeDTO.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def authorized_time(self):
        """Gets the authorized_time of this QueryAuthorizedNodeDTO.

        授权时间

        :return: The authorized_time of this QueryAuthorizedNodeDTO.
        :rtype: str
        """
        return self._authorized_time

    @authorized_time.setter
    def authorized_time(self, authorized_time):
        """Sets the authorized_time of this QueryAuthorizedNodeDTO.

        授权时间

        :param authorized_time: The authorized_time of this QueryAuthorizedNodeDTO.
        :type authorized_time: str
        """
        self._authorized_time = authorized_time

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
        if not isinstance(other, QueryAuthorizedNodeDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
