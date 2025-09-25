# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListChatRequest:

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
        'title': 'str'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'sort_dir': 'sort_dir',
        'title': 'title'
    }

    def __init__(self, limit=None, offset=None, sort_dir=None, title=None):
        r"""ListChatRequest

        The model defined in huaweicloud sdk

        :param limit: **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,1000]。 **默认取值**： 100 
        :type limit: int
        :param offset: **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 
        :type offset: int
        :param sort_dir: **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 
        :type sort_dir: str
        :param title: **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-500]个字符。 **默认取值**： 不涉及 
        :type title: str
        """
        
        

        self._limit = None
        self._offset = None
        self._sort_dir = None
        self._title = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if sort_dir is not None:
            self.sort_dir = sort_dir
        if title is not None:
            self.title = title

    @property
    def limit(self):
        r"""Gets the limit of this ListChatRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,1000]。 **默认取值**： 100 

        :return: The limit of this ListChatRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListChatRequest.

        **参数解释**： 限制量，单次查询总量。 **约束限制**： 不涉及 **取值范围**： 取值范围[1,1000]。 **默认取值**： 100 

        :param limit: The limit of this ListChatRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListChatRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 

        :return: The offset of this ListChatRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListChatRequest.

        **参数解释**： 偏移量，查询起始偏移。 **约束限制**： 不涉及 **取值范围**： 取值范围[0,100000000]。 **默认取值**： 0 

        :param offset: The offset of this ListChatRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def sort_dir(self):
        r"""Gets the sort_dir of this ListChatRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :return: The sort_dir of this ListChatRequest.
        :rtype: str
        """
        return self._sort_dir

    @sort_dir.setter
    def sort_dir(self, sort_dir):
        r"""Sets the sort_dir of this ListChatRequest.

        **参数解释**： 排序规则。 **约束限制**： 不涉及 **取值范围**： - DESC：降序。 - ASC：升序。 **默认取值**： DESC 

        :param sort_dir: The sort_dir of this ListChatRequest.
        :type sort_dir: str
        """
        self._sort_dir = sort_dir

    @property
    def title(self):
        r"""Gets the title of this ListChatRequest.

        **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-500]个字符。 **默认取值**： 不涉及 

        :return: The title of this ListChatRequest.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this ListChatRequest.

        **参数解释**： 对话名称，支持模糊搜索。 **约束限制**： 不涉及 **取值范围**： 取值范围为[1-500]个字符。 **默认取值**： 不涉及 

        :param title: The title of this ListChatRequest.
        :type title: str
        """
        self._title = title

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
        if not isinstance(other, ListChatRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
