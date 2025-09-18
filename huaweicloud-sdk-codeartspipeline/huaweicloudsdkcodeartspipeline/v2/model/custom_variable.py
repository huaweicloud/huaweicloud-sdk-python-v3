# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomVariable:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pipeline_id': 'str',
        'name': 'str',
        'sequence': 'int',
        'type': 'str',
        'value': 'str',
        'is_secret': 'bool',
        'description': 'str',
        'is_runtime': 'bool',
        'limits': 'list[object]',
        'is_reset': 'bool',
        'latest_value': 'str',
        'runtime_value': 'str'
    }

    attribute_map = {
        'pipeline_id': 'pipeline_id',
        'name': 'name',
        'sequence': 'sequence',
        'type': 'type',
        'value': 'value',
        'is_secret': 'is_secret',
        'description': 'description',
        'is_runtime': 'is_runtime',
        'limits': 'limits',
        'is_reset': 'is_reset',
        'latest_value': 'latest_value',
        'runtime_value': 'runtime_value'
    }

    def __init__(self, pipeline_id=None, name=None, sequence=None, type=None, value=None, is_secret=None, description=None, is_runtime=None, limits=None, is_reset=None, latest_value=None, runtime_value=None):
        r"""CustomVariable

        The model defined in huaweicloud sdk

        :param pipeline_id: **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 
        :type pipeline_id: str
        :param name: **参数解释**： 自定义参数名称。 **约束限制**： 不涉及。 **取值范围**： 仅支持大小写英文字母、数字、“_”，不超过128个字符。 **默认取值**： 不涉及。 
        :type name: str
        :param sequence: **参数解释**： 参数序号，从1开始。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type sequence: int
        :param type: **参数解释**： 自定义参数类型。 **约束限制**： 不涉及。 **取值范围**： - autoIncrement：自增长参数。 - enum：枚举参数。 - string：字符串参数。 **默认取值**： 不涉及。 
        :type type: str
        :param value: **参数解释**： 自定义参数默认值。 **约束限制**： 不涉及。 **取值范围**： 最长8192字符。 **默认取值**： 不涉及。 
        :type value: str
        :param is_secret: **参数解释**： 是否私密参数。 **约束限制**： 不涉及。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 **默认取值**： false。 
        :type is_secret: bool
        :param description: **参数解释**： 参数描述。 **约束限制**： 不涉及。 **取值范围**： 最长1024字符。 **默认取值**： 不涉及。 
        :type description: str
        :param is_runtime: **参数解释**： 是否运行时设置参数。 **约束限制**： 不涉及。 **取值范围**： - true：是运行时设置参数。 - false：不是运行时设置参数。 **默认取值**： false。 
        :type is_runtime: bool
        :param limits: **参数解释**： 枚举值列表。 **约束限制**： 不涉及。 **取值范围**： 每个枚举值不超过1024字符。 **默认取值**： 不涉及。 
        :type limits: list[object]
        :param is_reset: **参数解释**： 是否重置。自增长参数被编辑，则使用编辑后的值，否则进行末位数字递增。 **约束限制**： 不涉及。 **取值范围**： - true：使用编辑后的参数值。 - false：使用自增长参数。 **默认取值**： false。 
        :type is_reset: bool
        :param latest_value: **参数解释**： 最近一次运行的参数值。 **约束限制**： 不涉及。 **取值范围**： 最长8192字符。 **默认取值**： 不涉及。 
        :type latest_value: str
        :param runtime_value: **参数解释**： 流水线运行时设置参数的传入值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 
        :type runtime_value: str
        """
        
        

        self._pipeline_id = None
        self._name = None
        self._sequence = None
        self._type = None
        self._value = None
        self._is_secret = None
        self._description = None
        self._is_runtime = None
        self._limits = None
        self._is_reset = None
        self._latest_value = None
        self._runtime_value = None
        self.discriminator = None

        if pipeline_id is not None:
            self.pipeline_id = pipeline_id
        if name is not None:
            self.name = name
        if sequence is not None:
            self.sequence = sequence
        if type is not None:
            self.type = type
        if value is not None:
            self.value = value
        if is_secret is not None:
            self.is_secret = is_secret
        if description is not None:
            self.description = description
        if is_runtime is not None:
            self.is_runtime = is_runtime
        if limits is not None:
            self.limits = limits
        if is_reset is not None:
            self.is_reset = is_reset
        if latest_value is not None:
            self.latest_value = latest_value
        if runtime_value is not None:
            self.runtime_value = runtime_value

    @property
    def pipeline_id(self):
        r"""Gets the pipeline_id of this CustomVariable.

        **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :return: The pipeline_id of this CustomVariable.
        :rtype: str
        """
        return self._pipeline_id

    @pipeline_id.setter
    def pipeline_id(self, pipeline_id):
        r"""Sets the pipeline_id of this CustomVariable.

        **参数解释**： 流水线ID，可以通过[查询流水线列表](ListPipelines.xml)接口，其中pipelines.pipelineId即为流水线ID。 **约束限制**： 不涉及。 **取值范围**： 32位字符，由数字和字母组成。 **默认取值**： 不涉及。 

        :param pipeline_id: The pipeline_id of this CustomVariable.
        :type pipeline_id: str
        """
        self._pipeline_id = pipeline_id

    @property
    def name(self):
        r"""Gets the name of this CustomVariable.

        **参数解释**： 自定义参数名称。 **约束限制**： 不涉及。 **取值范围**： 仅支持大小写英文字母、数字、“_”，不超过128个字符。 **默认取值**： 不涉及。 

        :return: The name of this CustomVariable.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CustomVariable.

        **参数解释**： 自定义参数名称。 **约束限制**： 不涉及。 **取值范围**： 仅支持大小写英文字母、数字、“_”，不超过128个字符。 **默认取值**： 不涉及。 

        :param name: The name of this CustomVariable.
        :type name: str
        """
        self._name = name

    @property
    def sequence(self):
        r"""Gets the sequence of this CustomVariable.

        **参数解释**： 参数序号，从1开始。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The sequence of this CustomVariable.
        :rtype: int
        """
        return self._sequence

    @sequence.setter
    def sequence(self, sequence):
        r"""Sets the sequence of this CustomVariable.

        **参数解释**： 参数序号，从1开始。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param sequence: The sequence of this CustomVariable.
        :type sequence: int
        """
        self._sequence = sequence

    @property
    def type(self):
        r"""Gets the type of this CustomVariable.

        **参数解释**： 自定义参数类型。 **约束限制**： 不涉及。 **取值范围**： - autoIncrement：自增长参数。 - enum：枚举参数。 - string：字符串参数。 **默认取值**： 不涉及。 

        :return: The type of this CustomVariable.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this CustomVariable.

        **参数解释**： 自定义参数类型。 **约束限制**： 不涉及。 **取值范围**： - autoIncrement：自增长参数。 - enum：枚举参数。 - string：字符串参数。 **默认取值**： 不涉及。 

        :param type: The type of this CustomVariable.
        :type type: str
        """
        self._type = type

    @property
    def value(self):
        r"""Gets the value of this CustomVariable.

        **参数解释**： 自定义参数默认值。 **约束限制**： 不涉及。 **取值范围**： 最长8192字符。 **默认取值**： 不涉及。 

        :return: The value of this CustomVariable.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this CustomVariable.

        **参数解释**： 自定义参数默认值。 **约束限制**： 不涉及。 **取值范围**： 最长8192字符。 **默认取值**： 不涉及。 

        :param value: The value of this CustomVariable.
        :type value: str
        """
        self._value = value

    @property
    def is_secret(self):
        r"""Gets the is_secret of this CustomVariable.

        **参数解释**： 是否私密参数。 **约束限制**： 不涉及。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 **默认取值**： false。 

        :return: The is_secret of this CustomVariable.
        :rtype: bool
        """
        return self._is_secret

    @is_secret.setter
    def is_secret(self, is_secret):
        r"""Sets the is_secret of this CustomVariable.

        **参数解释**： 是否私密参数。 **约束限制**： 不涉及。 **取值范围**： - true：是私密参数。 - false：不是私密参数。 **默认取值**： false。 

        :param is_secret: The is_secret of this CustomVariable.
        :type is_secret: bool
        """
        self._is_secret = is_secret

    @property
    def description(self):
        r"""Gets the description of this CustomVariable.

        **参数解释**： 参数描述。 **约束限制**： 不涉及。 **取值范围**： 最长1024字符。 **默认取值**： 不涉及。 

        :return: The description of this CustomVariable.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CustomVariable.

        **参数解释**： 参数描述。 **约束限制**： 不涉及。 **取值范围**： 最长1024字符。 **默认取值**： 不涉及。 

        :param description: The description of this CustomVariable.
        :type description: str
        """
        self._description = description

    @property
    def is_runtime(self):
        r"""Gets the is_runtime of this CustomVariable.

        **参数解释**： 是否运行时设置参数。 **约束限制**： 不涉及。 **取值范围**： - true：是运行时设置参数。 - false：不是运行时设置参数。 **默认取值**： false。 

        :return: The is_runtime of this CustomVariable.
        :rtype: bool
        """
        return self._is_runtime

    @is_runtime.setter
    def is_runtime(self, is_runtime):
        r"""Sets the is_runtime of this CustomVariable.

        **参数解释**： 是否运行时设置参数。 **约束限制**： 不涉及。 **取值范围**： - true：是运行时设置参数。 - false：不是运行时设置参数。 **默认取值**： false。 

        :param is_runtime: The is_runtime of this CustomVariable.
        :type is_runtime: bool
        """
        self._is_runtime = is_runtime

    @property
    def limits(self):
        r"""Gets the limits of this CustomVariable.

        **参数解释**： 枚举值列表。 **约束限制**： 不涉及。 **取值范围**： 每个枚举值不超过1024字符。 **默认取值**： 不涉及。 

        :return: The limits of this CustomVariable.
        :rtype: list[object]
        """
        return self._limits

    @limits.setter
    def limits(self, limits):
        r"""Sets the limits of this CustomVariable.

        **参数解释**： 枚举值列表。 **约束限制**： 不涉及。 **取值范围**： 每个枚举值不超过1024字符。 **默认取值**： 不涉及。 

        :param limits: The limits of this CustomVariable.
        :type limits: list[object]
        """
        self._limits = limits

    @property
    def is_reset(self):
        r"""Gets the is_reset of this CustomVariable.

        **参数解释**： 是否重置。自增长参数被编辑，则使用编辑后的值，否则进行末位数字递增。 **约束限制**： 不涉及。 **取值范围**： - true：使用编辑后的参数值。 - false：使用自增长参数。 **默认取值**： false。 

        :return: The is_reset of this CustomVariable.
        :rtype: bool
        """
        return self._is_reset

    @is_reset.setter
    def is_reset(self, is_reset):
        r"""Sets the is_reset of this CustomVariable.

        **参数解释**： 是否重置。自增长参数被编辑，则使用编辑后的值，否则进行末位数字递增。 **约束限制**： 不涉及。 **取值范围**： - true：使用编辑后的参数值。 - false：使用自增长参数。 **默认取值**： false。 

        :param is_reset: The is_reset of this CustomVariable.
        :type is_reset: bool
        """
        self._is_reset = is_reset

    @property
    def latest_value(self):
        r"""Gets the latest_value of this CustomVariable.

        **参数解释**： 最近一次运行的参数值。 **约束限制**： 不涉及。 **取值范围**： 最长8192字符。 **默认取值**： 不涉及。 

        :return: The latest_value of this CustomVariable.
        :rtype: str
        """
        return self._latest_value

    @latest_value.setter
    def latest_value(self, latest_value):
        r"""Sets the latest_value of this CustomVariable.

        **参数解释**： 最近一次运行的参数值。 **约束限制**： 不涉及。 **取值范围**： 最长8192字符。 **默认取值**： 不涉及。 

        :param latest_value: The latest_value of this CustomVariable.
        :type latest_value: str
        """
        self._latest_value = latest_value

    @property
    def runtime_value(self):
        r"""Gets the runtime_value of this CustomVariable.

        **参数解释**： 流水线运行时设置参数的传入值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :return: The runtime_value of this CustomVariable.
        :rtype: str
        """
        return self._runtime_value

    @runtime_value.setter
    def runtime_value(self, runtime_value):
        r"""Sets the runtime_value of this CustomVariable.

        **参数解释**： 流水线运行时设置参数的传入值。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： 不涉及。 

        :param runtime_value: The runtime_value of this CustomVariable.
        :type runtime_value: str
        """
        self._runtime_value = runtime_value

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
        if not isinstance(other, CustomVariable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
