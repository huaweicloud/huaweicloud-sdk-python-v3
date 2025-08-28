# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VulHostBackupsResponseInfoDataList:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_time': 'int',
        'backup_id': 'str',
        'backup_name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'backup_time': 'backup_time',
        'backup_id': 'backup_id',
        'backup_name': 'backup_name',
        'status': 'status'
    }

    def __init__(self, backup_time=None, backup_id=None, backup_name=None, status=None):
        r"""VulHostBackupsResponseInfoDataList

        The model defined in huaweicloud sdk

        :param backup_time: **参数解释**: 备份时间（时间戳，单位为毫秒） **取值范围**: 取值0-9223372036854775807 
        :type backup_time: int
        :param backup_id: **参数解释**: 备份id **取值范围**: 字符长度1-128位 
        :type backup_id: str
        :param backup_name: **参数解释**: 备份名称 **取值范围**: 字符长度1-64位 
        :type backup_name: str
        :param status: **参数解释**: 备份状态 **取值范围**: - available：可用 - protecting：备份中 - deleting：删除中 - restoring：恢复中 - error：错误 - waiting_protect：待备份 - waiting_delete：待删除 - waiting_restore：待恢复 
        :type status: str
        """
        
        

        self._backup_time = None
        self._backup_id = None
        self._backup_name = None
        self._status = None
        self.discriminator = None

        if backup_time is not None:
            self.backup_time = backup_time
        if backup_id is not None:
            self.backup_id = backup_id
        if backup_name is not None:
            self.backup_name = backup_name
        if status is not None:
            self.status = status

    @property
    def backup_time(self):
        r"""Gets the backup_time of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份时间（时间戳，单位为毫秒） **取值范围**: 取值0-9223372036854775807 

        :return: The backup_time of this VulHostBackupsResponseInfoDataList.
        :rtype: int
        """
        return self._backup_time

    @backup_time.setter
    def backup_time(self, backup_time):
        r"""Sets the backup_time of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份时间（时间戳，单位为毫秒） **取值范围**: 取值0-9223372036854775807 

        :param backup_time: The backup_time of this VulHostBackupsResponseInfoDataList.
        :type backup_time: int
        """
        self._backup_time = backup_time

    @property
    def backup_id(self):
        r"""Gets the backup_id of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份id **取值范围**: 字符长度1-128位 

        :return: The backup_id of this VulHostBackupsResponseInfoDataList.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份id **取值范围**: 字符长度1-128位 

        :param backup_id: The backup_id of this VulHostBackupsResponseInfoDataList.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def backup_name(self):
        r"""Gets the backup_name of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份名称 **取值范围**: 字符长度1-64位 

        :return: The backup_name of this VulHostBackupsResponseInfoDataList.
        :rtype: str
        """
        return self._backup_name

    @backup_name.setter
    def backup_name(self, backup_name):
        r"""Sets the backup_name of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份名称 **取值范围**: 字符长度1-64位 

        :param backup_name: The backup_name of this VulHostBackupsResponseInfoDataList.
        :type backup_name: str
        """
        self._backup_name = backup_name

    @property
    def status(self):
        r"""Gets the status of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份状态 **取值范围**: - available：可用 - protecting：备份中 - deleting：删除中 - restoring：恢复中 - error：错误 - waiting_protect：待备份 - waiting_delete：待删除 - waiting_restore：待恢复 

        :return: The status of this VulHostBackupsResponseInfoDataList.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this VulHostBackupsResponseInfoDataList.

        **参数解释**: 备份状态 **取值范围**: - available：可用 - protecting：备份中 - deleting：删除中 - restoring：恢复中 - error：错误 - waiting_protect：待备份 - waiting_delete：待删除 - waiting_restore：待恢复 

        :param status: The status of this VulHostBackupsResponseInfoDataList.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, VulHostBackupsResponseInfoDataList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
