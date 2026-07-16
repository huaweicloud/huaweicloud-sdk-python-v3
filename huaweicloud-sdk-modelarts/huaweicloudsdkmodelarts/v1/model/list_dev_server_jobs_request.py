# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDevServerJobsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'type': 'str',
        'status': 'str',
        'visible': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'type': 'type',
        'status': 'status',
        'visible': 'visible'
    }

    def __init__(self, id=None, name=None, type=None, status=None, visible=None):
        r"""ListDevServerJobsRequest

        The model defined in huaweicloud sdk

        :param id: **参数解释**：Lite Server job id。 **约束限制**：无。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。
        :type id: str
        :param name: **参数解释**：Lite Server job的name。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param type: **参数解释**：Lite Server job的类型。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type type: str
        :param status: **参数解释**：Lite Server job的状态。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type status: str
        :param visible: **参数解释**：是否可见。 **约束限制**：bool。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type visible: bool
        """
        
        

        self._id = None
        self._name = None
        self._type = None
        self._status = None
        self._visible = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status
        if visible is not None:
            self.visible = visible

    @property
    def id(self):
        r"""Gets the id of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job id。 **约束限制**：无。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :return: The id of this ListDevServerJobsRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job id。 **约束限制**：无。 **取值范围**：1 - 64字符。 **默认取值**：不涉及。

        :param id: The id of this ListDevServerJobsRequest.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job的name。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this ListDevServerJobsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job的name。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this ListDevServerJobsRequest.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job的类型。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The type of this ListDevServerJobsRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job的类型。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param type: The type of this ListDevServerJobsRequest.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job的状态。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The status of this ListDevServerJobsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListDevServerJobsRequest.

        **参数解释**：Lite Server job的状态。 **约束限制**：无。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param status: The status of this ListDevServerJobsRequest.
        :type status: str
        """
        self._status = status

    @property
    def visible(self):
        r"""Gets the visible of this ListDevServerJobsRequest.

        **参数解释**：是否可见。 **约束限制**：bool。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The visible of this ListDevServerJobsRequest.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        r"""Sets the visible of this ListDevServerJobsRequest.

        **参数解释**：是否可见。 **约束限制**：bool。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param visible: The visible of this ListDevServerJobsRequest.
        :type visible: bool
        """
        self._visible = visible

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
        if not isinstance(other, ListDevServerJobsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
