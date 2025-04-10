# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CloseAccountStatusDto:

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
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'organization_id': 'str',
        'state': 'str',
        'failure_reason': 'str'
    }

    attribute_map = {
        'account_id': 'account_id',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'organization_id': 'organization_id',
        'state': 'state',
        'failure_reason': 'failure_reason'
    }

    def __init__(self, account_id=None, created_at=None, updated_at=None, organization_id=None, state=None, failure_reason=None):
        r"""CloseAccountStatusDto

        The model defined in huaweicloud sdk

        :param account_id: 账号的唯一标识符（ID）。
        :type account_id: str
        :param created_at: 请求关闭账号的日期和时间。
        :type created_at: datetime
        :param updated_at: 请求关闭账号状态更新的日期和时间。
        :type updated_at: datetime
        :param organization_id: 组织的唯一标识符（ID）。
        :type organization_id: str
        :param state: 关闭账号的状态，pending_closure：关闭中，suspended：已关闭
        :type state: str
        :param failure_reason: 如果请求失败，则说明失败原因。
        :type failure_reason: str
        """
        
        

        self._account_id = None
        self._created_at = None
        self._updated_at = None
        self._organization_id = None
        self._state = None
        self._failure_reason = None
        self.discriminator = None

        self.account_id = account_id
        self.created_at = created_at
        self.updated_at = updated_at
        self.organization_id = organization_id
        self.state = state
        if failure_reason is not None:
            self.failure_reason = failure_reason

    @property
    def account_id(self):
        r"""Gets the account_id of this CloseAccountStatusDto.

        账号的唯一标识符（ID）。

        :return: The account_id of this CloseAccountStatusDto.
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        r"""Sets the account_id of this CloseAccountStatusDto.

        账号的唯一标识符（ID）。

        :param account_id: The account_id of this CloseAccountStatusDto.
        :type account_id: str
        """
        self._account_id = account_id

    @property
    def created_at(self):
        r"""Gets the created_at of this CloseAccountStatusDto.

        请求关闭账号的日期和时间。

        :return: The created_at of this CloseAccountStatusDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this CloseAccountStatusDto.

        请求关闭账号的日期和时间。

        :param created_at: The created_at of this CloseAccountStatusDto.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this CloseAccountStatusDto.

        请求关闭账号状态更新的日期和时间。

        :return: The updated_at of this CloseAccountStatusDto.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this CloseAccountStatusDto.

        请求关闭账号状态更新的日期和时间。

        :param updated_at: The updated_at of this CloseAccountStatusDto.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def organization_id(self):
        r"""Gets the organization_id of this CloseAccountStatusDto.

        组织的唯一标识符（ID）。

        :return: The organization_id of this CloseAccountStatusDto.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this CloseAccountStatusDto.

        组织的唯一标识符（ID）。

        :param organization_id: The organization_id of this CloseAccountStatusDto.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def state(self):
        r"""Gets the state of this CloseAccountStatusDto.

        关闭账号的状态，pending_closure：关闭中，suspended：已关闭

        :return: The state of this CloseAccountStatusDto.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        r"""Sets the state of this CloseAccountStatusDto.

        关闭账号的状态，pending_closure：关闭中，suspended：已关闭

        :param state: The state of this CloseAccountStatusDto.
        :type state: str
        """
        self._state = state

    @property
    def failure_reason(self):
        r"""Gets the failure_reason of this CloseAccountStatusDto.

        如果请求失败，则说明失败原因。

        :return: The failure_reason of this CloseAccountStatusDto.
        :rtype: str
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        r"""Sets the failure_reason of this CloseAccountStatusDto.

        如果请求失败，则说明失败原因。

        :param failure_reason: The failure_reason of this CloseAccountStatusDto.
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
        if not isinstance(other, CloseAccountStatusDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
