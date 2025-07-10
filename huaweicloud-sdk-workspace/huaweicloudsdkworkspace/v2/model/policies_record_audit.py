# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoliciesRecordAudit:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'rules': 'PoliciesRecordAuditRules',
        'storage_type': 'str',
        'obs_bucket_source': 'str',
        'obs_bucket_name': 'str',
        'retention_duration': 'int'
    }

    attribute_map = {
        'enable': 'enable',
        'rules': 'rules',
        'storage_type': 'storage_type',
        'obs_bucket_source': 'obs_bucket_source',
        'obs_bucket_name': 'obs_bucket_name',
        'retention_duration': 'retention_duration'
    }

    def __init__(self, enable=None, rules=None, storage_type=None, obs_bucket_source=None, obs_bucket_name=None, retention_duration=None):
        r"""PoliciesRecordAudit

        The model defined in huaweicloud sdk

        :param enable: 是否开启录屏审计。取值为： false：表示关闭。 true：表示开启。
        :type enable: bool
        :param rules: 
        :type rules: :class:`huaweicloudsdkworkspace.v2.PoliciesRecordAuditRules`
        :param storage_type: 存储类型。取值为： OBS：OBS桶类型。 SFTP：SFTP对接类型。
        :type storage_type: str
        :param obs_bucket_source: OBS桶来源。取值为： AUTO_CREATE：自动创建。 CREATED：已创建的。
        :type obs_bucket_source: str
        :param obs_bucket_name: obs 桶名
        :type obs_bucket_name: str
        :param retention_duration: 录屏文件保留时长（天）。取值为1~180天，0 表示永久保留。
        :type retention_duration: int
        """
        
        

        self._enable = None
        self._rules = None
        self._storage_type = None
        self._obs_bucket_source = None
        self._obs_bucket_name = None
        self._retention_duration = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if rules is not None:
            self.rules = rules
        if storage_type is not None:
            self.storage_type = storage_type
        if obs_bucket_source is not None:
            self.obs_bucket_source = obs_bucket_source
        if obs_bucket_name is not None:
            self.obs_bucket_name = obs_bucket_name
        if retention_duration is not None:
            self.retention_duration = retention_duration

    @property
    def enable(self):
        r"""Gets the enable of this PoliciesRecordAudit.

        是否开启录屏审计。取值为： false：表示关闭。 true：表示开启。

        :return: The enable of this PoliciesRecordAudit.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        r"""Sets the enable of this PoliciesRecordAudit.

        是否开启录屏审计。取值为： false：表示关闭。 true：表示开启。

        :param enable: The enable of this PoliciesRecordAudit.
        :type enable: bool
        """
        self._enable = enable

    @property
    def rules(self):
        r"""Gets the rules of this PoliciesRecordAudit.

        :return: The rules of this PoliciesRecordAudit.
        :rtype: :class:`huaweicloudsdkworkspace.v2.PoliciesRecordAuditRules`
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this PoliciesRecordAudit.

        :param rules: The rules of this PoliciesRecordAudit.
        :type rules: :class:`huaweicloudsdkworkspace.v2.PoliciesRecordAuditRules`
        """
        self._rules = rules

    @property
    def storage_type(self):
        r"""Gets the storage_type of this PoliciesRecordAudit.

        存储类型。取值为： OBS：OBS桶类型。 SFTP：SFTP对接类型。

        :return: The storage_type of this PoliciesRecordAudit.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        r"""Sets the storage_type of this PoliciesRecordAudit.

        存储类型。取值为： OBS：OBS桶类型。 SFTP：SFTP对接类型。

        :param storage_type: The storage_type of this PoliciesRecordAudit.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def obs_bucket_source(self):
        r"""Gets the obs_bucket_source of this PoliciesRecordAudit.

        OBS桶来源。取值为： AUTO_CREATE：自动创建。 CREATED：已创建的。

        :return: The obs_bucket_source of this PoliciesRecordAudit.
        :rtype: str
        """
        return self._obs_bucket_source

    @obs_bucket_source.setter
    def obs_bucket_source(self, obs_bucket_source):
        r"""Sets the obs_bucket_source of this PoliciesRecordAudit.

        OBS桶来源。取值为： AUTO_CREATE：自动创建。 CREATED：已创建的。

        :param obs_bucket_source: The obs_bucket_source of this PoliciesRecordAudit.
        :type obs_bucket_source: str
        """
        self._obs_bucket_source = obs_bucket_source

    @property
    def obs_bucket_name(self):
        r"""Gets the obs_bucket_name of this PoliciesRecordAudit.

        obs 桶名

        :return: The obs_bucket_name of this PoliciesRecordAudit.
        :rtype: str
        """
        return self._obs_bucket_name

    @obs_bucket_name.setter
    def obs_bucket_name(self, obs_bucket_name):
        r"""Sets the obs_bucket_name of this PoliciesRecordAudit.

        obs 桶名

        :param obs_bucket_name: The obs_bucket_name of this PoliciesRecordAudit.
        :type obs_bucket_name: str
        """
        self._obs_bucket_name = obs_bucket_name

    @property
    def retention_duration(self):
        r"""Gets the retention_duration of this PoliciesRecordAudit.

        录屏文件保留时长（天）。取值为1~180天，0 表示永久保留。

        :return: The retention_duration of this PoliciesRecordAudit.
        :rtype: int
        """
        return self._retention_duration

    @retention_duration.setter
    def retention_duration(self, retention_duration):
        r"""Sets the retention_duration of this PoliciesRecordAudit.

        录屏文件保留时长（天）。取值为1~180天，0 表示永久保留。

        :param retention_duration: The retention_duration of this PoliciesRecordAudit.
        :type retention_duration: int
        """
        self._retention_duration = retention_duration

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
        if not isinstance(other, PoliciesRecordAudit):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
