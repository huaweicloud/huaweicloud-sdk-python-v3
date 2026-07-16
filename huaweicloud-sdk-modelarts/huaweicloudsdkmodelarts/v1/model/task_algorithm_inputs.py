# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskAlgorithmInputs:

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
        'local_dir': 'str',
        'remote': 'InputDataInfo'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'local_dir': 'local_dir',
        'remote': 'remote'
    }

    def __init__(self, name=None, description=None, local_dir=None, remote=None):
        r"""TaskAlgorithmInputs

        The model defined in huaweicloud sdk

        :param name: **参数解释**：数据输入通道名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param description: **参数解释**：数据输入通道描述信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type description: str
        :param local_dir: **参数解释**：数据输入通道映射的容器本地路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type local_dir: str
        :param remote: 
        :type remote: :class:`huaweicloudsdkmodelarts.v1.InputDataInfo`
        """
        
        

        self._name = None
        self._description = None
        self._local_dir = None
        self._remote = None
        self.discriminator = None

        self.name = name
        if description is not None:
            self.description = description
        if local_dir is not None:
            self.local_dir = local_dir
        self.remote = remote

    @property
    def name(self):
        r"""Gets the name of this TaskAlgorithmInputs.

        **参数解释**：数据输入通道名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this TaskAlgorithmInputs.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this TaskAlgorithmInputs.

        **参数解释**：数据输入通道名称。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this TaskAlgorithmInputs.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this TaskAlgorithmInputs.

        **参数解释**：数据输入通道描述信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The description of this TaskAlgorithmInputs.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this TaskAlgorithmInputs.

        **参数解释**：数据输入通道描述信息。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param description: The description of this TaskAlgorithmInputs.
        :type description: str
        """
        self._description = description

    @property
    def local_dir(self):
        r"""Gets the local_dir of this TaskAlgorithmInputs.

        **参数解释**：数据输入通道映射的容器本地路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The local_dir of this TaskAlgorithmInputs.
        :rtype: str
        """
        return self._local_dir

    @local_dir.setter
    def local_dir(self, local_dir):
        r"""Sets the local_dir of this TaskAlgorithmInputs.

        **参数解释**：数据输入通道映射的容器本地路径。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param local_dir: The local_dir of this TaskAlgorithmInputs.
        :type local_dir: str
        """
        self._local_dir = local_dir

    @property
    def remote(self):
        r"""Gets the remote of this TaskAlgorithmInputs.

        :return: The remote of this TaskAlgorithmInputs.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.InputDataInfo`
        """
        return self._remote

    @remote.setter
    def remote(self, remote):
        r"""Sets the remote of this TaskAlgorithmInputs.

        :param remote: The remote of this TaskAlgorithmInputs.
        :type remote: :class:`huaweicloudsdkmodelarts.v1.InputDataInfo`
        """
        self._remote = remote

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
        if not isinstance(other, TaskAlgorithmInputs):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
