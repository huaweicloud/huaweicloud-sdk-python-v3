# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaurusDbAdvancedBackupPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'begin_time': 'str',
        'end_time': 'str',
        'retention_num_backup_level1': 'int',
        'policies': 'list[BackupPolicyInfo]'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'retention_num_backup_level1': 'retention_num_backup_level1',
        'policies': 'policies'
    }

    def __init__(self, begin_time=None, end_time=None, retention_num_backup_level1=None, policies=None):
        r"""ShowTaurusDbAdvancedBackupPolicyResponse

        The model defined in huaweicloud sdk

        :param begin_time: **参数解释**：  备份时间段开始时间。  **取值范围**：  非空，格式必须为hh:mm且有效，当前时间指UTC时间。
        :type begin_time: str
        :param end_time: **参数解释**：  备份时间段结束时间。  **取值范围**：  非空，格式必须为hh:mm且有效，当前时间指UTC时间。end_time必须大于begin_time。
        :type end_time: str
        :param retention_num_backup_level1: **参数解释**：  一级备份保留数量。当一级备份开关开启时，返回此参数。  **取值范围**：  不涉及。
        :type retention_num_backup_level1: int
        :param policies: **参数解释**：  备份策略集。
        :type policies: list[:class:`huaweicloudsdkgaussdb.v3.BackupPolicyInfo`]
        """
        
        super().__init__()

        self._begin_time = None
        self._end_time = None
        self._retention_num_backup_level1 = None
        self._policies = None
        self.discriminator = None

        if begin_time is not None:
            self.begin_time = begin_time
        if end_time is not None:
            self.end_time = end_time
        if retention_num_backup_level1 is not None:
            self.retention_num_backup_level1 = retention_num_backup_level1
        if policies is not None:
            self.policies = policies

    @property
    def begin_time(self):
        r"""Gets the begin_time of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  备份时间段开始时间。  **取值范围**：  非空，格式必须为hh:mm且有效，当前时间指UTC时间。

        :return: The begin_time of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  备份时间段开始时间。  **取值范围**：  非空，格式必须为hh:mm且有效，当前时间指UTC时间。

        :param begin_time: The begin_time of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  备份时间段结束时间。  **取值范围**：  非空，格式必须为hh:mm且有效，当前时间指UTC时间。end_time必须大于begin_time。

        :return: The end_time of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  备份时间段结束时间。  **取值范围**：  非空，格式必须为hh:mm且有效，当前时间指UTC时间。end_time必须大于begin_time。

        :param end_time: The end_time of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def retention_num_backup_level1(self):
        r"""Gets the retention_num_backup_level1 of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  一级备份保留数量。当一级备份开关开启时，返回此参数。  **取值范围**：  不涉及。

        :return: The retention_num_backup_level1 of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :rtype: int
        """
        return self._retention_num_backup_level1

    @retention_num_backup_level1.setter
    def retention_num_backup_level1(self, retention_num_backup_level1):
        r"""Sets the retention_num_backup_level1 of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  一级备份保留数量。当一级备份开关开启时，返回此参数。  **取值范围**：  不涉及。

        :param retention_num_backup_level1: The retention_num_backup_level1 of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :type retention_num_backup_level1: int
        """
        self._retention_num_backup_level1 = retention_num_backup_level1

    @property
    def policies(self):
        r"""Gets the policies of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  备份策略集。

        :return: The policies of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.BackupPolicyInfo`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this ShowTaurusDbAdvancedBackupPolicyResponse.

        **参数解释**：  备份策略集。

        :param policies: The policies of this ShowTaurusDbAdvancedBackupPolicyResponse.
        :type policies: list[:class:`huaweicloudsdkgaussdb.v3.BackupPolicyInfo`]
        """
        self._policies = policies

    def to_dict(self):
        import warnings
        warnings.warn("ShowTaurusDbAdvancedBackupPolicyResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTaurusDbAdvancedBackupPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
