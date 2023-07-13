# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeInstanceOrderRequest:

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
        'instance_key': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'instance_key': 'instance_key'
    }

    def __init__(self, server_id=None, instance_key=None):
        """ChangeInstanceOrderRequest

        The model defined in huaweicloud sdk

        :param server_id: 云堡垒机实例ID。
        :type server_id: str
        :param instance_key: 云堡垒机实例Key。
        :type instance_key: str
        """
        
        

        self._server_id = None
        self._instance_key = None
        self.discriminator = None

        self.server_id = server_id
        self.instance_key = instance_key

    @property
    def server_id(self):
        """Gets the server_id of this ChangeInstanceOrderRequest.

        云堡垒机实例ID。

        :return: The server_id of this ChangeInstanceOrderRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        """Sets the server_id of this ChangeInstanceOrderRequest.

        云堡垒机实例ID。

        :param server_id: The server_id of this ChangeInstanceOrderRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def instance_key(self):
        """Gets the instance_key of this ChangeInstanceOrderRequest.

        云堡垒机实例Key。

        :return: The instance_key of this ChangeInstanceOrderRequest.
        :rtype: str
        """
        return self._instance_key

    @instance_key.setter
    def instance_key(self, instance_key):
        """Sets the instance_key of this ChangeInstanceOrderRequest.

        云堡垒机实例Key。

        :param instance_key: The instance_key of this ChangeInstanceOrderRequest.
        :type instance_key: str
        """
        self._instance_key = instance_key

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
        if not isinstance(other, ChangeInstanceOrderRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
