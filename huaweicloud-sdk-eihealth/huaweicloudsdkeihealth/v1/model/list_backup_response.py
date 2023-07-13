# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'backups': 'list[BackupDto]'
    }

    attribute_map = {
        'count': 'count',
        'backups': 'backups'
    }

    def __init__(self, count=None, backups=None):
        """ListBackupResponse

        The model defined in huaweicloud sdk

        :param count: 归档记录总数量
        :type count: int
        :param backups: 归档记录列表
        :type backups: list[:class:`huaweicloudsdkeihealth.v1.BackupDto`]
        """
        
        super(ListBackupResponse, self).__init__()

        self._count = None
        self._backups = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if backups is not None:
            self.backups = backups

    @property
    def count(self):
        """Gets the count of this ListBackupResponse.

        归档记录总数量

        :return: The count of this ListBackupResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ListBackupResponse.

        归档记录总数量

        :param count: The count of this ListBackupResponse.
        :type count: int
        """
        self._count = count

    @property
    def backups(self):
        """Gets the backups of this ListBackupResponse.

        归档记录列表

        :return: The backups of this ListBackupResponse.
        :rtype: list[:class:`huaweicloudsdkeihealth.v1.BackupDto`]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this ListBackupResponse.

        归档记录列表

        :param backups: The backups of this ListBackupResponse.
        :type backups: list[:class:`huaweicloudsdkeihealth.v1.BackupDto`]
        """
        self._backups = backups

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
        if not isinstance(other, ListBackupResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
