# coding: utf-8

import pprint
import re

import six





class OffSiteBackupPolicy:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keep_days': 'int',
        'backup_type': 'object',
        'destination_region': 'str',
        'destination_project_id': 'str'
    }

    attribute_map = {
        'keep_days': 'keep_days',
        'backup_type': 'backup_type',
        'destination_region': 'destination_region',
        'destination_project_id': 'destination_project_id'
    }

    def __init__(self, keep_days=None, backup_type=None, destination_region=None, destination_project_id=None):
        """OffSiteBackupPolicy - a model defined in huaweicloud sdk"""
        
        

        self._keep_days = None
        self._backup_type = None
        self._destination_region = None
        self._destination_project_id = None
        self.discriminator = None

        self.keep_days = keep_days
        if backup_type is not None:
            self.backup_type = backup_type
        if destination_region is not None:
            self.destination_region = destination_region
        if destination_project_id is not None:
            self.destination_project_id = destination_project_id

    @property
    def keep_days(self):
        """Gets the keep_days of this OffSiteBackupPolicy.

        指定已生成的备份文件可以保存的天数。  取值范围：0～732。取0值，表示关闭自动备份策略。如果需要延长保留时间请联系客服人员申请，自动备份最长可以保留2562天。  注意： 关闭备份策略后，备份任务将立即停止，所有增量备份任务将立即删除，使用增量备份的相关操作可能失败，相关操作不限于下载、复制、恢复、重建等，请谨慎操作。

        :return: The keep_days of this OffSiteBackupPolicy.
        :rtype: int
        """
        return self._keep_days

    @keep_days.setter
    def keep_days(self, keep_days):
        """Sets the keep_days of this OffSiteBackupPolicy.

        指定已生成的备份文件可以保存的天数。  取值范围：0～732。取0值，表示关闭自动备份策略。如果需要延长保留时间请联系客服人员申请，自动备份最长可以保留2562天。  注意： 关闭备份策略后，备份任务将立即停止，所有增量备份任务将立即删除，使用增量备份的相关操作可能失败，相关操作不限于下载、复制、恢复、重建等，请谨慎操作。

        :param keep_days: The keep_days of this OffSiteBackupPolicy.
        :type: int
        """
        self._keep_days = keep_days

    @property
    def backup_type(self):
        """Gets the backup_type of this OffSiteBackupPolicy.

        备份类型，取值：  - “auto”: 自动全量备份 - “incremental”: 自动增量备份 - “all”: 同时设置自动全量和自动增量备份

        :return: The backup_type of this OffSiteBackupPolicy.
        :rtype: object
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """Sets the backup_type of this OffSiteBackupPolicy.

        备份类型，取值：  - “auto”: 自动全量备份 - “incremental”: 自动增量备份 - “all”: 同时设置自动全量和自动增量备份

        :param backup_type: The backup_type of this OffSiteBackupPolicy.
        :type: object
        """
        self._backup_type = backup_type

    @property
    def destination_region(self):
        """Gets the destination_region of this OffSiteBackupPolicy.

        目标区域ID。

        :return: The destination_region of this OffSiteBackupPolicy.
        :rtype: str
        """
        return self._destination_region

    @destination_region.setter
    def destination_region(self, destination_region):
        """Sets the destination_region of this OffSiteBackupPolicy.

        目标区域ID。

        :param destination_region: The destination_region of this OffSiteBackupPolicy.
        :type: str
        """
        self._destination_region = destination_region

    @property
    def destination_project_id(self):
        """Gets the destination_project_id of this OffSiteBackupPolicy.

        项目ID。

        :return: The destination_project_id of this OffSiteBackupPolicy.
        :rtype: str
        """
        return self._destination_project_id

    @destination_project_id.setter
    def destination_project_id(self, destination_project_id):
        """Sets the destination_project_id of this OffSiteBackupPolicy.

        项目ID。

        :param destination_project_id: The destination_project_id of this OffSiteBackupPolicy.
        :type: str
        """
        self._destination_project_id = destination_project_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, OffSiteBackupPolicy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
