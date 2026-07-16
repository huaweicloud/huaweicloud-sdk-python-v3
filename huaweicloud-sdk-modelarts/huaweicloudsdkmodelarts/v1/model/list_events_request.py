# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListEventsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'str',
        'name': 'str',
        'limit': 'int',
        '_continue': 'str',
        'since': 'int',
        'until': 'int',
        'type': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'name': 'name',
        'limit': 'limit',
        '_continue': 'continue',
        'since': 'since',
        'until': 'until',
        'type': 'type'
    }

    def __init__(self, resource=None, name=None, limit=None, _continue=None, since=None, until=None, type=None):
        r"""ListEventsRequest

        The model defined in huaweicloud sdk

        :param resource: **参数解释**：事件所属资源类型。可选值为pools，表示资源池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type resource: str
        :param name: **参数解释**：事件所属资源名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param limit: **参数解释**：单页查询最大数量，该值为空或者0时默认返回500条记录，单页最大允许查询500条记录。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type limit: int
        :param _continue: **参数解释**：分页查询的上一页标记，内容为UUID字符串，查询第一页时为空。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type _continue: str
        :param since: **参数解释**：事件开始时间戳。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type since: int
        :param until: **参数解释**：事件结束时间戳。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type until: int
        :param type: **参数解释**：事件类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Normal：正常 - Warning：异常 **默认取值**：不涉及。
        :type type: str
        """
        
        

        self._resource = None
        self._name = None
        self._limit = None
        self.__continue = None
        self._since = None
        self._until = None
        self._type = None
        self.discriminator = None

        self.resource = resource
        self.name = name
        if limit is not None:
            self.limit = limit
        if _continue is not None:
            self._continue = _continue
        if since is not None:
            self.since = since
        if until is not None:
            self.until = until
        if type is not None:
            self.type = type

    @property
    def resource(self):
        r"""Gets the resource of this ListEventsRequest.

        **参数解释**：事件所属资源类型。可选值为pools，表示资源池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The resource of this ListEventsRequest.
        :rtype: str
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this ListEventsRequest.

        **参数解释**：事件所属资源类型。可选值为pools，表示资源池。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param resource: The resource of this ListEventsRequest.
        :type resource: str
        """
        self._resource = resource

    @property
    def name(self):
        r"""Gets the name of this ListEventsRequest.

        **参数解释**：事件所属资源名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this ListEventsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListEventsRequest.

        **参数解释**：事件所属资源名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this ListEventsRequest.
        :type name: str
        """
        self._name = name

    @property
    def limit(self):
        r"""Gets the limit of this ListEventsRequest.

        **参数解释**：单页查询最大数量，该值为空或者0时默认返回500条记录，单页最大允许查询500条记录。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The limit of this ListEventsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListEventsRequest.

        **参数解释**：单页查询最大数量，该值为空或者0时默认返回500条记录，单页最大允许查询500条记录。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param limit: The limit of this ListEventsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def _continue(self):
        r"""Gets the _continue of this ListEventsRequest.

        **参数解释**：分页查询的上一页标记，内容为UUID字符串，查询第一页时为空。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The _continue of this ListEventsRequest.
        :rtype: str
        """
        return self.__continue

    @_continue.setter
    def _continue(self, _continue):
        r"""Sets the _continue of this ListEventsRequest.

        **参数解释**：分页查询的上一页标记，内容为UUID字符串，查询第一页时为空。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param _continue: The _continue of this ListEventsRequest.
        :type _continue: str
        """
        self.__continue = _continue

    @property
    def since(self):
        r"""Gets the since of this ListEventsRequest.

        **参数解释**：事件开始时间戳。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The since of this ListEventsRequest.
        :rtype: int
        """
        return self._since

    @since.setter
    def since(self, since):
        r"""Sets the since of this ListEventsRequest.

        **参数解释**：事件开始时间戳。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param since: The since of this ListEventsRequest.
        :type since: int
        """
        self._since = since

    @property
    def until(self):
        r"""Gets the until of this ListEventsRequest.

        **参数解释**：事件结束时间戳。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The until of this ListEventsRequest.
        :rtype: int
        """
        return self._until

    @until.setter
    def until(self, until):
        r"""Sets the until of this ListEventsRequest.

        **参数解释**：事件结束时间戳。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param until: The until of this ListEventsRequest.
        :type until: int
        """
        self._until = until

    @property
    def type(self):
        r"""Gets the type of this ListEventsRequest.

        **参数解释**：事件类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Normal：正常 - Warning：异常 **默认取值**：不涉及。

        :return: The type of this ListEventsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListEventsRequest.

        **参数解释**：事件类型。 **约束限制**：不涉及。 **取值范围**：可选值如下： - Normal：正常 - Warning：异常 **默认取值**：不涉及。

        :param type: The type of this ListEventsRequest.
        :type type: str
        """
        self._type = type

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ListEventsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
