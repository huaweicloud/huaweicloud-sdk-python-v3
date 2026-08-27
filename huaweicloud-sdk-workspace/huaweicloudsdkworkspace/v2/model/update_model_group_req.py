# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateModelGroupReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'priority': 'int',
        'default_model_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'priority': 'priority',
        'default_model_id': 'default_model_id'
    }

    def __init__(self, name=None, description=None, priority=None, default_model_id=None):
        r"""UpdateModelGroupReq

        The model defined in huaweicloud sdk

        :param name: 分组名称。
        :type name: str
        :param description: 分组描述。
        :type description: str
        :param priority: 分组优先级，最小值为1。
        :type priority: int
        :param default_model_id: 默认模型ID。
        :type default_model_id: str
        """
        
        

        self._name = None
        self._description = None
        self._priority = None
        self._default_model_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if priority is not None:
            self.priority = priority
        if default_model_id is not None:
            self.default_model_id = default_model_id

    @property
    def name(self):
        r"""Gets the name of this UpdateModelGroupReq.

        分组名称。

        :return: The name of this UpdateModelGroupReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateModelGroupReq.

        分组名称。

        :param name: The name of this UpdateModelGroupReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateModelGroupReq.

        分组描述。

        :return: The description of this UpdateModelGroupReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateModelGroupReq.

        分组描述。

        :param description: The description of this UpdateModelGroupReq.
        :type description: str
        """
        self._description = description

    @property
    def priority(self):
        r"""Gets the priority of this UpdateModelGroupReq.

        分组优先级，最小值为1。

        :return: The priority of this UpdateModelGroupReq.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this UpdateModelGroupReq.

        分组优先级，最小值为1。

        :param priority: The priority of this UpdateModelGroupReq.
        :type priority: int
        """
        self._priority = priority

    @property
    def default_model_id(self):
        r"""Gets the default_model_id of this UpdateModelGroupReq.

        默认模型ID。

        :return: The default_model_id of this UpdateModelGroupReq.
        :rtype: str
        """
        return self._default_model_id

    @default_model_id.setter
    def default_model_id(self, default_model_id):
        r"""Sets the default_model_id of this UpdateModelGroupReq.

        默认模型ID。

        :param default_model_id: The default_model_id of this UpdateModelGroupReq.
        :type default_model_id: str
        """
        self._default_model_id = default_model_id

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
        if not isinstance(other, UpdateModelGroupReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
