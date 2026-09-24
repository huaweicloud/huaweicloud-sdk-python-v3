# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateExpirationTimeResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'affected_backups_count': 'int',
        'new_expiration_day': 'str',
        'operation_log_id': 'str'
    }

    attribute_map = {
        'affected_backups_count': 'affected_backups_count',
        'new_expiration_day': 'new_expiration_day',
        'operation_log_id': 'operation_log_id'
    }

    def __init__(self, affected_backups_count=None, new_expiration_day=None, operation_log_id=None):
        r"""UpdateExpirationTimeResponse

        The model defined in huaweicloud sdk

        :param affected_backups_count: 成功修改过期时间的备份数量。
        :type affected_backups_count: int
        :param new_expiration_day: 修改后的备份过期时间，格式：YYYY-MM-DD。
        :type new_expiration_day: str
        :param operation_log_id: 任务ID
        :type operation_log_id: str
        """
        
        super().__init__()

        self._affected_backups_count = None
        self._new_expiration_day = None
        self._operation_log_id = None
        self.discriminator = None

        if affected_backups_count is not None:
            self.affected_backups_count = affected_backups_count
        if new_expiration_day is not None:
            self.new_expiration_day = new_expiration_day
        if operation_log_id is not None:
            self.operation_log_id = operation_log_id

    @property
    def affected_backups_count(self):
        r"""Gets the affected_backups_count of this UpdateExpirationTimeResponse.

        成功修改过期时间的备份数量。

        :return: The affected_backups_count of this UpdateExpirationTimeResponse.
        :rtype: int
        """
        return self._affected_backups_count

    @affected_backups_count.setter
    def affected_backups_count(self, affected_backups_count):
        r"""Sets the affected_backups_count of this UpdateExpirationTimeResponse.

        成功修改过期时间的备份数量。

        :param affected_backups_count: The affected_backups_count of this UpdateExpirationTimeResponse.
        :type affected_backups_count: int
        """
        self._affected_backups_count = affected_backups_count

    @property
    def new_expiration_day(self):
        r"""Gets the new_expiration_day of this UpdateExpirationTimeResponse.

        修改后的备份过期时间，格式：YYYY-MM-DD。

        :return: The new_expiration_day of this UpdateExpirationTimeResponse.
        :rtype: str
        """
        return self._new_expiration_day

    @new_expiration_day.setter
    def new_expiration_day(self, new_expiration_day):
        r"""Sets the new_expiration_day of this UpdateExpirationTimeResponse.

        修改后的备份过期时间，格式：YYYY-MM-DD。

        :param new_expiration_day: The new_expiration_day of this UpdateExpirationTimeResponse.
        :type new_expiration_day: str
        """
        self._new_expiration_day = new_expiration_day

    @property
    def operation_log_id(self):
        r"""Gets the operation_log_id of this UpdateExpirationTimeResponse.

        任务ID

        :return: The operation_log_id of this UpdateExpirationTimeResponse.
        :rtype: str
        """
        return self._operation_log_id

    @operation_log_id.setter
    def operation_log_id(self, operation_log_id):
        r"""Sets the operation_log_id of this UpdateExpirationTimeResponse.

        任务ID

        :param operation_log_id: The operation_log_id of this UpdateExpirationTimeResponse.
        :type operation_log_id: str
        """
        self._operation_log_id = operation_log_id

    def to_dict(self):
        import warnings
        warnings.warn("UpdateExpirationTimeResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdateExpirationTimeResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
