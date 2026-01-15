# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableAlertRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'alert_rule_id': 'str',
        'status': 'JobStatus',
        'process_status': 'JobProcessStatus'
    }

    attribute_map = {
        'alert_rule_id': 'alert_rule_id',
        'status': 'status',
        'process_status': 'process_status'
    }

    def __init__(self, alert_rule_id=None, status=None, process_status=None):
        r"""EnableAlertRuleResponse

        The model defined in huaweicloud sdk

        :param alert_rule_id: UUID
        :type alert_rule_id: str
        :param status: 
        :type status: :class:`huaweicloudsdksecmaster.v2.JobStatus`
        :param process_status: 
        :type process_status: :class:`huaweicloudsdksecmaster.v2.JobProcessStatus`
        """
        
        super().__init__()

        self._alert_rule_id = None
        self._status = None
        self._process_status = None
        self.discriminator = None

        if alert_rule_id is not None:
            self.alert_rule_id = alert_rule_id
        if status is not None:
            self.status = status
        if process_status is not None:
            self.process_status = process_status

    @property
    def alert_rule_id(self):
        r"""Gets the alert_rule_id of this EnableAlertRuleResponse.

        UUID

        :return: The alert_rule_id of this EnableAlertRuleResponse.
        :rtype: str
        """
        return self._alert_rule_id

    @alert_rule_id.setter
    def alert_rule_id(self, alert_rule_id):
        r"""Sets the alert_rule_id of this EnableAlertRuleResponse.

        UUID

        :param alert_rule_id: The alert_rule_id of this EnableAlertRuleResponse.
        :type alert_rule_id: str
        """
        self._alert_rule_id = alert_rule_id

    @property
    def status(self):
        r"""Gets the status of this EnableAlertRuleResponse.

        :return: The status of this EnableAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.JobStatus`
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this EnableAlertRuleResponse.

        :param status: The status of this EnableAlertRuleResponse.
        :type status: :class:`huaweicloudsdksecmaster.v2.JobStatus`
        """
        self._status = status

    @property
    def process_status(self):
        r"""Gets the process_status of this EnableAlertRuleResponse.

        :return: The process_status of this EnableAlertRuleResponse.
        :rtype: :class:`huaweicloudsdksecmaster.v2.JobProcessStatus`
        """
        return self._process_status

    @process_status.setter
    def process_status(self, process_status):
        r"""Sets the process_status of this EnableAlertRuleResponse.

        :param process_status: The process_status of this EnableAlertRuleResponse.
        :type process_status: :class:`huaweicloudsdksecmaster.v2.JobProcessStatus`
        """
        self._process_status = process_status

    def to_dict(self):
        import warnings
        warnings.warn("EnableAlertRuleResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, EnableAlertRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
