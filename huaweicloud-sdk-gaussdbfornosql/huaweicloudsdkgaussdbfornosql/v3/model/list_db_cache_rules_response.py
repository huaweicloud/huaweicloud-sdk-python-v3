# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbCacheRulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'dbcache_mapping_id': 'str',
        'rules': 'list[QueryDBCacheRuleResponse]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'dbcache_mapping_id': 'dbcache_mapping_id',
        'rules': 'rules'
    }

    def __init__(self, total_count=None, dbcache_mapping_id=None, rules=None):
        r"""ListDbCacheRulesResponse

        The model defined in huaweicloud sdk

        :param total_count: 总记录数。
        :type total_count: int
        :param dbcache_mapping_id: 内存加速映射ID。
        :type dbcache_mapping_id: str
        :param rules: 内存加速规则详情。
        :type rules: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDBCacheRuleResponse`]
        """
        
        super(ListDbCacheRulesResponse, self).__init__()

        self._total_count = None
        self._dbcache_mapping_id = None
        self._rules = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if dbcache_mapping_id is not None:
            self.dbcache_mapping_id = dbcache_mapping_id
        if rules is not None:
            self.rules = rules

    @property
    def total_count(self):
        r"""Gets the total_count of this ListDbCacheRulesResponse.

        总记录数。

        :return: The total_count of this ListDbCacheRulesResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ListDbCacheRulesResponse.

        总记录数。

        :param total_count: The total_count of this ListDbCacheRulesResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def dbcache_mapping_id(self):
        r"""Gets the dbcache_mapping_id of this ListDbCacheRulesResponse.

        内存加速映射ID。

        :return: The dbcache_mapping_id of this ListDbCacheRulesResponse.
        :rtype: str
        """
        return self._dbcache_mapping_id

    @dbcache_mapping_id.setter
    def dbcache_mapping_id(self, dbcache_mapping_id):
        r"""Sets the dbcache_mapping_id of this ListDbCacheRulesResponse.

        内存加速映射ID。

        :param dbcache_mapping_id: The dbcache_mapping_id of this ListDbCacheRulesResponse.
        :type dbcache_mapping_id: str
        """
        self._dbcache_mapping_id = dbcache_mapping_id

    @property
    def rules(self):
        r"""Gets the rules of this ListDbCacheRulesResponse.

        内存加速规则详情。

        :return: The rules of this ListDbCacheRulesResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDBCacheRuleResponse`]
        """
        return self._rules

    @rules.setter
    def rules(self, rules):
        r"""Sets the rules of this ListDbCacheRulesResponse.

        内存加速规则详情。

        :param rules: The rules of this ListDbCacheRulesResponse.
        :type rules: list[:class:`huaweicloudsdkgaussdbfornosql.v3.QueryDBCacheRuleResponse`]
        """
        self._rules = rules

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
        if not isinstance(other, ListDbCacheRulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
