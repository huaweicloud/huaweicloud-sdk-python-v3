# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAutoIncrementUsageResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'status': 'str',
        'total': 'int',
        'auto_increment_usage_list': 'list[AutoIncrementUsageRespAutoIncrementUsageList]'
    }

    attribute_map = {
        'status': 'status',
        'total': 'total',
        'auto_increment_usage_list': 'auto_increment_usage_list'
    }

    def __init__(self, status=None, total=None, auto_increment_usage_list=None):
        r"""ListAutoIncrementUsageResponse

        The model defined in huaweicloud sdk

        :param status: 任务执行状态。 取值：  值为“Running”，表示任务正在执行。  值为“Completed”，表示任务执行成功。  值为“Failed”，表示任务执行失败。
        :type status: str
        :param total: 数量
        :type total: int
        :param auto_increment_usage_list: 自增 ID 使用数据列表。
        :type auto_increment_usage_list: list[:class:`huaweicloudsdkdas.v3.AutoIncrementUsageRespAutoIncrementUsageList`]
        """
        
        super().__init__()

        self._status = None
        self._total = None
        self._auto_increment_usage_list = None
        self.discriminator = None

        if status is not None:
            self.status = status
        if total is not None:
            self.total = total
        if auto_increment_usage_list is not None:
            self.auto_increment_usage_list = auto_increment_usage_list

    @property
    def status(self):
        r"""Gets the status of this ListAutoIncrementUsageResponse.

        任务执行状态。 取值：  值为“Running”，表示任务正在执行。  值为“Completed”，表示任务执行成功。  值为“Failed”，表示任务执行失败。

        :return: The status of this ListAutoIncrementUsageResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListAutoIncrementUsageResponse.

        任务执行状态。 取值：  值为“Running”，表示任务正在执行。  值为“Completed”，表示任务执行成功。  值为“Failed”，表示任务执行失败。

        :param status: The status of this ListAutoIncrementUsageResponse.
        :type status: str
        """
        self._status = status

    @property
    def total(self):
        r"""Gets the total of this ListAutoIncrementUsageResponse.

        数量

        :return: The total of this ListAutoIncrementUsageResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAutoIncrementUsageResponse.

        数量

        :param total: The total of this ListAutoIncrementUsageResponse.
        :type total: int
        """
        self._total = total

    @property
    def auto_increment_usage_list(self):
        r"""Gets the auto_increment_usage_list of this ListAutoIncrementUsageResponse.

        自增 ID 使用数据列表。

        :return: The auto_increment_usage_list of this ListAutoIncrementUsageResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.AutoIncrementUsageRespAutoIncrementUsageList`]
        """
        return self._auto_increment_usage_list

    @auto_increment_usage_list.setter
    def auto_increment_usage_list(self, auto_increment_usage_list):
        r"""Sets the auto_increment_usage_list of this ListAutoIncrementUsageResponse.

        自增 ID 使用数据列表。

        :param auto_increment_usage_list: The auto_increment_usage_list of this ListAutoIncrementUsageResponse.
        :type auto_increment_usage_list: list[:class:`huaweicloudsdkdas.v3.AutoIncrementUsageRespAutoIncrementUsageList`]
        """
        self._auto_increment_usage_list = auto_increment_usage_list

    def to_dict(self):
        import warnings
        warnings.warn("ListAutoIncrementUsageResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListAutoIncrementUsageResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
