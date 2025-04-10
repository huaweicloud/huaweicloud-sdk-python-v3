# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateBackupOffsitePolicyInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'open_auto_backup': 'bool',
        'open_incremental_backup': 'bool',
        'destination_project_id': 'str',
        'destination_region': 'str',
        'keep_days': 'int'
    }

    attribute_map = {
        'open_auto_backup': 'open_auto_backup',
        'open_incremental_backup': 'open_incremental_backup',
        'destination_project_id': 'destination_project_id',
        'destination_region': 'destination_region',
        'keep_days': 'keep_days'
    }

    def __init__(self, open_auto_backup=None, open_incremental_backup=None, destination_project_id=None, destination_region=None, keep_days=None):
        r"""UpdateBackupOffsitePolicyInfo

        The model defined in huaweicloud sdk

        :param open_auto_backup: 是否开启跨区域全量备份。 - true：开启跨区域全量备份。 - false：关闭跨区域全量备份。
        :type open_auto_backup: bool
        :param open_incremental_backup: 是否开启跨区域增量备份。 - true：开启跨区域增量备份，当open_auto_backup开启时才可以开启。 - false：关闭跨区域增量备份。
        :type open_incremental_backup: bool
        :param destination_project_id: 设置跨区域备份策略的目标project ID。    租户在某一Region下的project ID。                              获取方法请参见[获取项目ID](https://support.huaweicloud.com/api-taurusdb/taurusdb_10_0004.html)。
        :type destination_project_id: str
        :param destination_region: 设置跨区域备份策略的目标区域。
        :type destination_region: str
        :param keep_days: 指定已生成的备份文件可以保存的天数。  取值范围：1～1825。
        :type keep_days: int
        """
        
        

        self._open_auto_backup = None
        self._open_incremental_backup = None
        self._destination_project_id = None
        self._destination_region = None
        self._keep_days = None
        self.discriminator = None

        self.open_auto_backup = open_auto_backup
        self.open_incremental_backup = open_incremental_backup
        self.destination_project_id = destination_project_id
        self.destination_region = destination_region
        self.keep_days = keep_days

    @property
    def open_auto_backup(self):
        r"""Gets the open_auto_backup of this UpdateBackupOffsitePolicyInfo.

        是否开启跨区域全量备份。 - true：开启跨区域全量备份。 - false：关闭跨区域全量备份。

        :return: The open_auto_backup of this UpdateBackupOffsitePolicyInfo.
        :rtype: bool
        """
        return self._open_auto_backup

    @open_auto_backup.setter
    def open_auto_backup(self, open_auto_backup):
        r"""Sets the open_auto_backup of this UpdateBackupOffsitePolicyInfo.

        是否开启跨区域全量备份。 - true：开启跨区域全量备份。 - false：关闭跨区域全量备份。

        :param open_auto_backup: The open_auto_backup of this UpdateBackupOffsitePolicyInfo.
        :type open_auto_backup: bool
        """
        self._open_auto_backup = open_auto_backup

    @property
    def open_incremental_backup(self):
        r"""Gets the open_incremental_backup of this UpdateBackupOffsitePolicyInfo.

        是否开启跨区域增量备份。 - true：开启跨区域增量备份，当open_auto_backup开启时才可以开启。 - false：关闭跨区域增量备份。

        :return: The open_incremental_backup of this UpdateBackupOffsitePolicyInfo.
        :rtype: bool
        """
        return self._open_incremental_backup

    @open_incremental_backup.setter
    def open_incremental_backup(self, open_incremental_backup):
        r"""Sets the open_incremental_backup of this UpdateBackupOffsitePolicyInfo.

        是否开启跨区域增量备份。 - true：开启跨区域增量备份，当open_auto_backup开启时才可以开启。 - false：关闭跨区域增量备份。

        :param open_incremental_backup: The open_incremental_backup of this UpdateBackupOffsitePolicyInfo.
        :type open_incremental_backup: bool
        """
        self._open_incremental_backup = open_incremental_backup

    @property
    def destination_project_id(self):
        r"""Gets the destination_project_id of this UpdateBackupOffsitePolicyInfo.

        设置跨区域备份策略的目标project ID。    租户在某一Region下的project ID。                              获取方法请参见[获取项目ID](https://support.huaweicloud.com/api-taurusdb/taurusdb_10_0004.html)。

        :return: The destination_project_id of this UpdateBackupOffsitePolicyInfo.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        r"""Sets the destination_project_id of this UpdateBackupOffsitePolicyInfo.

        设置跨区域备份策略的目标project ID。    租户在某一Region下的project ID。                              获取方法请参见[获取项目ID](https://support.huaweicloud.com/api-taurusdb/taurusdb_10_0004.html)。

        :param destination_project_id: The destination_project_id of this UpdateBackupOffsitePolicyInfo.
        :type destination_project_id: str
        """
        self._destination_project_id = destination_project_id

    @property
    def destination_region(self):
        r"""Gets the destination_region of this UpdateBackupOffsitePolicyInfo.

        设置跨区域备份策略的目标区域。

        :return: The destination_region of this UpdateBackupOffsitePolicyInfo.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        r"""Sets the destination_region of this UpdateBackupOffsitePolicyInfo.

        设置跨区域备份策略的目标区域。

        :param destination_region: The destination_region of this UpdateBackupOffsitePolicyInfo.
        :type destination_region: str
        """
        self._destination_region = destination_region

    @property
    def keep_days(self):
        r"""Gets the keep_days of this UpdateBackupOffsitePolicyInfo.

        指定已生成的备份文件可以保存的天数。  取值范围：1～1825。

        :return: The keep_days of this UpdateBackupOffsitePolicyInfo.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        r"""Sets the keep_days of this UpdateBackupOffsitePolicyInfo.

        指定已生成的备份文件可以保存的天数。  取值范围：1～1825。

        :param keep_days: The keep_days of this UpdateBackupOffsitePolicyInfo.
        :type keep_days: int
        """
        self._keep_days = keep_days

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
        if not isinstance(other, UpdateBackupOffsitePolicyInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
