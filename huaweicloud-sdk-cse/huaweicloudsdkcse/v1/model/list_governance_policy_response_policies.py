# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListGovernancePolicyResponsePolicies:

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
        'name': 'str',
        'kind': 'str',
        'status': 'str',
        'selector': 'GovSelector',
        'spec': 'object'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'kind': 'kind',
        'status': 'status',
        'selector': 'selector',
        'spec': 'spec'
    }

    def __init__(self, id=None, name=None, kind=None, status=None, selector=None, spec=None):
        """ListGovernancePolicyResponsePolicies

        The model defined in huaweicloud sdk

        :param id: 治理策略ID
        :type id: str
        :param name: 治理策略名称
        :type name: str
        :param kind: 治理类型，支持填写retry、rate-limiting、loadbalance、circuit-breaker、instance-isolation、fault-injection和bulkhead
        :type kind: str
        :param status: 启用状态，支持enabled和disabled
        :type status: str
        :param selector: 
        :type selector: :class:`huaweicloudsdkcse.v1.GovSelector`
        :param spec: 治理策略定义内容
        :type spec: object
        """
        
        

        self._id = None
        self._name = None
        self._kind = None
        self._status = None
        self._selector = None
        self._spec = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if kind is not None:
            self.kind = kind
        if status is not None:
            self.status = status
        if selector is not None:
            self.selector = selector
        if spec is not None:
            self.spec = spec

    @property
    def id(self):
        """Gets the id of this ListGovernancePolicyResponsePolicies.

        治理策略ID

        :return: The id of this ListGovernancePolicyResponsePolicies.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ListGovernancePolicyResponsePolicies.

        治理策略ID

        :param id: The id of this ListGovernancePolicyResponsePolicies.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ListGovernancePolicyResponsePolicies.

        治理策略名称

        :return: The name of this ListGovernancePolicyResponsePolicies.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListGovernancePolicyResponsePolicies.

        治理策略名称

        :param name: The name of this ListGovernancePolicyResponsePolicies.
        :type name: str
        """
        self._name = name

    @property
    def kind(self):
        """Gets the kind of this ListGovernancePolicyResponsePolicies.

        治理类型，支持填写retry、rate-limiting、loadbalance、circuit-breaker、instance-isolation、fault-injection和bulkhead

        :return: The kind of this ListGovernancePolicyResponsePolicies.
        :rtype: str
        """
        return self._kind

    @kind.setter
    def kind(self, kind):
        """Sets the kind of this ListGovernancePolicyResponsePolicies.

        治理类型，支持填写retry、rate-limiting、loadbalance、circuit-breaker、instance-isolation、fault-injection和bulkhead

        :param kind: The kind of this ListGovernancePolicyResponsePolicies.
        :type kind: str
        """
        self._kind = kind

    @property
    def status(self):
        """Gets the status of this ListGovernancePolicyResponsePolicies.

        启用状态，支持enabled和disabled

        :return: The status of this ListGovernancePolicyResponsePolicies.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListGovernancePolicyResponsePolicies.

        启用状态，支持enabled和disabled

        :param status: The status of this ListGovernancePolicyResponsePolicies.
        :type status: str
        """
        self._status = status

    @property
    def selector(self):
        """Gets the selector of this ListGovernancePolicyResponsePolicies.

        :return: The selector of this ListGovernancePolicyResponsePolicies.
        :rtype: :class:`huaweicloudsdkcse.v1.GovSelector`
        """
        return self._selector

    @selector.setter
    def selector(self, selector):
        """Sets the selector of this ListGovernancePolicyResponsePolicies.

        :param selector: The selector of this ListGovernancePolicyResponsePolicies.
        :type selector: :class:`huaweicloudsdkcse.v1.GovSelector`
        """
        self._selector = selector

    @property
    def spec(self):
        """Gets the spec of this ListGovernancePolicyResponsePolicies.

        治理策略定义内容

        :return: The spec of this ListGovernancePolicyResponsePolicies.
        :rtype: object
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ListGovernancePolicyResponsePolicies.

        治理策略定义内容

        :param spec: The spec of this ListGovernancePolicyResponsePolicies.
        :type spec: object
        """
        self._spec = spec

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
        if not isinstance(other, ListGovernancePolicyResponsePolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
