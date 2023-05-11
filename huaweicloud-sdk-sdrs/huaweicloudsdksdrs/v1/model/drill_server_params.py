# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DrillServerParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'protected_instance': 'str',
        'drill_server_id': 'str'
    }

    attribute_map = {
        'protected_instance': 'protected_instance',
        'drill_server_id': 'drill_server_id'
    }

    def __init__(self, protected_instance=None, drill_server_id=None):
        """DrillServerParams

        The model defined in huaweicloud sdk

        :param protected_instance: 演练云服务器对应的保护实例ID。
        :type protected_instance: str
        :param drill_server_id: 演练云服务器ID。
        :type drill_server_id: str
        """
        
        

        self._protected_instance = None
        self._drill_server_id = None
        self.discriminator = None

        self.protected_instance = protected_instance
        self.drill_server_id = drill_server_id

    @property
    def protected_instance(self):
        """Gets the protected_instance of this DrillServerParams.

        演练云服务器对应的保护实例ID。

        :return: The protected_instance of this DrillServerParams.
        :rtype: str
        """
        return self._protected_instance

    @protected_instance.setter
    def protected_instance(self, protected_instance):
        """Sets the protected_instance of this DrillServerParams.

        演练云服务器对应的保护实例ID。

        :param protected_instance: The protected_instance of this DrillServerParams.
        :type protected_instance: str
        """
        self._protected_instance = protected_instance

    @property
    def drill_server_id(self):
        """Gets the drill_server_id of this DrillServerParams.

        演练云服务器ID。

        :return: The drill_server_id of this DrillServerParams.
        :rtype: str
        """
        return self._drill_server_id

    @drill_server_id.setter
    def drill_server_id(self, drill_server_id):
        """Sets the drill_server_id of this DrillServerParams.

        演练云服务器ID。

        :param drill_server_id: The drill_server_id of this DrillServerParams.
        :type drill_server_id: str
        """
        self._drill_server_id = drill_server_id

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
        if not isinstance(other, DrillServerParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
