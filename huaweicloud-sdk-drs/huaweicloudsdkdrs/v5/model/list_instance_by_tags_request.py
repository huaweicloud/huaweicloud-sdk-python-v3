# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceByTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_type': 'str',
        'x_language': 'str',
        'limit': 'int',
        'offset': 'int',
        'body': 'QueryInstanceByTagReq'
    }

    attribute_map = {
        'resource_type': 'resource_type',
        'x_language': 'X-Language',
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, resource_type=None, x_language=None, limit=None, offset=None, body=None):
        r"""ListInstanceByTagsRequest

        The model defined in huaweicloud sdk

        :param resource_type: 资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：录制回放
        :type resource_type: str
        :param x_language: 请求语言类型。
        :type x_language: str
        :param limit: 查询记录数，默认为1000，limit最多为1000,不能为负数，最小值为1。
        :type limit: int
        :param offset: 索引位置，偏移量从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数。
        :type offset: int
        :param body: Body of the ListInstanceByTagsRequest
        :type body: :class:`huaweicloudsdkdrs.v5.QueryInstanceByTagReq`
        """
        
        

        self._resource_type = None
        self._x_language = None
        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        self.resource_type = resource_type
        if x_language is not None:
            self.x_language = x_language
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def resource_type(self):
        r"""Gets the resource_type of this ListInstanceByTagsRequest.

        资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：录制回放

        :return: The resource_type of this ListInstanceByTagsRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this ListInstanceByTagsRequest.

        资源类型。 - migration：实时迁移 - sync：实时同步 - cloudDataGuard：实时灾备 - subscription：数据订阅 - backupMigration：备份迁移 - replay：录制回放

        :param resource_type: The resource_type of this ListInstanceByTagsRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ListInstanceByTagsRequest.

        请求语言类型。

        :return: The x_language of this ListInstanceByTagsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListInstanceByTagsRequest.

        请求语言类型。

        :param x_language: The x_language of this ListInstanceByTagsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceByTagsRequest.

        查询记录数，默认为1000，limit最多为1000,不能为负数，最小值为1。

        :return: The limit of this ListInstanceByTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceByTagsRequest.

        查询记录数，默认为1000，limit最多为1000,不能为负数，最小值为1。

        :param limit: The limit of this ListInstanceByTagsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceByTagsRequest.

        索引位置，偏移量从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数。

        :return: The offset of this ListInstanceByTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceByTagsRequest.

        索引位置，偏移量从第一条数据偏移offset条数据后开始查询，默认为0（偏移0条数据，表示从第一条数据开始查询）,必须为数字，不能为负数。

        :param offset: The offset of this ListInstanceByTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ListInstanceByTagsRequest.

        :return: The body of this ListInstanceByTagsRequest.
        :rtype: :class:`huaweicloudsdkdrs.v5.QueryInstanceByTagReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListInstanceByTagsRequest.

        :param body: The body of this ListInstanceByTagsRequest.
        :type body: :class:`huaweicloudsdkdrs.v5.QueryInstanceByTagReq`
        """
        self._body = body

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
        if not isinstance(other, ListInstanceByTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
