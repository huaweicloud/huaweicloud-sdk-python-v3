# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTargetOfPolicyGroupRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'policy_group_id': 'str',
        'target_type': 'str',
        'target_name': 'str',
        'limit': 'int',
        'offset': 'str'
    }

    attribute_map = {
        'policy_group_id': 'policy_group_id',
        'target_type': 'target_type',
        'target_name': 'target_name',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, policy_group_id=None, target_type=None, target_name=None, limit=None, offset=None):
        r"""ListTargetOfPolicyGroupRequest

        The model defined in huaweicloud sdk

        :param policy_group_id: 策略组id。
        :type policy_group_id: str
        :param target_type: 应用对象的类型。 - INSTANCE：表示桌面。 - USER：表示用户。 - OU：表示组织单元。 - CLIENTIP：终端IP地址。
        :type target_type: str
        :param target_name: 对象名称，支持模糊查询。
        :type target_name: str
        :param limit: 每页数量。范围0-1000。
        :type limit: int
        :param offset: 偏移量。
        :type offset: str
        """
        
        

        self._policy_group_id = None
        self._target_type = None
        self._target_name = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        self.policy_group_id = policy_group_id
        if target_type is not None:
            self.target_type = target_type
        if target_name is not None:
            self.target_name = target_name
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def policy_group_id(self):
        r"""Gets the policy_group_id of this ListTargetOfPolicyGroupRequest.

        策略组id。

        :return: The policy_group_id of this ListTargetOfPolicyGroupRequest.
        :rtype: str
        """
        return self._policy_group_id

    @policy_group_id.setter
    def policy_group_id(self, policy_group_id):
        r"""Sets the policy_group_id of this ListTargetOfPolicyGroupRequest.

        策略组id。

        :param policy_group_id: The policy_group_id of this ListTargetOfPolicyGroupRequest.
        :type policy_group_id: str
        """
        self._policy_group_id = policy_group_id

    @property
    def target_type(self):
        r"""Gets the target_type of this ListTargetOfPolicyGroupRequest.

        应用对象的类型。 - INSTANCE：表示桌面。 - USER：表示用户。 - OU：表示组织单元。 - CLIENTIP：终端IP地址。

        :return: The target_type of this ListTargetOfPolicyGroupRequest.
        :rtype: str
        """
        return self._target_type

    @target_type.setter
    def target_type(self, target_type):
        r"""Sets the target_type of this ListTargetOfPolicyGroupRequest.

        应用对象的类型。 - INSTANCE：表示桌面。 - USER：表示用户。 - OU：表示组织单元。 - CLIENTIP：终端IP地址。

        :param target_type: The target_type of this ListTargetOfPolicyGroupRequest.
        :type target_type: str
        """
        self._target_type = target_type

    @property
    def target_name(self):
        r"""Gets the target_name of this ListTargetOfPolicyGroupRequest.

        对象名称，支持模糊查询。

        :return: The target_name of this ListTargetOfPolicyGroupRequest.
        :rtype: str
        """
        return self._target_name

    @target_name.setter
    def target_name(self, target_name):
        r"""Sets the target_name of this ListTargetOfPolicyGroupRequest.

        对象名称，支持模糊查询。

        :param target_name: The target_name of this ListTargetOfPolicyGroupRequest.
        :type target_name: str
        """
        self._target_name = target_name

    @property
    def limit(self):
        r"""Gets the limit of this ListTargetOfPolicyGroupRequest.

        每页数量。范围0-1000。

        :return: The limit of this ListTargetOfPolicyGroupRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListTargetOfPolicyGroupRequest.

        每页数量。范围0-1000。

        :param limit: The limit of this ListTargetOfPolicyGroupRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        r"""Gets the offset of this ListTargetOfPolicyGroupRequest.

        偏移量。

        :return: The offset of this ListTargetOfPolicyGroupRequest.
        :rtype: str
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListTargetOfPolicyGroupRequest.

        偏移量。

        :param offset: The offset of this ListTargetOfPolicyGroupRequest.
        :type offset: str
        """
        self._offset = offset

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
        if not isinstance(other, ListTargetOfPolicyGroupRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
