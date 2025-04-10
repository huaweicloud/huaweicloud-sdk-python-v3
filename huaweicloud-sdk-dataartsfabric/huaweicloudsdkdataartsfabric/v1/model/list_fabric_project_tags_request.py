# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFabricProjectTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'use_predefine_tags': 'bool',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'use_predefine_tags': 'use_predefine_tags',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, use_predefine_tags=None, offset=None, limit=None):
        r"""ListFabricProjectTagsRequest

        The model defined in huaweicloud sdk

        :param use_predefine_tags: 使用预定义标签，true表示使用。
        :type use_predefine_tags: bool
        :param offset: 偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。
        :type offset: int
        :param limit: 查询记录数默认为1000，limit最多为1000,不能为负数，最小值为1
        :type limit: int
        """
        
        

        self._use_predefine_tags = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.use_predefine_tags = use_predefine_tags
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def use_predefine_tags(self):
        r"""Gets the use_predefine_tags of this ListFabricProjectTagsRequest.

        使用预定义标签，true表示使用。

        :return: The use_predefine_tags of this ListFabricProjectTagsRequest.
        :rtype: bool
        """
        return self._use_predefine_tags

    @use_predefine_tags.setter
    def use_predefine_tags(self, use_predefine_tags):
        r"""Sets the use_predefine_tags of this ListFabricProjectTagsRequest.

        使用预定义标签，true表示使用。

        :param use_predefine_tags: The use_predefine_tags of this ListFabricProjectTagsRequest.
        :type use_predefine_tags: bool
        """
        self._use_predefine_tags = use_predefine_tags

    @property
    def offset(self):
        r"""Gets the offset of this ListFabricProjectTagsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :return: The offset of this ListFabricProjectTagsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListFabricProjectTagsRequest.

        偏移量，表示从此偏移量开始查询， offset大于等于0，默认为0。

        :param offset: The offset of this ListFabricProjectTagsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListFabricProjectTagsRequest.

        查询记录数默认为1000，limit最多为1000,不能为负数，最小值为1

        :return: The limit of this ListFabricProjectTagsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListFabricProjectTagsRequest.

        查询记录数默认为1000，limit最多为1000,不能为负数，最小值为1

        :param limit: The limit of this ListFabricProjectTagsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListFabricProjectTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
