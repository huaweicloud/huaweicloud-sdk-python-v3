# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateReportCustomEventRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'integration_key': 'str',
        'body': 'ReportCustomEventRequestBody'
    }

    attribute_map = {
        'integration_key': 'integration_key',
        'body': 'body'
    }

    def __init__(self, integration_key=None, body=None):
        r"""CreateReportCustomEventRequest

        The model defined in huaweicloud sdk

        :param integration_key: 集成ID
        :type integration_key: str
        :param body: Body of the CreateReportCustomEventRequest
        :type body: :class:`huaweicloudsdkcoc.v1.ReportCustomEventRequestBody`
        """
        
        

        self._integration_key = None
        self._body = None
        self.discriminator = None

        self.integration_key = integration_key
        if body is not None:
            self.body = body

    @property
    def integration_key(self):
        r"""Gets the integration_key of this CreateReportCustomEventRequest.

        集成ID

        :return: The integration_key of this CreateReportCustomEventRequest.
        :rtype: str
        """
        return self._integration_key

    @integration_key.setter
    def integration_key(self, integration_key):
        r"""Sets the integration_key of this CreateReportCustomEventRequest.

        集成ID

        :param integration_key: The integration_key of this CreateReportCustomEventRequest.
        :type integration_key: str
        """
        self._integration_key = integration_key

    @property
    def body(self):
        r"""Gets the body of this CreateReportCustomEventRequest.

        :return: The body of this CreateReportCustomEventRequest.
        :rtype: :class:`huaweicloudsdkcoc.v1.ReportCustomEventRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateReportCustomEventRequest.

        :param body: The body of this CreateReportCustomEventRequest.
        :type body: :class:`huaweicloudsdkcoc.v1.ReportCustomEventRequestBody`
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
        if not isinstance(other, CreateReportCustomEventRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
