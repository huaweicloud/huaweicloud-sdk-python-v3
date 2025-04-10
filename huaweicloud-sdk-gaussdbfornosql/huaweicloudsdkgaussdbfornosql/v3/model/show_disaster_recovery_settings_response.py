# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowDisasterRecoverySettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'disaster_recovery_settings': 'list[SwitchoverRatioInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'disaster_recovery_settings': 'disaster_recovery_settings',
        'total_count': 'total_count'
    }

    def __init__(self, disaster_recovery_settings=None, total_count=None):
        r"""ShowDisasterRecoverySettingsResponse

        The model defined in huaweicloud sdk

        :param disaster_recovery_settings: 容灾切换的故障节点比例列表。
        :type disaster_recovery_settings: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchoverRatioInfo`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ShowDisasterRecoverySettingsResponse, self).__init__()

        self._disaster_recovery_settings = None
        self._total_count = None
        self.discriminator = None

        if disaster_recovery_settings is not None:
            self.disaster_recovery_settings = disaster_recovery_settings
        if total_count is not None:
            self.total_count = total_count

    @property
    def disaster_recovery_settings(self):
        r"""Gets the disaster_recovery_settings of this ShowDisasterRecoverySettingsResponse.

        容灾切换的故障节点比例列表。

        :return: The disaster_recovery_settings of this ShowDisasterRecoverySettingsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchoverRatioInfo`]
        """
        return self._disaster_recovery_settings

    @disaster_recovery_settings.setter
    def disaster_recovery_settings(self, disaster_recovery_settings):
        r"""Sets the disaster_recovery_settings of this ShowDisasterRecoverySettingsResponse.

        容灾切换的故障节点比例列表。

        :param disaster_recovery_settings: The disaster_recovery_settings of this ShowDisasterRecoverySettingsResponse.
        :type disaster_recovery_settings: list[:class:`huaweicloudsdkgaussdbfornosql.v3.SwitchoverRatioInfo`]
        """
        self._disaster_recovery_settings = disaster_recovery_settings

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowDisasterRecoverySettingsResponse.

        总记录数。

        :return: The total_count of this ShowDisasterRecoverySettingsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowDisasterRecoverySettingsResponse.

        总记录数。

        :param total_count: The total_count of this ShowDisasterRecoverySettingsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowDisasterRecoverySettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
