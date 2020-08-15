# coding: utf-8

import pprint
import re

import six


from huaweicloudsdkcore.sdk_response import SdkResponse


class ListKeysResponse(SdkResponse):


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keys': 'list[str]',
        'key_details': 'list[KeyDetails]',
        'next_marker': 'str',
        'truncated': 'str',
        'total': 'int'
    }

    attribute_map = {
        'keys': 'keys',
        'key_details': 'key_details',
        'next_marker': 'next_marker',
        'truncated': 'truncated',
        'total': 'total'
    }

    def __init__(self, keys=None, key_details=None, next_marker=None, truncated=None, total=None):
        """ListKeysResponse - a model defined in huaweicloud sdk"""
        
        super().__init__()

        self._keys = None
        self._key_details = None
        self._next_marker = None
        self._truncated = None
        self._total = None
        self.discriminator = None

        if keys is not None:
            self.keys = keys
        if key_details is not None:
            self.key_details = key_details
        if next_marker is not None:
            self.next_marker = next_marker
        if truncated is not None:
            self.truncated = truncated
        if total is not None:
            self.total = total

    @property
    def keys(self):
        """Gets the keys of this ListKeysResponse.

        key_id列表。

        :return: The keys of this ListKeysResponse.
        :rtype: list[str]
        """
        return self._keys

    @keys.setter
    def keys(self, keys):
        """Sets the keys of this ListKeysResponse.

        key_id列表。

        :param keys: The keys of this ListKeysResponse.
        :type: list[str]
        """
        self._keys = keys

    @property
    def key_details(self):
        """Gets the key_details of this ListKeysResponse.

        密钥详情列表。详情参见KeyDetails

        :return: The key_details of this ListKeysResponse.
        :rtype: list[KeyDetails]
        """
        return self._key_details

    @key_details.setter
    def key_details(self, key_details):
        """Sets the key_details of this ListKeysResponse.

        密钥详情列表。详情参见KeyDetails

        :param key_details: The key_details of this ListKeysResponse.
        :type: list[KeyDetails]
        """
        self._key_details = key_details

    @property
    def next_marker(self):
        """Gets the next_marker of this ListKeysResponse.

        获取下一页所需要传递的“marker”值。当“truncated”为“false”时，“next_marker”为空。

        :return: The next_marker of this ListKeysResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListKeysResponse.

        获取下一页所需要传递的“marker”值。当“truncated”为“false”时，“next_marker”为空。

        :param next_marker: The next_marker of this ListKeysResponse.
        :type: str
        """
        self._next_marker = next_marker

    @property
    def truncated(self):
        """Gets the truncated of this ListKeysResponse.

        是否还有下一页： - “true”表示还有数据。 - “false”表示已经是最后一页。

        :return: The truncated of this ListKeysResponse.
        :rtype: str
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this ListKeysResponse.

        是否还有下一页： - “true”表示还有数据。 - “false”表示已经是最后一页。

        :param truncated: The truncated of this ListKeysResponse.
        :type: str
        """
        self._truncated = truncated

    @property
    def total(self):
        """Gets the total of this ListKeysResponse.

        密钥总条数。

        :return: The total of this ListKeysResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListKeysResponse.

        密钥总条数。

        :param total: The total of this ListKeysResponse.
        :type: int
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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListKeysResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
