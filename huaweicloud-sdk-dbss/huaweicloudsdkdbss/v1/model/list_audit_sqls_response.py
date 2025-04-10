# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAuditSqlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'count': 'int',
        'sqls': 'list[AuditSqlResponseSqls]'
    }

    attribute_map = {
        'total': 'total',
        'count': 'count',
        'sqls': 'sqls'
    }

    def __init__(self, total=None, count=None, sqls=None):
        r"""ListAuditSqlsResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param count: 总数
        :type count: int
        :param sqls: sql语句列表
        :type sqls: list[:class:`huaweicloudsdkdbss.v1.AuditSqlResponseSqls`]
        """
        
        super(ListAuditSqlsResponse, self).__init__()

        self._total = None
        self._count = None
        self._sqls = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if count is not None:
            self.count = count
        if sqls is not None:
            self.sqls = sqls

    @property
    def total(self):
        r"""Gets the total of this ListAuditSqlsResponse.

        总数

        :return: The total of this ListAuditSqlsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListAuditSqlsResponse.

        总数

        :param total: The total of this ListAuditSqlsResponse.
        :type total: int
        """
        self._total = total

    @property
    def count(self):
        r"""Gets the count of this ListAuditSqlsResponse.

        总数

        :return: The count of this ListAuditSqlsResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListAuditSqlsResponse.

        总数

        :param count: The count of this ListAuditSqlsResponse.
        :type count: int
        """
        self._count = count

    @property
    def sqls(self):
        r"""Gets the sqls of this ListAuditSqlsResponse.

        sql语句列表

        :return: The sqls of this ListAuditSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkdbss.v1.AuditSqlResponseSqls`]
        """
        return self._sqls

    @sqls.setter
    def sqls(self, sqls):
        r"""Sets the sqls of this ListAuditSqlsResponse.

        sql语句列表

        :param sqls: The sqls of this ListAuditSqlsResponse.
        :type sqls: list[:class:`huaweicloudsdkdbss.v1.AuditSqlResponseSqls`]
        """
        self._sqls = sqls

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
        if not isinstance(other, ListAuditSqlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
