# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDisasterRecoveryDrillNameRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery_drill': 'UpdateDisasterRecoveryDrillNameRequestParams'
    }

    attribute_map = {
        'disaster_recovery_drill': 'disaster_recovery_drill'
    }

    def __init__(self, disaster_recovery_drill=None):
        """UpdateDisasterRecoveryDrillNameRequestBody

        The model defined in huaweicloud sdk

        :param disaster_recovery_drill: 
        :type disaster_recovery_drill: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequestParams`
        """
        
        

        self._disaster_recovery_drill = None
        self.discriminator = None

        self.disaster_recovery_drill = disaster_recovery_drill

    @property
    def disaster_recovery_drill(self):
        """Gets the disaster_recovery_drill of this UpdateDisasterRecoveryDrillNameRequestBody.

        :return: The disaster_recovery_drill of this UpdateDisasterRecoveryDrillNameRequestBody.
        :rtype: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequestParams`
        """
        return self._disaster_recovery_drill

    @disaster_recovery_drill.setter
    def disaster_recovery_drill(self, disaster_recovery_drill):
        """Sets the disaster_recovery_drill of this UpdateDisasterRecoveryDrillNameRequestBody.

        :param disaster_recovery_drill: The disaster_recovery_drill of this UpdateDisasterRecoveryDrillNameRequestBody.
        :type disaster_recovery_drill: :class:`huaweicloudsdksdrs.v1.UpdateDisasterRecoveryDrillNameRequestParams`
        """
        self._disaster_recovery_drill = disaster_recovery_drill

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
        if not isinstance(other, UpdateDisasterRecoveryDrillNameRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
