# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListControlsForAccountRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'managed_account_id': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'managed_account_id': 'managed_account_id',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, managed_account_id=None, limit=None, marker=None):
        r"""ListControlsForAccountRequest

        The model defined in huaweicloud sdk

        :param managed_account_id: 纳管账号ID。
        :type managed_account_id: str
        :param limit: 分页页面的最大值。
        :type limit: int
        :param marker: 页面标记。
        :type marker: str
        """
        
        

        self._managed_account_id = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.managed_account_id = managed_account_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def managed_account_id(self):
        r"""Gets the managed_account_id of this ListControlsForAccountRequest.

        纳管账号ID。

        :return: The managed_account_id of this ListControlsForAccountRequest.
        :rtype: str
        """
        return self._managed_account_id

    @managed_account_id.setter
    def managed_account_id(self, managed_account_id):
        r"""Sets the managed_account_id of this ListControlsForAccountRequest.

        纳管账号ID。

        :param managed_account_id: The managed_account_id of this ListControlsForAccountRequest.
        :type managed_account_id: str
        """
        self._managed_account_id = managed_account_id

    @property
    def limit(self):
        r"""Gets the limit of this ListControlsForAccountRequest.

        分页页面的最大值。

        :return: The limit of this ListControlsForAccountRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListControlsForAccountRequest.

        分页页面的最大值。

        :param limit: The limit of this ListControlsForAccountRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListControlsForAccountRequest.

        页面标记。

        :return: The marker of this ListControlsForAccountRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListControlsForAccountRequest.

        页面标记。

        :param marker: The marker of this ListControlsForAccountRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListControlsForAccountRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
