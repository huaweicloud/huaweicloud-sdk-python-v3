# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateHttpsInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'iam_user_uuid': 'str',
        'body': 'PasswordRequest'
    }

    attribute_map = {
        'iam_user_uuid': 'iam_user_uuid',
        'body': 'body'
    }

    def __init__(self, iam_user_uuid=None, body=None):
        """ValidateHttpsInfoRequest

        The model defined in huaweicloud sdk

        :param iam_user_uuid: 用户iam_user_uuid
        :type iam_user_uuid: str
        :param body: Body of the ValidateHttpsInfoRequest
        :type body: :class:`huaweicloudsdkcodehub.v3.PasswordRequest`
        """
        
        

        self._iam_user_uuid = None
        self._body = None
        self.discriminator = None

        self.iam_user_uuid = iam_user_uuid
        if body is not None:
            self.body = body

    @property
    def iam_user_uuid(self):
        """Gets the iam_user_uuid of this ValidateHttpsInfoRequest.

        用户iam_user_uuid

        :return: The iam_user_uuid of this ValidateHttpsInfoRequest.
        :rtype: str
        """
        return self._iam_user_uuid

    @iam_user_uuid.setter
    def iam_user_uuid(self, iam_user_uuid):
        """Sets the iam_user_uuid of this ValidateHttpsInfoRequest.

        用户iam_user_uuid

        :param iam_user_uuid: The iam_user_uuid of this ValidateHttpsInfoRequest.
        :type iam_user_uuid: str
        """
        self._iam_user_uuid = iam_user_uuid

    @property
    def body(self):
        """Gets the body of this ValidateHttpsInfoRequest.


        :return: The body of this ValidateHttpsInfoRequest.
        :rtype: :class:`huaweicloudsdkcodehub.v3.PasswordRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ValidateHttpsInfoRequest.


        :param body: The body of this ValidateHttpsInfoRequest.
        :type body: :class:`huaweicloudsdkcodehub.v3.PasswordRequest`
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
        if not isinstance(other, ValidateHttpsInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
