# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessPolicyDetailInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_name': 'str',
        'blacklist_type': 'str',
        'policy_id': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'policy_name': 'policy_name',
        'blacklist_type': 'blacklist_type',
        'policy_id': 'policy_id',
        'create_time': 'create_time'
    }

    def __init__(self, policy_name=None, blacklist_type=None, policy_id=None, create_time=None):
        """AccessPolicyDetailInfo

        The model defined in huaweicloud sdk

        :param policy_name: 策略名，当前只支持专线接入策略名。 * PRIVATE_ACCESS： 专线接入
        :type policy_name: str
        :param blacklist_type: 黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网
        :type blacklist_type: str
        :param policy_id: 策略id。
        :type policy_id: str
        :param create_time: 用户otp设备绑定时间。
        :type create_time: str
        """
        
        

        self._policy_name = None
        self._blacklist_type = None
        self._policy_id = None
        self._create_time = None
        self.discriminator = None

        self.policy_name = policy_name
        self.blacklist_type = blacklist_type
        if policy_id is not None:
            self.policy_id = policy_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def policy_name(self):
        """Gets the policy_name of this AccessPolicyDetailInfo.

        策略名，当前只支持专线接入策略名。 * PRIVATE_ACCESS： 专线接入

        :return: The policy_name of this AccessPolicyDetailInfo.
        :rtype: str
        """
        return self._policy_name

    @policy_name.setter
    def policy_name(self, policy_name):
        """Sets the policy_name of this AccessPolicyDetailInfo.

        策略名，当前只支持专线接入策略名。 * PRIVATE_ACCESS： 专线接入

        :param policy_name: The policy_name of this AccessPolicyDetailInfo.
        :type policy_name: str
        """
        self._policy_name = policy_name

    @property
    def blacklist_type(self):
        """Gets the blacklist_type of this AccessPolicyDetailInfo.

        黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网

        :return: The blacklist_type of this AccessPolicyDetailInfo.
        :rtype: str
        """
        return self._blacklist_type

    @blacklist_type.setter
    def blacklist_type(self, blacklist_type):
        """Sets the blacklist_type of this AccessPolicyDetailInfo.

        黑名单类型，当前黑名单只支持互联网。 * INTERNET： 互联网

        :param blacklist_type: The blacklist_type of this AccessPolicyDetailInfo.
        :type blacklist_type: str
        """
        self._blacklist_type = blacklist_type

    @property
    def policy_id(self):
        """Gets the policy_id of this AccessPolicyDetailInfo.

        策略id。

        :return: The policy_id of this AccessPolicyDetailInfo.
        :rtype: str
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        """Sets the policy_id of this AccessPolicyDetailInfo.

        策略id。

        :param policy_id: The policy_id of this AccessPolicyDetailInfo.
        :type policy_id: str
        """
        self._policy_id = policy_id

    @property
    def create_time(self):
        """Gets the create_time of this AccessPolicyDetailInfo.

        用户otp设备绑定时间。

        :return: The create_time of this AccessPolicyDetailInfo.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this AccessPolicyDetailInfo.

        用户otp设备绑定时间。

        :param create_time: The create_time of this AccessPolicyDetailInfo.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, AccessPolicyDetailInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
