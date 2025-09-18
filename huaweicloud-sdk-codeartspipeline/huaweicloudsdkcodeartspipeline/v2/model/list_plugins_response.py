# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPluginsResponse(SdkResponse):

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
        'total': 'int',
        'data': 'list[PluginBasicVO]'
    }

    attribute_map = {
        'offset': 'offset',
        'limit': 'limit',
        'total': 'total',
        'data': 'data'
    }

    def __init__(self, offset=None, limit=None, total=None, data=None):
        r"""ListPluginsResponse

        The model defined in huaweicloud sdk

        :param offset: **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： offset大于等于0。 **默认取值**： 默认为0。 
        :type offset: int
        :param limit: **参数解释**： 每次查询的条目数量。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。 
        :type limit: int
        :param total: **参数解释**： 总条目数量。 **取值范围**： 大于等于0。 
        :type total: int
        :param data: **参数解释**： 扩展插件列表。 **取值范围**： 不涉及。 
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginBasicVO`]
        """
        
        super(ListPluginsResponse, self).__init__()

        self._offset = None
        self._limit = None
        self._total = None
        self._data = None
        self.discriminator = None

        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if total is not None:
            self.total = total
        if data is not None:
            self.data = data

    @property
    def offset(self):
        r"""Gets the offset of this ListPluginsResponse.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： offset大于等于0。 **默认取值**： 默认为0。 

        :return: The offset of this ListPluginsResponse.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPluginsResponse.

        **参数解释**： 偏移量，表示从此偏移量开始查询。 **约束限制**： 不涉及。 **取值范围**： offset大于等于0。 **默认取值**： 默认为0。 

        :param offset: The offset of this ListPluginsResponse.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListPluginsResponse.

        **参数解释**： 每次查询的条目数量。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。 

        :return: The limit of this ListPluginsResponse.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPluginsResponse.

        **参数解释**： 每次查询的条目数量。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 不涉及。 

        :param limit: The limit of this ListPluginsResponse.
        :type limit: int
        """
        self._limit = limit

    @property
    def total(self):
        r"""Gets the total of this ListPluginsResponse.

        **参数解释**： 总条目数量。 **取值范围**： 大于等于0。 

        :return: The total of this ListPluginsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListPluginsResponse.

        **参数解释**： 总条目数量。 **取值范围**： 大于等于0。 

        :param total: The total of this ListPluginsResponse.
        :type total: int
        """
        self._total = total

    @property
    def data(self):
        r"""Gets the data of this ListPluginsResponse.

        **参数解释**： 扩展插件列表。 **取值范围**： 不涉及。 

        :return: The data of this ListPluginsResponse.
        :rtype: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginBasicVO`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListPluginsResponse.

        **参数解释**： 扩展插件列表。 **取值范围**： 不涉及。 

        :param data: The data of this ListPluginsResponse.
        :type data: list[:class:`huaweicloudsdkcodeartspipeline.v2.PluginBasicVO`]
        """
        self._data = data

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
        if not isinstance(other, ListPluginsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
