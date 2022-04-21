# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDefectsStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'severity': 'StatisticSeverityV2',
        'status': 'StatisticStatusV2'
    }

    attribute_map = {
        'severity': 'severity',
        'status': 'status'
    }

    def __init__(self, severity=None, status=None):
        """ShowTaskDefectsStatisticResponse

        The model defined in huaweicloud sdk

        :param severity: 
        :type severity: :class:`huaweicloudsdkcodecheck.v2.StatisticSeverityV2`
        :param status: 
        :type status: :class:`huaweicloudsdkcodecheck.v2.StatisticStatusV2`
        """
        
        super(ShowTaskDefectsStatisticResponse, self).__init__()

        self._severity = None
        self._status = None
        self.discriminator = None

        if severity is not None:
            self.severity = severity
        if status is not None:
            self.status = status

    @property
    def severity(self):
        """Gets the severity of this ShowTaskDefectsStatisticResponse.


        :return: The severity of this ShowTaskDefectsStatisticResponse.
        :rtype: :class:`huaweicloudsdkcodecheck.v2.StatisticSeverityV2`
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        """Sets the severity of this ShowTaskDefectsStatisticResponse.


        :param severity: The severity of this ShowTaskDefectsStatisticResponse.
        :type severity: :class:`huaweicloudsdkcodecheck.v2.StatisticSeverityV2`
        """
        self._severity = severity

    @property
    def status(self):
        """Gets the status of this ShowTaskDefectsStatisticResponse.


        :return: The status of this ShowTaskDefectsStatisticResponse.
        :rtype: :class:`huaweicloudsdkcodecheck.v2.StatisticStatusV2`
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ShowTaskDefectsStatisticResponse.


        :param status: The status of this ShowTaskDefectsStatisticResponse.
        :type status: :class:`huaweicloudsdkcodecheck.v2.StatisticStatusV2`
        """
        self._status = status

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
        if not isinstance(other, ShowTaskDefectsStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
