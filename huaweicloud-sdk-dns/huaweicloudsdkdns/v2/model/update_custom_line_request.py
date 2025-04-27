# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateCustomLineRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'line_id': 'str',
        'body': 'UpdateCustomLineRequestBody'
    }

    attribute_map = {
        'line_id': 'line_id',
        'body': 'body'
    }

    def __init__(self, line_id=None, body=None):
        r"""UpdateCustomLineRequest

        The model defined in huaweicloud sdk

        :param line_id: 自定义线路ID。
        :type line_id: str
        :param body: Body of the UpdateCustomLineRequest
        :type body: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequestBody`
        """
        
        

        self._line_id = None
        self._body = None
        self.discriminator = None

        self.line_id = line_id
        if body is not None:
            self.body = body

    @property
    def line_id(self):
        r"""Gets the line_id of this UpdateCustomLineRequest.

        自定义线路ID。

        :return: The line_id of this UpdateCustomLineRequest.
        :rtype: str
        """
        return self._line_id

    @line_id.setter
    def line_id(self, line_id):
        r"""Sets the line_id of this UpdateCustomLineRequest.

        自定义线路ID。

        :param line_id: The line_id of this UpdateCustomLineRequest.
        :type line_id: str
        """
        self._line_id = line_id

    @property
    def body(self):
        r"""Gets the body of this UpdateCustomLineRequest.

        :return: The body of this UpdateCustomLineRequest.
        :rtype: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateCustomLineRequest.

        :param body: The body of this UpdateCustomLineRequest.
        :type body: :class:`huaweicloudsdkdns.v2.UpdateCustomLineRequestBody`
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
        if not isinstance(other, UpdateCustomLineRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
