# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTaurusBackupPolicyRequest:

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
        'policies': 'list[Policy]'
    }

    attribute_map = {
        'begin_time': 'begin_time',
        'end_time': 'end_time',
        'retention_num_backup_level1': 'retention_num_backup_level1',
        'policies': 'policies'
    }

    def __init__(self, begin_time=None, end_time=None, retention_num_backup_level1=None, policies=None):
        r"""UpdateTaurusBackupPolicyRequest

        The model defined in huaweicloud sdk

        :param begin_time: **参数解释**：  备份时间段开始时间。  **约束限制**：  不涉及。  **取值范围**：  格式必须为hh:mm且有效，h为0~23的数字，m为0~59的数字，当前时间指UTC时间。  **默认取值**：  不涉及。
        :type begin_time: str
        :param end_time: **参数解释**：  备份时间段结束时间。  **约束限制**：  end_time必须大于begin_time。  **取值范围**：  格式必须为hh:mm且有效，h为0~23的数字，m为0~59的数字，当前时间指UTC时间。  **默认取值**：  不涉及。
        :type end_time: str
        :param retention_num_backup_level1: **参数解释**：  一级备份保留数量。  **约束限制**：  当一级备份开关开启时，该参数必传。反之，不能传。  **取值范围**：  - 0：不保留一级备份。 - 1：一级备份保留数量，单位为个。  **默认取值**：  0。
        :type retention_num_backup_level1: int
        :param policies: **参数解释**：  备份策略集，包含备份周期、保留天数和策略类型等配置信息，详见Policy数据结构。  **约束限制**：  不涉及。
        :type policies: list[:class:`huaweicloudsdkgaussdb.v3.Policy`]
        """
        
        

        self._begin_time = None
        self._end_time = None
        self._retention_num_backup_level1 = None
        self._policies = None
        self.discriminator = None

        self.begin_time = begin_time
        self.end_time = end_time
        if retention_num_backup_level1 is not None:
            self.retention_num_backup_level1 = retention_num_backup_level1
        self.policies = policies

    @property
    def begin_time(self):
        r"""Gets the begin_time of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  备份时间段开始时间。  **约束限制**：  不涉及。  **取值范围**：  格式必须为hh:mm且有效，h为0~23的数字，m为0~59的数字，当前时间指UTC时间。  **默认取值**：  不涉及。

        :return: The begin_time of this UpdateTaurusBackupPolicyRequest.
        :rtype: str
        """
        return self._begin_time

    @begin_time.setter
    def begin_time(self, begin_time):
        r"""Sets the begin_time of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  备份时间段开始时间。  **约束限制**：  不涉及。  **取值范围**：  格式必须为hh:mm且有效，h为0~23的数字，m为0~59的数字，当前时间指UTC时间。  **默认取值**：  不涉及。

        :param begin_time: The begin_time of this UpdateTaurusBackupPolicyRequest.
        :type begin_time: str
        """
        self._begin_time = begin_time

    @property
    def end_time(self):
        r"""Gets the end_time of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  备份时间段结束时间。  **约束限制**：  end_time必须大于begin_time。  **取值范围**：  格式必须为hh:mm且有效，h为0~23的数字，m为0~59的数字，当前时间指UTC时间。  **默认取值**：  不涉及。

        :return: The end_time of this UpdateTaurusBackupPolicyRequest.
        :rtype: str
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  备份时间段结束时间。  **约束限制**：  end_time必须大于begin_time。  **取值范围**：  格式必须为hh:mm且有效，h为0~23的数字，m为0~59的数字，当前时间指UTC时间。  **默认取值**：  不涉及。

        :param end_time: The end_time of this UpdateTaurusBackupPolicyRequest.
        :type end_time: str
        """
        self._end_time = end_time

    @property
    def retention_num_backup_level1(self):
        r"""Gets the retention_num_backup_level1 of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  一级备份保留数量。  **约束限制**：  当一级备份开关开启时，该参数必传。反之，不能传。  **取值范围**：  - 0：不保留一级备份。 - 1：一级备份保留数量，单位为个。  **默认取值**：  0。

        :return: The retention_num_backup_level1 of this UpdateTaurusBackupPolicyRequest.
        :rtype: int
        """
        return self._retention_num_backup_level1

    @retention_num_backup_level1.setter
    def retention_num_backup_level1(self, retention_num_backup_level1):
        r"""Sets the retention_num_backup_level1 of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  一级备份保留数量。  **约束限制**：  当一级备份开关开启时，该参数必传。反之，不能传。  **取值范围**：  - 0：不保留一级备份。 - 1：一级备份保留数量，单位为个。  **默认取值**：  0。

        :param retention_num_backup_level1: The retention_num_backup_level1 of this UpdateTaurusBackupPolicyRequest.
        :type retention_num_backup_level1: int
        """
        self._retention_num_backup_level1 = retention_num_backup_level1

    @property
    def policies(self):
        r"""Gets the policies of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  备份策略集，包含备份周期、保留天数和策略类型等配置信息，详见Policy数据结构。  **约束限制**：  不涉及。

        :return: The policies of this UpdateTaurusBackupPolicyRequest.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.Policy`]
        """
        return self._policies

    @policies.setter
    def policies(self, policies):
        r"""Sets the policies of this UpdateTaurusBackupPolicyRequest.

        **参数解释**：  备份策略集，包含备份周期、保留天数和策略类型等配置信息，详见Policy数据结构。  **约束限制**：  不涉及。

        :param policies: The policies of this UpdateTaurusBackupPolicyRequest.
        :type policies: list[:class:`huaweicloudsdkgaussdb.v3.Policy`]
        """
        self._policies = policies

    def to_dict(self):
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
        if not isinstance(other, UpdateTaurusBackupPolicyRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
