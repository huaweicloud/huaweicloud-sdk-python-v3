# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InterpreterInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'login_account': 'str',
        'user_id': 'str',
        'call_number': 'str',
        'name': 'str',
        'interpreter_id': 'str',
        'interpreter_type': 'str',
        'ai_digital_info': 'InterpreterAiDigitalInfo'
    }

    attribute_map = {
        'login_account': 'loginAccount',
        'user_id': 'userID',
        'call_number': 'callNumber',
        'name': 'name',
        'interpreter_id': 'interpreterId',
        'interpreter_type': 'interpreterType',
        'ai_digital_info': 'aiDigitalInfo'
    }

    def __init__(self, login_account=None, user_id=None, call_number=None, name=None, interpreter_id=None, interpreter_type=None, ai_digital_info=None):
        r"""InterpreterInfo

        The model defined in huaweicloud sdk

        :param login_account: 用户登录账号，可以是账号、手机、邮箱其中一个,loginAccount和userID必须二选一。
        :type login_account: str
        :param user_id: 用户的userUUID。
        :type user_id: str
        :param call_number: 呼叫号码。
        :type call_number: str
        :param name: 用户名。
        :type name: str
        :param interpreter_id: 传译员序号，AI传译组下传译员唯一标识。
        :type interpreter_id: str
        :param interpreter_type: 传译员类型，MANUAL：人工传译，AI：AI传译。默认MANUAL。
        :type interpreter_type: str
        :param ai_digital_info: 
        :type ai_digital_info: :class:`huaweicloudsdkmeeting.v1.InterpreterAiDigitalInfo`
        """
        
        

        self._login_account = None
        self._user_id = None
        self._call_number = None
        self._name = None
        self._interpreter_id = None
        self._interpreter_type = None
        self._ai_digital_info = None
        self.discriminator = None

        self.login_account = login_account
        if user_id is not None:
            self.user_id = user_id
        if call_number is not None:
            self.call_number = call_number
        if name is not None:
            self.name = name
        if interpreter_id is not None:
            self.interpreter_id = interpreter_id
        if interpreter_type is not None:
            self.interpreter_type = interpreter_type
        if ai_digital_info is not None:
            self.ai_digital_info = ai_digital_info

    @property
    def login_account(self):
        r"""Gets the login_account of this InterpreterInfo.

        用户登录账号，可以是账号、手机、邮箱其中一个,loginAccount和userID必须二选一。

        :return: The login_account of this InterpreterInfo.
        :rtype: str
        """
        return self._login_account

    @login_account.setter
    def login_account(self, login_account):
        r"""Sets the login_account of this InterpreterInfo.

        用户登录账号，可以是账号、手机、邮箱其中一个,loginAccount和userID必须二选一。

        :param login_account: The login_account of this InterpreterInfo.
        :type login_account: str
        """
        self._login_account = login_account

    @property
    def user_id(self):
        r"""Gets the user_id of this InterpreterInfo.

        用户的userUUID。

        :return: The user_id of this InterpreterInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this InterpreterInfo.

        用户的userUUID。

        :param user_id: The user_id of this InterpreterInfo.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def call_number(self):
        r"""Gets the call_number of this InterpreterInfo.

        呼叫号码。

        :return: The call_number of this InterpreterInfo.
        :rtype: str
        """
        return self._call_number

    @call_number.setter
    def call_number(self, call_number):
        r"""Sets the call_number of this InterpreterInfo.

        呼叫号码。

        :param call_number: The call_number of this InterpreterInfo.
        :type call_number: str
        """
        self._call_number = call_number

    @property
    def name(self):
        r"""Gets the name of this InterpreterInfo.

        用户名。

        :return: The name of this InterpreterInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this InterpreterInfo.

        用户名。

        :param name: The name of this InterpreterInfo.
        :type name: str
        """
        self._name = name

    @property
    def interpreter_id(self):
        r"""Gets the interpreter_id of this InterpreterInfo.

        传译员序号，AI传译组下传译员唯一标识。

        :return: The interpreter_id of this InterpreterInfo.
        :rtype: str
        """
        return self._interpreter_id

    @interpreter_id.setter
    def interpreter_id(self, interpreter_id):
        r"""Sets the interpreter_id of this InterpreterInfo.

        传译员序号，AI传译组下传译员唯一标识。

        :param interpreter_id: The interpreter_id of this InterpreterInfo.
        :type interpreter_id: str
        """
        self._interpreter_id = interpreter_id

    @property
    def interpreter_type(self):
        r"""Gets the interpreter_type of this InterpreterInfo.

        传译员类型，MANUAL：人工传译，AI：AI传译。默认MANUAL。

        :return: The interpreter_type of this InterpreterInfo.
        :rtype: str
        """
        return self._interpreter_type

    @interpreter_type.setter
    def interpreter_type(self, interpreter_type):
        r"""Sets the interpreter_type of this InterpreterInfo.

        传译员类型，MANUAL：人工传译，AI：AI传译。默认MANUAL。

        :param interpreter_type: The interpreter_type of this InterpreterInfo.
        :type interpreter_type: str
        """
        self._interpreter_type = interpreter_type

    @property
    def ai_digital_info(self):
        r"""Gets the ai_digital_info of this InterpreterInfo.

        :return: The ai_digital_info of this InterpreterInfo.
        :rtype: :class:`huaweicloudsdkmeeting.v1.InterpreterAiDigitalInfo`
        """
        return self._ai_digital_info

    @ai_digital_info.setter
    def ai_digital_info(self, ai_digital_info):
        r"""Sets the ai_digital_info of this InterpreterInfo.

        :param ai_digital_info: The ai_digital_info of this InterpreterInfo.
        :type ai_digital_info: :class:`huaweicloudsdkmeeting.v1.InterpreterAiDigitalInfo`
        """
        self._ai_digital_info = ai_digital_info

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
        if not isinstance(other, InterpreterInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
