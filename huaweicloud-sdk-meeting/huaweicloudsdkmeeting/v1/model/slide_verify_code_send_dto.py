# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SlideVerifyCodeSendDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'user': 'str',
        'client_type': 'int',
        'check_type': 'int'
    }

    attribute_map = {
        'user': 'user',
        'client_type': 'clientType',
        'check_type': 'checkType'
    }

    def __init__(self, user=None, client_type=None, check_type=None):
        """SlideVerifyCodeSendDTO

        The model defined in huaweicloud sdk

        :param user: 用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 
        :type user: str
        :param client_type: 登录客户端类型。 * 0：Web客户端类型 * 5：cloudlink pc * 6：cloudlink mobile 
        :type client_type: int
        :param check_type: 校验类型。默认值：0。 * 0：登录 * 1：忘记密码 
        :type check_type: int
        """
        
        

        self._user = None
        self._client_type = None
        self._check_type = None
        self.discriminator = None

        self.user = user
        self.client_type = client_type
        if check_type is not None:
            self.check_type = check_type

    @property
    def user(self):
        """Gets the user of this SlideVerifyCodeSendDTO.

        用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 

        :return: The user of this SlideVerifyCodeSendDTO.
        :rtype: str
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this SlideVerifyCodeSendDTO.

        用户身份信息（手机号码或邮箱帐号或用户真实帐号）。 

        :param user: The user of this SlideVerifyCodeSendDTO.
        :type user: str
        """
        self._user = user

    @property
    def client_type(self):
        """Gets the client_type of this SlideVerifyCodeSendDTO.

        登录客户端类型。 * 0：Web客户端类型 * 5：cloudlink pc * 6：cloudlink mobile 

        :return: The client_type of this SlideVerifyCodeSendDTO.
        :rtype: int
        """
        return self._client_type

    @client_type.setter
    def client_type(self, client_type):
        """Sets the client_type of this SlideVerifyCodeSendDTO.

        登录客户端类型。 * 0：Web客户端类型 * 5：cloudlink pc * 6：cloudlink mobile 

        :param client_type: The client_type of this SlideVerifyCodeSendDTO.
        :type client_type: int
        """
        self._client_type = client_type

    @property
    def check_type(self):
        """Gets the check_type of this SlideVerifyCodeSendDTO.

        校验类型。默认值：0。 * 0：登录 * 1：忘记密码 

        :return: The check_type of this SlideVerifyCodeSendDTO.
        :rtype: int
        """
        return self._check_type

    @check_type.setter
    def check_type(self, check_type):
        """Sets the check_type of this SlideVerifyCodeSendDTO.

        校验类型。默认值：0。 * 0：登录 * 1：忘记密码 

        :param check_type: The check_type of this SlideVerifyCodeSendDTO.
        :type check_type: int
        """
        self._check_type = check_type

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
        if not isinstance(other, SlideVerifyCodeSendDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
