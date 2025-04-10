# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInitPasswordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user_id': 'str',
        'body': 'ResetPasswordReq'
    }

    attribute_map = {
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, user_id=None, body=None):
        r"""UpdateInitPasswordRequest

        The model defined in huaweicloud sdk

        :param user_id: 用户id
        :type user_id: str
        :param body: Body of the UpdateInitPasswordRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.ResetPasswordReq`
        """
        
        

        self._user_id = None
        self._body = None
        self.discriminator = None

        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def user_id(self):
        r"""Gets the user_id of this UpdateInitPasswordRequest.

        用户id

        :return: The user_id of this UpdateInitPasswordRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UpdateInitPasswordRequest.

        用户id

        :param user_id: The user_id of this UpdateInitPasswordRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        r"""Gets the body of this UpdateInitPasswordRequest.

        :return: The body of this UpdateInitPasswordRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.ResetPasswordReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateInitPasswordRequest.

        :param body: The body of this UpdateInitPasswordRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.ResetPasswordReq`
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
        if not isinstance(other, UpdateInitPasswordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
