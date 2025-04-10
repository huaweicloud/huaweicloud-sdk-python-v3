# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QuotaDetailSnapshotsESSD:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'in_use': 'int',
        'limit': 'int',
        'reserved': 'int'
    }

    attribute_map = {
        'in_use': 'in_use',
        'limit': 'limit',
        'reserved': 'reserved'
    }

    def __init__(self, in_use=None, limit=None, reserved=None):
        r"""QuotaDetailSnapshotsESSD

        The model defined in huaweicloud sdk

        :param in_use: 已使用的数量。
        :type in_use: int
        :param limit: 最大的数量。
        :type limit: int
        :param reserved: 预留属性。
        :type reserved: int
        """
        
        

        self._in_use = None
        self._limit = None
        self._reserved = None
        self.discriminator = None

        self.in_use = in_use
        self.limit = limit
        self.reserved = reserved

    @property
    def in_use(self):
        r"""Gets the in_use of this QuotaDetailSnapshotsESSD.

        已使用的数量。

        :return: The in_use of this QuotaDetailSnapshotsESSD.
        :rtype: int
        """
        return self._in_use

    @in_use.setter
    def in_use(self, in_use):
        r"""Sets the in_use of this QuotaDetailSnapshotsESSD.

        已使用的数量。

        :param in_use: The in_use of this QuotaDetailSnapshotsESSD.
        :type in_use: int
        """
        self._in_use = in_use

    @property
    def limit(self):
        r"""Gets the limit of this QuotaDetailSnapshotsESSD.

        最大的数量。

        :return: The limit of this QuotaDetailSnapshotsESSD.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this QuotaDetailSnapshotsESSD.

        最大的数量。

        :param limit: The limit of this QuotaDetailSnapshotsESSD.
        :type limit: int
        """
        self._limit = limit

    @property
    def reserved(self):
        r"""Gets the reserved of this QuotaDetailSnapshotsESSD.

        预留属性。

        :return: The reserved of this QuotaDetailSnapshotsESSD.
        :rtype: int
        """
        return self._reserved

    @reserved.setter
    def reserved(self, reserved):
        r"""Sets the reserved of this QuotaDetailSnapshotsESSD.

        预留属性。

        :param reserved: The reserved of this QuotaDetailSnapshotsESSD.
        :type reserved: int
        """
        self._reserved = reserved

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
        if not isinstance(other, QuotaDetailSnapshotsESSD):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
