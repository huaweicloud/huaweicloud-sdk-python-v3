# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListBaseModelRequest:

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
        'sort_dir': 'str',
        'sort_key': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'sort_key': 'sort_key'
    }

    def __init__(self, limit=None, offset=None, sort_dir=None, sort_key=None):
        r"""ListBaseModelRequest

        The model defined in huaweicloud sdk

        :param limit: 限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]
        :type limit: int
        :param offset: 偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]
        :type offset: int
        :param sort_dir: 排序规则 目前默认时间升序
        :type sort_dir: str
        :param sort_key: 排序规则 目前默认时间升序，支持根据create_time排序
        :type sort_key: str
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._sort_key = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if sort_key is not None:
            self.sort_key = sort_key

    @property
    def limit(self):
        r"""Gets the limit of this ListBaseModelRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :return: The limit of this ListBaseModelRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListBaseModelRequest.

        限制量，单次查询总量，必须由数字组成，默认为100，取值范围[1,1000]

        :param limit: The limit of this ListBaseModelRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListBaseModelRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :return: The offset of this ListBaseModelRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListBaseModelRequest.

        偏移量，查询起始偏移，必须由数字组成，默认为0，取值范围[0,100000000]

        :param offset: The offset of this ListBaseModelRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListBaseModelRequest.

        排序规则 目前默认时间升序

        :return: The sort_dir of this ListBaseModelRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListBaseModelRequest.

        排序规则 目前默认时间升序

        :param sort_dir: The sort_dir of this ListBaseModelRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def sort_key(self):
        r"""Gets the sort_key of this ListBaseModelRequest.

        排序规则 目前默认时间升序，支持根据create_time排序

        :return: The sort_key of this ListBaseModelRequest.
        :rtype: str
        """
        return self._sort_key

    @sort_key.setter
    def sort_key(self, sort_key):
        r"""Sets the sort_key of this ListBaseModelRequest.

        排序规则 目前默认时间升序，支持根据create_time排序

        :param sort_key: The sort_key of this ListBaseModelRequest.
        :type sort_key: str
        """
        self._sort_key = sort_key

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
        if not isinstance(other, ListBaseModelRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
