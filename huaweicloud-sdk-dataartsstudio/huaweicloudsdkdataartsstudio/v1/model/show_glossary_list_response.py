# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowGlossaryListResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'limit': 'int',
        'offset': 'int',
        'quota': 'int',
        'tags': 'list[GlossaryInfo]'
    }

    attribute_map = {
        'count': 'count',
        'limit': 'limit',
        'offset': 'offset',
        'quota': 'quota',
        'tags': 'tags'
    }

    def __init__(self, count=None, limit=None, offset=None, quota=None, tags=None):
        r"""ShowGlossaryListResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param limit: 分页参数limit
        :type limit: int
        :param offset: 分页参数offset
        :type offset: int
        :param quota: 指标配额
        :type quota: int
        :param tags: 标签信息列表
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.GlossaryInfo`]
        """
        
        super(ShowGlossaryListResponse, self).__init__()

        self._count = None
        self._limit = None
        self._offset = None
        self._quota = None
        self._tags = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if quota is not None:
            self.quota = quota
        if tags is not None:
            self.tags = tags

    @property
    def count(self):
        r"""Gets the count of this ShowGlossaryListResponse.

        总数

        :return: The count of this ShowGlossaryListResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowGlossaryListResponse.

        总数

        :param count: The count of this ShowGlossaryListResponse.
        :type count: int
        """
        self._count = count

    @property
    def limit(self):
        r"""Gets the limit of this ShowGlossaryListResponse.

        分页参数limit

        :return: The limit of this ShowGlossaryListResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowGlossaryListResponse.

        分页参数limit

        :param limit: The limit of this ShowGlossaryListResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ShowGlossaryListResponse.

        分页参数offset

        :return: The offset of this ShowGlossaryListResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ShowGlossaryListResponse.

        分页参数offset

        :param offset: The offset of this ShowGlossaryListResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def quota(self):
        r"""Gets the quota of this ShowGlossaryListResponse.

        指标配额

        :return: The quota of this ShowGlossaryListResponse.
        :rtype: int
        """
        return self._quota

    @quota.setter
    def quota(self, quota):
        r"""Sets the quota of this ShowGlossaryListResponse.

        指标配额

        :param quota: The quota of this ShowGlossaryListResponse.
        :type quota: int
        """
        self._quota = quota

    @property
    def tags(self):
        r"""Gets the tags of this ShowGlossaryListResponse.

        标签信息列表

        :return: The tags of this ShowGlossaryListResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.GlossaryInfo`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ShowGlossaryListResponse.

        标签信息列表

        :param tags: The tags of this ShowGlossaryListResponse.
        :type tags: list[:class:`huaweicloudsdkdataartsstudio.v1.GlossaryInfo`]
        """
        self._tags = tags

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
        if not isinstance(other, ShowGlossaryListResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
