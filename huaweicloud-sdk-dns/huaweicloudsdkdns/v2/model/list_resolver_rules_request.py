# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResolverRulesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'domain_name': 'str',
        'name': 'str',
        'endpoint_id': 'str',
        'id': 'str',
        'limit': 'int',
        'offset': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'domain_name': 'domain_name',
        'name': 'name',
        'endpoint_id': 'endpoint_id',
        'id': 'id',
        'limit': 'limit',
        'offset': 'offset',
        'marker': 'marker'
    }

    def __init__(self, domain_name=None, name=None, endpoint_id=None, id=None, limit=None, offset=None, marker=None):
        r"""ListResolverRulesRequest

        The model defined in huaweicloud sdk

        :param domain_name: 待查询的转发规则的域名。
        :type domain_name: str
        :param name: 待查询的转发规则的名称。
        :type name: str
        :param endpoint_id: 终端节点ID。
        :type endpoint_id: str
        :param id: 转发规则ID。
        :type id: str
        :param limit: **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500
        :type limit: int
        :param offset: **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0
        :type offset: int
        :param marker: **参数解释：** 分页查询的起始资源ID。 - 查询第一页时，设置为空。 - 查询下一页时，设置为上一页最后一条资源的ID。  **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type marker: str
        """
        
        

        self._domain_name = None
        self._name = None
        self._endpoint_id = None
        self._id = None
        self._limit = None
        self._offset = None
        self._marker = None
        self.discriminator = None

        if domain_name is not None:
            self.domain_name = domain_name
        if name is not None:
            self.name = name
        if endpoint_id is not None:
            self.endpoint_id = endpoint_id
        if id is not None:
            self.id = id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if marker is not None:
            self.marker = marker

    @property
    def domain_name(self):
        r"""Gets the domain_name of this ListResolverRulesRequest.

        待查询的转发规则的域名。

        :return: The domain_name of this ListResolverRulesRequest.
        :rtype: str
        """
        return self._domain_name

    @domain_name.setter
    def domain_name(self, domain_name):
        r"""Sets the domain_name of this ListResolverRulesRequest.

        待查询的转发规则的域名。

        :param domain_name: The domain_name of this ListResolverRulesRequest.
        :type domain_name: str
        """
        self._domain_name = domain_name

    @property
    def name(self):
        r"""Gets the name of this ListResolverRulesRequest.

        待查询的转发规则的名称。

        :return: The name of this ListResolverRulesRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListResolverRulesRequest.

        待查询的转发规则的名称。

        :param name: The name of this ListResolverRulesRequest.
        :type name: str
        """
        self._name = name

    @property
    def endpoint_id(self):
        r"""Gets the endpoint_id of this ListResolverRulesRequest.

        终端节点ID。

        :return: The endpoint_id of this ListResolverRulesRequest.
        :rtype: str
        """
        return self._endpoint_id

    @endpoint_id.setter
    def endpoint_id(self, endpoint_id):
        r"""Sets the endpoint_id of this ListResolverRulesRequest.

        终端节点ID。

        :param endpoint_id: The endpoint_id of this ListResolverRulesRequest.
        :type endpoint_id: str
        """
        self._endpoint_id = endpoint_id

    @property
    def id(self):
        r"""Gets the id of this ListResolverRulesRequest.

        转发规则ID。

        :return: The id of this ListResolverRulesRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListResolverRulesRequest.

        转发规则ID。

        :param id: The id of this ListResolverRulesRequest.
        :type id: str
        """
        self._id = id

    @property
    def limit(self):
        r"""Gets the limit of this ListResolverRulesRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :return: The limit of this ListResolverRulesRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListResolverRulesRequest.

        **参数解释：** 分页查询时配置每页返回的资源个数。 **约束限制：** 不涉及。 **取值范围：** 0~500。 **默认取值：** 500

        :param limit: The limit of this ListResolverRulesRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListResolverRulesRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :return: The offset of this ListResolverRulesRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListResolverRulesRequest.

        **参数解释：** 分页查询起始偏移量，表示从偏移量的下一个资源开始查询。 **约束限制：** 当设置marker不为空时，以marker为分页起始标识，offset不生效。 **取值范围：** 0~2147483647。 **默认取值：** 0

        :param offset: The offset of this ListResolverRulesRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def marker(self):
        r"""Gets the marker of this ListResolverRulesRequest.

        **参数解释：** 分页查询的起始资源ID。 - 查询第一页时，设置为空。 - 查询下一页时，设置为上一页最后一条资源的ID。  **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The marker of this ListResolverRulesRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListResolverRulesRequest.

        **参数解释：** 分页查询的起始资源ID。 - 查询第一页时，设置为空。 - 查询下一页时，设置为上一页最后一条资源的ID。  **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param marker: The marker of this ListResolverRulesRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ListResolverRulesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
