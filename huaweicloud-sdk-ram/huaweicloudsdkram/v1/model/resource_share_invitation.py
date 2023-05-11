# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceShareInvitation:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'receiver_account_id': 'str',
        'resource_share_id': 'str',
        'resource_share_name': 'str',
        'resource_share_invitation_id': 'str',
        'sender_account_id': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'receiver_account_id': 'receiver_account_id',
        'resource_share_id': 'resource_share_id',
        'resource_share_name': 'resource_share_name',
        'resource_share_invitation_id': 'resource_share_invitation_id',
        'sender_account_id': 'sender_account_id',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, receiver_account_id=None, resource_share_id=None, resource_share_name=None, resource_share_invitation_id=None, sender_account_id=None, status=None, created_at=None, updated_at=None):
        """ResourceShareInvitation

        The model defined in huaweicloud sdk

        :param receiver_account_id: 接收资源共享邀请的帐号ID。
        :type receiver_account_id: str
        :param resource_share_id: 资源共享实例的ID。
        :type resource_share_id: str
        :param resource_share_name: 资源共享实例的名称。
        :type resource_share_name: str
        :param resource_share_invitation_id: 资源共享邀请的ID。
        :type resource_share_invitation_id: str
        :param sender_account_id: 发送资源共享邀请的帐号ID。
        :type sender_account_id: str
        :param status: 资源共享邀请的当前状态。
        :type status: str
        :param created_at: 创建邀请的时间。
        :type created_at: datetime
        :param updated_at: 最后一次更新邀请的时间。
        :type updated_at: datetime
        """
        
        

        self._receiver_account_id = None
        self._resource_share_id = None
        self._resource_share_name = None
        self._resource_share_invitation_id = None
        self._sender_account_id = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if receiver_account_id is not None:
            self.receiver_account_id = receiver_account_id
        if resource_share_id is not None:
            self.resource_share_id = resource_share_id
        if resource_share_name is not None:
            self.resource_share_name = resource_share_name
        if resource_share_invitation_id is not None:
            self.resource_share_invitation_id = resource_share_invitation_id
        if sender_account_id is not None:
            self.sender_account_id = sender_account_id
        if status is not None:
            self.status = status
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def receiver_account_id(self):
        """Gets the receiver_account_id of this ResourceShareInvitation.

        接收资源共享邀请的帐号ID。

        :return: The receiver_account_id of this ResourceShareInvitation.
        :rtype: str
        """
        return self._receiver_account_id

    @receiver_account_id.setter
    def receiver_account_id(self, receiver_account_id):
        """Sets the receiver_account_id of this ResourceShareInvitation.

        接收资源共享邀请的帐号ID。

        :param receiver_account_id: The receiver_account_id of this ResourceShareInvitation.
        :type receiver_account_id: str
        """
        self._receiver_account_id = receiver_account_id

    @property
    def resource_share_id(self):
        """Gets the resource_share_id of this ResourceShareInvitation.

        资源共享实例的ID。

        :return: The resource_share_id of this ResourceShareInvitation.
        :rtype: str
        """
        return self._resource_share_id

    @resource_share_id.setter
    def resource_share_id(self, resource_share_id):
        """Sets the resource_share_id of this ResourceShareInvitation.

        资源共享实例的ID。

        :param resource_share_id: The resource_share_id of this ResourceShareInvitation.
        :type resource_share_id: str
        """
        self._resource_share_id = resource_share_id

    @property
    def resource_share_name(self):
        """Gets the resource_share_name of this ResourceShareInvitation.

        资源共享实例的名称。

        :return: The resource_share_name of this ResourceShareInvitation.
        :rtype: str
        """
        return self._resource_share_name

    @resource_share_name.setter
    def resource_share_name(self, resource_share_name):
        """Sets the resource_share_name of this ResourceShareInvitation.

        资源共享实例的名称。

        :param resource_share_name: The resource_share_name of this ResourceShareInvitation.
        :type resource_share_name: str
        """
        self._resource_share_name = resource_share_name

    @property
    def resource_share_invitation_id(self):
        """Gets the resource_share_invitation_id of this ResourceShareInvitation.

        资源共享邀请的ID。

        :return: The resource_share_invitation_id of this ResourceShareInvitation.
        :rtype: str
        """
        return self._resource_share_invitation_id

    @resource_share_invitation_id.setter
    def resource_share_invitation_id(self, resource_share_invitation_id):
        """Sets the resource_share_invitation_id of this ResourceShareInvitation.

        资源共享邀请的ID。

        :param resource_share_invitation_id: The resource_share_invitation_id of this ResourceShareInvitation.
        :type resource_share_invitation_id: str
        """
        self._resource_share_invitation_id = resource_share_invitation_id

    @property
    def sender_account_id(self):
        """Gets the sender_account_id of this ResourceShareInvitation.

        发送资源共享邀请的帐号ID。

        :return: The sender_account_id of this ResourceShareInvitation.
        :rtype: str
        """
        return self._sender_account_id

    @sender_account_id.setter
    def sender_account_id(self, sender_account_id):
        """Sets the sender_account_id of this ResourceShareInvitation.

        发送资源共享邀请的帐号ID。

        :param sender_account_id: The sender_account_id of this ResourceShareInvitation.
        :type sender_account_id: str
        """
        self._sender_account_id = sender_account_id

    @property
    def status(self):
        """Gets the status of this ResourceShareInvitation.

        资源共享邀请的当前状态。

        :return: The status of this ResourceShareInvitation.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ResourceShareInvitation.

        资源共享邀请的当前状态。

        :param status: The status of this ResourceShareInvitation.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        """Gets the created_at of this ResourceShareInvitation.

        创建邀请的时间。

        :return: The created_at of this ResourceShareInvitation.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ResourceShareInvitation.

        创建邀请的时间。

        :param created_at: The created_at of this ResourceShareInvitation.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ResourceShareInvitation.

        最后一次更新邀请的时间。

        :return: The updated_at of this ResourceShareInvitation.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ResourceShareInvitation.

        最后一次更新邀请的时间。

        :param updated_at: The updated_at of this ResourceShareInvitation.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ResourceShareInvitation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
