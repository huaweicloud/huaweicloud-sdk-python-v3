# coding: utf-8

import pprint
import re

import six





class GlanceAddImageMemberRequestBody:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'member': 'str'
    }

    attribute_map = {
        'member': 'member'
    }

    def __init__(self, member=None):
        """GlanceAddImageMemberRequestBody - a model defined in huaweicloud sdk"""
        
        

        self._member = None
        self.discriminator = None

        self.member = member

    @property
    def member(self):
        """Gets the member of this GlanceAddImageMemberRequestBody.

        镜像成员。取值为目标用户的项目ID。

        :return: The member of this GlanceAddImageMemberRequestBody.
        :rtype: str
        """
        return self._member

    @member.setter
    def member(self, member):
        """Sets the member of this GlanceAddImageMemberRequestBody.

        镜像成员。取值为目标用户的项目ID。

        :param member: The member of this GlanceAddImageMemberRequestBody.
        :type: str
        """
        self._member = member

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, GlanceAddImageMemberRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
