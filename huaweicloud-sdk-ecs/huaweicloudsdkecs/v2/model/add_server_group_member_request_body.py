# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddServerGroupMemberRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'add_member': 'ServerGroupMember'
    }

    attribute_map = {
        'add_member': 'add_member'
    }

    def __init__(self, add_member=None):
        """AddServerGroupMemberRequestBody

        The model defined in huaweicloud sdk

        :param add_member: 
        :type add_member: :class:`huaweicloudsdkecs.v2.ServerGroupMember`
        """
        
        

        self._add_member = None
        self.discriminator = None

        self.add_member = add_member

    @property
    def add_member(self):
        """Gets the add_member of this AddServerGroupMemberRequestBody.


        :return: The add_member of this AddServerGroupMemberRequestBody.
        :rtype: :class:`huaweicloudsdkecs.v2.ServerGroupMember`
        """
        return self._add_member

    @add_member.setter
    def add_member(self, add_member):
        """Sets the add_member of this AddServerGroupMemberRequestBody.


        :param add_member: The add_member of this AddServerGroupMemberRequestBody.
        :type add_member: :class:`huaweicloudsdkecs.v2.ServerGroupMember`
        """
        self._add_member = add_member

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
        if not isinstance(other, AddServerGroupMemberRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
