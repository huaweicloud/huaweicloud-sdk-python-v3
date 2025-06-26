# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateImmutableRuleRequest:

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
        'immutable_rule_id': 'int',
        'body': 'UpdateImmutableRuleBody'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'namespace_name': 'namespace_name',
        'immutable_rule_id': 'immutable_rule_id',
        'body': 'body'
    }

    def __init__(self, instance_id=None, namespace_name=None, immutable_rule_id=None, body=None):
        r"""UpdateImmutableRuleRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param namespace_name: 命名空间名称
        :type namespace_name: str
        :param immutable_rule_id: 不可变Tag策略ID
        :type immutable_rule_id: int
        :param body: Body of the UpdateImmutableRuleRequest
        :type body: :class:`huaweicloudsdkswr.v2.UpdateImmutableRuleBody`
        """
        
        

        self._instance_id = None
        self._namespace_name = None
        self._immutable_rule_id = None
        self._body = None
        self.discriminator = None

        self.instance_id = instance_id
        self.namespace_name = namespace_name
        self.immutable_rule_id = immutable_rule_id
        if body is not None:
            self.body = body

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateImmutableRuleRequest.

        企业仓库实例ID

        :return: The instance_id of this UpdateImmutableRuleRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateImmutableRuleRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this UpdateImmutableRuleRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def namespace_name(self):
        r"""Gets the namespace_name of this UpdateImmutableRuleRequest.

        命名空间名称

        :return: The namespace_name of this UpdateImmutableRuleRequest.
        :rtype: str
        """
        return self._namespace_name

    @namespace_name.setter
    def namespace_name(self, namespace_name):
        r"""Sets the namespace_name of this UpdateImmutableRuleRequest.

        命名空间名称

        :param namespace_name: The namespace_name of this UpdateImmutableRuleRequest.
        :type namespace_name: str
        """
        self._namespace_name = namespace_name

    @property
    def immutable_rule_id(self):
        r"""Gets the immutable_rule_id of this UpdateImmutableRuleRequest.

        不可变Tag策略ID

        :return: The immutable_rule_id of this UpdateImmutableRuleRequest.
        :rtype: int
        """
        return self._immutable_rule_id

    @immutable_rule_id.setter
    def immutable_rule_id(self, immutable_rule_id):
        r"""Sets the immutable_rule_id of this UpdateImmutableRuleRequest.

        不可变Tag策略ID

        :param immutable_rule_id: The immutable_rule_id of this UpdateImmutableRuleRequest.
        :type immutable_rule_id: int
        """
        self._immutable_rule_id = immutable_rule_id

    @property
    def body(self):
        r"""Gets the body of this UpdateImmutableRuleRequest.

        :return: The body of this UpdateImmutableRuleRequest.
        :rtype: :class:`huaweicloudsdkswr.v2.UpdateImmutableRuleBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateImmutableRuleRequest.

        :param body: The body of this UpdateImmutableRuleRequest.
        :type body: :class:`huaweicloudsdkswr.v2.UpdateImmutableRuleBody`
        """
        self._body = body

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
        if not isinstance(other, UpdateImmutableRuleRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
