# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GrowCheckResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        '_pass': 'bool',
        'reason': 'str',
        'required': 'bool',
        'desc': 'str',
        'type': 'str'
    }

    attribute_map = {
        '_pass': 'pass',
        'reason': 'reason',
        'required': 'required',
        'desc': 'desc',
        'type': 'type'
    }

    def __init__(self, _pass=None, reason=None, required=None, desc=None, type=None):
        r"""GrowCheckResult

        The model defined in huaweicloud sdk

        :param _pass: **参数解释**： 检查是否通过，检查通过项默认不展示。 **取值范围**： true/false
        :type _pass: bool
        :param reason: **参数解释**： 检查不通过的原因描述。 **取值范围**： 不涉及。
        :type reason: str
        :param required: **参数解释**： 是否必须检查项。 **取值范围**： - true：必须，校验不通过时不允许扩容，继续扩容也会失败 - false：非必须，校验不通过时允许扩容，仅做提示告知风险
        :type required: bool
        :param desc: **参数解释**： 描述信息。 **取值范围**： 不涉及。
        :type desc: str
        :param type: **参数解释**： 分类。 **取值范围**： 配额、权限、版本、状态
        :type type: str
        """
        
        

        self.__pass = None
        self._reason = None
        self._required = None
        self._desc = None
        self._type = None
        self.discriminator = None

        if _pass is not None:
            self._pass = _pass
        if reason is not None:
            self.reason = reason
        if required is not None:
            self.required = required
        if desc is not None:
            self.desc = desc
        if type is not None:
            self.type = type

    @property
    def _pass(self):
        r"""Gets the _pass of this GrowCheckResult.

        **参数解释**： 检查是否通过，检查通过项默认不展示。 **取值范围**： true/false

        :return: The _pass of this GrowCheckResult.
        :rtype: bool
        """
        return self.__pass

    @_pass.setter
    def _pass(self, _pass):
        r"""Sets the _pass of this GrowCheckResult.

        **参数解释**： 检查是否通过，检查通过项默认不展示。 **取值范围**： true/false

        :param _pass: The _pass of this GrowCheckResult.
        :type _pass: bool
        """
        self.__pass = _pass

    @property
    def reason(self):
        r"""Gets the reason of this GrowCheckResult.

        **参数解释**： 检查不通过的原因描述。 **取值范围**： 不涉及。

        :return: The reason of this GrowCheckResult.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        r"""Sets the reason of this GrowCheckResult.

        **参数解释**： 检查不通过的原因描述。 **取值范围**： 不涉及。

        :param reason: The reason of this GrowCheckResult.
        :type reason: str
        """
        self._reason = reason

    @property
    def required(self):
        r"""Gets the required of this GrowCheckResult.

        **参数解释**： 是否必须检查项。 **取值范围**： - true：必须，校验不通过时不允许扩容，继续扩容也会失败 - false：非必须，校验不通过时允许扩容，仅做提示告知风险

        :return: The required of this GrowCheckResult.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this GrowCheckResult.

        **参数解释**： 是否必须检查项。 **取值范围**： - true：必须，校验不通过时不允许扩容，继续扩容也会失败 - false：非必须，校验不通过时允许扩容，仅做提示告知风险

        :param required: The required of this GrowCheckResult.
        :type required: bool
        """
        self._required = required

    @property
    def desc(self):
        r"""Gets the desc of this GrowCheckResult.

        **参数解释**： 描述信息。 **取值范围**： 不涉及。

        :return: The desc of this GrowCheckResult.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this GrowCheckResult.

        **参数解释**： 描述信息。 **取值范围**： 不涉及。

        :param desc: The desc of this GrowCheckResult.
        :type desc: str
        """
        self._desc = desc

    @property
    def type(self):
        r"""Gets the type of this GrowCheckResult.

        **参数解释**： 分类。 **取值范围**： 配额、权限、版本、状态

        :return: The type of this GrowCheckResult.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this GrowCheckResult.

        **参数解释**： 分类。 **取值范围**： 配额、权限、版本、状态

        :param type: The type of this GrowCheckResult.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, GrowCheckResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
