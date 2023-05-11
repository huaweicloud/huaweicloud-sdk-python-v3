# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestInviteReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'attendees': 'list[Attendee]'
    }

    attribute_map = {
        'attendees': 'attendees'
    }

    def __init__(self, attendees=None):
        """RestInviteReqBody

        The model defined in huaweicloud sdk

        :param attendees: 邀请的与会者列表。
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.Attendee`]
        """
        
        

        self._attendees = None
        self.discriminator = None

        self.attendees = attendees

    @property
    def attendees(self):
        """Gets the attendees of this RestInviteReqBody.

        邀请的与会者列表。

        :return: The attendees of this RestInviteReqBody.
        :rtype: list[:class:`huaweicloudsdkmeeting.v1.Attendee`]
        """
        return self._attendees

    @attendees.setter
    def attendees(self, attendees):
        """Sets the attendees of this RestInviteReqBody.

        邀请的与会者列表。

        :param attendees: The attendees of this RestInviteReqBody.
        :type attendees: list[:class:`huaweicloudsdkmeeting.v1.Attendee`]
        """
        self._attendees = attendees

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
        if not isinstance(other, RestInviteReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
