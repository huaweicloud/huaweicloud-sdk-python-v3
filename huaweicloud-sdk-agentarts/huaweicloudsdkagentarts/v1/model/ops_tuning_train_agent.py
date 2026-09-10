# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OpsTuningTrainAgent:

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
        'version': 'str',
        'model_provider_id': 'str',
        'model_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'version': 'version',
        'model_provider_id': 'model_provider_id',
        'model_id': 'model_id'
    }

    def __init__(self, id=None, version=None, model_provider_id=None, model_id=None):
        r"""OpsTuningTrainAgent

        The model defined in huaweicloud sdk

        :param id: **参数解释：** 智能体ID，训练实例关联的智能体。  **取值范围：** 有效标识符字符串。
        :type id: str
        :param version: **参数解释：** 智能体版本。  **取值范围：** 版本号字符串。
        :type version: str
        :param model_provider_id: **参数解释：** 训练模型的供应商ID，标识模型来源的服务商。  **取值范围：** 供应商标识字符串。
        :type model_provider_id: str
        :param model_id: **参数解释：** 训练模型ID，标识正在被训练的具体模型实例。  **取值范围：** 模型标识字符串。
        :type model_id: str
        """
        
        

        self._id = None
        self._version = None
        self._model_provider_id = None
        self._model_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if version is not None:
            self.version = version
        if model_provider_id is not None:
            self.model_provider_id = model_provider_id
        if model_id is not None:
            self.model_id = model_id

    @property
    def id(self):
        r"""Gets the id of this OpsTuningTrainAgent.

        **参数解释：** 智能体ID，训练实例关联的智能体。  **取值范围：** 有效标识符字符串。

        :return: The id of this OpsTuningTrainAgent.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this OpsTuningTrainAgent.

        **参数解释：** 智能体ID，训练实例关联的智能体。  **取值范围：** 有效标识符字符串。

        :param id: The id of this OpsTuningTrainAgent.
        :type id: str
        """
        self._id = id

    @property
    def version(self):
        r"""Gets the version of this OpsTuningTrainAgent.

        **参数解释：** 智能体版本。  **取值范围：** 版本号字符串。

        :return: The version of this OpsTuningTrainAgent.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this OpsTuningTrainAgent.

        **参数解释：** 智能体版本。  **取值范围：** 版本号字符串。

        :param version: The version of this OpsTuningTrainAgent.
        :type version: str
        """
        self._version = version

    @property
    def model_provider_id(self):
        r"""Gets the model_provider_id of this OpsTuningTrainAgent.

        **参数解释：** 训练模型的供应商ID，标识模型来源的服务商。  **取值范围：** 供应商标识字符串。

        :return: The model_provider_id of this OpsTuningTrainAgent.
        :rtype: str
        """
        return self._model_provider_id

    @model_provider_id.setter
    def model_provider_id(self, model_provider_id):
        r"""Sets the model_provider_id of this OpsTuningTrainAgent.

        **参数解释：** 训练模型的供应商ID，标识模型来源的服务商。  **取值范围：** 供应商标识字符串。

        :param model_provider_id: The model_provider_id of this OpsTuningTrainAgent.
        :type model_provider_id: str
        """
        self._model_provider_id = model_provider_id

    @property
    def model_id(self):
        r"""Gets the model_id of this OpsTuningTrainAgent.

        **参数解释：** 训练模型ID，标识正在被训练的具体模型实例。  **取值范围：** 模型标识字符串。

        :return: The model_id of this OpsTuningTrainAgent.
        :rtype: str
        """
        return self._model_id

    @model_id.setter
    def model_id(self, model_id):
        r"""Sets the model_id of this OpsTuningTrainAgent.

        **参数解释：** 训练模型ID，标识正在被训练的具体模型实例。  **取值范围：** 模型标识字符串。

        :param model_id: The model_id of this OpsTuningTrainAgent.
        :type model_id: str
        """
        self._model_id = model_id

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
        if not isinstance(other, OpsTuningTrainAgent):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
