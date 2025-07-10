# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPolicyGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'limit': 'int',
        'offset': 'int',
        'policy_group_id': 'str',
        'policy_group_name': 'str',
        'priority': 'int',
        'update_time': 'str',
        'description': 'str',
        'is_group_name_accurate': 'bool'
    }

    attribute_map = {
        'limit': 'limit',
        'offset': 'offset',
        'policy_group_id': 'policy_group_id',
        'policy_group_name': 'policy_group_name',
        'priority': 'priority',
        'update_time': 'update_time',
        'description': 'description',
        'is_group_name_accurate': 'is_group_name_accurate'
    }

    def __init__(self, limit=None, offset=None, policy_group_id=None, policy_group_name=None, priority=None, update_time=None, description=None, is_group_name_accurate=None):
        r"""ListPolicyGroupRequest

        The model defined in huaweicloud sdk

        :param limit: 用于分页查询，返回策略组数量的限制。如果不指定，则返回所有符合条件的策略组。范围0~100。
        :type limit: int
        :param offset: 用于分页查询，查询的起始记录序号，范围0~1000。
        :type offset: int
        :param policy_group_id: 根据策略组ID过滤结果。
        :type policy_group_id: str
        :param policy_group_name: 根据策略组名字过滤结果。
        :type policy_group_name: str
        :param priority: 根据优先级过滤结果。所带的值需要满足现有策略组已有最大优先级值。
        :type priority: int
        :param update_time: 根据更新时间过滤结果。时间格式满足：yyyy-MM-dd HH:mm:ss。
        :type update_time: str
        :param description: 策略组描述。
        :type description: str
        :param is_group_name_accurate: 策略组名字精确查询。
        :type is_group_name_accurate: bool
        """
        
        

        self._limit = None
        self._offset = None
        self._policy_group_id = None
        self._policy_group_name = None
        self._priority = None
        self._update_time = None
        self._description = None
        self._is_group_name_accurate = None
        self.discriminator = None

        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if policy_group_id is not None:
            self.policy_group_id = policy_group_id
        if policy_group_name is not None:
            self.policy_group_name = policy_group_name
        if priority is not None:
            self.priority = priority
        if update_time is not None:
            self.update_time = update_time
        if description is not None:
            self.description = description
        if is_group_name_accurate is not None:
            self.is_group_name_accurate = is_group_name_accurate

    @property
    def limit(self):
        r"""Gets the limit of this ListPolicyGroupRequest.

        用于分页查询，返回策略组数量的限制。如果不指定，则返回所有符合条件的策略组。范围0~100。

        :return: The limit of this ListPolicyGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListPolicyGroupRequest.

        用于分页查询，返回策略组数量的限制。如果不指定，则返回所有符合条件的策略组。范围0~100。

        :param limit: The limit of this ListPolicyGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListPolicyGroupRequest.

        用于分页查询，查询的起始记录序号，范围0~1000。

        :return: The offset of this ListPolicyGroupRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListPolicyGroupRequest.

        用于分页查询，查询的起始记录序号，范围0~1000。

        :param offset: The offset of this ListPolicyGroupRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListPolicyGroupRequest.

        根据策略组ID过滤结果。

        :return: The policy_group_id of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListPolicyGroupRequest.

        根据策略组ID过滤结果。

        :param policy_group_id: The policy_group_id of this ListPolicyGroupRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def policy_group_name(self):
        r"""Gets the policy_group_name of this ListPolicyGroupRequest.

        根据策略组名字过滤结果。

        :return: The policy_group_name of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_group_name

    @policy_group_name.setter
    def policy_group_name(self, policy_group_name):
        r"""Sets the policy_group_name of this ListPolicyGroupRequest.

        根据策略组名字过滤结果。

        :param policy_group_name: The policy_group_name of this ListPolicyGroupRequest.
        :type policy_group_name: str
        """
        self._policy_group_name = policy_group_name

    @property
    def priority(self):
        r"""Gets the priority of this ListPolicyGroupRequest.

        根据优先级过滤结果。所带的值需要满足现有策略组已有最大优先级值。

        :return: The priority of this ListPolicyGroupRequest.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        r"""Sets the priority of this ListPolicyGroupRequest.

        根据优先级过滤结果。所带的值需要满足现有策略组已有最大优先级值。

        :param priority: The priority of this ListPolicyGroupRequest.
        :type priority: int
        """
        self._priority = priority

    @property
    def update_time(self):
        r"""Gets the update_time of this ListPolicyGroupRequest.

        根据更新时间过滤结果。时间格式满足：yyyy-MM-dd HH:mm:ss。

        :return: The update_time of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ListPolicyGroupRequest.

        根据更新时间过滤结果。时间格式满足：yyyy-MM-dd HH:mm:ss。

        :param update_time: The update_time of this ListPolicyGroupRequest.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def description(self):
        r"""Gets the description of this ListPolicyGroupRequest.

        策略组描述。

        :return: The description of this ListPolicyGroupRequest.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ListPolicyGroupRequest.

        策略组描述。

        :param description: The description of this ListPolicyGroupRequest.
        :type description: str
        """
        self._description = description

    @property
    def is_group_name_accurate(self):
        r"""Gets the is_group_name_accurate of this ListPolicyGroupRequest.

        策略组名字精确查询。

        :return: The is_group_name_accurate of this ListPolicyGroupRequest.
        :rtype: bool
        """
        return self._is_group_name_accurate

    @is_group_name_accurate.setter
    def is_group_name_accurate(self, is_group_name_accurate):
        r"""Sets the is_group_name_accurate of this ListPolicyGroupRequest.

        策略组名字精确查询。

        :param is_group_name_accurate: The is_group_name_accurate of this ListPolicyGroupRequest.
        :type is_group_name_accurate: bool
        """
        self._is_group_name_accurate = is_group_name_accurate

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
        if not isinstance(other, ListPolicyGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
