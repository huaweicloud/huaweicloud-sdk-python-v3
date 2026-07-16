# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EvaluationOpsUserInfo:

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
        'user_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'user_id': 'user_id'
    }

    def __init__(self, name=None, user_id=None):
        r"""EvaluationOpsUserInfo

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 用户在系统中的显示名称。 **取值范围：** 中英文、数字。
        :type name: str
        :param user_id: **参数解释：** 用户的系统内唯一标识符（ID）。 **取值范围：** 符合系统用户规则的字符串。
        :type user_id: str
        """
        
        

        self._name = None
        self._user_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if user_id is not None:
            self.user_id = user_id

    @property
    def name(self):
        r"""Gets the name of this EvaluationOpsUserInfo.

        **参数解释：** 用户在系统中的显示名称。 **取值范围：** 中英文、数字。

        :return: The name of this EvaluationOpsUserInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EvaluationOpsUserInfo.

        **参数解释：** 用户在系统中的显示名称。 **取值范围：** 中英文、数字。

        :param name: The name of this EvaluationOpsUserInfo.
        :type name: str
        """
        self._name = name

    @property
    def user_id(self):
        r"""Gets the user_id of this EvaluationOpsUserInfo.

        **参数解释：** 用户的系统内唯一标识符（ID）。 **取值范围：** 符合系统用户规则的字符串。

        :return: The user_id of this EvaluationOpsUserInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this EvaluationOpsUserInfo.

        **参数解释：** 用户的系统内唯一标识符（ID）。 **取值范围：** 符合系统用户规则的字符串。

        :param user_id: The user_id of this EvaluationOpsUserInfo.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, EvaluationOpsUserInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
