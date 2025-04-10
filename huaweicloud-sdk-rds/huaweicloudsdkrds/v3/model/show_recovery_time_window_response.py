# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowRecoveryTimeWindowResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recovery_min_time': 'str',
        'recovery_max_time': 'str'
    }

    attribute_map = {
        'recovery_min_time': 'recovery_min_time',
        'recovery_max_time': 'recovery_max_time'
    }

    def __init__(self, recovery_min_time=None, recovery_max_time=None):
        r"""ShowRecoveryTimeWindowResponse

        The model defined in huaweicloud sdk

        :param recovery_min_time: 恢复时间窗左边界（不包含）
        :type recovery_min_time: str
        :param recovery_max_time: 恢复时间窗右边界（包含）
        :type recovery_max_time: str
        """
        
        super(ShowRecoveryTimeWindowResponse, self).__init__()

        self._recovery_min_time = None
        self._recovery_max_time = None
        self.discriminator = None

        if recovery_min_time is not None:
            self.recovery_min_time = recovery_min_time
        if recovery_max_time is not None:
            self.recovery_max_time = recovery_max_time

    @property
    def recovery_min_time(self):
        r"""Gets the recovery_min_time of this ShowRecoveryTimeWindowResponse.

        恢复时间窗左边界（不包含）

        :return: The recovery_min_time of this ShowRecoveryTimeWindowResponse.
        :rtype: str
        """
        return self._recovery_min_time

    @recovery_min_time.setter
    def recovery_min_time(self, recovery_min_time):
        r"""Sets the recovery_min_time of this ShowRecoveryTimeWindowResponse.

        恢复时间窗左边界（不包含）

        :param recovery_min_time: The recovery_min_time of this ShowRecoveryTimeWindowResponse.
        :type recovery_min_time: str
        """
        self._recovery_min_time = recovery_min_time

    @property
    def recovery_max_time(self):
        r"""Gets the recovery_max_time of this ShowRecoveryTimeWindowResponse.

        恢复时间窗右边界（包含）

        :return: The recovery_max_time of this ShowRecoveryTimeWindowResponse.
        :rtype: str
        """
        return self._recovery_max_time

    @recovery_max_time.setter
    def recovery_max_time(self, recovery_max_time):
        r"""Sets the recovery_max_time of this ShowRecoveryTimeWindowResponse.

        恢复时间窗右边界（包含）

        :param recovery_max_time: The recovery_max_time of this ShowRecoveryTimeWindowResponse.
        :type recovery_max_time: str
        """
        self._recovery_max_time = recovery_max_time

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
        if not isinstance(other, ShowRecoveryTimeWindowResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
