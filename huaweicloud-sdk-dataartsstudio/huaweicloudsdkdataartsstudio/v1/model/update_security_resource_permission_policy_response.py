# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSecurityResourcePermissionPolicyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_id': 'str',
        'policy_name': 'str',
        'resources': 'list[ResourcePolicyItem]',
        'members': 'list[MemberPolicyItem]',
        'create_time': 'int',
        'create_user': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'policy_id': 'policy_id',
        'policy_name': 'policy_name',
        'resources': 'resources',
        'members': 'members',
        'create_time': 'create_time',
        'create_user': 'create_user',
        'update_time': 'update_time'
    }

    def __init__(self, policy_id=None, policy_name=None, resources=None, members=None, create_time=None, create_user=None, update_time=None):
        r"""UpdateSecurityResourcePermissionPolicyResponse

        The model defined in huaweicloud sdk

        :param policy_id: 策略id
        :type policy_id: str
        :param policy_name: 策略名称
        :type policy_name: str
        :param resources: 资源对象列表
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.ResourcePolicyItem`]
        :param members: 成员列表
        :type members: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPolicyItem`]
        :param create_time: 创建时间
        :type create_time: int
        :param create_user: 创建用户
        :type create_user: str
        :param update_time: 修改时间
        :type update_time: int
        """
        
        super(UpdateSecurityResourcePermissionPolicyResponse, self).__init__()

        self._policy_id = None
        self._policy_name = None
        self._resources = None
        self._members = None
        self._create_time = None
        self._create_user = None
        self._update_time = None
        self.discriminator = None

        if policy_id is not None:
            self.policy_id = policy_id
        if policy_name is not None:
            self.policy_name = policy_name
        if resources is not None:
            self.resources = resources
        if members is not None:
            self.members = members
        if create_time is not None:
            self.create_time = create_time
        if create_user is not None:
            self.create_user = create_user
        if update_time is not None:
            self.update_time = update_time

    @property
    def policy_id(self):
        r"""Gets the policy_id of this UpdateSecurityResourcePermissionPolicyResponse.

        策略id

        :return: The policy_id of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this UpdateSecurityResourcePermissionPolicyResponse.

        策略id

        :param policy_id: The policy_id of this UpdateSecurityResourcePermissionPolicyResponse.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def policy_name(self):
        r"""Gets the policy_name of this UpdateSecurityResourcePermissionPolicyResponse.

        策略名称

        :return: The policy_name of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        r"""Sets the policy_name of this UpdateSecurityResourcePermissionPolicyResponse.

        策略名称

        :param policy_name: The policy_name of this UpdateSecurityResourcePermissionPolicyResponse.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def resources(self):
        r"""Gets the resources of this UpdateSecurityResourcePermissionPolicyResponse.

        资源对象列表

        :return: The resources of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.ResourcePolicyItem`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this UpdateSecurityResourcePermissionPolicyResponse.

        资源对象列表

        :param resources: The resources of this UpdateSecurityResourcePermissionPolicyResponse.
        :type resources: list[:class:`huaweicloudsdkdataartsstudio.v1.ResourcePolicyItem`]
        """
        self._resources = resources

    @property
    def members(self):
        r"""Gets the members of this UpdateSecurityResourcePermissionPolicyResponse.

        成员列表

        :return: The members of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPolicyItem`]
        """
        return self._members

    @members.setter
    def members(self, members):
        r"""Sets the members of this UpdateSecurityResourcePermissionPolicyResponse.

        成员列表

        :param members: The members of this UpdateSecurityResourcePermissionPolicyResponse.
        :type members: list[:class:`huaweicloudsdkdataartsstudio.v1.MemberPolicyItem`]
        """
        self._members = members

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateSecurityResourcePermissionPolicyResponse.

        创建时间

        :return: The create_time of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateSecurityResourcePermissionPolicyResponse.

        创建时间

        :param create_time: The create_time of this UpdateSecurityResourcePermissionPolicyResponse.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def create_user(self):
        r"""Gets the create_user of this UpdateSecurityResourcePermissionPolicyResponse.

        创建用户

        :return: The create_user of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: str
        """
        return self._create_user

    @create_user.setter
    def create_user(self, create_user):
        r"""Sets the create_user of this UpdateSecurityResourcePermissionPolicyResponse.

        创建用户

        :param create_user: The create_user of this UpdateSecurityResourcePermissionPolicyResponse.
        :type create_user: str
        """
        self._create_user = create_user

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateSecurityResourcePermissionPolicyResponse.

        修改时间

        :return: The update_time of this UpdateSecurityResourcePermissionPolicyResponse.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateSecurityResourcePermissionPolicyResponse.

        修改时间

        :param update_time: The update_time of this UpdateSecurityResourcePermissionPolicyResponse.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, UpdateSecurityResourcePermissionPolicyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
