# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchDeleteBackupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_ids': 'list[str]'
    }

    attribute_map = {
        'backup_ids': 'backup_ids'
    }

    def __init__(self, backup_ids=None):
        r"""BatchDeleteBackupRequestBody

        The model defined in huaweicloud sdk

        :param backup_ids: 需要删除的手动备份ID列表。列表大小范围：[1-50]
        :type backup_ids: list[str]
        """
        
        

        self._backup_ids = None
        self.discriminator = None

        self.backup_ids = backup_ids

    @property
    def backup_ids(self):
        r"""Gets the backup_ids of this BatchDeleteBackupRequestBody.

        需要删除的手动备份ID列表。列表大小范围：[1-50]

        :return: The backup_ids of this BatchDeleteBackupRequestBody.
        :rtype: list[str]
        """
        return self._backup_ids

    @backup_ids.setter
    def backup_ids(self, backup_ids):
        r"""Sets the backup_ids of this BatchDeleteBackupRequestBody.

        需要删除的手动备份ID列表。列表大小范围：[1-50]

        :param backup_ids: The backup_ids of this BatchDeleteBackupRequestBody.
        :type backup_ids: list[str]
        """
        self._backup_ids = backup_ids

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
        if not isinstance(other, BatchDeleteBackupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
