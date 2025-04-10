# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlFilterRuleResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'node_id': 'str',
        'sql_filter_rules': 'list[SqlFilterRule]'
    }

    attribute_map = {
        'node_id': 'node_id',
        'sql_filter_rules': 'sql_filter_rules'
    }

    def __init__(self, node_id=None, sql_filter_rules=None):
        r"""ShowSqlFilterRuleResponse

        The model defined in huaweicloud sdk

        :param node_id: 节点ID
        :type node_id: str
        :param sql_filter_rules: SQL限流规则
        :type sql_filter_rules: list[:class:`huaweicloudsdkgaussdb.v3.SqlFilterRule`]
        """
        
        super(ShowSqlFilterRuleResponse, self).__init__()

        self._node_id = None
        self._sql_filter_rules = None
        self.discriminator = None

        if node_id is not None:
            self.node_id = node_id
        if sql_filter_rules is not None:
            self.sql_filter_rules = sql_filter_rules

    @property
    def node_id(self):
        r"""Gets the node_id of this ShowSqlFilterRuleResponse.

        节点ID

        :return: The node_id of this ShowSqlFilterRuleResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this ShowSqlFilterRuleResponse.

        节点ID

        :param node_id: The node_id of this ShowSqlFilterRuleResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def sql_filter_rules(self):
        r"""Gets the sql_filter_rules of this ShowSqlFilterRuleResponse.

        SQL限流规则

        :return: The sql_filter_rules of this ShowSqlFilterRuleResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.SqlFilterRule`]
        """
        return self._sql_filter_rules

    @sql_filter_rules.setter
    def sql_filter_rules(self, sql_filter_rules):
        r"""Sets the sql_filter_rules of this ShowSqlFilterRuleResponse.

        SQL限流规则

        :param sql_filter_rules: The sql_filter_rules of this ShowSqlFilterRuleResponse.
        :type sql_filter_rules: list[:class:`huaweicloudsdkgaussdb.v3.SqlFilterRule`]
        """
        self._sql_filter_rules = sql_filter_rules

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
        if not isinstance(other, ShowSqlFilterRuleResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
