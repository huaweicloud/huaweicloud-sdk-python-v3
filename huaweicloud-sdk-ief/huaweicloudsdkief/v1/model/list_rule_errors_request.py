# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRuleErrorsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ief_instance_id': 'str',
        'rule_id': 'str',
        'limit': 'int',
        'offset': 'int'
    }

    attribute_map = {
        'ief_instance_id': 'ief-instance-id',
        'rule_id': 'rule_id',
        'limit': 'limit',
        'offset': 'offset'
    }

    def __init__(self, ief_instance_id=None, rule_id=None, limit=None, offset=None):
        """ListRuleErrorsRequest

        The model defined in huaweicloud sdk

        :param ief_instance_id: 铂金版实例ID，专业版实例为空值
        :type ief_instance_id: str
        :param rule_id: 规则ID
        :type rule_id: str
        :param limit: 查询返回记录的数量限制
        :type limit: int
        :param offset: 偏移量，表示查询该偏移量后面的记录
        :type offset: int
        """
        
        

        self._ief_instance_id = None
        self._rule_id = None
        self._limit = None
        self._offset = None
        self.discriminator = None

        if ief_instance_id is not None:
            self.ief_instance_id = ief_instance_id
        self.rule_id = rule_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset

    @property
    def ief_instance_id(self):
        """Gets the ief_instance_id of this ListRuleErrorsRequest.

        铂金版实例ID，专业版实例为空值

        :return: The ief_instance_id of this ListRuleErrorsRequest.
        :rtype: str
        """
        return self._ief_instance_id

    @ief_instance_id.setter
    def ief_instance_id(self, ief_instance_id):
        """Sets the ief_instance_id of this ListRuleErrorsRequest.

        铂金版实例ID，专业版实例为空值

        :param ief_instance_id: The ief_instance_id of this ListRuleErrorsRequest.
        :type ief_instance_id: str
        """
        self._ief_instance_id = ief_instance_id

    @property
    def rule_id(self):
        """Gets the rule_id of this ListRuleErrorsRequest.

        规则ID

        :return: The rule_id of this ListRuleErrorsRequest.
        :rtype: str
        """
        return self._rule_id

    @rule_id.setter
    def rule_id(self, rule_id):
        """Sets the rule_id of this ListRuleErrorsRequest.

        规则ID

        :param rule_id: The rule_id of this ListRuleErrorsRequest.
        :type rule_id: str
        """
        self._rule_id = rule_id

    @property
    def limit(self):
        """Gets the limit of this ListRuleErrorsRequest.

        查询返回记录的数量限制

        :return: The limit of this ListRuleErrorsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListRuleErrorsRequest.

        查询返回记录的数量限制

        :param limit: The limit of this ListRuleErrorsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListRuleErrorsRequest.

        偏移量，表示查询该偏移量后面的记录

        :return: The offset of this ListRuleErrorsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListRuleErrorsRequest.

        偏移量，表示查询该偏移量后面的记录

        :param offset: The offset of this ListRuleErrorsRequest.
        :type offset: int
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
        if not isinstance(other, ListRuleErrorsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
