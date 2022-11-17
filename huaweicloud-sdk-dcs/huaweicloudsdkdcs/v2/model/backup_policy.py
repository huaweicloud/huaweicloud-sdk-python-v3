# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupPolicy:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_type': 'str',
        'save_days': 'int',
        'periodical_backup_plan': 'BackupPlan'
    }

    attribute_map = {
        'backup_type': 'backup_type',
        'save_days': 'save_days',
        'periodical_backup_plan': 'periodical_backup_plan'
    }

    def __init__(self, backup_type=None, save_days=None, periodical_backup_plan=None):
        """BackupPolicy

        The model defined in huaweicloud sdk

        :param backup_type: 备份类型。 - auto：自动备份 - manual：手动备份 
        :type backup_type: str
        :param save_days: 当backup_type设置为auto时，该参数为必填。 保留天数，单位：天，取值范围：1-7。 
        :type save_days: int
        :param periodical_backup_plan: 
        :type periodical_backup_plan: :class:`huaweicloudsdkdcs.v2.BackupPlan`
        """
        
        

        self._backup_type = None
        self._save_days = None
        self._periodical_backup_plan = None
        self.discriminator = None

        self.backup_type = backup_type
        if save_days is not None:
            self.save_days = save_days
        if periodical_backup_plan is not None:
            self.periodical_backup_plan = periodical_backup_plan

    @property
    def backup_type(self):
        """Gets the backup_type of this BackupPolicy.

        备份类型。 - auto：自动备份 - manual：手动备份 

        :return: The backup_type of this BackupPolicy.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this BackupPolicy.

        备份类型。 - auto：自动备份 - manual：手动备份 

        :param backup_type: The backup_type of this BackupPolicy.
        :type backup_type: str
        """
        self._backup_type = backup_type

    @property
    def save_days(self):
        """Gets the save_days of this BackupPolicy.

        当backup_type设置为auto时，该参数为必填。 保留天数，单位：天，取值范围：1-7。 

        :return: The save_days of this BackupPolicy.
        :rtype: int
        """
        return self._save_days

    @save_days.setter
    def save_days(self, save_days):
        """Sets the save_days of this BackupPolicy.

        当backup_type设置为auto时，该参数为必填。 保留天数，单位：天，取值范围：1-7。 

        :param save_days: The save_days of this BackupPolicy.
        :type save_days: int
        """
        self._save_days = save_days

    @property
    def periodical_backup_plan(self):
        """Gets the periodical_backup_plan of this BackupPolicy.

        :return: The periodical_backup_plan of this BackupPolicy.
        :rtype: :class:`huaweicloudsdkdcs.v2.BackupPlan`
        """
        return self._periodical_backup_plan

    @periodical_backup_plan.setter
    def periodical_backup_plan(self, periodical_backup_plan):
        """Sets the periodical_backup_plan of this BackupPolicy.

        :param periodical_backup_plan: The periodical_backup_plan of this BackupPolicy.
        :type periodical_backup_plan: :class:`huaweicloudsdkdcs.v2.BackupPlan`
        """
        self._periodical_backup_plan = periodical_backup_plan

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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
        if six.PY2:
            import sys
            reload(sys)
            sys.setdefaultencoding("utf-8")
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
