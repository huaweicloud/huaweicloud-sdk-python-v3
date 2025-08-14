# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetHaConfigurationResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery_choice': 'str'
    }

    attribute_map = {
        'disaster_recovery_choice': 'disaster_recovery_choice'
    }

    def __init__(self, disaster_recovery_choice=None):
        r"""GetHaConfigurationResponse

        The model defined in huaweicloud sdk

        :param disaster_recovery_choice: 高可用选项，接受高可用或者拒绝高可用功能。
        :type disaster_recovery_choice: str
        """
        
        super(GetHaConfigurationResponse, self).__init__()

        self._disaster_recovery_choice = None
        self.discriminator = None

        if disaster_recovery_choice is not None:
            self.disaster_recovery_choice = disaster_recovery_choice

    @property
    def disaster_recovery_choice(self):
        r"""Gets the disaster_recovery_choice of this GetHaConfigurationResponse.

        高可用选项，接受高可用或者拒绝高可用功能。

        :return: The disaster_recovery_choice of this GetHaConfigurationResponse.
        :rtype: str
        """
        return self._disaster_recovery_choice

    @disaster_recovery_choice.setter
    def disaster_recovery_choice(self, disaster_recovery_choice):
        r"""Sets the disaster_recovery_choice of this GetHaConfigurationResponse.

        高可用选项，接受高可用或者拒绝高可用功能。

        :param disaster_recovery_choice: The disaster_recovery_choice of this GetHaConfigurationResponse.
        :type disaster_recovery_choice: str
        """
        self._disaster_recovery_choice = disaster_recovery_choice

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
        if not isinstance(other, GetHaConfigurationResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
