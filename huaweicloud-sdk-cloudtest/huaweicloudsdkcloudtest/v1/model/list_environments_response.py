# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnvironmentsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'environments': 'list[Environment]',
        'offset': 'int',
        'limit': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'environments': 'environments',
        'offset': 'offset',
        'limit': 'limit',
        'total_count': 'total_count'
    }

    def __init__(self, environments=None, offset=None, limit=None, total_count=None):
        r"""ListEnvironmentsResponse

        The model defined in huaweicloud sdk

        :param environments: 环境分组列表
        :type environments: list[:class:`huaweicloudsdkcloudtest.v1.Environment`]
        :param offset: 偏移量，表示从此偏移量开始查询，offset大于等于0
        :type offset: int
        :param limit: 每页显示的条目数量,最大支持200条
        :type limit: int
        :param total_count: 环境分组总条数
        :type total_count: int
        """
        
        super(ListEnvironmentsResponse, self).__init__()

        self._environments = None
        self._offset = None
        self._limit = None
        self._total_count = None
        self.discriminator = None

        if environments is not None:
            self.environments = environments
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total_count is not None:
            self.total_count = total_count

    @property
    def environments(self):
        r"""Gets the environments of this ListEnvironmentsResponse.

        环境分组列表

        :return: The environments of this ListEnvironmentsResponse.
        :rtype: list[:class:`huaweicloudsdkcloudtest.v1.Environment`]
        """
        return self._environments

    @environments.setter
    def environments(self, environments):
        r"""Sets the environments of this ListEnvironmentsResponse.

        环境分组列表

        :param environments: The environments of this ListEnvironmentsResponse.
        :type environments: list[:class:`huaweicloudsdkcloudtest.v1.Environment`]
        """
        self._environments = environments

    @property
    def offset(self):
        r"""Gets the offset of this ListEnvironmentsResponse.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :return: The offset of this ListEnvironmentsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEnvironmentsResponse.

        偏移量，表示从此偏移量开始查询，offset大于等于0

        :param offset: The offset of this ListEnvironmentsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEnvironmentsResponse.

        每页显示的条目数量,最大支持200条

        :return: The limit of this ListEnvironmentsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnvironmentsResponse.

        每页显示的条目数量,最大支持200条

        :param limit: The limit of this ListEnvironmentsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total_count(self):
        r"""Gets the total_count of this ListEnvironmentsResponse.

        环境分组总条数

        :return: The total_count of this ListEnvironmentsResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListEnvironmentsResponse.

        环境分组总条数

        :param total_count: The total_count of this ListEnvironmentsResponse.
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
        if not isinstance(other, ListEnvironmentsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
