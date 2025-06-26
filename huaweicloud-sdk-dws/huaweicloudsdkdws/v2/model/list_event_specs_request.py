# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventSpecsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_name': 'str',
        'category': 'str',
        'severity': 'str',
        'source_type': 'str',
        'tag': 'str',
        'offset': 'str',
        'limit': 'str'
    }

    attribute_map = {
        'spec_name': 'spec_name',
        'category': 'category',
        'severity': 'severity',
        'source_type': 'source_type',
        'tag': 'tag',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, spec_name=None, category=None, severity=None, source_type=None, tag=None, offset=None, limit=None):
        r"""ListEventSpecsRequest

        The model defined in huaweicloud sdk

        :param spec_name: **参数解释**： 事件配置名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type spec_name: str
        :param category: **参数解释**： 事件类别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type category: str
        :param severity: **参数解释**： 事件级别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type severity: str
        :param source_type: **参数解释**： 事件源类别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type source_type: str
        :param tag: **参数解释**： 事件标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type tag: str
        :param offset: **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0
        :type offset: str
        :param limit: **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 1000
        :type limit: str
        """
        
        

        self._spec_name = None
        self._category = None
        self._severity = None
        self._source_type = None
        self._tag = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if spec_name is not None:
            self.spec_name = spec_name
        if category is not None:
            self.category = category
        if severity is not None:
            self.severity = severity
        if source_type is not None:
            self.source_type = source_type
        if tag is not None:
            self.tag = tag
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def spec_name(self):
        r"""Gets the spec_name of this ListEventSpecsRequest.

        **参数解释**： 事件配置名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The spec_name of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._spec_name

    @spec_name.setter
    def spec_name(self, spec_name):
        r"""Sets the spec_name of this ListEventSpecsRequest.

        **参数解释**： 事件配置名称。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param spec_name: The spec_name of this ListEventSpecsRequest.
        :type spec_name: str
        """
        self._spec_name = spec_name

    @property
    def category(self):
        r"""Gets the category of this ListEventSpecsRequest.

        **参数解释**： 事件类别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The category of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListEventSpecsRequest.

        **参数解释**： 事件类别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param category: The category of this ListEventSpecsRequest.
        :type category: str
        """
        self._category = category

    @property
    def severity(self):
        r"""Gets the severity of this ListEventSpecsRequest.

        **参数解释**： 事件级别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The severity of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._severity

    @severity.setter
    def severity(self, severity):
        r"""Sets the severity of this ListEventSpecsRequest.

        **参数解释**： 事件级别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param severity: The severity of this ListEventSpecsRequest.
        :type severity: str
        """
        self._severity = severity

    @property
    def source_type(self):
        r"""Gets the source_type of this ListEventSpecsRequest.

        **参数解释**： 事件源类别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The source_type of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this ListEventSpecsRequest.

        **参数解释**： 事件源类别。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param source_type: The source_type of this ListEventSpecsRequest.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def tag(self):
        r"""Gets the tag of this ListEventSpecsRequest.

        **参数解释**： 事件标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The tag of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ListEventSpecsRequest.

        **参数解释**： 事件标签。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param tag: The tag of this ListEventSpecsRequest.
        :type tag: str
        """
        self._tag = tag

    @property
    def offset(self):
        r"""Gets the offset of this ListEventSpecsRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :return: The offset of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEventSpecsRequest.

        **参数解释**： 分页偏移量，从0开始，页数减1。 **约束限制**： 不涉及。 **取值范围**： 大于等于0。 **默认取值**： 0

        :param offset: The offset of this ListEventSpecsRequest.
        :type offset: str
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEventSpecsRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 1000

        :return: The limit of this ListEventSpecsRequest.
        :rtype: str
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventSpecsRequest.

        **参数解释**： 分页单页大小。 **约束限制**： 不涉及。 **取值范围**： 大于0。 **默认取值**： 1000

        :param limit: The limit of this ListEventSpecsRequest.
        :type limit: str
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
        if not isinstance(other, ListEventSpecsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
