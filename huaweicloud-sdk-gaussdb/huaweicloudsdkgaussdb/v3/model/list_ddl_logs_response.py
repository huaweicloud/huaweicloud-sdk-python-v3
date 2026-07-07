# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDdlLogsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ddl_logs': 'list[DdlLogInfo]',
        'total_count': 'int',
        'keep_days': 'int',
        'switch_status': 'str'
    }

    attribute_map = {
        'ddl_logs': 'ddl_logs',
        'total_count': 'total_count',
        'keep_days': 'keep_days',
        'switch_status': 'switch_status'
    }

    def __init__(self, ddl_logs=None, total_count=None, keep_days=None, switch_status=None):
        r"""ListDdlLogsResponse

        The model defined in huaweicloud sdk

        :param ddl_logs: **参数解释**：  DDL下载日志列表。  **取值范围**：  不涉及。 
        :type ddl_logs: list[:class:`huaweicloudsdkgaussdb.v3.DdlLogInfo`]
        :param total_count: **参数解释**：  总条数。  **取值范围**：  不涉及。 
        :type total_count: int
        :param keep_days: **参数解释**：  日志保留天数。  **取值范围**：  不涉及。 
        :type keep_days: int
        :param switch_status: **参数解释**：  DDL日志下载开关状态。  **取值范围**：  - ON，开启。 - OFF，关闭。 
        :type switch_status: str
        """
        
        super().__init__()

        self._ddl_logs = None
        self._total_count = None
        self._keep_days = None
        self._switch_status = None
        self.discriminator = None

        if ddl_logs is not None:
            self.ddl_logs = ddl_logs
        if total_count is not None:
            self.total_count = total_count
        if keep_days is not None:
            self.keep_days = keep_days
        if switch_status is not None:
            self.switch_status = switch_status

    @property
    def ddl_logs(self):
        r"""Gets the ddl_logs of this ListDdlLogsResponse.

        **参数解释**：  DDL下载日志列表。  **取值范围**：  不涉及。 

        :return: The ddl_logs of this ListDdlLogsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.DdlLogInfo`]
        """
        return self._ddl_logs

    @ddl_logs.setter
    def ddl_logs(self, ddl_logs):
        r"""Sets the ddl_logs of this ListDdlLogsResponse.

        **参数解释**：  DDL下载日志列表。  **取值范围**：  不涉及。 

        :param ddl_logs: The ddl_logs of this ListDdlLogsResponse.
        :type ddl_logs: list[:class:`huaweicloudsdkgaussdb.v3.DdlLogInfo`]
        """
        self._ddl_logs = ddl_logs

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDdlLogsResponse.

        **参数解释**：  总条数。  **取值范围**：  不涉及。 

        :return: The total_count of this ListDdlLogsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDdlLogsResponse.

        **参数解释**：  总条数。  **取值范围**：  不涉及。 

        :param total_count: The total_count of this ListDdlLogsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def keep_days(self):
        r"""Gets the keep_days of this ListDdlLogsResponse.

        **参数解释**：  日志保留天数。  **取值范围**：  不涉及。 

        :return: The keep_days of this ListDdlLogsResponse.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this ListDdlLogsResponse.

        **参数解释**：  日志保留天数。  **取值范围**：  不涉及。 

        :param keep_days: The keep_days of this ListDdlLogsResponse.
        :type keep_days: int
        """
        self._keep_days = keep_days

    @property
    def switch_status(self):
        r"""Gets the switch_status of this ListDdlLogsResponse.

        **参数解释**：  DDL日志下载开关状态。  **取值范围**：  - ON，开启。 - OFF，关闭。 

        :return: The switch_status of this ListDdlLogsResponse.
        :rtype: str
        """
        return self._switch_status

    @switch_status.setter
    def switch_status(self, switch_status):
        r"""Sets the switch_status of this ListDdlLogsResponse.

        **参数解释**：  DDL日志下载开关状态。  **取值范围**：  - ON，开启。 - OFF，关闭。 

        :param switch_status: The switch_status of this ListDdlLogsResponse.
        :type switch_status: str
        """
        self._switch_status = switch_status

    def to_dict(self):
        import warnings
        warnings.warn("ListDdlLogsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListDdlLogsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
