# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePermanentAccessKeyRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_key': 'str',
        'body': 'UpdatePermanentAccessKeyRequestBody'
    }

    attribute_map = {
        'access_key': 'access_key',
        'body': 'body'
    }

    def __init__(self, access_key=None, body=None):
        r"""UpdatePermanentAccessKeyRequest

        The model defined in huaweicloud sdk

        :param access_key: 待修改的指定AK。
        :type access_key: str
        :param body: Body of the UpdatePermanentAccessKeyRequest
        :type body: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyRequestBody`
        """
        
        

        self._access_key = None
        self._body = None
        self.discriminator = None

        self.access_key = access_key
        if body is not None:
            self.body = body

    @property
    def access_key(self):
        r"""Gets the access_key of this UpdatePermanentAccessKeyRequest.

        待修改的指定AK。

        :return: The access_key of this UpdatePermanentAccessKeyRequest.
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        r"""Sets the access_key of this UpdatePermanentAccessKeyRequest.

        待修改的指定AK。

        :param access_key: The access_key of this UpdatePermanentAccessKeyRequest.
        :type access_key: str
        """
        self._access_key = access_key

    @property
    def body(self):
        r"""Gets the body of this UpdatePermanentAccessKeyRequest.

        :return: The body of this UpdatePermanentAccessKeyRequest.
        :rtype: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePermanentAccessKeyRequest.

        :param body: The body of this UpdatePermanentAccessKeyRequest.
        :type body: :class:`huaweicloudsdkiam.v3.UpdatePermanentAccessKeyRequestBody`
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
        if not isinstance(other, UpdatePermanentAccessKeyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
