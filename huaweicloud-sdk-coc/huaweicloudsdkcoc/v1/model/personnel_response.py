# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PersonnelResponse:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_root_user': 'bool',
        'dingtalk_webhook': 'str',
        'email': 'str',
        'id': 'str',
        'mobile': 'str',
        'name': 'str',
        'wecom_webhook': 'str',
        'description': 'str',
        'dingtalk_private_key': 'str',
        'msg_subscription_status': 'int',
        'weichat_subscription_status': 'int',
        'ding_talk_subscription_status': 'int',
        'email_subscription_status': 'int',
        'call_notify_subscription_status': 'int',
        'source_type': 'str',
        'source_status': 'str',
        'lark_webhook': 'str',
        'lark_subscription_status': 'int'
    }

    attribute_map = {
        'is_root_user': 'is_root_user',
        'dingtalk_webhook': 'dingtalk_webhook',
        'email': 'email',
        'id': 'id',
        'mobile': 'mobile',
        'name': 'name',
        'wecom_webhook': 'wecom_webhook',
        'description': 'description',
        'dingtalk_private_key': 'dingtalk_private_key',
        'msg_subscription_status': 'msg_subscription_status',
        'weichat_subscription_status': 'weichat_subscription_status',
        'ding_talk_subscription_status': 'ding_talk_subscription_status',
        'email_subscription_status': 'email_subscription_status',
        'call_notify_subscription_status': 'call_notify_subscription_status',
        'source_type': 'source_type',
        'source_status': 'source_status',
        'lark_webhook': 'lark_webhook',
        'lark_subscription_status': 'lark_subscription_status'
    }

    def __init__(self, is_root_user=None, dingtalk_webhook=None, email=None, id=None, mobile=None, name=None, wecom_webhook=None, description=None, dingtalk_private_key=None, msg_subscription_status=None, weichat_subscription_status=None, ding_talk_subscription_status=None, email_subscription_status=None, call_notify_subscription_status=None, source_type=None, source_status=None, lark_webhook=None, lark_subscription_status=None):
        r"""PersonnelResponse

        The model defined in huaweicloud sdk

        :param is_root_user: 该用户是否是根用户
        :type is_root_user: bool
        :param dingtalk_webhook: 钉钉回调
        :type dingtalk_webhook: str
        :param email: 邮箱
        :type email: str
        :param id: 用户id
        :type id: str
        :param mobile: 手机
        :type mobile: str
        :param name: 用户名
        :type name: str
        :param wecom_webhook: 企业微信回调
        :type wecom_webhook: str
        :param description: 描述
        :type description: str
        :param dingtalk_private_key: 钉钉秘钥
        :type dingtalk_private_key: str
        :param msg_subscription_status: 短信订阅状态
        :type msg_subscription_status: int
        :param weichat_subscription_status: 企业微信订阅状态
        :type weichat_subscription_status: int
        :param ding_talk_subscription_status: 钉钉订阅状态
        :type ding_talk_subscription_status: int
        :param email_subscription_status: 邮箱订阅
        :type email_subscription_status: int
        :param call_notify_subscription_status: 语音订阅状态
        :type call_notify_subscription_status: int
        :param source_type: 账号来源类型
        :type source_type: str
        :param source_status: 账号状态
        :type source_status: str
        :param lark_webhook: 飞书回调
        :type lark_webhook: str
        :param lark_subscription_status: 飞书订阅状态
        :type lark_subscription_status: int
        """
        
        

        self._is_root_user = None
        self._dingtalk_webhook = None
        self._email = None
        self._id = None
        self._mobile = None
        self._name = None
        self._wecom_webhook = None
        self._description = None
        self._dingtalk_private_key = None
        self._msg_subscription_status = None
        self._weichat_subscription_status = None
        self._ding_talk_subscription_status = None
        self._email_subscription_status = None
        self._call_notify_subscription_status = None
        self._source_type = None
        self._source_status = None
        self._lark_webhook = None
        self._lark_subscription_status = None
        self.discriminator = None

        if is_root_user is not None:
            self.is_root_user = is_root_user
        if dingtalk_webhook is not None:
            self.dingtalk_webhook = dingtalk_webhook
        if email is not None:
            self.email = email
        if id is not None:
            self.id = id
        if mobile is not None:
            self.mobile = mobile
        if name is not None:
            self.name = name
        if wecom_webhook is not None:
            self.wecom_webhook = wecom_webhook
        if description is not None:
            self.description = description
        if dingtalk_private_key is not None:
            self.dingtalk_private_key = dingtalk_private_key
        if msg_subscription_status is not None:
            self.msg_subscription_status = msg_subscription_status
        if weichat_subscription_status is not None:
            self.weichat_subscription_status = weichat_subscription_status
        if ding_talk_subscription_status is not None:
            self.ding_talk_subscription_status = ding_talk_subscription_status
        if email_subscription_status is not None:
            self.email_subscription_status = email_subscription_status
        if call_notify_subscription_status is not None:
            self.call_notify_subscription_status = call_notify_subscription_status
        if source_type is not None:
            self.source_type = source_type
        if source_status is not None:
            self.source_status = source_status
        if lark_webhook is not None:
            self.lark_webhook = lark_webhook
        if lark_subscription_status is not None:
            self.lark_subscription_status = lark_subscription_status

    @property
    def is_root_user(self):
        r"""Gets the is_root_user of this PersonnelResponse.

        该用户是否是根用户

        :return: The is_root_user of this PersonnelResponse.
        :rtype: bool
        """
        return self._is_root_user

    @is_root_user.setter
    def is_root_user(self, is_root_user):
        r"""Sets the is_root_user of this PersonnelResponse.

        该用户是否是根用户

        :param is_root_user: The is_root_user of this PersonnelResponse.
        :type is_root_user: bool
        """
        self._is_root_user = is_root_user

    @property
    def dingtalk_webhook(self):
        r"""Gets the dingtalk_webhook of this PersonnelResponse.

        钉钉回调

        :return: The dingtalk_webhook of this PersonnelResponse.
        :rtype: str
        """
        return self._dingtalk_webhook

    @dingtalk_webhook.setter
    def dingtalk_webhook(self, dingtalk_webhook):
        r"""Sets the dingtalk_webhook of this PersonnelResponse.

        钉钉回调

        :param dingtalk_webhook: The dingtalk_webhook of this PersonnelResponse.
        :type dingtalk_webhook: str
        """
        self._dingtalk_webhook = dingtalk_webhook

    @property
    def email(self):
        r"""Gets the email of this PersonnelResponse.

        邮箱

        :return: The email of this PersonnelResponse.
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        r"""Sets the email of this PersonnelResponse.

        邮箱

        :param email: The email of this PersonnelResponse.
        :type email: str
        """
        self._email = email

    @property
    def id(self):
        r"""Gets the id of this PersonnelResponse.

        用户id

        :return: The id of this PersonnelResponse.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this PersonnelResponse.

        用户id

        :param id: The id of this PersonnelResponse.
        :type id: str
        """
        self._id = id

    @property
    def mobile(self):
        r"""Gets the mobile of this PersonnelResponse.

        手机

        :return: The mobile of this PersonnelResponse.
        :rtype: str
        """
        return self._mobile

    @mobile.setter
    def mobile(self, mobile):
        r"""Sets the mobile of this PersonnelResponse.

        手机

        :param mobile: The mobile of this PersonnelResponse.
        :type mobile: str
        """
        self._mobile = mobile

    @property
    def name(self):
        r"""Gets the name of this PersonnelResponse.

        用户名

        :return: The name of this PersonnelResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PersonnelResponse.

        用户名

        :param name: The name of this PersonnelResponse.
        :type name: str
        """
        self._name = name

    @property
    def wecom_webhook(self):
        r"""Gets the wecom_webhook of this PersonnelResponse.

        企业微信回调

        :return: The wecom_webhook of this PersonnelResponse.
        :rtype: str
        """
        return self._wecom_webhook

    @wecom_webhook.setter
    def wecom_webhook(self, wecom_webhook):
        r"""Sets the wecom_webhook of this PersonnelResponse.

        企业微信回调

        :param wecom_webhook: The wecom_webhook of this PersonnelResponse.
        :type wecom_webhook: str
        """
        self._wecom_webhook = wecom_webhook

    @property
    def description(self):
        r"""Gets the description of this PersonnelResponse.

        描述

        :return: The description of this PersonnelResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this PersonnelResponse.

        描述

        :param description: The description of this PersonnelResponse.
        :type description: str
        """
        self._description = description

    @property
    def dingtalk_private_key(self):
        r"""Gets the dingtalk_private_key of this PersonnelResponse.

        钉钉秘钥

        :return: The dingtalk_private_key of this PersonnelResponse.
        :rtype: str
        """
        return self._dingtalk_private_key

    @dingtalk_private_key.setter
    def dingtalk_private_key(self, dingtalk_private_key):
        r"""Sets the dingtalk_private_key of this PersonnelResponse.

        钉钉秘钥

        :param dingtalk_private_key: The dingtalk_private_key of this PersonnelResponse.
        :type dingtalk_private_key: str
        """
        self._dingtalk_private_key = dingtalk_private_key

    @property
    def msg_subscription_status(self):
        r"""Gets the msg_subscription_status of this PersonnelResponse.

        短信订阅状态

        :return: The msg_subscription_status of this PersonnelResponse.
        :rtype: int
        """
        return self._msg_subscription_status

    @msg_subscription_status.setter
    def msg_subscription_status(self, msg_subscription_status):
        r"""Sets the msg_subscription_status of this PersonnelResponse.

        短信订阅状态

        :param msg_subscription_status: The msg_subscription_status of this PersonnelResponse.
        :type msg_subscription_status: int
        """
        self._msg_subscription_status = msg_subscription_status

    @property
    def weichat_subscription_status(self):
        r"""Gets the weichat_subscription_status of this PersonnelResponse.

        企业微信订阅状态

        :return: The weichat_subscription_status of this PersonnelResponse.
        :rtype: int
        """
        return self._weichat_subscription_status

    @weichat_subscription_status.setter
    def weichat_subscription_status(self, weichat_subscription_status):
        r"""Sets the weichat_subscription_status of this PersonnelResponse.

        企业微信订阅状态

        :param weichat_subscription_status: The weichat_subscription_status of this PersonnelResponse.
        :type weichat_subscription_status: int
        """
        self._weichat_subscription_status = weichat_subscription_status

    @property
    def ding_talk_subscription_status(self):
        r"""Gets the ding_talk_subscription_status of this PersonnelResponse.

        钉钉订阅状态

        :return: The ding_talk_subscription_status of this PersonnelResponse.
        :rtype: int
        """
        return self._ding_talk_subscription_status

    @ding_talk_subscription_status.setter
    def ding_talk_subscription_status(self, ding_talk_subscription_status):
        r"""Sets the ding_talk_subscription_status of this PersonnelResponse.

        钉钉订阅状态

        :param ding_talk_subscription_status: The ding_talk_subscription_status of this PersonnelResponse.
        :type ding_talk_subscription_status: int
        """
        self._ding_talk_subscription_status = ding_talk_subscription_status

    @property
    def email_subscription_status(self):
        r"""Gets the email_subscription_status of this PersonnelResponse.

        邮箱订阅

        :return: The email_subscription_status of this PersonnelResponse.
        :rtype: int
        """
        return self._email_subscription_status

    @email_subscription_status.setter
    def email_subscription_status(self, email_subscription_status):
        r"""Sets the email_subscription_status of this PersonnelResponse.

        邮箱订阅

        :param email_subscription_status: The email_subscription_status of this PersonnelResponse.
        :type email_subscription_status: int
        """
        self._email_subscription_status = email_subscription_status

    @property
    def call_notify_subscription_status(self):
        r"""Gets the call_notify_subscription_status of this PersonnelResponse.

        语音订阅状态

        :return: The call_notify_subscription_status of this PersonnelResponse.
        :rtype: int
        """
        return self._call_notify_subscription_status

    @call_notify_subscription_status.setter
    def call_notify_subscription_status(self, call_notify_subscription_status):
        r"""Sets the call_notify_subscription_status of this PersonnelResponse.

        语音订阅状态

        :param call_notify_subscription_status: The call_notify_subscription_status of this PersonnelResponse.
        :type call_notify_subscription_status: int
        """
        self._call_notify_subscription_status = call_notify_subscription_status

    @property
    def source_type(self):
        r"""Gets the source_type of this PersonnelResponse.

        账号来源类型

        :return: The source_type of this PersonnelResponse.
        :rtype: str
        """
        return self._source_type

    @source_type.setter
    def source_type(self, source_type):
        r"""Sets the source_type of this PersonnelResponse.

        账号来源类型

        :param source_type: The source_type of this PersonnelResponse.
        :type source_type: str
        """
        self._source_type = source_type

    @property
    def source_status(self):
        r"""Gets the source_status of this PersonnelResponse.

        账号状态

        :return: The source_status of this PersonnelResponse.
        :rtype: str
        """
        return self._source_status

    @source_status.setter
    def source_status(self, source_status):
        r"""Sets the source_status of this PersonnelResponse.

        账号状态

        :param source_status: The source_status of this PersonnelResponse.
        :type source_status: str
        """
        self._source_status = source_status

    @property
    def lark_webhook(self):
        r"""Gets the lark_webhook of this PersonnelResponse.

        飞书回调

        :return: The lark_webhook of this PersonnelResponse.
        :rtype: str
        """
        return self._lark_webhook

    @lark_webhook.setter
    def lark_webhook(self, lark_webhook):
        r"""Sets the lark_webhook of this PersonnelResponse.

        飞书回调

        :param lark_webhook: The lark_webhook of this PersonnelResponse.
        :type lark_webhook: str
        """
        self._lark_webhook = lark_webhook

    @property
    def lark_subscription_status(self):
        r"""Gets the lark_subscription_status of this PersonnelResponse.

        飞书订阅状态

        :return: The lark_subscription_status of this PersonnelResponse.
        :rtype: int
        """
        return self._lark_subscription_status

    @lark_subscription_status.setter
    def lark_subscription_status(self, lark_subscription_status):
        r"""Sets the lark_subscription_status of this PersonnelResponse.

        飞书订阅状态

        :param lark_subscription_status: The lark_subscription_status of this PersonnelResponse.
        :type lark_subscription_status: int
        """
        self._lark_subscription_status = lark_subscription_status

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
        if not isinstance(other, PersonnelResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
