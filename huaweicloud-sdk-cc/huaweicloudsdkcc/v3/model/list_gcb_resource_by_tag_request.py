# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGcbResourceByTagRequest:

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
        'body': 'QueryResourceByTagRequestBody'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, limit=None, offset=None, body=None):
        r"""ListGcbResourceByTagRequest

        The model defined in huaweicloud sdk

        :param limit: 查询记录数。
        :type limit: int
        :param offset: 索引位置，偏移量。
        :type offset: int
        :param body: Body of the ListGcbResourceByTagRequest
        :type body: :class:`huaweicloudsdkcc.v3.QueryResourceByTagRequestBody`
        """
        
        

        self._limit = None
        self._offset = None
        self._body = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if body is not None:
            self.body = body

    @property
    def limit(self):
        r"""Gets the limit of this ListGcbResourceByTagRequest.

        查询记录数。

        :return: The limit of this ListGcbResourceByTagRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListGcbResourceByTagRequest.

        查询记录数。

        :param limit: The limit of this ListGcbResourceByTagRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListGcbResourceByTagRequest.

        索引位置，偏移量。

        :return: The offset of this ListGcbResourceByTagRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListGcbResourceByTagRequest.

        索引位置，偏移量。

        :param offset: The offset of this ListGcbResourceByTagRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ListGcbResourceByTagRequest.

        :return: The body of this ListGcbResourceByTagRequest.
        :rtype: :class:`huaweicloudsdkcc.v3.QueryResourceByTagRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListGcbResourceByTagRequest.

        :param body: The body of this ListGcbResourceByTagRequest.
        :type body: :class:`huaweicloudsdkcc.v3.QueryResourceByTagRequestBody`
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
        if not isinstance(other, ListGcbResourceByTagRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
