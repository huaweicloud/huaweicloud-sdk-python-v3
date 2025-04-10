# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OnlineAttendeeRecordInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'participant_id': 'str',
        'name': 'str',
        'call_number': 'str',
        'role': 'int',
        'third_account': 'str',
        'account': 'str',
        'user_id': 'str'
    }

    attribute_map = {
        'participant_id': 'participant_id',
        'name': 'name',
        'call_number': 'call_number',
        'role': 'role',
        'third_account': 'third_account',
        'account': 'account',
        'user_id': 'user_id'
    }

    def __init__(self, participant_id=None, name=None, call_number=None, role=None, third_account=None, account=None, user_id=None):
        r"""OnlineAttendeeRecordInfo

        The model defined in huaweicloud sdk

        :param participant_id: 与会者标识
        :type participant_id: str
        :param name: 与会者名称
        :type name: str
        :param call_number: 呼叫号码
        :type call_number: str
        :param role: 会议中的角色，枚举值如下： 1：会议主席 0：普通与会者
        :type role: int
        :param third_account: 开放性场景标识第三方账号信息
        :type third_account: str
        :param account: 用户账号
        :type account: str
        :param user_id: 用户UUID
        :type user_id: str
        """
        
        

        self._participant_id = None
        self._name = None
        self._call_number = None
        self._role = None
        self._third_account = None
        self._account = None
        self._user_id = None
        self.discriminator = None

        if participant_id is not None:
            self.participant_id = participant_id
        if name is not None:
            self.name = name
        if call_number is not None:
            self.call_number = call_number
        if role is not None:
            self.role = role
        if third_account is not None:
            self.third_account = third_account
        if account is not None:
            self.account = account
        if user_id is not None:
            self.user_id = user_id

    @property
    def participant_id(self):
        r"""Gets the participant_id of this OnlineAttendeeRecordInfo.

        与会者标识

        :return: The participant_id of this OnlineAttendeeRecordInfo.
        :rtype: str
        """
        return self._participant_id

    @participant_id.setter
    def participant_id(self, participant_id):
        r"""Sets the participant_id of this OnlineAttendeeRecordInfo.

        与会者标识

        :param participant_id: The participant_id of this OnlineAttendeeRecordInfo.
        :type participant_id: str
        """
        self._participant_id = participant_id

    @property
    def name(self):
        r"""Gets the name of this OnlineAttendeeRecordInfo.

        与会者名称

        :return: The name of this OnlineAttendeeRecordInfo.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this OnlineAttendeeRecordInfo.

        与会者名称

        :param name: The name of this OnlineAttendeeRecordInfo.
        :type name: str
        """
        self._name = name

    @property
    def call_number(self):
        r"""Gets the call_number of this OnlineAttendeeRecordInfo.

        呼叫号码

        :return: The call_number of this OnlineAttendeeRecordInfo.
        :rtype: str
        """
        return self._call_number

    @call_number.setter
    def call_number(self, call_number):
        r"""Sets the call_number of this OnlineAttendeeRecordInfo.

        呼叫号码

        :param call_number: The call_number of this OnlineAttendeeRecordInfo.
        :type call_number: str
        """
        self._call_number = call_number

    @property
    def role(self):
        r"""Gets the role of this OnlineAttendeeRecordInfo.

        会议中的角色，枚举值如下： 1：会议主席 0：普通与会者

        :return: The role of this OnlineAttendeeRecordInfo.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        r"""Sets the role of this OnlineAttendeeRecordInfo.

        会议中的角色，枚举值如下： 1：会议主席 0：普通与会者

        :param role: The role of this OnlineAttendeeRecordInfo.
        :type role: int
        """
        self._role = role

    @property
    def third_account(self):
        r"""Gets the third_account of this OnlineAttendeeRecordInfo.

        开放性场景标识第三方账号信息

        :return: The third_account of this OnlineAttendeeRecordInfo.
        :rtype: str
        """
        return self._third_account

    @third_account.setter
    def third_account(self, third_account):
        r"""Sets the third_account of this OnlineAttendeeRecordInfo.

        开放性场景标识第三方账号信息

        :param third_account: The third_account of this OnlineAttendeeRecordInfo.
        :type third_account: str
        """
        self._third_account = third_account

    @property
    def account(self):
        r"""Gets the account of this OnlineAttendeeRecordInfo.

        用户账号

        :return: The account of this OnlineAttendeeRecordInfo.
        :rtype: str
        """
        return self._account

    @account.setter
    def account(self, account):
        r"""Sets the account of this OnlineAttendeeRecordInfo.

        用户账号

        :param account: The account of this OnlineAttendeeRecordInfo.
        :type account: str
        """
        self._account = account

    @property
    def user_id(self):
        r"""Gets the user_id of this OnlineAttendeeRecordInfo.

        用户UUID

        :return: The user_id of this OnlineAttendeeRecordInfo.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        r"""Sets the user_id of this OnlineAttendeeRecordInfo.

        用户UUID

        :param user_id: The user_id of this OnlineAttendeeRecordInfo.
        :type user_id: str
        """
        self._user_id = user_id

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
        if not isinstance(other, OnlineAttendeeRecordInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
