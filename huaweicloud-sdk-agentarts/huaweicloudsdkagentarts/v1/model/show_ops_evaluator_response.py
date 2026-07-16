# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowOpsEvaluatorResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluator_id': 'str',
        'name': 'str',
        'description': 'str',
        'evaluator_type': 'int',
        'box_type': 'str',
        'builtin': 'bool',
        'latest_version': 'str',
        'current_version': 'EvaluationOpsCurrentVersion',
        'base_info': 'OpsEvaluatorBaseInfo'
    }

    attribute_map = {
        'evaluator_id': 'evaluator_id',
        'name': 'name',
        'description': 'description',
        'evaluator_type': 'evaluator_type',
        'box_type': 'box_type',
        'builtin': 'builtin',
        'latest_version': 'latest_version',
        'current_version': 'current_version',
        'base_info': 'base_info'
    }

    def __init__(self, evaluator_id=None, name=None, description=None, evaluator_type=None, box_type=None, builtin=None, latest_version=None, current_version=None, base_info=None):
        r"""ShowOpsEvaluatorResponse

        The model defined in huaweicloud sdk

        :param evaluator_id: **参数解释** 评估器的唯一标识符ID。 **取值范围** 符合通用唯一识别码(UUID)标准的字符串。 
        :type evaluator_id: str
        :param name: **参数解释** 评估器的显示名称。 **取值范围** 支持中英文、数字及常用特殊符号。 
        :type name: str
        :param description: **参数解释** 对评估器功能、逻辑或评测维度的详细描述。 **取值范围** 任意字符串。 
        :type description: str
        :param evaluator_type: **参数解释** 评估器的分类类型编码。 **取值范围** 对应的整型编码。 
        :type evaluator_type: int
        :param box_type: **参数解释** 评估器的可见性类型（盒子类型），决定了评估逻辑的透明度。 **取值范围** - White: 白盒评估。 - Black: 黑盒评估。 
        :type box_type: str
        :param builtin: **参数解释** 标识该评估器是否为系统内置预置。 **取值范围** - true: 系统内置。 - false: 用户自定义。 
        :type builtin: bool
        :param latest_version: **参数解释** 该评估器下最新发布的版本号。 **取值范围** 符合语义化版本格式的字符串（如 0.0.2）。 
        :type latest_version: str
        :param current_version: 
        :type current_version: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        :param base_info: 
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        
        super().__init__()

        self._evaluator_id = None
        self._name = None
        self._description = None
        self._evaluator_type = None
        self._box_type = None
        self._builtin = None
        self._latest_version = None
        self._current_version = None
        self._base_info = None
        self.discriminator = None

        if evaluator_id is not None:
            self.evaluator_id = evaluator_id
        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if evaluator_type is not None:
            self.evaluator_type = evaluator_type
        if box_type is not None:
            self.box_type = box_type
        if builtin is not None:
            self.builtin = builtin
        if latest_version is not None:
            self.latest_version = latest_version
        if current_version is not None:
            self.current_version = current_version
        if base_info is not None:
            self.base_info = base_info

    @property
    def evaluator_id(self):
        r"""Gets the evaluator_id of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的唯一标识符ID。 **取值范围** 符合通用唯一识别码(UUID)标准的字符串。 

        :return: The evaluator_id of this ShowOpsEvaluatorResponse.
        :rtype: str
        """
        return self._evaluator_id

    @evaluator_id.setter
    def evaluator_id(self, evaluator_id):
        r"""Sets the evaluator_id of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的唯一标识符ID。 **取值范围** 符合通用唯一识别码(UUID)标准的字符串。 

        :param evaluator_id: The evaluator_id of this ShowOpsEvaluatorResponse.
        :type evaluator_id: str
        """
        self._evaluator_id = evaluator_id

    @property
    def name(self):
        r"""Gets the name of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的显示名称。 **取值范围** 支持中英文、数字及常用特殊符号。 

        :return: The name of this ShowOpsEvaluatorResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的显示名称。 **取值范围** 支持中英文、数字及常用特殊符号。 

        :param name: The name of this ShowOpsEvaluatorResponse.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this ShowOpsEvaluatorResponse.

        **参数解释** 对评估器功能、逻辑或评测维度的详细描述。 **取值范围** 任意字符串。 

        :return: The description of this ShowOpsEvaluatorResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ShowOpsEvaluatorResponse.

        **参数解释** 对评估器功能、逻辑或评测维度的详细描述。 **取值范围** 任意字符串。 

        :param description: The description of this ShowOpsEvaluatorResponse.
        :type description: str
        """
        self._description = description

    @property
    def evaluator_type(self):
        r"""Gets the evaluator_type of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的分类类型编码。 **取值范围** 对应的整型编码。 

        :return: The evaluator_type of this ShowOpsEvaluatorResponse.
        :rtype: int
        """
        return self._evaluator_type

    @evaluator_type.setter
    def evaluator_type(self, evaluator_type):
        r"""Sets the evaluator_type of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的分类类型编码。 **取值范围** 对应的整型编码。 

        :param evaluator_type: The evaluator_type of this ShowOpsEvaluatorResponse.
        :type evaluator_type: int
        """
        self._evaluator_type = evaluator_type

    @property
    def box_type(self):
        r"""Gets the box_type of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的可见性类型（盒子类型），决定了评估逻辑的透明度。 **取值范围** - White: 白盒评估。 - Black: 黑盒评估。 

        :return: The box_type of this ShowOpsEvaluatorResponse.
        :rtype: str
        """
        return self._box_type

    @box_type.setter
    def box_type(self, box_type):
        r"""Sets the box_type of this ShowOpsEvaluatorResponse.

        **参数解释** 评估器的可见性类型（盒子类型），决定了评估逻辑的透明度。 **取值范围** - White: 白盒评估。 - Black: 黑盒评估。 

        :param box_type: The box_type of this ShowOpsEvaluatorResponse.
        :type box_type: str
        """
        self._box_type = box_type

    @property
    def builtin(self):
        r"""Gets the builtin of this ShowOpsEvaluatorResponse.

        **参数解释** 标识该评估器是否为系统内置预置。 **取值范围** - true: 系统内置。 - false: 用户自定义。 

        :return: The builtin of this ShowOpsEvaluatorResponse.
        :rtype: bool
        """
        return self._builtin

    @builtin.setter
    def builtin(self, builtin):
        r"""Sets the builtin of this ShowOpsEvaluatorResponse.

        **参数解释** 标识该评估器是否为系统内置预置。 **取值范围** - true: 系统内置。 - false: 用户自定义。 

        :param builtin: The builtin of this ShowOpsEvaluatorResponse.
        :type builtin: bool
        """
        self._builtin = builtin

    @property
    def latest_version(self):
        r"""Gets the latest_version of this ShowOpsEvaluatorResponse.

        **参数解释** 该评估器下最新发布的版本号。 **取值范围** 符合语义化版本格式的字符串（如 0.0.2）。 

        :return: The latest_version of this ShowOpsEvaluatorResponse.
        :rtype: str
        """
        return self._latest_version

    @latest_version.setter
    def latest_version(self, latest_version):
        r"""Sets the latest_version of this ShowOpsEvaluatorResponse.

        **参数解释** 该评估器下最新发布的版本号。 **取值范围** 符合语义化版本格式的字符串（如 0.0.2）。 

        :param latest_version: The latest_version of this ShowOpsEvaluatorResponse.
        :type latest_version: str
        """
        self._latest_version = latest_version

    @property
    def current_version(self):
        r"""Gets the current_version of this ShowOpsEvaluatorResponse.

        :return: The current_version of this ShowOpsEvaluatorResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        """
        return self._current_version

    @current_version.setter
    def current_version(self, current_version):
        r"""Sets the current_version of this ShowOpsEvaluatorResponse.

        :param current_version: The current_version of this ShowOpsEvaluatorResponse.
        :type current_version: :class:`huaweicloudsdkagentarts.v1.EvaluationOpsCurrentVersion`
        """
        self._current_version = current_version

    @property
    def base_info(self):
        r"""Gets the base_info of this ShowOpsEvaluatorResponse.

        :return: The base_info of this ShowOpsEvaluatorResponse.
        :rtype: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        return self._base_info

    @base_info.setter
    def base_info(self, base_info):
        r"""Sets the base_info of this ShowOpsEvaluatorResponse.

        :param base_info: The base_info of this ShowOpsEvaluatorResponse.
        :type base_info: :class:`huaweicloudsdkagentarts.v1.OpsEvaluatorBaseInfo`
        """
        self._base_info = base_info

    def to_dict(self):
        import warnings
        warnings.warn("ShowOpsEvaluatorResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowOpsEvaluatorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
