# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskDetailsRequest:

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
        'instance_id': 'str',
        'job_id': 'str',
        'job_name': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'job_id': 'job_id',
        'job_name': 'job_name'
    }

    def __init__(self, x_language=None, instance_id=None, job_id=None, job_name=None):
        r"""ShowTaskDetailsRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param instance_id: **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param job_id: **参数解释**：  任务ID。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type job_id: str
        :param job_name: **参数解释**：  任务名称。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type job_name: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._job_id = None
        self._job_name = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.job_id = job_id
        self.job_name = job_name

    @property
    def x_language(self):
        r"""Gets the x_language of this ShowTaskDetailsRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this ShowTaskDetailsRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ShowTaskDetailsRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this ShowTaskDetailsRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ShowTaskDetailsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this ShowTaskDetailsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ShowTaskDetailsRequest.

        **参数解释**：  实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in07，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this ShowTaskDetailsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def job_id(self):
        r"""Gets the job_id of this ShowTaskDetailsRequest.

        **参数解释**：  任务ID。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The job_id of this ShowTaskDetailsRequest.
        :rtype: str
        """
        return self._job_id

    @job_id.setter
    def job_id(self, job_id):
        r"""Sets the job_id of this ShowTaskDetailsRequest.

        **参数解释**：  任务ID。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param job_id: The job_id of this ShowTaskDetailsRequest.
        :type job_id: str
        """
        self._job_id = job_id

    @property
    def job_name(self):
        r"""Gets the job_name of this ShowTaskDetailsRequest.

        **参数解释**：  任务名称。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The job_name of this ShowTaskDetailsRequest.
        :rtype: str
        """
        return self._job_name

    @job_name.setter
    def job_name(self, job_name):
        r"""Sets the job_name of this ShowTaskDetailsRequest.

        **参数解释**：  任务名称。  **约束限制**：   不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param job_name: The job_name of this ShowTaskDetailsRequest.
        :type job_name: str
        """
        self._job_name = job_name

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
        if not isinstance(other, ShowTaskDetailsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
