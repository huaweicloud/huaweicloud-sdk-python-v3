# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceRetentionPolicyExecTasksRequest:

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
        'namespace_name': 'str',
        'policy_id': 'int',
        'execution_id': 'int',
        'offset': 'int',
        'limit': 'int',
        'status': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'namespace_name': 'namespace_name',
        'policy_id': 'policy_id',
        'execution_id': 'execution_id',
        'offset': 'offset',
        'limit': 'limit',
        'status': 'status'
    }

    def __init__(self, instance_id=None, namespace_name=None, policy_id=None, execution_id=None, offset=None, limit=None, status=None):
        r"""ListInstanceRetentionPolicyExecTasksRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param policy_id: 老化策略ID
        :type policy_id: int
        :param execution_id: 老化策略执行记录ID
        :type execution_id: int
        :param offset: 起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type offset: int
        :param limit: 返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**
        :type limit: int
        :param status: 状态，可选Initialized、Pending、InProgress、Succeed、Failed、Stopped
        :type status: str
        """
        
        

        self._instance_id = None
        self._namespace_name = None
        self._policy_id = None
        self._execution_id = None
        self._offset = None
        self._limit = None
        self._status = None
        self.discriminator = None

        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.policy_id = policy_id
        self.execution_id = execution_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if status is not None:
            self.status = status

    @property
    def instance_id(self):
        r"""Gets the instance_id of this ListInstanceRetentionPolicyExecTasksRequest.

        企业仓库实例ID

        :return: The instance_id of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this ListInstanceRetentionPolicyExecTasksRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this ListInstanceRetentionPolicyExecTasksRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this ListInstanceRetentionPolicyExecTasksRequest.

        命名空间名称

        :return: The namespace_name of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this ListInstanceRetentionPolicyExecTasksRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this ListInstanceRetentionPolicyExecTasksRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def policy_id(self):
        r"""Gets the policy_id of this ListInstanceRetentionPolicyExecTasksRequest.

        老化策略ID

        :return: The policy_id of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: int
        """
        return self._policy_id

    @policy_id.setter
    def policy_id(self, policy_id):
        r"""Sets the policy_id of this ListInstanceRetentionPolicyExecTasksRequest.

        老化策略ID

        :param policy_id: The policy_id of this ListInstanceRetentionPolicyExecTasksRequest.
        :type policy_id: int
        """
        self._policy_id = policy_id

    @property
    def execution_id(self):
        r"""Gets the execution_id of this ListInstanceRetentionPolicyExecTasksRequest.

        老化策略执行记录ID

        :return: The execution_id of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: int
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this ListInstanceRetentionPolicyExecTasksRequest.

        老化策略执行记录ID

        :param execution_id: The execution_id of this ListInstanceRetentionPolicyExecTasksRequest.
        :type execution_id: int
        """
        self._execution_id = execution_id

    @property
    def offset(self):
        r"""Gets the offset of this ListInstanceRetentionPolicyExecTasksRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The offset of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListInstanceRetentionPolicyExecTasksRequest.

        起始索引，默认值为0。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param offset: The offset of this ListInstanceRetentionPolicyExecTasksRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListInstanceRetentionPolicyExecTasksRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :return: The limit of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListInstanceRetentionPolicyExecTasksRequest.

        返回条数，默认为10，最大值为100。**注意：offset和limit参数需要配套使用，offset必须为0或者为limit的倍数。**

        :param limit: The limit of this ListInstanceRetentionPolicyExecTasksRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def status(self):
        r"""Gets the status of this ListInstanceRetentionPolicyExecTasksRequest.

        状态，可选Initialized、Pending、InProgress、Succeed、Failed、Stopped

        :return: The status of this ListInstanceRetentionPolicyExecTasksRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ListInstanceRetentionPolicyExecTasksRequest.

        状态，可选Initialized、Pending、InProgress、Succeed、Failed、Stopped

        :param status: The status of this ListInstanceRetentionPolicyExecTasksRequest.
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
        if not isinstance(other, ListInstanceRetentionPolicyExecTasksRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
