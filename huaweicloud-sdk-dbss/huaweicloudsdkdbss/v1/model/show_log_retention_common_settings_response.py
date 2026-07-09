# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowLogRetentionCommonSettingsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'log_retention': 'CommonSettingsResponseLogRetention',
        'data_usage_limit': 'int'
    }

    attribute_map = {
        'log_retention': 'log_retention',
        'data_usage_limit': 'data_usage_limit'
    }

    def __init__(self, log_retention=None, data_usage_limit=None):
        r"""ShowLogRetentionCommonSettingsResponse

        The model defined in huaweicloud sdk

        :param log_retention: 
        :type log_retention: :class:`huaweicloudsdkdbss.v1.CommonSettingsResponseLogRetention`
        :param data_usage_limit: 日志存储磁盘占用上限
        :type data_usage_limit: int
        """
        
        super().__init__()

        self._log_retention = None
        self._data_usage_limit = None
        self.discriminator = None

        if log_retention is not None:
            self.log_retention = log_retention
        if data_usage_limit is not None:
            self.data_usage_limit = data_usage_limit

    @property
    def log_retention(self):
        r"""Gets the log_retention of this ShowLogRetentionCommonSettingsResponse.

        :return: The log_retention of this ShowLogRetentionCommonSettingsResponse.
        :rtype: :class:`huaweicloudsdkdbss.v1.CommonSettingsResponseLogRetention`
        """
        return self._log_retention

    @log_retention.setter
    def log_retention(self, log_retention):
        r"""Sets the log_retention of this ShowLogRetentionCommonSettingsResponse.

        :param log_retention: The log_retention of this ShowLogRetentionCommonSettingsResponse.
        :type log_retention: :class:`huaweicloudsdkdbss.v1.CommonSettingsResponseLogRetention`
        """
        self._log_retention = log_retention

    @property
    def data_usage_limit(self):
        r"""Gets the data_usage_limit of this ShowLogRetentionCommonSettingsResponse.

        日志存储磁盘占用上限

        :return: The data_usage_limit of this ShowLogRetentionCommonSettingsResponse.
        :rtype: int
        """
        return self._data_usage_limit

    @data_usage_limit.setter
    def data_usage_limit(self, data_usage_limit):
        r"""Sets the data_usage_limit of this ShowLogRetentionCommonSettingsResponse.

        日志存储磁盘占用上限

        :param data_usage_limit: The data_usage_limit of this ShowLogRetentionCommonSettingsResponse.
        :type data_usage_limit: int
        """
        self._data_usage_limit = data_usage_limit

    def to_dict(self):
        import warnings
        warnings.warn("ShowLogRetentionCommonSettingsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowLogRetentionCommonSettingsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
