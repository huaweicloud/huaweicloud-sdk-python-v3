# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBackupUsageExceededInstancesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instances': 'list[ExceededInstanceInfo]',
        'total': 'int'
    }

    attribute_map = {
        'instances': 'instances',
        'total': 'total'
    }

    def __init__(self, instances=None, total=None):
        r"""ShowBackupUsageExceededInstancesResponse

        The model defined in huaweicloud sdk

        :param instances: **参数解释**：  超阈值实例列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type instances: list[:class:`huaweicloudsdkrds.v3.ExceededInstanceInfo`]
        :param total: **参数解释**：  超阈值实例总数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._instances = None
        self._total = None
        self.discriminator = None

        if instances is not None:
            self.instances = instances
        if total is not None:
            self.total = total

    @property
    def instances(self):
        r"""Gets the instances of this ShowBackupUsageExceededInstancesResponse.

        **参数解释**：  超阈值实例列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The instances of this ShowBackupUsageExceededInstancesResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ExceededInstanceInfo`]
        """
        return self._instances

    @instances.setter
    def instances(self, instances):
        r"""Sets the instances of this ShowBackupUsageExceededInstancesResponse.

        **参数解释**：  超阈值实例列表。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param instances: The instances of this ShowBackupUsageExceededInstancesResponse.
        :type instances: list[:class:`huaweicloudsdkrds.v3.ExceededInstanceInfo`]
        """
        self._instances = instances

    @property
    def total(self):
        r"""Gets the total of this ShowBackupUsageExceededInstancesResponse.

        **参数解释**：  超阈值实例总数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The total of this ShowBackupUsageExceededInstancesResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowBackupUsageExceededInstancesResponse.

        **参数解释**：  超阈值实例总数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param total: The total of this ShowBackupUsageExceededInstancesResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ShowBackupUsageExceededInstancesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowBackupUsageExceededInstancesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
