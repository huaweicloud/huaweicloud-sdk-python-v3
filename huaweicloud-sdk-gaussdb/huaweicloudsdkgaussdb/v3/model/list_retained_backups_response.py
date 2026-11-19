# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRetainedBackupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'recycle_backup_infos': 'list[RetainedBackupInfo]',
        'policy': 'RetainedBackupPolicy',
        'total': 'int'
    }

    attribute_map = {
        'recycle_backup_infos': 'recycle_backup_infos',
        'policy': 'policy',
        'total': 'total'
    }

    def __init__(self, recycle_backup_infos=None, policy=None, total=None):
        r"""ListRetainedBackupsResponse

        The model defined in huaweicloud sdk

        :param recycle_backup_infos: **参数解释**：  保留备份信息列表。
        :type recycle_backup_infos: list[:class:`huaweicloudsdkgaussdb.v3.RetainedBackupInfo`]
        :param policy: 
        :type policy: :class:`huaweicloudsdkgaussdb.v3.RetainedBackupPolicy`
        :param total: **参数解释**：  保留备份总数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type total: int
        """
        
        super().__init__()

        self._recycle_backup_infos = None
        self._policy = None
        self._total = None
        self.discriminator = None

        if recycle_backup_infos is not None:
            self.recycle_backup_infos = recycle_backup_infos
        if policy is not None:
            self.policy = policy
        if total is not None:
            self.total = total

    @property
    def recycle_backup_infos(self):
        r"""Gets the recycle_backup_infos of this ListRetainedBackupsResponse.

        **参数解释**：  保留备份信息列表。

        :return: The recycle_backup_infos of this ListRetainedBackupsResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.RetainedBackupInfo`]
        """
        return self._recycle_backup_infos

    @recycle_backup_infos.setter
    def recycle_backup_infos(self, recycle_backup_infos):
        r"""Sets the recycle_backup_infos of this ListRetainedBackupsResponse.

        **参数解释**：  保留备份信息列表。

        :param recycle_backup_infos: The recycle_backup_infos of this ListRetainedBackupsResponse.
        :type recycle_backup_infos: list[:class:`huaweicloudsdkgaussdb.v3.RetainedBackupInfo`]
        """
        self._recycle_backup_infos = recycle_backup_infos

    @property
    def policy(self):
        r"""Gets the policy of this ListRetainedBackupsResponse.

        :return: The policy of this ListRetainedBackupsResponse.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.RetainedBackupPolicy`
        """
        return self._policy

    @policy.setter
    def policy(self, policy):
        r"""Sets the policy of this ListRetainedBackupsResponse.

        :param policy: The policy of this ListRetainedBackupsResponse.
        :type policy: :class:`huaweicloudsdkgaussdb.v3.RetainedBackupPolicy`
        """
        self._policy = policy

    @property
    def total(self):
        r"""Gets the total of this ListRetainedBackupsResponse.

        **参数解释**：  保留备份总数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The total of this ListRetainedBackupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListRetainedBackupsResponse.

        **参数解释**：  保留备份总数。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param total: The total of this ListRetainedBackupsResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListRetainedBackupsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRetainedBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
