# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskRulesetInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'language': 'str',
        'template_name': 'str',
        'type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'template_id': 'template_id',
        'language': 'language',
        'template_name': 'template_name',
        'type': 'type',
        'status': 'status'
    }

    def __init__(self, template_id=None, language=None, template_name=None, type=None, status=None):
        r"""TaskRulesetInfo

        The model defined in huaweicloud sdk

        :param template_id: **参数解释：** 规则集ID。 **取值范围:** 长度为[1~32]个字符。
        :type template_id: str
        :param language: **参数解释：** 规则集语言。 **取值范围:** 自定义语言或者系统内置语言，当前支持的系统内置语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES
        :type language: str
        :param template_name: **参数解释：** 规则集名称。 **取值范围:** 任意中英文，数字，点，连字符-及下划线_。长度为[1~128]个字符。
        :type template_name: str
        :param type: **参数解释：** 规则集选取状态。 **取值范围:** - selected：已选。 - optional：可选，指未开启的语言在当前项目下的默认规则集。
        :type type: str
        :param status: **参数解释：** 规则集属性。 **取值范围:** - 0：用户自定义规则集。 - 1：系统规则集。
        :type status: str
        """
        
        

        self._template_id = None
        self._language = None
        self._template_name = None
        self._type = None
        self._status = None
        self.discriminator = None

        if template_id is not None:
            self.template_id = template_id
        if language is not None:
            self.language = language
        if template_name is not None:
            self.template_name = template_name
        if type is not None:
            self.type = type
        if status is not None:
            self.status = status

    @property
    def template_id(self):
        r"""Gets the template_id of this TaskRulesetInfo.

        **参数解释：** 规则集ID。 **取值范围:** 长度为[1~32]个字符。

        :return: The template_id of this TaskRulesetInfo.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this TaskRulesetInfo.

        **参数解释：** 规则集ID。 **取值范围:** 长度为[1~32]个字符。

        :param template_id: The template_id of this TaskRulesetInfo.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def language(self):
        r"""Gets the language of this TaskRulesetInfo.

        **参数解释：** 规则集语言。 **取值范围:** 自定义语言或者系统内置语言，当前支持的系统内置语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :return: The language of this TaskRulesetInfo.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        r"""Sets the language of this TaskRulesetInfo.

        **参数解释：** 规则集语言。 **取值范围:** 自定义语言或者系统内置语言，当前支持的系统内置语言有： - ARKTS - C# - CANGJIE - C++ - CSS - GO - HTML - JAVA - JAVASCRIPT - KOTLIN - LUA - PHP - PYTHON - RUST - SCALA - SHELL - SQL - TERRAFORM - TYPESCRIPT - AZURERESOURCEMANAGER - DOCKER - KUBERNETES

        :param language: The language of this TaskRulesetInfo.
        :type language: str
        """
        self._language = language

    @property
    def template_name(self):
        r"""Gets the template_name of this TaskRulesetInfo.

        **参数解释：** 规则集名称。 **取值范围:** 任意中英文，数字，点，连字符-及下划线_。长度为[1~128]个字符。

        :return: The template_name of this TaskRulesetInfo.
        :rtype: str
        """
        return self._template_name

    @template_name.setter
    def template_name(self, template_name):
        r"""Sets the template_name of this TaskRulesetInfo.

        **参数解释：** 规则集名称。 **取值范围:** 任意中英文，数字，点，连字符-及下划线_。长度为[1~128]个字符。

        :param template_name: The template_name of this TaskRulesetInfo.
        :type template_name: str
        """
        self._template_name = template_name

    @property
    def type(self):
        r"""Gets the type of this TaskRulesetInfo.

        **参数解释：** 规则集选取状态。 **取值范围:** - selected：已选。 - optional：可选，指未开启的语言在当前项目下的默认规则集。

        :return: The type of this TaskRulesetInfo.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this TaskRulesetInfo.

        **参数解释：** 规则集选取状态。 **取值范围:** - selected：已选。 - optional：可选，指未开启的语言在当前项目下的默认规则集。

        :param type: The type of this TaskRulesetInfo.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this TaskRulesetInfo.

        **参数解释：** 规则集属性。 **取值范围:** - 0：用户自定义规则集。 - 1：系统规则集。

        :return: The status of this TaskRulesetInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this TaskRulesetInfo.

        **参数解释：** 规则集属性。 **取值范围:** - 0：用户自定义规则集。 - 1：系统规则集。

        :param status: The status of this TaskRulesetInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, TaskRulesetInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
