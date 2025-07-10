# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnrollAccountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_account_id': 'str',
        'body': 'EnrollAccountRequestBody'
    }

    attribute_map = {
        'managed_account_id': 'managed_account_id',
        'body': 'body'
    }

    def __init__(self, managed_account_id=None, body=None):
        r"""EnrollAccountRequest

        The model defined in huaweicloud sdk

        :param managed_account_id: 纳管账号ID。
        :type managed_account_id: str
        :param body: Body of the EnrollAccountRequest
        :type body: :class:`huaweicloudsdkrgc.v1.EnrollAccountRequestBody`
        """
        
        

        self._managed_account_id = None
        self._body = None
        self.discriminator = None

        self.managed_account_id = managed_account_id
        if body is not None:
            self.body = body

    @property
    def managed_account_id(self):
        r"""Gets the managed_account_id of this EnrollAccountRequest.

        纳管账号ID。

        :return: The managed_account_id of this EnrollAccountRequest.
        :rtype: str
        """
        return self._managed_account_id

    @managed_account_id.setter
    def managed_account_id(self, managed_account_id):
        r"""Sets the managed_account_id of this EnrollAccountRequest.

        纳管账号ID。

        :param managed_account_id: The managed_account_id of this EnrollAccountRequest.
        :type managed_account_id: str
        """
        self._managed_account_id = managed_account_id

    @property
    def body(self):
        r"""Gets the body of this EnrollAccountRequest.

        :return: The body of this EnrollAccountRequest.
        :rtype: :class:`huaweicloudsdkrgc.v1.EnrollAccountRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this EnrollAccountRequest.

        :param body: The body of this EnrollAccountRequest.
        :type body: :class:`huaweicloudsdkrgc.v1.EnrollAccountRequestBody`
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
        if not isinstance(other, EnrollAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
