# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNotificationMasksRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'offset': 'int',
        'limit': 'int',
        'body': 'ListNotificationMaskRequestBody'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'body': 'body'
    }

    def __init__(self, offset=None, limit=None, body=None):
        """ListNotificationMasksRequest

        The model defined in huaweicloud sdk

        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        :param body: Body of the ListNotificationMasksRequest
        :type body: :class:`huaweicloudsdkces.v2.ListNotificationMaskRequestBody`
        """
        
        

        self._offset = None
        self._limit = None
        self._body = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if body is not None:
            self.body = body

    @property
    def offset(self):
        """Gets the offset of this ListNotificationMasksRequest.

        分页偏移量

        :return: The offset of this ListNotificationMasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListNotificationMasksRequest.

        分页偏移量

        :param offset: The offset of this ListNotificationMasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        """Gets the limit of this ListNotificationMasksRequest.

        分页大小

        :return: The limit of this ListNotificationMasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNotificationMasksRequest.

        分页大小

        :param limit: The limit of this ListNotificationMasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def body(self):
        """Gets the body of this ListNotificationMasksRequest.

        :return: The body of this ListNotificationMasksRequest.
        :rtype: :class:`huaweicloudsdkces.v2.ListNotificationMaskRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ListNotificationMasksRequest.

        :param body: The body of this ListNotificationMasksRequest.
        :type body: :class:`huaweicloudsdkces.v2.ListNotificationMaskRequestBody`
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
        if not isinstance(other, ListNotificationMasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other