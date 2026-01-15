# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AiOpsRiskObject:

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
        'name': 'str',
        'desc': 'str',
        'level': 'str',
        'result': 'str',
        'suggestion': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'desc': 'desc',
        'level': 'level',
        'result': 'result',
        'suggestion': 'suggestion'
    }

    def __init__(self, id=None, name=None, desc=None, level=None, result=None, suggestion=None):
        r"""AiOpsRiskObject

        The model defined in huaweicloud sdk

        :param id: **参数解释**： 检测项ID **取值范围**： 不涉及
        :type id: str
        :param name: **参数解释**： 检测项名称 **取值范围**： 不涉及
        :type name: str
        :param desc: **参数解释**： 检测项说明 **取值范围**： 不涉及
        :type desc: str
        :param level: **参数解释**： 检测结果风险等级 **取值范围**： 不涉及
        :type level: str
        :param result: **参数解释**： 检测结果 **取值范围**： 不涉及
        :type result: str
        :param suggestion: **参数解释**： 检测建议 **取值范围**： 不涉及
        :type suggestion: str
        """
        
        

        self._id = None
        self._name = None
        self._desc = None
        self._level = None
        self._result = None
        self._suggestion = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if desc is not None:
            self.desc = desc
        if level is not None:
            self.level = level
        if result is not None:
            self.result = result
        if suggestion is not None:
            self.suggestion = suggestion

    @property
    def id(self):
        r"""Gets the id of this AiOpsRiskObject.

        **参数解释**： 检测项ID **取值范围**： 不涉及

        :return: The id of this AiOpsRiskObject.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AiOpsRiskObject.

        **参数解释**： 检测项ID **取值范围**： 不涉及

        :param id: The id of this AiOpsRiskObject.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AiOpsRiskObject.

        **参数解释**： 检测项名称 **取值范围**： 不涉及

        :return: The name of this AiOpsRiskObject.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AiOpsRiskObject.

        **参数解释**： 检测项名称 **取值范围**： 不涉及

        :param name: The name of this AiOpsRiskObject.
        :type name: str
        """
        self._name = name

    @property
    def desc(self):
        r"""Gets the desc of this AiOpsRiskObject.

        **参数解释**： 检测项说明 **取值范围**： 不涉及

        :return: The desc of this AiOpsRiskObject.
        :rtype: str
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this AiOpsRiskObject.

        **参数解释**： 检测项说明 **取值范围**： 不涉及

        :param desc: The desc of this AiOpsRiskObject.
        :type desc: str
        """
        self._desc = desc

    @property
    def level(self):
        r"""Gets the level of this AiOpsRiskObject.

        **参数解释**： 检测结果风险等级 **取值范围**： 不涉及

        :return: The level of this AiOpsRiskObject.
        :rtype: str
        """
        return self._level

    @level.setter
    def level(self, level):
        r"""Sets the level of this AiOpsRiskObject.

        **参数解释**： 检测结果风险等级 **取值范围**： 不涉及

        :param level: The level of this AiOpsRiskObject.
        :type level: str
        """
        self._level = level

    @property
    def result(self):
        r"""Gets the result of this AiOpsRiskObject.

        **参数解释**： 检测结果 **取值范围**： 不涉及

        :return: The result of this AiOpsRiskObject.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this AiOpsRiskObject.

        **参数解释**： 检测结果 **取值范围**： 不涉及

        :param result: The result of this AiOpsRiskObject.
        :type result: str
        """
        self._result = result

    @property
    def suggestion(self):
        r"""Gets the suggestion of this AiOpsRiskObject.

        **参数解释**： 检测建议 **取值范围**： 不涉及

        :return: The suggestion of this AiOpsRiskObject.
        :rtype: str
        """
        return self._suggestion

    @suggestion.setter
    def suggestion(self, suggestion):
        r"""Sets the suggestion of this AiOpsRiskObject.

        **参数解释**： 检测建议 **取值范围**： 不涉及

        :param suggestion: The suggestion of this AiOpsRiskObject.
        :type suggestion: str
        """
        self._suggestion = suggestion

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
        if not isinstance(other, AiOpsRiskObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
