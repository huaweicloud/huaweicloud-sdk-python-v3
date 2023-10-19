# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTagsResponse(SdkResponse):

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
        'count': 'int',
        'quota': 'int',
        'tags': 'list[OpenTag]',
        'total': 'int'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'count': 'count',
        'quota': 'quota',
        'tags': 'tags',
        'total': 'total'
    }

    def __init__(self, limit=None, offset=None, count=None, quota=None, tags=None, total=None):
        """ShowTagsResponse

        The model defined in huaweicloud sdk

        :param limit: 每页大小
        :type limit: int
        :param offset: 页码
        :type offset: int
        :param count: 查询出来的条数
        :type count: int
        :param quota: 可创建标签数量配额额
        :type quota: int
        :param tags: 标签实体
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenTag`]
        :param total: 已创建的标签总条数
        :type total: int
        """
        
        super(ShowTagsResponse, self).__init__()

        self._limit = None
        self._offset = None
        self._count = None
        self._quota = None
        self._tags = None
        self._total = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if count is not None:
            self.count = count
        if quota is not None:
            self.quota = quota
        if tags is not None:
            self.tags = tags
        if total is not None:
            self.total = total

    @property
    def limit(self):
        """Gets the limit of this ShowTagsResponse.

        每页大小

        :return: The limit of this ShowTagsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ShowTagsResponse.

        每页大小

        :param limit: The limit of this ShowTagsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ShowTagsResponse.

        页码

        :return: The offset of this ShowTagsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ShowTagsResponse.

        页码

        :param offset: The offset of this ShowTagsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def count(self):
        """Gets the count of this ShowTagsResponse.

        查询出来的条数

        :return: The count of this ShowTagsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowTagsResponse.

        查询出来的条数

        :param count: The count of this ShowTagsResponse.
        :type count: int
        """
        self._count = count

    @property
    def quota(self):
        """Gets the quota of this ShowTagsResponse.

        可创建标签数量配额额

        :return: The quota of this ShowTagsResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        """Sets the quota of this ShowTagsResponse.

        可创建标签数量配额额

        :param quota: The quota of this ShowTagsResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def tags(self):
        """Gets the tags of this ShowTagsResponse.

        标签实体

        :return: The tags of this ShowTagsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this ShowTagsResponse.

        标签实体

        :param tags: The tags of this ShowTagsResponse.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.OpenTag`]
        """
        self._tags = tags

    @property
    def total(self):
        """Gets the total of this ShowTagsResponse.

        已创建的标签总条数

        :return: The total of this ShowTagsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ShowTagsResponse.

        已创建的标签总条数

        :param total: The total of this ShowTagsResponse.
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
        if not isinstance(other, ShowTagsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
