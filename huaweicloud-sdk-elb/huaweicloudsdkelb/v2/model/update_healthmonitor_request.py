# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateHealthmonitorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'healthmonitor_id': 'str',
        'body': 'UpdateHealthmonitorRequestBody'
    }

    attribute_map = {
        'healthmonitor_id': 'healthmonitor_id',
        'body': 'body'
    }

    def __init__(self, healthmonitor_id=None, body=None):
        r"""UpdateHealthmonitorRequest

        The model defined in huaweicloud sdk

        :param healthmonitor_id: 健康检查id
        :type healthmonitor_id: str
        :param body: Body of the UpdateHealthmonitorRequest
        :type body: :class:`huaweicloudsdkelb.v2.UpdateHealthmonitorRequestBody`
        """
        
        

        self._healthmonitor_id = None
        self._body = None
        self.discriminator = None

        self.healthmonitor_id = healthmonitor_id
        if body is not None:
            self.body = body

    @property
    def healthmonitor_id(self):
        r"""Gets the healthmonitor_id of this UpdateHealthmonitorRequest.

        健康检查id

        :return: The healthmonitor_id of this UpdateHealthmonitorRequest.
        :rtype: str
        """
        return self._healthmonitor_id

    @healthmonitor_id.setter
    def healthmonitor_id(self, healthmonitor_id):
        r"""Sets the healthmonitor_id of this UpdateHealthmonitorRequest.

        健康检查id

        :param healthmonitor_id: The healthmonitor_id of this UpdateHealthmonitorRequest.
        :type healthmonitor_id: str
        """
        self._healthmonitor_id = healthmonitor_id

    @property
    def body(self):
        r"""Gets the body of this UpdateHealthmonitorRequest.

        :return: The body of this UpdateHealthmonitorRequest.
        :rtype: :class:`huaweicloudsdkelb.v2.UpdateHealthmonitorRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateHealthmonitorRequest.

        :param body: The body of this UpdateHealthmonitorRequest.
        :type body: :class:`huaweicloudsdkelb.v2.UpdateHealthmonitorRequestBody`
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
        if not isinstance(other, UpdateHealthmonitorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
