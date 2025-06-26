# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceReplicationPolicyExecutionsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'policy_id': 'int',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'policy_id': 'policy_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, instance_id=None, policy_id=None, offset=None, limit=None):
        r"""ListInstanceReplicationPolicyExecutionsRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param policy_id: 同步策略ID
        :type policy_id: int
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100 **注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        """
        
        

        self._instance_id = None
        self._policy_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.instance_id = instance_id
        if policy_id is not None:
            self.policy_id = policy_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceReplicationPolicyExecutionsRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceReplicationPolicyExecutionsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceReplicationPolicyExecutionsRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceReplicationPolicyExecutionsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListInstanceReplicationPolicyExecutionsRequest.

        同步策略ID

        :return: The policy_id of this ListInstanceReplicationPolicyExecutionsRequest.
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListInstanceReplicationPolicyExecutionsRequest.

        同步策略ID

        :param policy_id: The policy_id of this ListInstanceReplicationPolicyExecutionsRequest.
        :type policy_id: int
        """
        self._policy_id = policy_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceReplicationPolicyExecutionsRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListInstanceReplicationPolicyExecutionsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceReplicationPolicyExecutionsRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListInstanceReplicationPolicyExecutionsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceReplicationPolicyExecutionsRequest.

        返回条数，默认为10，最大值为100 **注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListInstanceReplicationPolicyExecutionsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceReplicationPolicyExecutionsRequest.

        返回条数，默认为10，最大值为100 **注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListInstanceReplicationPolicyExecutionsRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListInstanceReplicationPolicyExecutionsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
