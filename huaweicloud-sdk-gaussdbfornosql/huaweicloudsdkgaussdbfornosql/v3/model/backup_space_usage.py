# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BackupSpaceUsage:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_usage': 'int'
    }

    attribute_map = {
        'backup_usage': 'backup_usage'
    }

    def __init__(self, backup_usage=None):
        r"""BackupSpaceUsage

        The model defined in huaweicloud sdk

        :param backup_usage: **参数解释：** 备份空间使用量。 **取值范围：** 不涉及。
        :type backup_usage: int
        """
        
        

        self._backup_usage = None
        self.discriminator = None

        if backup_usage is not None:
            self.backup_usage = backup_usage

    @property
    def backup_usage(self):
        r"""Gets the backup_usage of this BackupSpaceUsage.

        **参数解释：** 备份空间使用量。 **取值范围：** 不涉及。

        :return: The backup_usage of this BackupSpaceUsage.
        :rtype: int
        """
        return self._backup_usage

    @backup_usage.setter
    def backup_usage(self, backup_usage):
        r"""Sets the backup_usage of this BackupSpaceUsage.

        **参数解释：** 备份空间使用量。 **取值范围：** 不涉及。

        :param backup_usage: The backup_usage of this BackupSpaceUsage.
        :type backup_usage: int
        """
        self._backup_usage = backup_usage

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
        if not isinstance(other, BackupSpaceUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
