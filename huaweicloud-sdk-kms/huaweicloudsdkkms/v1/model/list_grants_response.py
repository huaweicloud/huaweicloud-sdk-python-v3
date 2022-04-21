# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGrantsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'grants': 'list[Grants]',
        'next_marker': 'str',
        'truncated': 'str',
        'total': 'int'
    }

    attribute_map = {
        'grants': 'grants',
        'next_marker': 'next_marker',
        'truncated': 'truncated',
        'total': 'total'
    }

    def __init__(self, grants=None, next_marker=None, truncated=None, total=None):
        """ListGrantsResponse

        The model defined in huaweicloud sdk

        :param grants: grant列表，详情请参见grants字段数据结构说明。
        :type grants: list[:class:`huaweicloudsdkkms.v1.Grants`]
        :param next_marker: 获取下一页所需要传递的marker值。 当“truncated”为“false”时，“next_marker”为空。
        :type next_marker: str
        :param truncated: 是否还有下一页：  - “true”表示还有数据。  - “false”表示已经是最后一页。
        :type truncated: str
        :param total: grant总条数。
        :type total: int
        """
        
        super(ListGrantsResponse, self).__init__()

        self._grants = None
        self._next_marker = None
        self._truncated = None
        self._total = None
        self.discriminator = None

        if grants is not None:
            self.grants = grants
        if next_marker is not None:
            self.next_marker = next_marker
        if truncated is not None:
            self.truncated = truncated
        if total is not None:
            self.total = total

    @property
    def grants(self):
        """Gets the grants of this ListGrantsResponse.

        grant列表，详情请参见grants字段数据结构说明。

        :return: The grants of this ListGrantsResponse.
        :rtype: list[:class:`huaweicloudsdkkms.v1.Grants`]
        """
        return self._grants

    @grants.setter
    def grants(self, grants):
        """Sets the grants of this ListGrantsResponse.

        grant列表，详情请参见grants字段数据结构说明。

        :param grants: The grants of this ListGrantsResponse.
        :type grants: list[:class:`huaweicloudsdkkms.v1.Grants`]
        """
        self._grants = grants

    @property
    def next_marker(self):
        """Gets the next_marker of this ListGrantsResponse.

        获取下一页所需要传递的marker值。 当“truncated”为“false”时，“next_marker”为空。

        :return: The next_marker of this ListGrantsResponse.
        :rtype: str
        """
        return self._next_marker

    @next_marker.setter
    def next_marker(self, next_marker):
        """Sets the next_marker of this ListGrantsResponse.

        获取下一页所需要传递的marker值。 当“truncated”为“false”时，“next_marker”为空。

        :param next_marker: The next_marker of this ListGrantsResponse.
        :type next_marker: str
        """
        self._next_marker = next_marker

    @property
    def truncated(self):
        """Gets the truncated of this ListGrantsResponse.

        是否还有下一页：  - “true”表示还有数据。  - “false”表示已经是最后一页。

        :return: The truncated of this ListGrantsResponse.
        :rtype: str
        """
        return self._truncated

    @truncated.setter
    def truncated(self, truncated):
        """Sets the truncated of this ListGrantsResponse.

        是否还有下一页：  - “true”表示还有数据。  - “false”表示已经是最后一页。

        :param truncated: The truncated of this ListGrantsResponse.
        :type truncated: str
        """
        self._truncated = truncated

    @property
    def total(self):
        """Gets the total of this ListGrantsResponse.

        grant总条数。

        :return: The total of this ListGrantsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListGrantsResponse.

        grant总条数。

        :param total: The total of this ListGrantsResponse.
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
        if not isinstance(other, ListGrantsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
