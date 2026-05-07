# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateDaemonsetRequestBodyResourceInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'mode': 'str',
        'cpu_limit': 'str',
        'mem_limit': 'str'
    }

    attribute_map = {
        'mode': 'mode',
        'cpu_limit': 'cpu_limit',
        'mem_limit': 'mem_limit'
    }

    def __init__(self, mode=None, cpu_limit=None, mem_limit=None):
        r"""CreateDaemonsetRequestBodyResourceInfo

        The model defined in huaweicloud sdk

        :param mode: **参数解释**： 资源限制类型：默认规则or自定义or自适应 **约束限制**： 不涉及 **取值范围**： - default：默认类型。 - customized：用户自定义类型。 - adaptive：自适应类型。  **默认取值**： 不涉及 
        :type mode: str
        :param cpu_limit: **参数解释**: cpu最大值 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 
        :type cpu_limit: str
        :param mem_limit: **参数解释**: 内存最大值 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 
        :type mem_limit: str
        """
        
        

        self._mode = None
        self._cpu_limit = None
        self._mem_limit = None
        self.discriminator = None

        if mode is not None:
            self.mode = mode
        if cpu_limit is not None:
            self.cpu_limit = cpu_limit
        if mem_limit is not None:
            self.mem_limit = mem_limit

    @property
    def mode(self):
        r"""Gets the mode of this CreateDaemonsetRequestBodyResourceInfo.

        **参数解释**： 资源限制类型：默认规则or自定义or自适应 **约束限制**： 不涉及 **取值范围**： - default：默认类型。 - customized：用户自定义类型。 - adaptive：自适应类型。  **默认取值**： 不涉及 

        :return: The mode of this CreateDaemonsetRequestBodyResourceInfo.
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        r"""Sets the mode of this CreateDaemonsetRequestBodyResourceInfo.

        **参数解释**： 资源限制类型：默认规则or自定义or自适应 **约束限制**： 不涉及 **取值范围**： - default：默认类型。 - customized：用户自定义类型。 - adaptive：自适应类型。  **默认取值**： 不涉及 

        :param mode: The mode of this CreateDaemonsetRequestBodyResourceInfo.
        :type mode: str
        """
        self._mode = mode

    @property
    def cpu_limit(self):
        r"""Gets the cpu_limit of this CreateDaemonsetRequestBodyResourceInfo.

        **参数解释**: cpu最大值 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :return: The cpu_limit of this CreateDaemonsetRequestBodyResourceInfo.
        :rtype: str
        """
        return self._cpu_limit

    @cpu_limit.setter
    def cpu_limit(self, cpu_limit):
        r"""Sets the cpu_limit of this CreateDaemonsetRequestBodyResourceInfo.

        **参数解释**: cpu最大值 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :param cpu_limit: The cpu_limit of this CreateDaemonsetRequestBodyResourceInfo.
        :type cpu_limit: str
        """
        self._cpu_limit = cpu_limit

    @property
    def mem_limit(self):
        r"""Gets the mem_limit of this CreateDaemonsetRequestBodyResourceInfo.

        **参数解释**: 内存最大值 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :return: The mem_limit of this CreateDaemonsetRequestBodyResourceInfo.
        :rtype: str
        """
        return self._mem_limit

    @mem_limit.setter
    def mem_limit(self, mem_limit):
        r"""Sets the mem_limit of this CreateDaemonsetRequestBodyResourceInfo.

        **参数解释**: 内存最大值 **约束限制**: 不涉及 **取值范围**: 字符长度0-32位 **默认取值**: 不涉及 

        :param mem_limit: The mem_limit of this CreateDaemonsetRequestBodyResourceInfo.
        :type mem_limit: str
        """
        self._mem_limit = mem_limit

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
        if not isinstance(other, CreateDaemonsetRequestBodyResourceInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
