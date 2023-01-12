# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackups2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backup_count': 'int',
        'backup_list': 'list[ListBackupsRespBackupList]'
    }

    attribute_map = {
        'backup_count': 'backup_count',
        'backup_list': 'backup_list'
    }

    def __init__(self, backup_count=None, backup_list=None):
        """ListBackups2Response

        The model defined in huaweicloud sdk

        :param backup_count: 备份总个数。请求失败时，字段为空。
        :type backup_count: int
        :param backup_list: 当前Project ID下的所有图的备份列表。请求失败时，字段为空。
        :type backup_list: list[:class:`huaweicloudsdkges.v2.ListBackupsRespBackupList`]
        """
        
        super(ListBackups2Response, self).__init__()

        self._backup_count = None
        self._backup_list = None
        self.discriminator = None

        if backup_count is not None:
            self.backup_count = backup_count
        if backup_list is not None:
            self.backup_list = backup_list

    @property
    def backup_count(self):
        """Gets the backup_count of this ListBackups2Response.

        备份总个数。请求失败时，字段为空。

        :return: The backup_count of this ListBackups2Response.
        :rtype: int
        """
        return self._backup_count

    @backup_count.setter
    def backup_count(self, backup_count):
        """Sets the backup_count of this ListBackups2Response.

        备份总个数。请求失败时，字段为空。

        :param backup_count: The backup_count of this ListBackups2Response.
        :type backup_count: int
        """
        self._backup_count = backup_count

    @property
    def backup_list(self):
        """Gets the backup_list of this ListBackups2Response.

        当前Project ID下的所有图的备份列表。请求失败时，字段为空。

        :return: The backup_list of this ListBackups2Response.
        :rtype: list[:class:`huaweicloudsdkges.v2.ListBackupsRespBackupList`]
        """
        return self._backup_list

    @backup_list.setter
    def backup_list(self, backup_list):
        """Sets the backup_list of this ListBackups2Response.

        当前Project ID下的所有图的备份列表。请求失败时，字段为空。

        :param backup_list: The backup_list of this ListBackups2Response.
        :type backup_list: list[:class:`huaweicloudsdkges.v2.ListBackupsRespBackupList`]
        """
        self._backup_list = backup_list

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
        if not isinstance(other, ListBackups2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
