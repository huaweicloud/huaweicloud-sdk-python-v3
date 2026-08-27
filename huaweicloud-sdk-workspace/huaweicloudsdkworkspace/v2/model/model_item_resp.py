# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelItemResp:

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
        'provider_model_id': 'str',
        'input': 'list[str]',
        'description': 'str',
        'is_builtin': 'bool'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'provider_model_id': 'provider_model_id',
        'input': 'input',
        'description': 'description',
        'is_builtin': 'is_builtin'
    }

    def __init__(self, id=None, name=None, provider_model_id=None, input=None, description=None, is_builtin=None):
        r"""ModelItemResp

        The model defined in huaweicloud sdk

        :param id: 模型id。
        :type id: str
        :param name: 模型名称。
        :type name: str
        :param provider_model_id: 供应商侧模型标识。
        :type provider_model_id: str
        :param input: 输入类型数组。
        :type input: list[str]
        :param description: 模型描述。
        :type description: str
        :param is_builtin: 是否为内置模型。
        :type is_builtin: bool
        """
        
        

        self._id = None
        self._name = None
        self._provider_model_id = None
        self._input = None
        self._description = None
        self._is_builtin = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if provider_model_id is not None:
            self.provider_model_id = provider_model_id
        if input is not None:
            self.input = input
        if description is not None:
            self.description = description
        if is_builtin is not None:
            self.is_builtin = is_builtin

    @property
    def id(self):
        r"""Gets the id of this ModelItemResp.

        模型id。

        :return: The id of this ModelItemResp.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ModelItemResp.

        模型id。

        :param id: The id of this ModelItemResp.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this ModelItemResp.

        模型名称。

        :return: The name of this ModelItemResp.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ModelItemResp.

        模型名称。

        :param name: The name of this ModelItemResp.
        :type name: str
        """
        self._name = name

    @property
    def provider_model_id(self):
        r"""Gets the provider_model_id of this ModelItemResp.

        供应商侧模型标识。

        :return: The provider_model_id of this ModelItemResp.
        :rtype: str
        """
        return self._provider_model_id

    @provider_model_id.setter
    def provider_model_id(self, provider_model_id):
        r"""Sets the provider_model_id of this ModelItemResp.

        供应商侧模型标识。

        :param provider_model_id: The provider_model_id of this ModelItemResp.
        :type provider_model_id: str
        """
        self._provider_model_id = provider_model_id

    @property
    def input(self):
        r"""Gets the input of this ModelItemResp.

        输入类型数组。

        :return: The input of this ModelItemResp.
        :rtype: list[str]
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ModelItemResp.

        输入类型数组。

        :param input: The input of this ModelItemResp.
        :type input: list[str]
        """
        self._input = input

    @property
    def description(self):
        r"""Gets the description of this ModelItemResp.

        模型描述。

        :return: The description of this ModelItemResp.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ModelItemResp.

        模型描述。

        :param description: The description of this ModelItemResp.
        :type description: str
        """
        self._description = description

    @property
    def is_builtin(self):
        r"""Gets the is_builtin of this ModelItemResp.

        是否为内置模型。

        :return: The is_builtin of this ModelItemResp.
        :rtype: bool
        """
        return self._is_builtin

    @is_builtin.setter
    def is_builtin(self, is_builtin):
        r"""Sets the is_builtin of this ModelItemResp.

        是否为内置模型。

        :param is_builtin: The is_builtin of this ModelItemResp.
        :type is_builtin: bool
        """
        self._is_builtin = is_builtin

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
        if not isinstance(other, ModelItemResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
