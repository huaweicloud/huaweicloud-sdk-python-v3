# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOnlineDdlTaskRecordsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'records': 'list[RecordItem]',
        'total_count': 'int'
    }

    attribute_map = {
        'records': 'records',
        'total_count': 'total_count'
    }

    def __init__(self, records=None, total_count=None):
        r"""ListOnlineDdlTaskRecordsResponse

        The model defined in huaweicloud sdk

        :param records: **参数解释**：  无锁变更任务详情列表。
        :type records: list[:class:`huaweicloudsdkgaussdb.v3.RecordItem`]
        :param total_count: **参数解释**：   无锁变更任务记录总数，整数。  **取值范围**：   ≥0。
        :type total_count: int
        """
        
        super().__init__()

        self._records = None
        self._total_count = None
        self.discriminator = None

        if records is not None:
            self.records = records
        if total_count is not None:
            self.total_count = total_count

    @property
    def records(self):
        r"""Gets the records of this ListOnlineDdlTaskRecordsResponse.

        **参数解释**：  无锁变更任务详情列表。

        :return: The records of this ListOnlineDdlTaskRecordsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.RecordItem`]
        """
        return self._records

    @records.setter
    def records(self, records):
        r"""Sets the records of this ListOnlineDdlTaskRecordsResponse.

        **参数解释**：  无锁变更任务详情列表。

        :param records: The records of this ListOnlineDdlTaskRecordsResponse.
        :type records: list[:class:`huaweicloudsdkgaussdb.v3.RecordItem`]
        """
        self._records = records

    @property
    def total_count(self):
        r"""Gets the total_count of this ListOnlineDdlTaskRecordsResponse.

        **参数解释**：   无锁变更任务记录总数，整数。  **取值范围**：   ≥0。

        :return: The total_count of this ListOnlineDdlTaskRecordsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListOnlineDdlTaskRecordsResponse.

        **参数解释**：   无锁变更任务记录总数，整数。  **取值范围**：   ≥0。

        :param total_count: The total_count of this ListOnlineDdlTaskRecordsResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListOnlineDdlTaskRecordsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOnlineDdlTaskRecordsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
