# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateEdgeSite:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'location': 'UpdateLocation'
    }

    attribute_map = {
        'description': 'description',
        'location': 'location'
    }

    def __init__(self, description=None, location=None):
        """UpdateEdgeSite

        The model defined in huaweicloud sdk

        :param description: 边缘小站描述，最大支持长度为255个字节，不允许包含&lt;&gt;
        :type description: str
        :param location: 
        :type location: :class:`huaweicloudsdkies.v1.UpdateLocation`
        """
        
        

        self._description = None
        self._location = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if location is not None:
            self.location = location

    @property
    def description(self):
        """Gets the description of this UpdateEdgeSite.

        边缘小站描述，最大支持长度为255个字节，不允许包含<>

        :return: The description of this UpdateEdgeSite.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateEdgeSite.

        边缘小站描述，最大支持长度为255个字节，不允许包含<>

        :param description: The description of this UpdateEdgeSite.
        :type description: str
        """
        self._description = description

    @property
    def location(self):
        """Gets the location of this UpdateEdgeSite.


        :return: The location of this UpdateEdgeSite.
        :rtype: :class:`huaweicloudsdkies.v1.UpdateLocation`
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this UpdateEdgeSite.


        :param location: The location of this UpdateEdgeSite.
        :type location: :class:`huaweicloudsdkies.v1.UpdateLocation`
        """
        self._location = location

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
        if not isinstance(other, UpdateEdgeSite):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
