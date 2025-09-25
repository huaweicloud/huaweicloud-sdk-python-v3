# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlLimitTaskResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit_task_list': 'list[ListSqlLimitTaskResponseResult]',
        'limit': 'int',
        'offset': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'limit_task_list': 'limit_task_list',
        'limit': 'limit',
        'offset': 'offset',
        'total_count': 'total_count'
    }

    def __init__(self, limit_task_list=None, limit=None, offset=None, total_count=None):
        r"""ListSqlLimitTaskResponse

        The model defined in huaweicloud sdk

        :param limit_task_list: **参数解释**: 限流任务列表。
        :type limit_task_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListSqlLimitTaskResponseResult`]
        :param limit: **参数解释**: 查询记录数。 **取值范围**: 不涉及。
        :type limit: int
        :param offset: **参数解释**: 索引位置。 **取值范围**: 不涉及。
        :type offset: int
        :param total_count: **参数解释**: 总数。 **取值范围**: 不涉及。
        :type total_count: int
        """
        
        super(ListSqlLimitTaskResponse, self).__init__()

        self._limit_task_list = None
        self._limit = None
        self._offset = None
        self._total_count = None
        self.discriminator = None

        if limit_task_list is not None:
            self.limit_task_list = limit_task_list
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if total_count is not None:
            self.total_count = total_count

    @property
    def limit_task_list(self):
        r"""Gets the limit_task_list of this ListSqlLimitTaskResponse.

        **参数解释**: 限流任务列表。

        :return: The limit_task_list of this ListSqlLimitTaskResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListSqlLimitTaskResponseResult`]
        """
        return self._limit_task_list

    @limit_task_list.setter
    def limit_task_list(self, limit_task_list):
        r"""Sets the limit_task_list of this ListSqlLimitTaskResponse.

        **参数解释**: 限流任务列表。

        :param limit_task_list: The limit_task_list of this ListSqlLimitTaskResponse.
        :type limit_task_list: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.ListSqlLimitTaskResponseResult`]
        """
        self._limit_task_list = limit_task_list

    @property
    def limit(self):
        r"""Gets the limit of this ListSqlLimitTaskResponse.

        **参数解释**: 查询记录数。 **取值范围**: 不涉及。

        :return: The limit of this ListSqlLimitTaskResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSqlLimitTaskResponse.

        **参数解释**: 查询记录数。 **取值范围**: 不涉及。

        :param limit: The limit of this ListSqlLimitTaskResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListSqlLimitTaskResponse.

        **参数解释**: 索引位置。 **取值范围**: 不涉及。

        :return: The offset of this ListSqlLimitTaskResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSqlLimitTaskResponse.

        **参数解释**: 索引位置。 **取值范围**: 不涉及。

        :param offset: The offset of this ListSqlLimitTaskResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def total_count(self):
        r"""Gets the total_count of this ListSqlLimitTaskResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。

        :return: The total_count of this ListSqlLimitTaskResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListSqlLimitTaskResponse.

        **参数解释**: 总数。 **取值范围**: 不涉及。

        :param total_count: The total_count of this ListSqlLimitTaskResponse.
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
        if not isinstance(other, ListSqlLimitTaskResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
