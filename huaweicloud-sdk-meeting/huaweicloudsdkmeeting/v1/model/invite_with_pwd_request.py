# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InviteWithPwdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'conference_id': 'str',
        'body': 'RestInviteWithPwdReqBody'
    }

    attribute_map = {
        'conference_id': 'conferenceID',
        'body': 'body'
    }

    def __init__(self, conference_id=None, body=None):
        """InviteWithPwdRequest

        The model defined in huaweicloud sdk

        :param conference_id: 会议ID。
        :type conference_id: str
        :param body: Body of the InviteWithPwdRequest
        :type body: :class:`huaweicloudsdkmeeting.v1.RestInviteWithPwdReqBody`
        """
        
        

        self._conference_id = None
        self._body = None
        self.discriminator = None

        self.conference_id = conference_id
        if body is not None:
            self.body = body

    @property
    def conference_id(self):
        """Gets the conference_id of this InviteWithPwdRequest.

        会议ID。

        :return: The conference_id of this InviteWithPwdRequest.
        :rtype: str
        """
        return self._conference_id

    @conference_id.setter
    def conference_id(self, conference_id):
        """Sets the conference_id of this InviteWithPwdRequest.

        会议ID。

        :param conference_id: The conference_id of this InviteWithPwdRequest.
        :type conference_id: str
        """
        self._conference_id = conference_id

    @property
    def body(self):
        """Gets the body of this InviteWithPwdRequest.


        :return: The body of this InviteWithPwdRequest.
        :rtype: :class:`huaweicloudsdkmeeting.v1.RestInviteWithPwdReqBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this InviteWithPwdRequest.


        :param body: The body of this InviteWithPwdRequest.
        :type body: :class:`huaweicloudsdkmeeting.v1.RestInviteWithPwdReqBody`
        """
        self._body = body

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
        if not isinstance(other, InviteWithPwdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
