# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateComplianceRuleRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'local_backup_enabled': 'bool',
        'local_backup_retention': 'int',
        'local_backup_frequency': 'CreateComplianceRuleRequestBodyLocalBackupFrequency',
        'remote_backup_enabled': 'bool',
        'local_worm_enabled': 'bool',
        'remote_backup_retention': 'int',
        'remote_worm_enabled': 'bool',
        'description': 'str',
        'is_cross_account_backup_forced': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'local_backup_enabled': 'local_backup_enabled',
        'local_backup_retention': 'local_backup_retention',
        'local_backup_frequency': 'local_backup_frequency',
        'remote_backup_enabled': 'remote_backup_enabled',
        'local_worm_enabled': 'local_worm_enabled',
        'remote_backup_retention': 'remote_backup_retention',
        'remote_worm_enabled': 'remote_worm_enabled',
        'description': 'description',
        'is_cross_account_backup_forced': 'is_cross_account_backup_forced'
    }

    def __init__(self, name=None, local_backup_enabled=None, local_backup_retention=None, local_backup_frequency=None, remote_backup_enabled=None, local_worm_enabled=None, remote_backup_retention=None, remote_worm_enabled=None, description=None, is_cross_account_backup_forced=None):
        r"""CreateComplianceRuleRequestBody

        The model defined in huaweicloud sdk

        :param name: 合规规则名称
        :type name: str
        :param local_backup_enabled: 是否启用本地备份
        :type local_backup_enabled: bool
        :param local_backup_retention: 本地备份保留时长，取值范围-1-99999
        :type local_backup_retention: int
        :param local_backup_frequency: 
        :type local_backup_frequency: :class:`huaweicloudsdkbcc.v1.CreateComplianceRuleRequestBodyLocalBackupFrequency`
        :param remote_backup_enabled: 是否启用异地复制。
        :type remote_backup_enabled: bool
        :param local_worm_enabled: 本地副本是否启用WORM特性。
        :type local_worm_enabled: bool
        :param remote_backup_retention: 异地复制副本保留时长。
        :type remote_backup_retention: int
        :param remote_worm_enabled: 异地复制副本是否启用WORM特性。
        :type remote_worm_enabled: bool
        :param description: 规则描述
        :type description: str
        :param is_cross_account_backup_forced: 是否强制开启跨账号备份。
        :type is_cross_account_backup_forced: bool
        """
        
        

        self._name = None
        self._local_backup_enabled = None
        self._local_backup_retention = None
        self._local_backup_frequency = None
        self._remote_backup_enabled = None
        self._local_worm_enabled = None
        self._remote_backup_retention = None
        self._remote_worm_enabled = None
        self._description = None
        self._is_cross_account_backup_forced = None
        self.discriminator = None

        self.name = name
        self.local_backup_enabled = local_backup_enabled
        if local_backup_retention is not None:
            self.local_backup_retention = local_backup_retention
        if local_backup_frequency is not None:
            self.local_backup_frequency = local_backup_frequency
        if remote_backup_enabled is not None:
            self.remote_backup_enabled = remote_backup_enabled
        if local_worm_enabled is not None:
            self.local_worm_enabled = local_worm_enabled
        if remote_backup_retention is not None:
            self.remote_backup_retention = remote_backup_retention
        if remote_worm_enabled is not None:
            self.remote_worm_enabled = remote_worm_enabled
        if description is not None:
            self.description = description
        if is_cross_account_backup_forced is not None:
            self.is_cross_account_backup_forced = is_cross_account_backup_forced

    @property
    def name(self):
        r"""Gets the name of this CreateComplianceRuleRequestBody.

        合规规则名称

        :return: The name of this CreateComplianceRuleRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateComplianceRuleRequestBody.

        合规规则名称

        :param name: The name of this CreateComplianceRuleRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def local_backup_enabled(self):
        r"""Gets the local_backup_enabled of this CreateComplianceRuleRequestBody.

        是否启用本地备份

        :return: The local_backup_enabled of this CreateComplianceRuleRequestBody.
        :rtype: bool
        """
        return self._local_backup_enabled

    @local_backup_enabled.setter
    def local_backup_enabled(self, local_backup_enabled):
        r"""Sets the local_backup_enabled of this CreateComplianceRuleRequestBody.

        是否启用本地备份

        :param local_backup_enabled: The local_backup_enabled of this CreateComplianceRuleRequestBody.
        :type local_backup_enabled: bool
        """
        self._local_backup_enabled = local_backup_enabled

    @property
    def local_backup_retention(self):
        r"""Gets the local_backup_retention of this CreateComplianceRuleRequestBody.

        本地备份保留时长，取值范围-1-99999

        :return: The local_backup_retention of this CreateComplianceRuleRequestBody.
        :rtype: int
        """
        return self._local_backup_retention

    @local_backup_retention.setter
    def local_backup_retention(self, local_backup_retention):
        r"""Sets the local_backup_retention of this CreateComplianceRuleRequestBody.

        本地备份保留时长，取值范围-1-99999

        :param local_backup_retention: The local_backup_retention of this CreateComplianceRuleRequestBody.
        :type local_backup_retention: int
        """
        self._local_backup_retention = local_backup_retention

    @property
    def local_backup_frequency(self):
        r"""Gets the local_backup_frequency of this CreateComplianceRuleRequestBody.

        :return: The local_backup_frequency of this CreateComplianceRuleRequestBody.
        :rtype: :class:`huaweicloudsdkbcc.v1.CreateComplianceRuleRequestBodyLocalBackupFrequency`
        """
        return self._local_backup_frequency

    @local_backup_frequency.setter
    def local_backup_frequency(self, local_backup_frequency):
        r"""Sets the local_backup_frequency of this CreateComplianceRuleRequestBody.

        :param local_backup_frequency: The local_backup_frequency of this CreateComplianceRuleRequestBody.
        :type local_backup_frequency: :class:`huaweicloudsdkbcc.v1.CreateComplianceRuleRequestBodyLocalBackupFrequency`
        """
        self._local_backup_frequency = local_backup_frequency

    @property
    def remote_backup_enabled(self):
        r"""Gets the remote_backup_enabled of this CreateComplianceRuleRequestBody.

        是否启用异地复制。

        :return: The remote_backup_enabled of this CreateComplianceRuleRequestBody.
        :rtype: bool
        """
        return self._remote_backup_enabled

    @remote_backup_enabled.setter
    def remote_backup_enabled(self, remote_backup_enabled):
        r"""Sets the remote_backup_enabled of this CreateComplianceRuleRequestBody.

        是否启用异地复制。

        :param remote_backup_enabled: The remote_backup_enabled of this CreateComplianceRuleRequestBody.
        :type remote_backup_enabled: bool
        """
        self._remote_backup_enabled = remote_backup_enabled

    @property
    def local_worm_enabled(self):
        r"""Gets the local_worm_enabled of this CreateComplianceRuleRequestBody.

        本地副本是否启用WORM特性。

        :return: The local_worm_enabled of this CreateComplianceRuleRequestBody.
        :rtype: bool
        """
        return self._local_worm_enabled

    @local_worm_enabled.setter
    def local_worm_enabled(self, local_worm_enabled):
        r"""Sets the local_worm_enabled of this CreateComplianceRuleRequestBody.

        本地副本是否启用WORM特性。

        :param local_worm_enabled: The local_worm_enabled of this CreateComplianceRuleRequestBody.
        :type local_worm_enabled: bool
        """
        self._local_worm_enabled = local_worm_enabled

    @property
    def remote_backup_retention(self):
        r"""Gets the remote_backup_retention of this CreateComplianceRuleRequestBody.

        异地复制副本保留时长。

        :return: The remote_backup_retention of this CreateComplianceRuleRequestBody.
        :rtype: int
        """
        return self._remote_backup_retention

    @remote_backup_retention.setter
    def remote_backup_retention(self, remote_backup_retention):
        r"""Sets the remote_backup_retention of this CreateComplianceRuleRequestBody.

        异地复制副本保留时长。

        :param remote_backup_retention: The remote_backup_retention of this CreateComplianceRuleRequestBody.
        :type remote_backup_retention: int
        """
        self._remote_backup_retention = remote_backup_retention

    @property
    def remote_worm_enabled(self):
        r"""Gets the remote_worm_enabled of this CreateComplianceRuleRequestBody.

        异地复制副本是否启用WORM特性。

        :return: The remote_worm_enabled of this CreateComplianceRuleRequestBody.
        :rtype: bool
        """
        return self._remote_worm_enabled

    @remote_worm_enabled.setter
    def remote_worm_enabled(self, remote_worm_enabled):
        r"""Sets the remote_worm_enabled of this CreateComplianceRuleRequestBody.

        异地复制副本是否启用WORM特性。

        :param remote_worm_enabled: The remote_worm_enabled of this CreateComplianceRuleRequestBody.
        :type remote_worm_enabled: bool
        """
        self._remote_worm_enabled = remote_worm_enabled

    @property
    def description(self):
        r"""Gets the description of this CreateComplianceRuleRequestBody.

        规则描述

        :return: The description of this CreateComplianceRuleRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateComplianceRuleRequestBody.

        规则描述

        :param description: The description of this CreateComplianceRuleRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def is_cross_account_backup_forced(self):
        r"""Gets the is_cross_account_backup_forced of this CreateComplianceRuleRequestBody.

        是否强制开启跨账号备份。

        :return: The is_cross_account_backup_forced of this CreateComplianceRuleRequestBody.
        :rtype: bool
        """
        return self._is_cross_account_backup_forced

    @is_cross_account_backup_forced.setter
    def is_cross_account_backup_forced(self, is_cross_account_backup_forced):
        r"""Sets the is_cross_account_backup_forced of this CreateComplianceRuleRequestBody.

        是否强制开启跨账号备份。

        :param is_cross_account_backup_forced: The is_cross_account_backup_forced of this CreateComplianceRuleRequestBody.
        :type is_cross_account_backup_forced: bool
        """
        self._is_cross_account_backup_forced = is_cross_account_backup_forced

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
        if not isinstance(other, CreateComplianceRuleRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
