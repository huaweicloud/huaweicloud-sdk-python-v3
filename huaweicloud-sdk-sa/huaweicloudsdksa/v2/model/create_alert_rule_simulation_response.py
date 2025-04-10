# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAlertRuleSimulationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_count': 'int',
        'severity': 'str',
        'x_request_id': 'str'
    }

    attribute_map = {
        'alert_count': 'alert_count',
        'severity': 'severity',
        'x_request_id': 'X-request-id'
    }

    def __init__(self, alert_count=None, severity=None, x_request_id=None):
        r"""CreateAlertRuleSimulationResponse

        The model defined in huaweicloud sdk

        :param alert_count: alert_count
        :type alert_count: int
        :param severity: severity. TIPS, LOW, MEDIUM, HIGH, FATAL
        :type severity: str
        :param x_request_id: 
        :type x_request_id: str
        """
        
        super(CreateAlertRuleSimulationResponse, self).__init__()

        self._alert_count = None
        self._severity = None
        self._x_request_id = None
        self.discriminator = None

        if alert_count is not None:
            self.alert_count = alert_count
        if severity is not None:
            self.severity = severity
        if x_request_id is not None:
            self.x_request_id = x_request_id

    @property
    def alert_count(self):
        r"""Gets the alert_count of this CreateAlertRuleSimulationResponse.

        alert_count

        :return: The alert_count of this CreateAlertRuleSimulationResponse.
        :rtype: int
        """
        return self._alert_count

    @alert_count.setter
    def alert_count(self, alert_count):
        r"""Sets the alert_count of this CreateAlertRuleSimulationResponse.

        alert_count

        :param alert_count: The alert_count of this CreateAlertRuleSimulationResponse.
        :type alert_count: int
        """
        self._alert_count = alert_count

    @property
    def severity(self):
        r"""Gets the severity of this CreateAlertRuleSimulationResponse.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :return: The severity of this CreateAlertRuleSimulationResponse.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this CreateAlertRuleSimulationResponse.

        severity. TIPS, LOW, MEDIUM, HIGH, FATAL

        :param severity: The severity of this CreateAlertRuleSimulationResponse.
        :type severity: str
        """
        self._severity = severity

    @property
    def x_request_id(self):
        r"""Gets the x_request_id of this CreateAlertRuleSimulationResponse.

        :return: The x_request_id of this CreateAlertRuleSimulationResponse.
        :rtype: str
        """
        return self._x_request_id

    @x_request_id.setter
    def x_request_id(self, x_request_id):
        r"""Sets the x_request_id of this CreateAlertRuleSimulationResponse.

        :param x_request_id: The x_request_id of this CreateAlertRuleSimulationResponse.
        :type x_request_id: str
        """
        self._x_request_id = x_request_id

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
        if not isinstance(other, CreateAlertRuleSimulationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
