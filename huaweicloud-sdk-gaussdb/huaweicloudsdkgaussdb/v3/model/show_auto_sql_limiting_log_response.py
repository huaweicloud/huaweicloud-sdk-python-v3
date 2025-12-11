# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAutoSqlLimitingLogResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'logs': 'list[AutoSqlLimitingLog]'
    }

    attribute_map = {
        'logs': 'logs'
    }

    def __init__(self, logs=None):
        r"""ShowAutoSqlLimitingLogResponse

        The model defined in huaweicloud sdk

        :param logs: **参数解释**：  查询自治限流执行记录列表。  **约束限制**：  不涉及。
        :type logs: list[:class:`huaweicloudsdkgaussdb.v3.AutoSqlLimitingLog`]
        """
        
        super().__init__()

        self._logs = None
        self.discriminator = None

        if logs is not None:
            self.logs = logs

    @property
    def logs(self):
        r"""Gets the logs of this ShowAutoSqlLimitingLogResponse.

        **参数解释**：  查询自治限流执行记录列表。  **约束限制**：  不涉及。

        :return: The logs of this ShowAutoSqlLimitingLogResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.AutoSqlLimitingLog`]
        """
        return self._logs

    @logs.setter
    def logs(self, logs):
        r"""Sets the logs of this ShowAutoSqlLimitingLogResponse.

        **参数解释**：  查询自治限流执行记录列表。  **约束限制**：  不涉及。

        :param logs: The logs of this ShowAutoSqlLimitingLogResponse.
        :type logs: list[:class:`huaweicloudsdkgaussdb.v3.AutoSqlLimitingLog`]
        """
        self._logs = logs

    def to_dict(self):
        import warnings
        warnings.warn("ShowAutoSqlLimitingLogResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowAutoSqlLimitingLogResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
