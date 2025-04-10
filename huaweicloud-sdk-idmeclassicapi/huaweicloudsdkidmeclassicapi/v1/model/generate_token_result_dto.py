# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GenerateTokenResultDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'token': 'str',
        'user_id': 'str',
        'user_name': 'str',
        'app_id': 'str'
    }

    attribute_map = {
        'token': 'token',
        'user_id': 'user_id',
        'user_name': 'user_name',
        'app_id': 'app_id'
    }

    def __init__(self, token=None, user_id=None, user_name=None, app_id=None):
        r"""GenerateTokenResultDto

        The model defined in huaweicloud sdk

        :param token: **参数解释**：  认证token。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type token: str
        :param user_id: **参数解释**：  用户ID。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type user_id: str
        :param user_name: **参数解释**：  用户名。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type user_name: str
        :param app_id: **参数解释**：  应用ID。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type app_id: str
        """
        
        

        self._token = None
        self._user_id = None
        self._user_name = None
        self._app_id = None
        self.discriminator = None

        if token is not None:
            self.token = token
        if user_id is not None:
            self.user_id = user_id
        if user_name is not None:
            self.user_name = user_name
        if app_id is not None:
            self.app_id = app_id

    @property
    def token(self):
        r"""Gets the token of this GenerateTokenResultDto.

        **参数解释**：  认证token。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The token of this GenerateTokenResultDto.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        r"""Sets the token of this GenerateTokenResultDto.

        **参数解释**：  认证token。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param token: The token of this GenerateTokenResultDto.
        :type token: str
        """
        self._token = token

    @property
    def user_id(self):
        r"""Gets the user_id of this GenerateTokenResultDto.

        **参数解释**：  用户ID。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The user_id of this GenerateTokenResultDto.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this GenerateTokenResultDto.

        **参数解释**：  用户ID。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param user_id: The user_id of this GenerateTokenResultDto.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def user_name(self):
        r"""Gets the user_name of this GenerateTokenResultDto.

        **参数解释**：  用户名。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The user_name of this GenerateTokenResultDto.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this GenerateTokenResultDto.

        **参数解释**：  用户名。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param user_name: The user_name of this GenerateTokenResultDto.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def app_id(self):
        r"""Gets the app_id of this GenerateTokenResultDto.

        **参数解释**：  应用ID。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The app_id of this GenerateTokenResultDto.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        r"""Sets the app_id of this GenerateTokenResultDto.

        **参数解释**：  应用ID。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param app_id: The app_id of this GenerateTokenResultDto.
        :type app_id: str
        """
        self._app_id = app_id

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
        if not isinstance(other, GenerateTokenResultDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
