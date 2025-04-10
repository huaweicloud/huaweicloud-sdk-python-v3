# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDisasterRecoveryDrillNameRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery_drill_id': 'str',
        'body': 'UpdateDisasterRecoveryDrillNameRequestBody'
    }

    attribute_map = {
        'disaster_recovery_drill_id': 'disaster_recovery_drill_id',
        'body': 'body'
    }

    def __init__(self, disaster_recovery_drill_id=None, body=None):
        r"""UpdateDisasterRecoveryDrillNameRequest

        The model defined in huaweicloud sdk

        :param disaster_recovery_drill_id: 容灾演练的ID。
        :type disaster_recovery_drill_id: str
        :param body: Body of the UpdateDisasterRecoveryDrillNameRequest
        :type body: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequestBody`
        """
        
        

        self._disaster_recovery_drill_id = None
        self._body = None
        self.discriminator = None

        self.disaster_recovery_drill_id = disaster_recovery_drill_id
        if body is not None:
            self.body = body

    @property
    def disaster_recovery_drill_id(self):
        r"""Gets the disaster_recovery_drill_id of this UpdateDisasterRecoveryDrillNameRequest.

        容灾演练的ID。

        :return: The disaster_recovery_drill_id of this UpdateDisasterRecoveryDrillNameRequest.
        :rtype: str
        """
        return self._disaster_recovery_drill_id

    @disaster_recovery_drill_id.setter
    def disaster_recovery_drill_id(self, disaster_recovery_drill_id):
        r"""Sets the disaster_recovery_drill_id of this UpdateDisasterRecoveryDrillNameRequest.

        容灾演练的ID。

        :param disaster_recovery_drill_id: The disaster_recovery_drill_id of this UpdateDisasterRecoveryDrillNameRequest.
        :type disaster_recovery_drill_id: str
        """
        self._disaster_recovery_drill_id = disaster_recovery_drill_id

    @property
    def body(self):
        r"""Gets the body of this UpdateDisasterRecoveryDrillNameRequest.

        :return: The body of this UpdateDisasterRecoveryDrillNameRequest.
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateDisasterRecoveryDrillNameRequest.

        :param body: The body of this UpdateDisasterRecoveryDrillNameRequest.
        :type body: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequestBody`
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
        if not isinstance(other, UpdateDisasterRecoveryDrillNameRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
