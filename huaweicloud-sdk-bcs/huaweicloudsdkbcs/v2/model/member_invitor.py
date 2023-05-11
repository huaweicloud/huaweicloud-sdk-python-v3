# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MemberInvitor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'invitor_bcs_id': 'str',
        'invitor_bcs_name': 'str',
        'invitor_project_id': 'str',
        'invitor_user_id': 'str',
        'invitor_username': 'str'
    }

    attribute_map = {
        'invitor_bcs_id': 'invitor_bcs_id',
        'invitor_bcs_name': 'invitor_bcs_name',
        'invitor_project_id': 'invitor_project_id',
        'invitor_user_id': 'invitor_user_id',
        'invitor_username': 'invitor_username'
    }

    def __init__(self, invitor_bcs_id=None, invitor_bcs_name=None, invitor_project_id=None, invitor_user_id=None, invitor_username=None):
        """MemberInvitor

        The model defined in huaweicloud sdk

        :param invitor_bcs_id: 邀请方BCS服务实例ID
        :type invitor_bcs_id: str
        :param invitor_bcs_name: 邀请方BCS服务实例名称
        :type invitor_bcs_name: str
        :param invitor_project_id: 邀请方project id
        :type invitor_project_id: str
        :param invitor_user_id: 邀请方租户id
        :type invitor_user_id: str
        :param invitor_username: 邀请方租户名
        :type invitor_username: str
        """
        
        

        self._invitor_bcs_id = None
        self._invitor_bcs_name = None
        self._invitor_project_id = None
        self._invitor_user_id = None
        self._invitor_username = None
        self.discriminator = None

        if invitor_bcs_id is not None:
            self.invitor_bcs_id = invitor_bcs_id
        if invitor_bcs_name is not None:
            self.invitor_bcs_name = invitor_bcs_name
        if invitor_project_id is not None:
            self.invitor_project_id = invitor_project_id
        if invitor_user_id is not None:
            self.invitor_user_id = invitor_user_id
        if invitor_username is not None:
            self.invitor_username = invitor_username

    @property
    def invitor_bcs_id(self):
        """Gets the invitor_bcs_id of this MemberInvitor.

        邀请方BCS服务实例ID

        :return: The invitor_bcs_id of this MemberInvitor.
        :rtype: str
        """
        return self._invitor_bcs_id

    @invitor_bcs_id.setter
    def invitor_bcs_id(self, invitor_bcs_id):
        """Sets the invitor_bcs_id of this MemberInvitor.

        邀请方BCS服务实例ID

        :param invitor_bcs_id: The invitor_bcs_id of this MemberInvitor.
        :type invitor_bcs_id: str
        """
        self._invitor_bcs_id = invitor_bcs_id

    @property
    def invitor_bcs_name(self):
        """Gets the invitor_bcs_name of this MemberInvitor.

        邀请方BCS服务实例名称

        :return: The invitor_bcs_name of this MemberInvitor.
        :rtype: str
        """
        return self._invitor_bcs_name

    @invitor_bcs_name.setter
    def invitor_bcs_name(self, invitor_bcs_name):
        """Sets the invitor_bcs_name of this MemberInvitor.

        邀请方BCS服务实例名称

        :param invitor_bcs_name: The invitor_bcs_name of this MemberInvitor.
        :type invitor_bcs_name: str
        """
        self._invitor_bcs_name = invitor_bcs_name

    @property
    def invitor_project_id(self):
        """Gets the invitor_project_id of this MemberInvitor.

        邀请方project id

        :return: The invitor_project_id of this MemberInvitor.
        :rtype: str
        """
        return self._invitor_project_id

    @invitor_project_id.setter
    def invitor_project_id(self, invitor_project_id):
        """Sets the invitor_project_id of this MemberInvitor.

        邀请方project id

        :param invitor_project_id: The invitor_project_id of this MemberInvitor.
        :type invitor_project_id: str
        """
        self._invitor_project_id = invitor_project_id

    @property
    def invitor_user_id(self):
        """Gets the invitor_user_id of this MemberInvitor.

        邀请方租户id

        :return: The invitor_user_id of this MemberInvitor.
        :rtype: str
        """
        return self._invitor_user_id

    @invitor_user_id.setter
    def invitor_user_id(self, invitor_user_id):
        """Sets the invitor_user_id of this MemberInvitor.

        邀请方租户id

        :param invitor_user_id: The invitor_user_id of this MemberInvitor.
        :type invitor_user_id: str
        """
        self._invitor_user_id = invitor_user_id

    @property
    def invitor_username(self):
        """Gets the invitor_username of this MemberInvitor.

        邀请方租户名

        :return: The invitor_username of this MemberInvitor.
        :rtype: str
        """
        return self._invitor_username

    @invitor_username.setter
    def invitor_username(self, invitor_username):
        """Sets the invitor_username of this MemberInvitor.

        邀请方租户名

        :param invitor_username: The invitor_username of this MemberInvitor.
        :type invitor_username: str
        """
        self._invitor_username = invitor_username

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
        if not isinstance(other, MemberInvitor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
