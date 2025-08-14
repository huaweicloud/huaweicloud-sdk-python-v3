# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AuthorizationMail:

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
        'account': 'str',
        'account_auth_type': 'AccountTypeEnum',
        'account_auth_name': 'str',
        'app_group_id': 'str',
        'app_group_name': 'str',
        'mail_send_type': 'str',
        'mail_send_result': 'str',
        'error_msg': 'str',
        'send_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'account': 'account',
        'account_auth_type': 'account_auth_type',
        'account_auth_name': 'account_auth_name',
        'app_group_id': 'app_group_id',
        'app_group_name': 'app_group_name',
        'mail_send_type': 'mail_send_type',
        'mail_send_result': 'mail_send_result',
        'error_msg': 'error_msg',
        'send_at': 'send_at'
    }

    def __init__(self, id=None, account=None, account_auth_type=None, account_auth_name=None, app_group_id=None, app_group_name=None, mail_send_type=None, mail_send_result=None, error_msg=None, send_at=None):
        r"""AuthorizationMail

        The model defined in huaweicloud sdk

        :param id: 邮件记录id。
        :type id: str
        :param account: 用户(组)。
        :type account: str
        :param account_auth_type: 
        :type account_auth_type: :class:`huaweicloudsdkworkspaceapp.v1.AccountTypeEnum`
        :param account_auth_name: 授权对象名称。
        :type account_auth_name: str
        :param app_group_id: 应用组ID。
        :type app_group_id: str
        :param app_group_name: 应用组名称。
        :type app_group_name: str
        :param mail_send_type: 授权类型： - ADD_GROUP_AUTHORIZATION 添加组授权邮件 - DEL_GROUP_AUTHORIZATION 删除组授权邮件 - ADD_GROUP_AUTHORIZATION_SMS 添加组授权短信 - DEL_GROUP_AUTHORIZATION_SMS 删除组授权短信。
        :type mail_send_type: str
        :param mail_send_result: 发送结果。 - SUEECESS -发送成功 - FAIL -发送失败。
        :type mail_send_result: str
        :param error_msg: 报错信息。
        :type error_msg: str
        :param send_at: 发布时间。
        :type send_at: datetime
        """
        
        

        self._id = None
        self._account = None
        self._account_auth_type = None
        self._account_auth_name = None
        self._app_group_id = None
        self._app_group_name = None
        self._mail_send_type = None
        self._mail_send_result = None
        self._error_msg = None
        self._send_at = None
        self.discriminator = None

        self.id = id
        if account is not None:
            self.account = account
        if account_auth_type is not None:
            self.account_auth_type = account_auth_type
        if account_auth_name is not None:
            self.account_auth_name = account_auth_name
        if app_group_id is not None:
            self.app_group_id = app_group_id
        if app_group_name is not None:
            self.app_group_name = app_group_name
        if mail_send_type is not None:
            self.mail_send_type = mail_send_type
        if mail_send_result is not None:
            self.mail_send_result = mail_send_result
        if error_msg is not None:
            self.error_msg = error_msg
        if send_at is not None:
            self.send_at = send_at

    @property
    def id(self):
        r"""Gets the id of this AuthorizationMail.

        邮件记录id。

        :return: The id of this AuthorizationMail.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AuthorizationMail.

        邮件记录id。

        :param id: The id of this AuthorizationMail.
        :type id: str
        """
        self._id = id

    @property
    def account(self):
        r"""Gets the account of this AuthorizationMail.

        用户(组)。

        :return: The account of this AuthorizationMail.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this AuthorizationMail.

        用户(组)。

        :param account: The account of this AuthorizationMail.
        :type account: str
        """
        self._account = account

    @property
    def account_auth_type(self):
        r"""Gets the account_auth_type of this AuthorizationMail.

        :return: The account_auth_type of this AuthorizationMail.
        :rtype: :class:`huaweicloudsdkworkspaceapp.v1.AccountTypeEnum`
        """
        return self._account_auth_type

    @account_auth_type.setter
    def account_auth_type(self, account_auth_type):
        r"""Sets the account_auth_type of this AuthorizationMail.

        :param account_auth_type: The account_auth_type of this AuthorizationMail.
        :type account_auth_type: :class:`huaweicloudsdkworkspaceapp.v1.AccountTypeEnum`
        """
        self._account_auth_type = account_auth_type

    @property
    def account_auth_name(self):
        r"""Gets the account_auth_name of this AuthorizationMail.

        授权对象名称。

        :return: The account_auth_name of this AuthorizationMail.
        :rtype: str
        """
        return self._account_auth_name

    @account_auth_name.setter
    def account_auth_name(self, account_auth_name):
        r"""Sets the account_auth_name of this AuthorizationMail.

        授权对象名称。

        :param account_auth_name: The account_auth_name of this AuthorizationMail.
        :type account_auth_name: str
        """
        self._account_auth_name = account_auth_name

    @property
    def app_group_id(self):
        r"""Gets the app_group_id of this AuthorizationMail.

        应用组ID。

        :return: The app_group_id of this AuthorizationMail.
        :rtype: str
        """
        return self._app_group_id

    @app_group_id.setter
    def app_group_id(self, app_group_id):
        r"""Sets the app_group_id of this AuthorizationMail.

        应用组ID。

        :param app_group_id: The app_group_id of this AuthorizationMail.
        :type app_group_id: str
        """
        self._app_group_id = app_group_id

    @property
    def app_group_name(self):
        r"""Gets the app_group_name of this AuthorizationMail.

        应用组名称。

        :return: The app_group_name of this AuthorizationMail.
        :rtype: str
        """
        return self._app_group_name

    @app_group_name.setter
    def app_group_name(self, app_group_name):
        r"""Sets the app_group_name of this AuthorizationMail.

        应用组名称。

        :param app_group_name: The app_group_name of this AuthorizationMail.
        :type app_group_name: str
        """
        self._app_group_name = app_group_name

    @property
    def mail_send_type(self):
        r"""Gets the mail_send_type of this AuthorizationMail.

        授权类型： - ADD_GROUP_AUTHORIZATION 添加组授权邮件 - DEL_GROUP_AUTHORIZATION 删除组授权邮件 - ADD_GROUP_AUTHORIZATION_SMS 添加组授权短信 - DEL_GROUP_AUTHORIZATION_SMS 删除组授权短信。

        :return: The mail_send_type of this AuthorizationMail.
        :rtype: str
        """
        return self._mail_send_type

    @mail_send_type.setter
    def mail_send_type(self, mail_send_type):
        r"""Sets the mail_send_type of this AuthorizationMail.

        授权类型： - ADD_GROUP_AUTHORIZATION 添加组授权邮件 - DEL_GROUP_AUTHORIZATION 删除组授权邮件 - ADD_GROUP_AUTHORIZATION_SMS 添加组授权短信 - DEL_GROUP_AUTHORIZATION_SMS 删除组授权短信。

        :param mail_send_type: The mail_send_type of this AuthorizationMail.
        :type mail_send_type: str
        """
        self._mail_send_type = mail_send_type

    @property
    def mail_send_result(self):
        r"""Gets the mail_send_result of this AuthorizationMail.

        发送结果。 - SUEECESS -发送成功 - FAIL -发送失败。

        :return: The mail_send_result of this AuthorizationMail.
        :rtype: str
        """
        return self._mail_send_result

    @mail_send_result.setter
    def mail_send_result(self, mail_send_result):
        r"""Sets the mail_send_result of this AuthorizationMail.

        发送结果。 - SUEECESS -发送成功 - FAIL -发送失败。

        :param mail_send_result: The mail_send_result of this AuthorizationMail.
        :type mail_send_result: str
        """
        self._mail_send_result = mail_send_result

    @property
    def error_msg(self):
        r"""Gets the error_msg of this AuthorizationMail.

        报错信息。

        :return: The error_msg of this AuthorizationMail.
        :rtype: str
        """
        return self._error_msg

    @error_msg.setter
    def error_msg(self, error_msg):
        r"""Sets the error_msg of this AuthorizationMail.

        报错信息。

        :param error_msg: The error_msg of this AuthorizationMail.
        :type error_msg: str
        """
        self._error_msg = error_msg

    @property
    def send_at(self):
        r"""Gets the send_at of this AuthorizationMail.

        发布时间。

        :return: The send_at of this AuthorizationMail.
        :rtype: datetime
        """
        return self._send_at

    @send_at.setter
    def send_at(self, send_at):
        r"""Sets the send_at of this AuthorizationMail.

        发布时间。

        :param send_at: The send_at of this AuthorizationMail.
        :type send_at: datetime
        """
        self._send_at = send_at

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
        if not isinstance(other, AuthorizationMail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
