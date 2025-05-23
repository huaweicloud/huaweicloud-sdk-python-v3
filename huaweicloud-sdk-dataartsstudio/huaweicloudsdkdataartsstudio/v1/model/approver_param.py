# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ApproverParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_name': 'str',
        'approver_name': 'str',
        'user_id': 'str',
        'email': 'str',
        'phone_number': 'str',
        'email_notify': 'bool',
        'sms_notify': 'bool'
    }

    attribute_map = {
        'app_name': 'app_name',
        'approver_name': 'approver_name',
        'user_id': 'user_id',
        'email': 'email',
        'phone_number': 'phone_number',
        'email_notify': 'email_notify',
        'sms_notify': 'sms_notify'
    }

    def __init__(self, app_name=None, approver_name=None, user_id=None, email=None, phone_number=None, email_notify=None, sms_notify=None):
        r"""ApproverParam

        The model defined in huaweicloud sdk

        :param app_name: 调用审核系统的应用名称，开发人员自己定。
        :type app_name: str
        :param approver_name: 审批人姓名。
        :type approver_name: str
        :param user_id: 审批人ID。
        :type user_id: str
        :param email: 邮箱地址。
        :type email: str
        :param phone_number: 电话号码。
        :type phone_number: str
        :param email_notify: 邮件通知。
        :type email_notify: bool
        :param sms_notify: 短信通知。
        :type sms_notify: bool
        """
        
        

        self._app_name = None
        self._approver_name = None
        self._user_id = None
        self._email = None
        self._phone_number = None
        self._email_notify = None
        self._sms_notify = None
        self.discriminator = None

        if app_name is not None:
            self.app_name = app_name
        self.approver_name = approver_name
        self.user_id = user_id
        if email is not None:
            self.email = email
        if phone_number is not None:
            self.phone_number = phone_number
        if email_notify is not None:
            self.email_notify = email_notify
        if sms_notify is not None:
            self.sms_notify = sms_notify

    @property
    def app_name(self):
        r"""Gets the app_name of this ApproverParam.

        调用审核系统的应用名称，开发人员自己定。

        :return: The app_name of this ApproverParam.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ApproverParam.

        调用审核系统的应用名称，开发人员自己定。

        :param app_name: The app_name of this ApproverParam.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def approver_name(self):
        r"""Gets the approver_name of this ApproverParam.

        审批人姓名。

        :return: The approver_name of this ApproverParam.
        :rtype: str
        """
        return self._approver_name

    @approver_name.setter
    def approver_name(self, approver_name):
        r"""Sets the approver_name of this ApproverParam.

        审批人姓名。

        :param approver_name: The approver_name of this ApproverParam.
        :type approver_name: str
        """
        self._approver_name = approver_name

    @property
    def user_id(self):
        r"""Gets the user_id of this ApproverParam.

        审批人ID。

        :return: The user_id of this ApproverParam.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this ApproverParam.

        审批人ID。

        :param user_id: The user_id of this ApproverParam.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def email(self):
        r"""Gets the email of this ApproverParam.

        邮箱地址。

        :return: The email of this ApproverParam.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this ApproverParam.

        邮箱地址。

        :param email: The email of this ApproverParam.
        :type email: str
        """
        self._email = email

    @property
    def phone_number(self):
        r"""Gets the phone_number of this ApproverParam.

        电话号码。

        :return: The phone_number of this ApproverParam.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        r"""Sets the phone_number of this ApproverParam.

        电话号码。

        :param phone_number: The phone_number of this ApproverParam.
        :type phone_number: str
        """
        self._phone_number = phone_number

    @property
    def email_notify(self):
        r"""Gets the email_notify of this ApproverParam.

        邮件通知。

        :return: The email_notify of this ApproverParam.
        :rtype: bool
        """
        return self._email_notify

    @email_notify.setter
    def email_notify(self, email_notify):
        r"""Sets the email_notify of this ApproverParam.

        邮件通知。

        :param email_notify: The email_notify of this ApproverParam.
        :type email_notify: bool
        """
        self._email_notify = email_notify

    @property
    def sms_notify(self):
        r"""Gets the sms_notify of this ApproverParam.

        短信通知。

        :return: The sms_notify of this ApproverParam.
        :rtype: bool
        """
        return self._sms_notify

    @sms_notify.setter
    def sms_notify(self, sms_notify):
        r"""Sets the sms_notify of this ApproverParam.

        短信通知。

        :param sms_notify: The sms_notify of this ApproverParam.
        :type sms_notify: bool
        """
        self._sms_notify = sms_notify

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
        if not isinstance(other, ApproverParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
