# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEnterpriseProjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'name_keyword': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'name_keyword': 'name_keyword',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, x_language=None, name_keyword=None, offset=None, limit=None):
        r"""ListEnterpriseProjectsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us
        :type x_language: str
        :param name_keyword: **参数解释**: 企业项目名称关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。
        :type name_keyword: str
        :param offset: **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 不涉及。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。
        :type offset: int
        :param limit: **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 100
        :type limit: int
        """
        
        

        self._x_language = None
        self._name_keyword = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        if name_keyword is not None:
            self.name_keyword = name_keyword
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def x_language(self):
        r"""Gets the x_language of this ListEnterpriseProjectsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :return: The x_language of this ListEnterpriseProjectsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ListEnterpriseProjectsRequest.

        **参数解释**: 语言。 **约束限制**: 不涉及。 **取值范围**: - zh-cn  - en-us  **默认取值**: en-us

        :param x_language: The x_language of this ListEnterpriseProjectsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def name_keyword(self):
        r"""Gets the name_keyword of this ListEnterpriseProjectsRequest.

        **参数解释**: 企业项目名称关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :return: The name_keyword of this ListEnterpriseProjectsRequest.
        :rtype: str
        """
        return self._name_keyword

    @name_keyword.setter
    def name_keyword(self, name_keyword):
        r"""Sets the name_keyword of this ListEnterpriseProjectsRequest.

        **参数解释**: 企业项目名称关键字。 **约束限制**: 不涉及。 **取值范围**: 不涉及。 **默认取值**: 不涉及。

        :param name_keyword: The name_keyword of this ListEnterpriseProjectsRequest.
        :type name_keyword: str
        """
        self._name_keyword = name_keyword

    @property
    def offset(self):
        r"""Gets the offset of this ListEnterpriseProjectsRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 不涉及。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :return: The offset of this ListEnterpriseProjectsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListEnterpriseProjectsRequest.

        **参数解释**: 索引位置，偏移量。从第一条数据偏移offset条数据后开始查询。 **约束限制**: 必须为数字，不能为负数。 **取值范围**: 不涉及。 **默认取值**: 默认为0（偏移0条数据，表示从第一条数据开始查询）。

        :param offset: The offset of this ListEnterpriseProjectsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListEnterpriseProjectsRequest.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 100

        :return: The limit of this ListEnterpriseProjectsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEnterpriseProjectsRequest.

        **参数解释**: 查询记录数。 **约束限制**: 不能为负数。 **取值范围**: 最小值为1，最大值为1000。 **默认取值**: 100

        :param limit: The limit of this ListEnterpriseProjectsRequest.
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
        if not isinstance(other, ListEnterpriseProjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
