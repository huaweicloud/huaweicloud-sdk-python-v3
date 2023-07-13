# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOffSiteBackupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backups': 'list[OffSiteBackupForList]',
        'total_count': 'int'
    }

    attribute_map = {
        'backups': 'backups',
        'total_count': 'total_count'
    }

    def __init__(self, backups=None, total_count=None):
        """ListOffSiteBackupsResponse

        The model defined in huaweicloud sdk

        :param backups: 跨区域备份信息。
        :type backups: list[:class:`huaweicloudsdkrds.v3.OffSiteBackupForList`]
        :param total_count: 总记录数。
        :type total_count: int
        """
        
        super(ListOffSiteBackupsResponse, self).__init__()

        self._backups = None
        self._total_count = None
        self.discriminator = None

        if backups is not None:
            self.backups = backups
        if total_count is not None:
            self.total_count = total_count

    @property
    def backups(self):
        """Gets the backups of this ListOffSiteBackupsResponse.

        跨区域备份信息。

        :return: The backups of this ListOffSiteBackupsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.OffSiteBackupForList`]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        """Sets the backups of this ListOffSiteBackupsResponse.

        跨区域备份信息。

        :param backups: The backups of this ListOffSiteBackupsResponse.
        :type backups: list[:class:`huaweicloudsdkrds.v3.OffSiteBackupForList`]
        """
        self._backups = backups

    @property
    def total_count(self):
        """Gets the total_count of this ListOffSiteBackupsResponse.

        总记录数。

        :return: The total_count of this ListOffSiteBackupsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ListOffSiteBackupsResponse.

        总记录数。

        :param total_count: The total_count of this ListOffSiteBackupsResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ListOffSiteBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
