# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePtrRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ptr_id': 'str',
        'body': 'UpdatePtrRequestBody'
    }

    attribute_map = {
        'ptr_id': 'ptr_id',
        'body': 'body'
    }

    def __init__(self, ptr_id=None, body=None):
        r"""UpdatePtrRequest

        The model defined in huaweicloud sdk

        :param ptr_id: 反向解析ID。
        :type ptr_id: str
        :param body: Body of the UpdatePtrRequest
        :type body: :class:`huaweicloudsdkdns.v2.UpdatePtrRequestBody`
        """
        
        

        self._ptr_id = None
        self._body = None
        self.discriminator = None

        self.ptr_id = ptr_id
        if body is not None:
            self.body = body

    @property
    def ptr_id(self):
        r"""Gets the ptr_id of this UpdatePtrRequest.

        反向解析ID。

        :return: The ptr_id of this UpdatePtrRequest.
        :rtype: str
        """
        return self._ptr_id

    @ptr_id.setter
    def ptr_id(self, ptr_id):
        r"""Sets the ptr_id of this UpdatePtrRequest.

        反向解析ID。

        :param ptr_id: The ptr_id of this UpdatePtrRequest.
        :type ptr_id: str
        """
        self._ptr_id = ptr_id

    @property
    def body(self):
        r"""Gets the body of this UpdatePtrRequest.

        :return: The body of this UpdatePtrRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.UpdatePtrRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdatePtrRequest.

        :param body: The body of this UpdatePtrRequest.
        :type body: :class:`huaweicloudsdkdns.v2.UpdatePtrRequestBody`
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
        if not isinstance(other, UpdatePtrRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
