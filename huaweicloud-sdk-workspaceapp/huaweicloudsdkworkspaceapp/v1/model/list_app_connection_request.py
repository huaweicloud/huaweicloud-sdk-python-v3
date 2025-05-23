# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAppConnectionRequest:

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
        'body': 'ListAppConnectionReq'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'body': 'body'
    }

    def __init__(self, limit=None, offset=None, body=None):
        r"""ListAppConnectionRequest

        The model defined in huaweicloud sdk

        :param limit: 单次查询的大小[1-100]。
        :type limit: int
        :param offset: 查询的偏移量。
        :type offset: int
        :param body: Body of the ListAppConnectionRequest
        :type body: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionReq`
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
        r"""Gets the limit of this ListAppConnectionRequest.

        单次查询的大小[1-100]。

        :return: The limit of this ListAppConnectionRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListAppConnectionRequest.

        单次查询的大小[1-100]。

        :param limit: The limit of this ListAppConnectionRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListAppConnectionRequest.

        查询的偏移量。

        :return: The offset of this ListAppConnectionRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListAppConnectionRequest.

        查询的偏移量。

        :param offset: The offset of this ListAppConnectionRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def body(self):
        r"""Gets the body of this ListAppConnectionRequest.

        :return: The body of this ListAppConnectionRequest.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListAppConnectionRequest.

        :param body: The body of this ListAppConnectionRequest.
        :type body: :class:`huaweicloudsdkworkspaceapp.v1.ListAppConnectionReq`
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
        if not isinstance(other, ListAppConnectionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
