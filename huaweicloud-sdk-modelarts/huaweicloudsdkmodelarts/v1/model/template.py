# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Template:

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
        'version': 'str',
        'inputs': 'dict(str, object)'
    }

    attribute_map = {
        'name': 'name',
        'version': 'version',
        'inputs': 'inputs'
    }

    def __init__(self, name=None, version=None, inputs=None):
        r"""Template

        The model defined in huaweicloud sdk

        :param name: **参数解释**：待安装插件模板名称，如log-agent。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type name: str
        :param version: **参数解释**：待安装、升级插件的版本号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。
        :type version: str
        :param inputs: **参数解释**：插件模板安装参数（各插件不同），升级插件时需要填写全量安装参数，未填写参数将使用插件模板中的默认值，当前插件安装参数可通过查询插件实例接口获取。 **约束限制**：不涉及。
        :type inputs: dict(str, object)
        """
        
        

        self._name = None
        self._version = None
        self._inputs = None
        self.discriminator = None

        self.name = name
        if version is not None:
            self.version = version
        if inputs is not None:
            self.inputs = inputs

    @property
    def name(self):
        r"""Gets the name of this Template.

        **参数解释**：待安装插件模板名称，如log-agent。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The name of this Template.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Template.

        **参数解释**：待安装插件模板名称，如log-agent。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param name: The name of this Template.
        :type name: str
        """
        self._name = name

    @property
    def version(self):
        r"""Gets the version of this Template.

        **参数解释**：待安装、升级插件的版本号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :return: The version of this Template.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Template.

        **参数解释**：待安装、升级插件的版本号。 **约束限制**：不涉及。 **取值范围**：不涉及。 **默认取值**：不涉及。

        :param version: The version of this Template.
        :type version: str
        """
        self._version = version

    @property
    def inputs(self):
        r"""Gets the inputs of this Template.

        **参数解释**：插件模板安装参数（各插件不同），升级插件时需要填写全量安装参数，未填写参数将使用插件模板中的默认值，当前插件安装参数可通过查询插件实例接口获取。 **约束限制**：不涉及。

        :return: The inputs of this Template.
        :rtype: dict(str, object)
        """
        return self._inputs

    @inputs.setter
    def inputs(self, inputs):
        r"""Sets the inputs of this Template.

        **参数解释**：插件模板安装参数（各插件不同），升级插件时需要填写全量安装参数，未填写参数将使用插件模板中的默认值，当前插件安装参数可通过查询插件实例接口获取。 **约束限制**：不涉及。

        :param inputs: The inputs of this Template.
        :type inputs: dict(str, object)
        """
        self._inputs = inputs

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
        if not isinstance(other, Template):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
