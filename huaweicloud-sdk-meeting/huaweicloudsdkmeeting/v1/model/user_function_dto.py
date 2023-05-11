# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UserFunctionDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable_room': 'bool'
    }

    attribute_map = {
        'enable_room': 'enableRoom'
    }

    def __init__(self, enable_room=None):
        """UserFunctionDTO

        The model defined in huaweicloud sdk

        :param enable_room: 是否开启智能协同白板功能。如果开启，表示该帐号是给智能协同白板使用，占用企业智能协同白板的资源，如果资源不足，则无法开启。 默认值：false。 &gt; 该参数将废弃，请勿使用。 
        :type enable_room: bool
        """
        
        

        self._enable_room = None
        self.discriminator = None

        if enable_room is not None:
            self.enable_room = enable_room

    @property
    def enable_room(self):
        """Gets the enable_room of this UserFunctionDTO.

        是否开启智能协同白板功能。如果开启，表示该帐号是给智能协同白板使用，占用企业智能协同白板的资源，如果资源不足，则无法开启。 默认值：false。 > 该参数将废弃，请勿使用。 

        :return: The enable_room of this UserFunctionDTO.
        :rtype: bool
        """
        return self._enable_room

    @enable_room.setter
    def enable_room(self, enable_room):
        """Sets the enable_room of this UserFunctionDTO.

        是否开启智能协同白板功能。如果开启，表示该帐号是给智能协同白板使用，占用企业智能协同白板的资源，如果资源不足，则无法开启。 默认值：false。 > 该参数将废弃，请勿使用。 

        :param enable_room: The enable_room of this UserFunctionDTO.
        :type enable_room: bool
        """
        self._enable_room = enable_room

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
        if not isinstance(other, UserFunctionDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
