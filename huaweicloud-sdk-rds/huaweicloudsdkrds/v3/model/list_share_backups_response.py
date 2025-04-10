# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareBackupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backups': 'list[ShareBackups]',
        'total': 'int'
    }

    attribute_map = {
        'backups': 'backups',
        'total': 'total'
    }

    def __init__(self, backups=None, total=None):
        r"""ListShareBackupsResponse

        The model defined in huaweicloud sdk

        :param backups: 共享备份列表。
        :type backups: list[:class:`huaweicloudsdkrds.v3.ShareBackups`]
        :param total: 总记录数。
        :type total: int
        """
        
        super(ListShareBackupsResponse, self).__init__()

        self._backups = None
        self._total = None
        self.discriminator = None

        if backups is not None:
            self.backups = backups
        if total is not None:
            self.total = total

    @property
    def backups(self):
        r"""Gets the backups of this ListShareBackupsResponse.

        共享备份列表。

        :return: The backups of this ListShareBackupsResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.ShareBackups`]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        r"""Sets the backups of this ListShareBackupsResponse.

        共享备份列表。

        :param backups: The backups of this ListShareBackupsResponse.
        :type backups: list[:class:`huaweicloudsdkrds.v3.ShareBackups`]
        """
        self._backups = backups

    @property
    def total(self):
        r"""Gets the total of this ListShareBackupsResponse.

        总记录数。

        :return: The total of this ListShareBackupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListShareBackupsResponse.

        总记录数。

        :param total: The total of this ListShareBackupsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ListShareBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
