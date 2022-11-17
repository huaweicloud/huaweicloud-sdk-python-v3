# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupSyncRespBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_id': 'str',
        'operation_log_id': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'operation_log_id': 'operation_log_id'
    }

    def __init__(self, backup_id=None, operation_log_id=None):
        """BackupSyncRespBody

        The model defined in huaweicloud sdk

        :param backup_id: 备份副本ID
        :type backup_id: str
        :param operation_log_id: 同步任务ID
        :type operation_log_id: str
        """
        
        

        self._backup_id = None
        self._operation_log_id = None
        self.discriminator = None

        self.backup_id = backup_id
        self.operation_log_id = operation_log_id

    @property
    def backup_id(self):
        """Gets the backup_id of this BackupSyncRespBody.

        备份副本ID

        :return: The backup_id of this BackupSyncRespBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this BackupSyncRespBody.

        备份副本ID

        :param backup_id: The backup_id of this BackupSyncRespBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def operation_log_id(self):
        """Gets the operation_log_id of this BackupSyncRespBody.

        同步任务ID

        :return: The operation_log_id of this BackupSyncRespBody.
        :rtype: str
        """
        return self._operation_log_id

    @operation_log_id.setter
    def operation_log_id(self, operation_log_id):
        """Sets the operation_log_id of this BackupSyncRespBody.

        同步任务ID

        :param operation_log_id: The operation_log_id of this BackupSyncRespBody.
        :type operation_log_id: str
        """
        self._operation_log_id = operation_log_id

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
        if not isinstance(other, BackupSyncRespBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
