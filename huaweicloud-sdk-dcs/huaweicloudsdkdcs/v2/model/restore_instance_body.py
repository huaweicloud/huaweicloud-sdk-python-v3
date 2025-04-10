# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestoreInstanceBody:

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
        'remark': 'str'
    }

    attribute_map = {
        'backup_id': 'backup_id',
        'remark': 'remark'
    }

    def __init__(self, backup_id=None, remark=None):
        r"""RestoreInstanceBody

        The model defined in huaweicloud sdk

        :param backup_id: 备份记录ID。
        :type backup_id: str
        :param remark: 恢复缓存实例的备注信息。
        :type remark: str
        """
        
        

        self._backup_id = None
        self._remark = None
        self.discriminator = None

        self.backup_id = backup_id
        if remark is not None:
            self.remark = remark

    @property
    def backup_id(self):
        r"""Gets the backup_id of this RestoreInstanceBody.

        备份记录ID。

        :return: The backup_id of this RestoreInstanceBody.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        r"""Sets the backup_id of this RestoreInstanceBody.

        备份记录ID。

        :param backup_id: The backup_id of this RestoreInstanceBody.
        :type backup_id: str
        """
        self._backup_id = backup_id

    @property
    def remark(self):
        r"""Gets the remark of this RestoreInstanceBody.

        恢复缓存实例的备注信息。

        :return: The remark of this RestoreInstanceBody.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this RestoreInstanceBody.

        恢复缓存实例的备注信息。

        :param remark: The remark of this RestoreInstanceBody.
        :type remark: str
        """
        self._remark = remark

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
        if not isinstance(other, RestoreInstanceBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
