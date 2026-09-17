# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServiceSpecificCredentialV5Request:

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
        'credential_id': 'str',
        'body': 'UpdateServiceSpecificCredentialReq'
    }

    attribute_map = {
        'user_id': 'user_id',
        'credential_id': 'credential_id',
        'body': 'body'
    }

    def __init__(self, user_id=None, credential_id=None, body=None):
        r"""UpdateServiceSpecificCredentialV5Request

        The model defined in huaweicloud sdk

        :param user_id: IAM用户ID。
        :type user_id: str
        :param credential_id: 服务专属凭证ID。
        :type credential_id: str
        :param body: Body of the UpdateServiceSpecificCredentialV5Request
        :type body: :class:`huaweicloudsdkiam.v5.UpdateServiceSpecificCredentialReq`
        """
        
        

        self._user_id = None
        self._credential_id = None
        self._body = None
        self.discriminator = None

        self.user_id = user_id
        self.credential_id = credential_id
        if body is not None:
            self.body = body

    @property
    def user_id(self):
        r"""Gets the user_id of this UpdateServiceSpecificCredentialV5Request.

        IAM用户ID。

        :return: The user_id of this UpdateServiceSpecificCredentialV5Request.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this UpdateServiceSpecificCredentialV5Request.

        IAM用户ID。

        :param user_id: The user_id of this UpdateServiceSpecificCredentialV5Request.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def credential_id(self):
        r"""Gets the credential_id of this UpdateServiceSpecificCredentialV5Request.

        服务专属凭证ID。

        :return: The credential_id of this UpdateServiceSpecificCredentialV5Request.
        :rtype: str
        """
        return self._credential_id

    @credential_id.setter
    def credential_id(self, credential_id):
        r"""Sets the credential_id of this UpdateServiceSpecificCredentialV5Request.

        服务专属凭证ID。

        :param credential_id: The credential_id of this UpdateServiceSpecificCredentialV5Request.
        :type credential_id: str
        """
        self._credential_id = credential_id

    @property
    def body(self):
        r"""Gets the body of this UpdateServiceSpecificCredentialV5Request.

        :return: The body of this UpdateServiceSpecificCredentialV5Request.
        :rtype: :class:`huaweicloudsdkiam.v5.UpdateServiceSpecificCredentialReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateServiceSpecificCredentialV5Request.

        :param body: The body of this UpdateServiceSpecificCredentialV5Request.
        :type body: :class:`huaweicloudsdkiam.v5.UpdateServiceSpecificCredentialReq`
        """
        self._body = body

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateServiceSpecificCredentialV5Request):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
