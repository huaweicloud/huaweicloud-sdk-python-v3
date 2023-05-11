# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListNoticeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_read': 'bool',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'is_read': 'is_read',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, is_read=None, limit=None, offset=None):
        """ListNoticeRequest

        The model defined in huaweicloud sdk

        :param is_read: 消息状态是否已读，true返回已读，false返回未读，不填返回全部
        :type is_read: bool
        :param limit: 查询条数
        :type limit: int
        :param offset: 查询偏移量
        :type offset: int
        """
        
        

        self._is_read = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if is_read is not None:
            self.is_read = is_read
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def is_read(self):
        """Gets the is_read of this ListNoticeRequest.

        消息状态是否已读，true返回已读，false返回未读，不填返回全部

        :return: The is_read of this ListNoticeRequest.
        :rtype: bool
        """
        return self._is_read

    @is_read.setter
    def is_read(self, is_read):
        """Sets the is_read of this ListNoticeRequest.

        消息状态是否已读，true返回已读，false返回未读，不填返回全部

        :param is_read: The is_read of this ListNoticeRequest.
        :type is_read: bool
        """
        self._is_read = is_read

    @property
    def limit(self):
        """Gets the limit of this ListNoticeRequest.

        查询条数

        :return: The limit of this ListNoticeRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListNoticeRequest.

        查询条数

        :param limit: The limit of this ListNoticeRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListNoticeRequest.

        查询偏移量

        :return: The offset of this ListNoticeRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListNoticeRequest.

        查询偏移量

        :param offset: The offset of this ListNoticeRequest.
        :type offset: int
        """
        self._offset = offset

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
        if not isinstance(other, ListNoticeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
