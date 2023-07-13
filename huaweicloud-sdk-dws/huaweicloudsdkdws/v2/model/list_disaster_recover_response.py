# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDisasterRecoverResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery': 'list[DisasterRecovery]'
    }

    attribute_map = {
        'disaster_recovery': 'disaster_recovery'
    }

    def __init__(self, disaster_recovery=None):
        """ListDisasterRecoverResponse

        The model defined in huaweicloud sdk

        :param disaster_recovery: 容灾对象
        :type disaster_recovery: list[:class:`huaweicloudsdkdws.v2.DisasterRecovery`]
        """
        
        super(ListDisasterRecoverResponse, self).__init__()

        self._disaster_recovery = None
        self.discriminator = None

        if disaster_recovery is not None:
            self.disaster_recovery = disaster_recovery

    @property
    def disaster_recovery(self):
        """Gets the disaster_recovery of this ListDisasterRecoverResponse.

        容灾对象

        :return: The disaster_recovery of this ListDisasterRecoverResponse.
        :rtype: list[:class:`huaweicloudsdkdws.v2.DisasterRecovery`]
        """
        return self._disaster_recovery

    @disaster_recovery.setter
    def disaster_recovery(self, disaster_recovery):
        """Sets the disaster_recovery of this ListDisasterRecoverResponse.

        容灾对象

        :param disaster_recovery: The disaster_recovery of this ListDisasterRecoverResponse.
        :type disaster_recovery: list[:class:`huaweicloudsdkdws.v2.DisasterRecovery`]
        """
        self._disaster_recovery = disaster_recovery

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
        if not isinstance(other, ListDisasterRecoverResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
