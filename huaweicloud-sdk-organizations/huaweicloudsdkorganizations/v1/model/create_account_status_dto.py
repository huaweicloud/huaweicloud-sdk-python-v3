# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccountStatusDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'account_id': 'str',
        'account_name': 'str',
        'completed_at': 'datetime',
        'created_at': 'datetime',
        'id': 'str',
        'state': 'str',
        'failure_reason': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'account_name': 'account_name',
        'completed_at': 'completed_at',
        'created_at': 'created_at',
        'id': 'id',
        'state': 'state',
        'failure_reason': 'failure_reason'
    }

    def __init__(self, account_id=None, account_name=None, completed_at=None, created_at=None, id=None, state=None, failure_reason=None):
        """CreateAccountStatusDto

        The model defined in huaweicloud sdk

        :param account_id: 如果帐号创建成功，则为新帐号的唯一标识符（ID）。
        :type account_id: str
        :param account_name: 帐号名称。
        :type account_name: str
        :param completed_at: 创建帐号和完成请求的日期和时间。
        :type completed_at: datetime
        :param created_at: 请求创建帐号的日期和时间。
        :type created_at: datetime
        :param id: 请求的唯一标识符（ID）。您可以从创建帐号的初始CreateAccount请求的响应中获得此值。
        :type id: str
        :param state: 创建帐号的异步请求的状态，in_progress：处理中，succeeded：成功，failed：失败。
        :type state: str
        :param failure_reason: 如果请求失败，则说明失败原因。
        :type failure_reason: str
        """
        
        

        self._account_id = None
        self._account_name = None
        self._completed_at = None
        self._created_at = None
        self._id = None
        self._state = None
        self._failure_reason = None
        self.discriminator = None

        self.account_id = account_id
        self.account_name = account_name
        self.completed_at = completed_at
        self.created_at = created_at
        self.id = id
        self.state = state
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def account_id(self):
        """Gets the account_id of this CreateAccountStatusDto.

        如果帐号创建成功，则为新帐号的唯一标识符（ID）。

        :return: The account_id of this CreateAccountStatusDto.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this CreateAccountStatusDto.

        如果帐号创建成功，则为新帐号的唯一标识符（ID）。

        :param account_id: The account_id of this CreateAccountStatusDto.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def account_name(self):
        """Gets the account_name of this CreateAccountStatusDto.

        帐号名称。

        :return: The account_name of this CreateAccountStatusDto.
        :rtype: str
        """
        return self._account_name

    @account_name.setter
    def account_name(self, account_name):
        """Sets the account_name of this CreateAccountStatusDto.

        帐号名称。

        :param account_name: The account_name of this CreateAccountStatusDto.
        :type account_name: str
        """
        self._account_name = account_name

    @property
    def completed_at(self):
        """Gets the completed_at of this CreateAccountStatusDto.

        创建帐号和完成请求的日期和时间。

        :return: The completed_at of this CreateAccountStatusDto.
        :rtype: datetime
        """
        return self._completed_at

    @completed_at.setter
    def completed_at(self, completed_at):
        """Sets the completed_at of this CreateAccountStatusDto.

        创建帐号和完成请求的日期和时间。

        :param completed_at: The completed_at of this CreateAccountStatusDto.
        :type completed_at: datetime
        """
        self._completed_at = completed_at

    @property
    def created_at(self):
        """Gets the created_at of this CreateAccountStatusDto.

        请求创建帐号的日期和时间。

        :return: The created_at of this CreateAccountStatusDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateAccountStatusDto.

        请求创建帐号的日期和时间。

        :param created_at: The created_at of this CreateAccountStatusDto.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def id(self):
        """Gets the id of this CreateAccountStatusDto.

        请求的唯一标识符（ID）。您可以从创建帐号的初始CreateAccount请求的响应中获得此值。

        :return: The id of this CreateAccountStatusDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CreateAccountStatusDto.

        请求的唯一标识符（ID）。您可以从创建帐号的初始CreateAccount请求的响应中获得此值。

        :param id: The id of this CreateAccountStatusDto.
        :type id: str
        """
        self._id = id

    @property
    def state(self):
        """Gets the state of this CreateAccountStatusDto.

        创建帐号的异步请求的状态，in_progress：处理中，succeeded：成功，failed：失败。

        :return: The state of this CreateAccountStatusDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this CreateAccountStatusDto.

        创建帐号的异步请求的状态，in_progress：处理中，succeeded：成功，failed：失败。

        :param state: The state of this CreateAccountStatusDto.
        :type state: str
        """
        self._state = state

    @property
    def failure_reason(self):
        """Gets the failure_reason of this CreateAccountStatusDto.

        如果请求失败，则说明失败原因。

        :return: The failure_reason of this CreateAccountStatusDto.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this CreateAccountStatusDto.

        如果请求失败，则说明失败原因。

        :param failure_reason: The failure_reason of this CreateAccountStatusDto.
        :type failure_reason: str
        """
        self._failure_reason = failure_reason

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
        if not isinstance(other, CreateAccountStatusDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
