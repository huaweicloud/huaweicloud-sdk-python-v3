# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddImageMemberRequestBody:

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
        r"""AddImageMemberRequestBody

        The model defined in huaweicloud sdk

        :param member: 被共享账号的PROJECT_ID
        :type member: str
        """
        
        

        self._member = None
        self.discriminator = None

        if member is not None:
            self.member = member

    @property
    def member(self):
        r"""Gets the member of this AddImageMemberRequestBody.

        被共享账号的PROJECT_ID

        :return: The member of this AddImageMemberRequestBody.
        :rtype: str
        """
        return self._member

    @member.setter
    def member(self, member):
        r"""Sets the member of this AddImageMemberRequestBody.

        被共享账号的PROJECT_ID

        :param member: The member of this AddImageMemberRequestBody.
        :type member: str
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
        if not isinstance(other, AddImageMemberRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
