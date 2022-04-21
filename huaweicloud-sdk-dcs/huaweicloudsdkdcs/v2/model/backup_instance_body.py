# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupInstanceBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'remark': 'str',
        'backup_format': 'str'
    }

    attribute_map = {
        'remark': 'remark',
        'backup_format': 'backup_format'
    }

    def __init__(self, remark=None, backup_format=None):
        """BackupInstanceBody

        The model defined in huaweicloud sdk

        :param remark: 备份缓存实例的备注信息。
        :type remark: str
        :param backup_format: 备份缓存实例的格式。
        :type backup_format: str
        """
        
        

        self._remark = None
        self._backup_format = None
        self.discriminator = None

        if remark is not None:
            self.remark = remark
        if backup_format is not None:
            self.backup_format = backup_format

    @property
    def remark(self):
        """Gets the remark of this BackupInstanceBody.

        备份缓存实例的备注信息。

        :return: The remark of this BackupInstanceBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        """Sets the remark of this BackupInstanceBody.

        备份缓存实例的备注信息。

        :param remark: The remark of this BackupInstanceBody.
        :type remark: str
        """
        self._remark = remark

    @property
    def backup_format(self):
        """Gets the backup_format of this BackupInstanceBody.

        备份缓存实例的格式。

        :return: The backup_format of this BackupInstanceBody.
        :rtype: str
        """
        return self._backup_format

    @backup_format.setter
    def backup_format(self, backup_format):
        """Sets the backup_format of this BackupInstanceBody.

        备份缓存实例的格式。

        :param backup_format: The backup_format of this BackupInstanceBody.
        :type backup_format: str
        """
        self._backup_format = backup_format

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
        if not isinstance(other, BackupInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
