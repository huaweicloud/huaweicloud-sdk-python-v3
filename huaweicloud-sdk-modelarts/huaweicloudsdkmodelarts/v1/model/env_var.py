# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnvVar:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'label': 'str',
        'des': 'str',
        'env_name': 'str',
        'env_type': 'str',
        'value': 'str',
        'modifiable': 'bool',
        'displayable': 'bool',
        'used_steps': 'list[str]'
    }

    attribute_map = {
        'label': 'label',
        'des': 'des',
        'env_name': 'env_name',
        'env_type': 'env_type',
        'value': 'value',
        'modifiable': 'modifiable',
        'displayable': 'displayable',
        'used_steps': 'used_steps'
    }

    def __init__(self, label=None, des=None, env_name=None, env_type=None, value=None, modifiable=None, displayable=None, used_steps=None):
        r"""EnvVar

        The model defined in huaweicloud sdk

        :param label: 标签
        :type label: str
        :param des: 描述信息
        :type des: str
        :param env_name: 环境变量名称
        :type env_name: str
        :param env_type: 环境变量类型
        :type env_type: str
        :param value: 环境变量值
        :type value: str
        :param modifiable: 环境变量是否可修改
        :type modifiable: bool
        :param displayable: 环境变量是否展示
        :type displayable: bool
        :param used_steps: 环境变量使用阶段
        :type used_steps: list[str]
        """
        
        

        self._label = None
        self._des = None
        self._env_name = None
        self._env_type = None
        self._value = None
        self._modifiable = None
        self._displayable = None
        self._used_steps = None
        self.discriminator = None

        if label is not None:
            self.label = label
        if des is not None:
            self.des = des
        if env_name is not None:
            self.env_name = env_name
        if env_type is not None:
            self.env_type = env_type
        if value is not None:
            self.value = value
        if modifiable is not None:
            self.modifiable = modifiable
        if displayable is not None:
            self.displayable = displayable
        if used_steps is not None:
            self.used_steps = used_steps

    @property
    def label(self):
        r"""Gets the label of this EnvVar.

        标签

        :return: The label of this EnvVar.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        r"""Sets the label of this EnvVar.

        标签

        :param label: The label of this EnvVar.
        :type label: str
        """
        self._label = label

    @property
    def des(self):
        r"""Gets the des of this EnvVar.

        描述信息

        :return: The des of this EnvVar.
        :rtype: str
        """
        return self._des

    @des.setter
    def des(self, des):
        r"""Sets the des of this EnvVar.

        描述信息

        :param des: The des of this EnvVar.
        :type des: str
        """
        self._des = des

    @property
    def env_name(self):
        r"""Gets the env_name of this EnvVar.

        环境变量名称

        :return: The env_name of this EnvVar.
        :rtype: str
        """
        return self._env_name

    @env_name.setter
    def env_name(self, env_name):
        r"""Sets the env_name of this EnvVar.

        环境变量名称

        :param env_name: The env_name of this EnvVar.
        :type env_name: str
        """
        self._env_name = env_name

    @property
    def env_type(self):
        r"""Gets the env_type of this EnvVar.

        环境变量类型

        :return: The env_type of this EnvVar.
        :rtype: str
        """
        return self._env_type

    @env_type.setter
    def env_type(self, env_type):
        r"""Sets the env_type of this EnvVar.

        环境变量类型

        :param env_type: The env_type of this EnvVar.
        :type env_type: str
        """
        self._env_type = env_type

    @property
    def value(self):
        r"""Gets the value of this EnvVar.

        环境变量值

        :return: The value of this EnvVar.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        r"""Sets the value of this EnvVar.

        环境变量值

        :param value: The value of this EnvVar.
        :type value: str
        """
        self._value = value

    @property
    def modifiable(self):
        r"""Gets the modifiable of this EnvVar.

        环境变量是否可修改

        :return: The modifiable of this EnvVar.
        :rtype: bool
        """
        return self._modifiable

    @modifiable.setter
    def modifiable(self, modifiable):
        r"""Sets the modifiable of this EnvVar.

        环境变量是否可修改

        :param modifiable: The modifiable of this EnvVar.
        :type modifiable: bool
        """
        self._modifiable = modifiable

    @property
    def displayable(self):
        r"""Gets the displayable of this EnvVar.

        环境变量是否展示

        :return: The displayable of this EnvVar.
        :rtype: bool
        """
        return self._displayable

    @displayable.setter
    def displayable(self, displayable):
        r"""Sets the displayable of this EnvVar.

        环境变量是否展示

        :param displayable: The displayable of this EnvVar.
        :type displayable: bool
        """
        self._displayable = displayable

    @property
    def used_steps(self):
        r"""Gets the used_steps of this EnvVar.

        环境变量使用阶段

        :return: The used_steps of this EnvVar.
        :rtype: list[str]
        """
        return self._used_steps

    @used_steps.setter
    def used_steps(self, used_steps):
        r"""Sets the used_steps of this EnvVar.

        环境变量使用阶段

        :param used_steps: The used_steps of this EnvVar.
        :type used_steps: list[str]
        """
        self._used_steps = used_steps

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
        if not isinstance(other, EnvVar):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
