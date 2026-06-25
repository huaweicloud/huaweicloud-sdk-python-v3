# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceBackupSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'infos': 'list[InstanceBackupSummary]',
        'total_count': 'int'
    }

    attribute_map = {
        'infos': 'infos',
        'total_count': 'total_count'
    }

    def __init__(self, infos=None, total_count=None):
        r"""ListInstanceBackupSummaryResponse

        The model defined in huaweicloud sdk

        :param infos: **参数解释**：  实例备份概览列表  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type infos: list[:class:`huaweicloudsdkrds.v3.InstanceBackupSummary`]
        :param total_count: **参数解释**：  总记录数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type total_count: int
        """
        
        super().__init__()

        self._infos = None
        self._total_count = None
        self.discriminator = None

        if infos is not None:
            self.infos = infos
        if total_count is not None:
            self.total_count = total_count

    @property
    def infos(self):
        r"""Gets the infos of this ListInstanceBackupSummaryResponse.

        **参数解释**：  实例备份概览列表  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The infos of this ListInstanceBackupSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.InstanceBackupSummary`]
        """
        return self._infos

    @infos.setter
    def infos(self, infos):
        r"""Sets the infos of this ListInstanceBackupSummaryResponse.

        **参数解释**：  实例备份概览列表  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param infos: The infos of this ListInstanceBackupSummaryResponse.
        :type infos: list[:class:`huaweicloudsdkrds.v3.InstanceBackupSummary`]
        """
        self._infos = infos

    @property
    def total_count(self):
        r"""Gets the total_count of this ListInstanceBackupSummaryResponse.

        **参数解释**：  总记录数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The total_count of this ListInstanceBackupSummaryResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListInstanceBackupSummaryResponse.

        **参数解释**：  总记录数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param total_count: The total_count of this ListInstanceBackupSummaryResponse.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
        import warnings
        warnings.warn("ListInstanceBackupSummaryResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListInstanceBackupSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
