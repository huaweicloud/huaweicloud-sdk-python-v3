# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthCheckRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'health_check_id': 'str',
        'body': 'UpdateHealthCheckRequestBody'
    }

    attribute_map = {
        'health_check_id': 'health_check_id',
        'body': 'body'
    }

    def __init__(self, health_check_id=None, body=None):
        r"""UpdateHealthCheckRequest

        The model defined in huaweicloud sdk

        :param health_check_id: 健康检查ID。
        :type health_check_id: str
        :param body: Body of the UpdateHealthCheckRequest
        :type body: :class:`huaweicloudsdkga.v1.UpdateHealthCheckRequestBody`
        """
        
        

        self._health_check_id = None
        self._body = None
        self.discriminator = None

        self.health_check_id = health_check_id
        if body is not None:
            self.body = body

    @property
    def health_check_id(self):
        r"""Gets the health_check_id of this UpdateHealthCheckRequest.

        健康检查ID。

        :return: The health_check_id of this UpdateHealthCheckRequest.
        :rtype: str
        """
        return self._health_check_id

    @health_check_id.setter
    def health_check_id(self, health_check_id):
        r"""Sets the health_check_id of this UpdateHealthCheckRequest.

        健康检查ID。

        :param health_check_id: The health_check_id of this UpdateHealthCheckRequest.
        :type health_check_id: str
        """
        self._health_check_id = health_check_id

    @property
    def body(self):
        r"""Gets the body of this UpdateHealthCheckRequest.

        :return: The body of this UpdateHealthCheckRequest.
        :rtype: :class:`huaweicloudsdkga.v1.UpdateHealthCheckRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHealthCheckRequest.

        :param body: The body of this UpdateHealthCheckRequest.
        :type body: :class:`huaweicloudsdkga.v1.UpdateHealthCheckRequestBody`
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
        if not isinstance(other, UpdateHealthCheckRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
