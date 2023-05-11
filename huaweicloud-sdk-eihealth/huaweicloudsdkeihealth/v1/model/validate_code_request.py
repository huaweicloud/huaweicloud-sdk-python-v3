# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateCodeRequest:

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
        'body': 'CodeVerifyReq'
    }

    attribute_map = {
        'user_id': 'user_id',
        'body': 'body'
    }

    def __init__(self, user_id=None, body=None):
        """ValidateCodeRequest

        The model defined in huaweicloud sdk

        :param user_id: 用户id
        :type user_id: str
        :param body: Body of the ValidateCodeRequest
        :type body: :class:`huaweicloudsdkeihealth.v1.CodeVerifyReq`
        """
        
        

        self._user_id = None
        self._body = None
        self.discriminator = None

        self.user_id = user_id
        if body is not None:
            self.body = body

    @property
    def user_id(self):
        """Gets the user_id of this ValidateCodeRequest.

        用户id

        :return: The user_id of this ValidateCodeRequest.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this ValidateCodeRequest.

        用户id

        :param user_id: The user_id of this ValidateCodeRequest.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def body(self):
        """Gets the body of this ValidateCodeRequest.

        :return: The body of this ValidateCodeRequest.
        :rtype: :class:`huaweicloudsdkeihealth.v1.CodeVerifyReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ValidateCodeRequest.

        :param body: The body of this ValidateCodeRequest.
        :type body: :class:`huaweicloudsdkeihealth.v1.CodeVerifyReq`
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
        if not isinstance(other, ValidateCodeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
