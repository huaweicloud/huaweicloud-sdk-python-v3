# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateTokenReqDTO:

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
        'need_gen_new_token': 'bool',
        'need_account_info': 'bool'
    }

    attribute_map = {
        'token': 'token',
        'need_gen_new_token': 'needGenNewToken',
        'need_account_info': 'needAccountInfo'
    }

    def __init__(self, token=None, need_gen_new_token=None, need_account_info=None):
        """ValidateTokenReqDTO

        The model defined in huaweicloud sdk

        :param token: Access Token。
        :type token: str
        :param need_gen_new_token: 是否生成新的Token。 * true：生成新的token值 * false：不生成新的token值 
        :type need_gen_new_token: bool
        :param need_account_info: 是否需要返回用户帐号信息（帐号、用户名称等信息）。
        :type need_account_info: bool
        """
        
        

        self._token = None
        self._need_gen_new_token = None
        self._need_account_info = None
        self.discriminator = None

        self.token = token
        self.need_gen_new_token = need_gen_new_token
        if need_account_info is not None:
            self.need_account_info = need_account_info

    @property
    def token(self):
        """Gets the token of this ValidateTokenReqDTO.

        Access Token。

        :return: The token of this ValidateTokenReqDTO.
        :rtype: str
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ValidateTokenReqDTO.

        Access Token。

        :param token: The token of this ValidateTokenReqDTO.
        :type token: str
        """
        self._token = token

    @property
    def need_gen_new_token(self):
        """Gets the need_gen_new_token of this ValidateTokenReqDTO.

        是否生成新的Token。 * true：生成新的token值 * false：不生成新的token值 

        :return: The need_gen_new_token of this ValidateTokenReqDTO.
        :rtype: bool
        """
        return self._need_gen_new_token

    @need_gen_new_token.setter
    def need_gen_new_token(self, need_gen_new_token):
        """Sets the need_gen_new_token of this ValidateTokenReqDTO.

        是否生成新的Token。 * true：生成新的token值 * false：不生成新的token值 

        :param need_gen_new_token: The need_gen_new_token of this ValidateTokenReqDTO.
        :type need_gen_new_token: bool
        """
        self._need_gen_new_token = need_gen_new_token

    @property
    def need_account_info(self):
        """Gets the need_account_info of this ValidateTokenReqDTO.

        是否需要返回用户帐号信息（帐号、用户名称等信息）。

        :return: The need_account_info of this ValidateTokenReqDTO.
        :rtype: bool
        """
        return self._need_account_info

    @need_account_info.setter
    def need_account_info(self, need_account_info):
        """Sets the need_account_info of this ValidateTokenReqDTO.

        是否需要返回用户帐号信息（帐号、用户名称等信息）。

        :param need_account_info: The need_account_info of this ValidateTokenReqDTO.
        :type need_account_info: bool
        """
        self._need_account_info = need_account_info

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
        if not isinstance(other, ValidateTokenReqDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
