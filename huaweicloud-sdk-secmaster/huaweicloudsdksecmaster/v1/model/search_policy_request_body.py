# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchPolicyRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'condition': 'SearchPolicyRequestBodyCondition',
        'sort': 'list[SearchPolicyRequestBodySort]',
        'group_by': 'SearchPolicyRequestBodyGroupBy'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'condition': 'condition',
        'sort': 'sort',
        'group_by': 'group_by'
    }

    def __init__(self, limit=None, offset=None, condition=None, sort=None, group_by=None):
        r"""SearchPolicyRequestBody

        The model defined in huaweicloud sdk

        :param limit: 分页数量
        :type limit: int
        :param offset: 偏移量
        :type offset: int
        :param condition: 
        :type condition: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyCondition`
        :param sort: 排序条件
        :type sort: list[:class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodySort`]
        :param group_by: 
        :type group_by: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyGroupBy`
        """
        
        

        self._limit = None
        self._offset = None
        self._condition = None
        self._sort = None
        self._group_by = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if condition is not None:
            self.condition = condition
        if sort is not None:
            self.sort = sort
        if group_by is not None:
            self.group_by = group_by

    @property
    def limit(self):
        r"""Gets the limit of this SearchPolicyRequestBody.

        分页数量

        :return: The limit of this SearchPolicyRequestBody.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this SearchPolicyRequestBody.

        分页数量

        :param limit: The limit of this SearchPolicyRequestBody.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this SearchPolicyRequestBody.

        偏移量

        :return: The offset of this SearchPolicyRequestBody.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this SearchPolicyRequestBody.

        偏移量

        :param offset: The offset of this SearchPolicyRequestBody.
        :type offset: int
        """
        self._offset = offset

    @property
    def condition(self):
        r"""Gets the condition of this SearchPolicyRequestBody.

        :return: The condition of this SearchPolicyRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyCondition`
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        r"""Sets the condition of this SearchPolicyRequestBody.

        :param condition: The condition of this SearchPolicyRequestBody.
        :type condition: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyCondition`
        """
        self._condition = condition

    @property
    def sort(self):
        r"""Gets the sort of this SearchPolicyRequestBody.

        排序条件

        :return: The sort of this SearchPolicyRequestBody.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodySort`]
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        r"""Sets the sort of this SearchPolicyRequestBody.

        排序条件

        :param sort: The sort of this SearchPolicyRequestBody.
        :type sort: list[:class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodySort`]
        """
        self._sort = sort

    @property
    def group_by(self):
        r"""Gets the group_by of this SearchPolicyRequestBody.

        :return: The group_by of this SearchPolicyRequestBody.
        :rtype: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyGroupBy`
        """
        return self._group_by

    @group_by.setter
    def group_by(self, group_by):
        r"""Sets the group_by of this SearchPolicyRequestBody.

        :param group_by: The group_by of this SearchPolicyRequestBody.
        :type group_by: :class:`huaweicloudsdksecmaster.v1.SearchPolicyRequestBodyGroupBy`
        """
        self._group_by = group_by

    def to_dict(self):
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
        if not isinstance(other, SearchPolicyRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
