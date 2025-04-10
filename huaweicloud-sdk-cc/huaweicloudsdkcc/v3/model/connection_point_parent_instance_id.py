# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConnectionPointParentInstanceId:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_instance_id': 'str'
    }

    attribute_map = {
        'parent_instance_id': 'parent_instance_id'
    }

    def __init__(self, parent_instance_id=None):
        r"""ConnectionPointParentInstanceId

        The model defined in huaweicloud sdk

        :param parent_instance_id: 连接点的实例的父资源ID。
        :type parent_instance_id: str
        """
        
        

        self._parent_instance_id = None
        self.discriminator = None

        if parent_instance_id is not None:
            self.parent_instance_id = parent_instance_id

    @property
    def parent_instance_id(self):
        r"""Gets the parent_instance_id of this ConnectionPointParentInstanceId.

        连接点的实例的父资源ID。

        :return: The parent_instance_id of this ConnectionPointParentInstanceId.
        :rtype: str
        """
        return self._parent_instance_id

    @parent_instance_id.setter
    def parent_instance_id(self, parent_instance_id):
        r"""Sets the parent_instance_id of this ConnectionPointParentInstanceId.

        连接点的实例的父资源ID。

        :param parent_instance_id: The parent_instance_id of this ConnectionPointParentInstanceId.
        :type parent_instance_id: str
        """
        self._parent_instance_id = parent_instance_id

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
        if not isinstance(other, ConnectionPointParentInstanceId):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
