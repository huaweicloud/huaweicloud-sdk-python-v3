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
        'sort_key': 'str',
        'sort_dir': 'str',
        'body': 'ListNotificationMaskRequestBody'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'sort_key': 'sort_key',
        'sort_dir': 'sort_dir',
        'body': 'body'
    }

    def __init__(self, offset=None, limit=None, sort_key=None, sort_dir=None, body=None):
        r"""ListNotificationMasksRequest

        The model defined in huaweicloud sdk

        :param offset: 分页偏移量
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        :param sort_key: 排序关键字，与sort_dir同时使用。 目前只支持create_time与update_time create_time表示按创建时间排序，update_time表示按修改时间排序
        :type sort_key: str
        :param sort_dir: 排序顺序，与sort_key同时使用。DESC表示降序排序；ASC表示升序排序；
        :type sort_dir: str
        :param body: Body of the ListNotificationMasksRequest
        :type body: :class:`huaweicloudsdkces.v2.ListNotificationMaskRequestBody`
        """
        
        

        self._offset = None
        self._limit = None
        self._sort_key = None
        self._sort_dir = None
        self._body = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if sort_key is not None:
            self.sort_key = sort_key
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if body is not None:
            self.body = body

    @property
    def offset(self):
        r"""Gets the offset of this ListNotificationMasksRequest.

        分页偏移量

        :return: The offset of this ListNotificationMasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListNotificationMasksRequest.

        分页偏移量

        :param offset: The offset of this ListNotificationMasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListNotificationMasksRequest.

        分页大小

        :return: The limit of this ListNotificationMasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListNotificationMasksRequest.

        分页大小

        :param limit: The limit of this ListNotificationMasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListNotificationMasksRequest.

        排序关键字，与sort_dir同时使用。 目前只支持create_time与update_time create_time表示按创建时间排序，update_time表示按修改时间排序

        :return: The sort_key of this ListNotificationMasksRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListNotificationMasksRequest.

        排序关键字，与sort_dir同时使用。 目前只支持create_time与update_time create_time表示按创建时间排序，update_time表示按修改时间排序

        :param sort_key: The sort_key of this ListNotificationMasksRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListNotificationMasksRequest.

        排序顺序，与sort_key同时使用。DESC表示降序排序；ASC表示升序排序；

        :return: The sort_dir of this ListNotificationMasksRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListNotificationMasksRequest.

        排序顺序，与sort_key同时使用。DESC表示降序排序；ASC表示升序排序；

        :param sort_dir: The sort_dir of this ListNotificationMasksRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def body(self):
        r"""Gets the body of this ListNotificationMasksRequest.

        :return: The body of this ListNotificationMasksRequest.
        :rtype: :class:`huaweicloudsdkces.v2.ListNotificationMaskRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ListNotificationMasksRequest.

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
