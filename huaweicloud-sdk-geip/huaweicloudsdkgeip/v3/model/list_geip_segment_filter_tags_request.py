# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGeipSegmentFilterTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'list[int]',
        'offset': 'list[int]',
        'body': 'ListResourcesByTagsRequestBody'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, limit=None, offset=None, body=None):
        """ListGeipSegmentFilterTagsRequest

        The model defined in huaweicloud sdk

        :param limit: 每页条数
        :type limit: list[int]
        :param offset: 分页起始点
        :type offset: list[int]
        :param body: Body of the ListGeipSegmentFilterTagsRequest
        :type body: :class:`huaweicloudsdkgeip.v3.ListResourcesByTagsRequestBody`
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
        """Gets the limit of this ListGeipSegmentFilterTagsRequest.

        每页条数

        :return: The limit of this ListGeipSegmentFilterTagsRequest.
        :rtype: list[int]
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListGeipSegmentFilterTagsRequest.

        每页条数

        :param limit: The limit of this ListGeipSegmentFilterTagsRequest.
        :type limit: list[int]
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListGeipSegmentFilterTagsRequest.

        分页起始点

        :return: The offset of this ListGeipSegmentFilterTagsRequest.
        :rtype: list[int]
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListGeipSegmentFilterTagsRequest.

        分页起始点

        :param offset: The offset of this ListGeipSegmentFilterTagsRequest.
        :type offset: list[int]
        """
        self._offset = offset

    @property
    def body(self):
        """Gets the body of this ListGeipSegmentFilterTagsRequest.

        :return: The body of this ListGeipSegmentFilterTagsRequest.
        :rtype: :class:`huaweicloudsdkgeip.v3.ListResourcesByTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListGeipSegmentFilterTagsRequest.

        :param body: The body of this ListGeipSegmentFilterTagsRequest.
        :type body: :class:`huaweicloudsdkgeip.v3.ListResourcesByTagsRequestBody`
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
        if not isinstance(other, ListGeipSegmentFilterTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
