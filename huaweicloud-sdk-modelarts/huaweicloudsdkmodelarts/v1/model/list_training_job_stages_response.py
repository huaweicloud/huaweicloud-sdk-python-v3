# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTrainingJobStagesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'running_records': 'list[StageRecord]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'running_records': 'running_records'
    }

    def __init__(self, total_count=None, running_records=None):
        r"""ListTrainingJobStagesResponse

        The model defined in huaweicloud sdk

        :param total_count: **参数解释**：总条数。 **取值范围**：不涉及。
        :type total_count: int
        :param running_records: **参数解释**：阶段记录。
        :type running_records: list[:class:`huaweicloudsdkmodelarts.v1.StageRecord`]
        """
        
        super().__init__()

        self._total_count = None
        self._running_records = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if running_records is not None:
            self.running_records = running_records

    @property
    def total_count(self):
        r"""Gets the total_count of this ListTrainingJobStagesResponse.

        **参数解释**：总条数。 **取值范围**：不涉及。

        :return: The total_count of this ListTrainingJobStagesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListTrainingJobStagesResponse.

        **参数解释**：总条数。 **取值范围**：不涉及。

        :param total_count: The total_count of this ListTrainingJobStagesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def running_records(self):
        r"""Gets the running_records of this ListTrainingJobStagesResponse.

        **参数解释**：阶段记录。

        :return: The running_records of this ListTrainingJobStagesResponse.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.StageRecord`]
        """
        return self._running_records

    @running_records.setter
    def running_records(self, running_records):
        r"""Sets the running_records of this ListTrainingJobStagesResponse.

        **参数解释**：阶段记录。

        :param running_records: The running_records of this ListTrainingJobStagesResponse.
        :type running_records: list[:class:`huaweicloudsdkmodelarts.v1.StageRecord`]
        """
        self._running_records = running_records

    def to_dict(self):
        import warnings
        warnings.warn("ListTrainingJobStagesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTrainingJobStagesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
