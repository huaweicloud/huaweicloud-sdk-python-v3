# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssistantModel:

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
        'service_name': 'str',
        'name': 'str',
        'type': 'str',
        'model_service_api': 'str',
        'function_call': 'bool',
        'chain_of_thought': 'bool',
        'creator': 'str',
        'creator_id': 'str',
        'create_time': 'str',
        'update_time': 'str',
        'description': 'str'
    }

    attribute_map = {
        'id': 'id',
        'service_name': 'service_name',
        'name': 'name',
        'type': 'type',
        'model_service_api': 'model_service_api',
        'function_call': 'function_call',
        'chain_of_thought': 'chain_of_thought',
        'creator': 'creator',
        'creator_id': 'creator_id',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'description': 'description'
    }

    def __init__(self, id=None, service_name=None, name=None, type=None, model_service_api=None, function_call=None, chain_of_thought=None, creator=None, creator_id=None, create_time=None, update_time=None, description=None):
        r"""AssistantModel

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type id: str
        :param service_name: **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type service_name: str
        :param name: **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type name: str
        :param type: **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * CHAT：文本对话模型 * EMBEDDING：嵌入模型 **默认取值**： 不涉及 
        :type type: str
        :param model_service_api: **参数解释**： 模型服务API地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type model_service_api: str
        :param function_call: **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 
        :type function_call: bool
        :param chain_of_thought: **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 
        :type chain_of_thought: bool
        :param creator: **参数解释**： 模型创建人。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type creator: str
        :param creator_id: **参数解释**： 模型创建人ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type creator_id: str
        :param create_time: **参数解释**： 模型创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type create_time: str
        :param update_time: **参数解释**： 模型修改时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type update_time: str
        :param description: **参数解释**： 模型描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 
        :type description: str
        """
        
        

        self._id = None
        self._service_name = None
        self._name = None
        self._type = None
        self._model_service_api = None
        self._function_call = None
        self._chain_of_thought = None
        self._creator = None
        self._creator_id = None
        self._create_time = None
        self._update_time = None
        self._description = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if service_name is not None:
            self.service_name = service_name
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if model_service_api is not None:
            self.model_service_api = model_service_api
        if function_call is not None:
            self.function_call = function_call
        if chain_of_thought is not None:
            self.chain_of_thought = chain_of_thought
        if creator is not None:
            self.creator = creator
        if creator_id is not None:
            self.creator_id = creator_id
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description

    @property
    def id(self):
        r"""Gets the id of this AssistantModel.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The id of this AssistantModel.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AssistantModel.

        **参数解释**： 模型供应商ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param id: The id of this AssistantModel.
        :type id: str
        """
        self._id = id

    @property
    def service_name(self):
        r"""Gets the service_name of this AssistantModel.

        **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The service_name of this AssistantModel.
        :rtype: str
        """
        return self._service_name

    @service_name.setter
    def service_name(self, service_name):
        r"""Sets the service_name of this AssistantModel.

        **参数解释**： 服务名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param service_name: The service_name of this AssistantModel.
        :type service_name: str
        """
        self._service_name = service_name

    @property
    def name(self):
        r"""Gets the name of this AssistantModel.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The name of this AssistantModel.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AssistantModel.

        **参数解释**： 模型名称。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param name: The name of this AssistantModel.
        :type name: str
        """
        self._name = name

    @property
    def type(self):
        r"""Gets the type of this AssistantModel.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * CHAT：文本对话模型 * EMBEDDING：嵌入模型 **默认取值**： 不涉及 

        :return: The type of this AssistantModel.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this AssistantModel.

        **参数解释**： 模型类型。 **约束限制**： 不涉及 **取值范围**： * CHAT：文本对话模型 * EMBEDDING：嵌入模型 **默认取值**： 不涉及 

        :param type: The type of this AssistantModel.
        :type type: str
        """
        self._type = type

    @property
    def model_service_api(self):
        r"""Gets the model_service_api of this AssistantModel.

        **参数解释**： 模型服务API地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The model_service_api of this AssistantModel.
        :rtype: str
        """
        return self._model_service_api

    @model_service_api.setter
    def model_service_api(self, model_service_api):
        r"""Sets the model_service_api of this AssistantModel.

        **参数解释**： 模型服务API地址。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param model_service_api: The model_service_api of this AssistantModel.
        :type model_service_api: str
        """
        self._model_service_api = model_service_api

    @property
    def function_call(self):
        r"""Gets the function_call of this AssistantModel.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :return: The function_call of this AssistantModel.
        :rtype: bool
        """
        return self._function_call

    @function_call.setter
    def function_call(self, function_call):
        r"""Sets the function_call of this AssistantModel.

        **参数解释**： 是否支持工具调用。 **约束限制**： 不涉及 **取值范围**： * true：支持工具调用 * false：不支持工具调用 **默认取值**： 不涉及 

        :param function_call: The function_call of this AssistantModel.
        :type function_call: bool
        """
        self._function_call = function_call

    @property
    def chain_of_thought(self):
        r"""Gets the chain_of_thought of this AssistantModel.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :return: The chain_of_thought of this AssistantModel.
        :rtype: bool
        """
        return self._chain_of_thought

    @chain_of_thought.setter
    def chain_of_thought(self, chain_of_thought):
        r"""Sets the chain_of_thought of this AssistantModel.

        **参数解释**： 是否支持思维链。 **约束限制**： 不涉及 **取值范围**： * true：支持思维链 * false：不支持思维链 **默认取值**： 不涉及 

        :param chain_of_thought: The chain_of_thought of this AssistantModel.
        :type chain_of_thought: bool
        """
        self._chain_of_thought = chain_of_thought

    @property
    def creator(self):
        r"""Gets the creator of this AssistantModel.

        **参数解释**： 模型创建人。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The creator of this AssistantModel.
        :rtype: str
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        r"""Sets the creator of this AssistantModel.

        **参数解释**： 模型创建人。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param creator: The creator of this AssistantModel.
        :type creator: str
        """
        self._creator = creator

    @property
    def creator_id(self):
        r"""Gets the creator_id of this AssistantModel.

        **参数解释**： 模型创建人ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The creator_id of this AssistantModel.
        :rtype: str
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        r"""Sets the creator_id of this AssistantModel.

        **参数解释**： 模型创建人ID。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param creator_id: The creator_id of this AssistantModel.
        :type creator_id: str
        """
        self._creator_id = creator_id

    @property
    def create_time(self):
        r"""Gets the create_time of this AssistantModel.

        **参数解释**： 模型创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The create_time of this AssistantModel.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this AssistantModel.

        **参数解释**： 模型创建时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param create_time: The create_time of this AssistantModel.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this AssistantModel.

        **参数解释**： 模型修改时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The update_time of this AssistantModel.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this AssistantModel.

        **参数解释**： 模型修改时间。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param update_time: The update_time of this AssistantModel.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this AssistantModel.

        **参数解释**： 模型描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :return: The description of this AssistantModel.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this AssistantModel.

        **参数解释**： 模型描述。 **约束限制**： 不涉及 **取值范围**： 不涉及 **默认取值**： 不涉及 

        :param description: The description of this AssistantModel.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, AssistantModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
