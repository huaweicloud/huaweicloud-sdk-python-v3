# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateDisasterInfoRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery_id': 'str',
        'body': 'UpdateDisasterRecoveryRequest'
    }

    attribute_map = {
        'disaster_recovery_id': 'disaster_recovery_id',
        'body': 'body'
    }

    def __init__(self, disaster_recovery_id=None, body=None):
        """UpdateDisasterInfoRequest

        The model defined in huaweicloud sdk

        :param disaster_recovery_id: 容灾ID
        :type disaster_recovery_id: str
        :param body: Body of the UpdateDisasterInfoRequest
        :type body: :class:`huaweicloudsdkdws.v2.UpdateDisasterRecoveryRequest`
        """
        
        

        self._disaster_recovery_id = None
        self._body = None
        self.discriminator = None

        self.disaster_recovery_id = disaster_recovery_id
        if body is not None:
            self.body = body

    @property
    def disaster_recovery_id(self):
        """Gets the disaster_recovery_id of this UpdateDisasterInfoRequest.

        容灾ID

        :return: The disaster_recovery_id of this UpdateDisasterInfoRequest.
        :rtype: str
        """
        return self._disaster_recovery_id

    @disaster_recovery_id.setter
    def disaster_recovery_id(self, disaster_recovery_id):
        """Sets the disaster_recovery_id of this UpdateDisasterInfoRequest.

        容灾ID

        :param disaster_recovery_id: The disaster_recovery_id of this UpdateDisasterInfoRequest.
        :type disaster_recovery_id: str
        """
        self._disaster_recovery_id = disaster_recovery_id

    @property
    def body(self):
        """Gets the body of this UpdateDisasterInfoRequest.

        :return: The body of this UpdateDisasterInfoRequest.
        :rtype: :class:`huaweicloudsdkdws.v2.UpdateDisasterRecoveryRequest`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this UpdateDisasterInfoRequest.

        :param body: The body of this UpdateDisasterInfoRequest.
        :type body: :class:`huaweicloudsdkdws.v2.UpdateDisasterRecoveryRequest`
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
        if not isinstance(other, UpdateDisasterInfoRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other