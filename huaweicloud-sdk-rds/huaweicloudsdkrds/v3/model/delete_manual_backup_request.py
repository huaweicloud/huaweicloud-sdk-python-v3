# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteManualBackupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'backup_id': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'backup_id': 'backup_id'
    }

    def __init__(self, x_language=None, backup_id=None):
        """DeleteManualBackupRequest

        The model defined in huaweicloud sdk

        :param x_language: 语言
        :type x_language: str
        :param backup_id: 备份ID。
        :type backup_id: str
        """
        
        

        self._x_language = None
        self._backup_id = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.backup_id = backup_id

    @property
    def x_language(self):
        """Gets the x_language of this DeleteManualBackupRequest.

        语言

        :return: The x_language of this DeleteManualBackupRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this DeleteManualBackupRequest.

        语言

        :param x_language: The x_language of this DeleteManualBackupRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def backup_id(self):
        """Gets the backup_id of this DeleteManualBackupRequest.

        备份ID。

        :return: The backup_id of this DeleteManualBackupRequest.
        :rtype: str
        """
        return self._backup_id

    @backup_id.setter
    def backup_id(self, backup_id):
        """Sets the backup_id of this DeleteManualBackupRequest.

        备份ID。

        :param backup_id: The backup_id of this DeleteManualBackupRequest.
        :type backup_id: str
        """
        self._backup_id = backup_id

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
        if not isinstance(other, DeleteManualBackupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
