# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateRepoNameResultDto:

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
        'project_id': 'str',
        'group_id': 'int',
        'result': 'bool',
        'error_message': 'str'
    }

    attribute_map = {
        'name': 'name',
        'project_id': 'project_id',
        'group_id': 'group_id',
        'result': 'result',
        'error_message': 'error_message'
    }

    def __init__(self, name=None, project_id=None, group_id=None, result=None, error_message=None):
        r"""ValidateRepoNameResultDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 仓库名。 **约束限制：** - 必填。 - 大小写字母、数字、下划线开头，可包含大小写字母、数字、中划线、下划线、英文句点，但不能以.git、.atom或.结尾 - 代码总路径长度（代码组名称和仓库名称总长度）不超过256字符 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type name: str
        :param project_id: **参数解释：** 项目ID。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。
        :type project_id: str
        :param group_id: **参数解释：** 代码组ID，若需要检查的仓库名称在项目根目录下可不传此参数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 1-2147483647
        :type group_id: int
        :param result: **参数解释：** 是否校验通过 **取值范围：** - true，校验通过。 - false，校验未通过。 **约束限制：** 不涉及。
        :type result: bool
        :param error_message: **参数解释：** 异常信息 **约束限制：** 不涉及。
        :type error_message: str
        """
        
        

        self._name = None
        self._project_id = None
        self._group_id = None
        self._result = None
        self._error_message = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if project_id is not None:
            self.project_id = project_id
        if group_id is not None:
            self.group_id = group_id
        if result is not None:
            self.result = result
        if error_message is not None:
            self.error_message = error_message

    @property
    def name(self):
        r"""Gets the name of this ValidateRepoNameResultDto.

        **参数解释：** 仓库名。 **约束限制：** - 必填。 - 大小写字母、数字、下划线开头，可包含大小写字母、数字、中划线、下划线、英文句点，但不能以.git、.atom或.结尾 - 代码总路径长度（代码组名称和仓库名称总长度）不超过256字符 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The name of this ValidateRepoNameResultDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ValidateRepoNameResultDto.

        **参数解释：** 仓库名。 **约束限制：** - 必填。 - 大小写字母、数字、下划线开头，可包含大小写字母、数字、中划线、下划线、英文句点，但不能以.git、.atom或.结尾 - 代码总路径长度（代码组名称和仓库名称总长度）不超过256字符 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param name: The name of this ValidateRepoNameResultDto.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this ValidateRepoNameResultDto.

        **参数解释：** 项目ID。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :return: The project_id of this ValidateRepoNameResultDto.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ValidateRepoNameResultDto.

        **参数解释：** 项目ID。 **约束限制：** 必填。 **取值范围：** 不涉及。 **默认取值：** 不涉及。

        :param project_id: The project_id of this ValidateRepoNameResultDto.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def group_id(self):
        r"""Gets the group_id of this ValidateRepoNameResultDto.

        **参数解释：** 代码组ID，若需要检查的仓库名称在项目根目录下可不传此参数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 1-2147483647

        :return: The group_id of this ValidateRepoNameResultDto.
        :rtype: int
        """
        return self._group_id

    @group_id.setter
    def group_id(self, group_id):
        r"""Sets the group_id of this ValidateRepoNameResultDto.

        **参数解释：** 代码组ID，若需要检查的仓库名称在项目根目录下可不传此参数。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值：** 1-2147483647

        :param group_id: The group_id of this ValidateRepoNameResultDto.
        :type group_id: int
        """
        self._group_id = group_id

    @property
    def result(self):
        r"""Gets the result of this ValidateRepoNameResultDto.

        **参数解释：** 是否校验通过 **取值范围：** - true，校验通过。 - false，校验未通过。 **约束限制：** 不涉及。

        :return: The result of this ValidateRepoNameResultDto.
        :rtype: bool
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ValidateRepoNameResultDto.

        **参数解释：** 是否校验通过 **取值范围：** - true，校验通过。 - false，校验未通过。 **约束限制：** 不涉及。

        :param result: The result of this ValidateRepoNameResultDto.
        :type result: bool
        """
        self._result = result

    @property
    def error_message(self):
        r"""Gets the error_message of this ValidateRepoNameResultDto.

        **参数解释：** 异常信息 **约束限制：** 不涉及。

        :return: The error_message of this ValidateRepoNameResultDto.
        :rtype: str
        """
        return self._error_message

    @error_message.setter
    def error_message(self, error_message):
        r"""Sets the error_message of this ValidateRepoNameResultDto.

        **参数解释：** 异常信息 **约束限制：** 不涉及。

        :param error_message: The error_message of this ValidateRepoNameResultDto.
        :type error_message: str
        """
        self._error_message = error_message

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
        if not isinstance(other, ValidateRepoNameResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
