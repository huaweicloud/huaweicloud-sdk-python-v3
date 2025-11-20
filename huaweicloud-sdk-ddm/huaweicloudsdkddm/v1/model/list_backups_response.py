# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBackupsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'offset': 'int',
        'limit': 'int',
        'backups': 'list[BackupInfo]'
    }

    attribute_map = {
        'total': 'total',
        'offset': 'offset',
        'limit': 'limit',
        'backups': 'backups'
    }

    def __init__(self, total=None, offset=None, limit=None, backups=None):
        r"""ListBackupsResponse

        The model defined in huaweicloud sdk

        :param total: 备份总数。
        :type total: int
        :param offset: 分页参数起始值。
        :type offset: int
        :param limit: 分页参数每页多少条。
        :type limit: int
        :param backups: 备份信息。
        :type backups: list[:class:`huaweicloudsdkddm.v1.BackupInfo`]
        """
        
        super().__init__()

        self._total = None
        self._offset = None
        self._limit = None
        self._backups = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if backups is not None:
            self.backups = backups

    @property
    def total(self):
        r"""Gets the total of this ListBackupsResponse.

        备份总数。

        :return: The total of this ListBackupsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListBackupsResponse.

        备份总数。

        :param total: The total of this ListBackupsResponse.
        :type total: int
        """
        self._total = total

    @property
    def offset(self):
        r"""Gets the offset of this ListBackupsResponse.

        分页参数起始值。

        :return: The offset of this ListBackupsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBackupsResponse.

        分页参数起始值。

        :param offset: The offset of this ListBackupsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListBackupsResponse.

        分页参数每页多少条。

        :return: The limit of this ListBackupsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBackupsResponse.

        分页参数每页多少条。

        :param limit: The limit of this ListBackupsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def backups(self):
        r"""Gets the backups of this ListBackupsResponse.

        备份信息。

        :return: The backups of this ListBackupsResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.BackupInfo`]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        r"""Sets the backups of this ListBackupsResponse.

        备份信息。

        :param backups: The backups of this ListBackupsResponse.
        :type backups: list[:class:`huaweicloudsdkddm.v1.BackupInfo`]
        """
        self._backups = backups

    def to_dict(self):
        import warnings
        warnings.warn("ListBackupsResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ListBackupsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
