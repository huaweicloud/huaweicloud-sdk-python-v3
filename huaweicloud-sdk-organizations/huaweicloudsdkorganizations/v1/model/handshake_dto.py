# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HandshakeDto:

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
        'urn': 'str',
        'updated_at': 'datetime',
        'created_at': 'datetime',
        'expired_at': 'datetime',
        'management_account_id': 'str',
        'management_account_name': 'str',
        'organization_id': 'str',
        'notes': 'str',
        'target': 'TargetDto',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'urn': 'urn',
        'updated_at': 'updated_at',
        'created_at': 'created_at',
        'expired_at': 'expired_at',
        'management_account_id': 'management_account_id',
        'management_account_name': 'management_account_name',
        'organization_id': 'organization_id',
        'notes': 'notes',
        'target': 'target',
        'status': 'status'
    }

    def __init__(self, id=None, urn=None, updated_at=None, created_at=None, expired_at=None, management_account_id=None, management_account_name=None, organization_id=None, notes=None, target=None, status=None):
        r"""HandshakeDto

        The model defined in huaweicloud sdk

        :param id: 邀请（握手）的唯一标识符（ID）。源账号在发起邀请（握手）时创建ID。
        :type id: str
        :param urn: 邀请（握手）的统一资源名称。
        :type urn: str
        :param updated_at: 邀请（握手）请求被接受、取消、拒绝或到期的日期和时间。
        :type updated_at: datetime
        :param created_at: 提出邀请（握手）请求的日期和时间。
        :type created_at: datetime
        :param expired_at: 邀请（握手）过期的日期和时间。
        :type expired_at: datetime
        :param management_account_id: 组织管理账号的唯一标识符（ID）。
        :type management_account_id: str
        :param management_account_name: 组织管理账号的名称。
        :type management_account_name: str
        :param organization_id: 组织的唯一标识符（ID）。
        :type organization_id: str
        :param notes: 给收件账号所有者的邮件中的附加信息。
        :type notes: str
        :param target: 
        :type target: :class:`huaweicloudsdkorganizations.v1.TargetDto`
        :param status: 邀请（握手）的当前状态, pending：邀请中；accepted：接受邀请；cancelled：取消邀请；declined：拒绝邀请；expired：邀请过期。
        :type status: str
        """
        
        

        self._id = None
        self._urn = None
        self._updated_at = None
        self._created_at = None
        self._expired_at = None
        self._management_account_id = None
        self._management_account_name = None
        self._organization_id = None
        self._notes = None
        self._target = None
        self._status = None
        self.discriminator = None

        self.id = id
        self.urn = urn
        self.updated_at = updated_at
        self.created_at = created_at
        self.expired_at = expired_at
        self.management_account_id = management_account_id
        self.management_account_name = management_account_name
        self.organization_id = organization_id
        self.notes = notes
        self.target = target
        self.status = status

    @property
    def id(self):
        r"""Gets the id of this HandshakeDto.

        邀请（握手）的唯一标识符（ID）。源账号在发起邀请（握手）时创建ID。

        :return: The id of this HandshakeDto.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this HandshakeDto.

        邀请（握手）的唯一标识符（ID）。源账号在发起邀请（握手）时创建ID。

        :param id: The id of this HandshakeDto.
        :type id: str
        """
        self._id = id

    @property
    def urn(self):
        r"""Gets the urn of this HandshakeDto.

        邀请（握手）的统一资源名称。

        :return: The urn of this HandshakeDto.
        :rtype: str
        """
        return self._urn

    @urn.setter
    def urn(self, urn):
        r"""Sets the urn of this HandshakeDto.

        邀请（握手）的统一资源名称。

        :param urn: The urn of this HandshakeDto.
        :type urn: str
        """
        self._urn = urn

    @property
    def updated_at(self):
        r"""Gets the updated_at of this HandshakeDto.

        邀请（握手）请求被接受、取消、拒绝或到期的日期和时间。

        :return: The updated_at of this HandshakeDto.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this HandshakeDto.

        邀请（握手）请求被接受、取消、拒绝或到期的日期和时间。

        :param updated_at: The updated_at of this HandshakeDto.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def created_at(self):
        r"""Gets the created_at of this HandshakeDto.

        提出邀请（握手）请求的日期和时间。

        :return: The created_at of this HandshakeDto.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this HandshakeDto.

        提出邀请（握手）请求的日期和时间。

        :param created_at: The created_at of this HandshakeDto.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def expired_at(self):
        r"""Gets the expired_at of this HandshakeDto.

        邀请（握手）过期的日期和时间。

        :return: The expired_at of this HandshakeDto.
        :rtype: datetime
        """
        return self._expired_at

    @expired_at.setter
    def expired_at(self, expired_at):
        r"""Sets the expired_at of this HandshakeDto.

        邀请（握手）过期的日期和时间。

        :param expired_at: The expired_at of this HandshakeDto.
        :type expired_at: datetime
        """
        self._expired_at = expired_at

    @property
    def management_account_id(self):
        r"""Gets the management_account_id of this HandshakeDto.

        组织管理账号的唯一标识符（ID）。

        :return: The management_account_id of this HandshakeDto.
        :rtype: str
        """
        return self._management_account_id

    @management_account_id.setter
    def management_account_id(self, management_account_id):
        r"""Sets the management_account_id of this HandshakeDto.

        组织管理账号的唯一标识符（ID）。

        :param management_account_id: The management_account_id of this HandshakeDto.
        :type management_account_id: str
        """
        self._management_account_id = management_account_id

    @property
    def management_account_name(self):
        r"""Gets the management_account_name of this HandshakeDto.

        组织管理账号的名称。

        :return: The management_account_name of this HandshakeDto.
        :rtype: str
        """
        return self._management_account_name

    @management_account_name.setter
    def management_account_name(self, management_account_name):
        r"""Sets the management_account_name of this HandshakeDto.

        组织管理账号的名称。

        :param management_account_name: The management_account_name of this HandshakeDto.
        :type management_account_name: str
        """
        self._management_account_name = management_account_name

    @property
    def organization_id(self):
        r"""Gets the organization_id of this HandshakeDto.

        组织的唯一标识符（ID）。

        :return: The organization_id of this HandshakeDto.
        :rtype: str
        """
        return self._organization_id

    @organization_id.setter
    def organization_id(self, organization_id):
        r"""Sets the organization_id of this HandshakeDto.

        组织的唯一标识符（ID）。

        :param organization_id: The organization_id of this HandshakeDto.
        :type organization_id: str
        """
        self._organization_id = organization_id

    @property
    def notes(self):
        r"""Gets the notes of this HandshakeDto.

        给收件账号所有者的邮件中的附加信息。

        :return: The notes of this HandshakeDto.
        :rtype: str
        """
        return self._notes

    @notes.setter
    def notes(self, notes):
        r"""Sets the notes of this HandshakeDto.

        给收件账号所有者的邮件中的附加信息。

        :param notes: The notes of this HandshakeDto.
        :type notes: str
        """
        self._notes = notes

    @property
    def target(self):
        r"""Gets the target of this HandshakeDto.

        :return: The target of this HandshakeDto.
        :rtype: :class:`huaweicloudsdkorganizations.v1.TargetDto`
        """
        return self._target

    @target.setter
    def target(self, target):
        r"""Sets the target of this HandshakeDto.

        :param target: The target of this HandshakeDto.
        :type target: :class:`huaweicloudsdkorganizations.v1.TargetDto`
        """
        self._target = target

    @property
    def status(self):
        r"""Gets the status of this HandshakeDto.

        邀请（握手）的当前状态, pending：邀请中；accepted：接受邀请；cancelled：取消邀请；declined：拒绝邀请；expired：邀请过期。

        :return: The status of this HandshakeDto.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this HandshakeDto.

        邀请（握手）的当前状态, pending：邀请中；accepted：接受邀请；cancelled：取消邀请；declined：拒绝邀请；expired：邀请过期。

        :param status: The status of this HandshakeDto.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, HandshakeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
