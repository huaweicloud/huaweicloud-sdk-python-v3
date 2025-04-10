# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlLimitResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'sql_limit_objects': 'list[SqlLimitObject]'
    }

    attribute_map = {
        'count': 'count',
        'sql_limit_objects': 'sql_limit_objects'
    }

    def __init__(self, count=None, sql_limit_objects=None):
        r"""ListSqlLimitResponse

        The model defined in huaweicloud sdk

        :param count: SQL限流总数
        :type count: int
        :param sql_limit_objects: SQL限流详情
        :type sql_limit_objects: list[:class:`huaweicloudsdkrds.v3.SqlLimitObject`]
        """
        
        super(ListSqlLimitResponse, self).__init__()

        self._count = None
        self._sql_limit_objects = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if sql_limit_objects is not None:
            self.sql_limit_objects = sql_limit_objects

    @property
    def count(self):
        r"""Gets the count of this ListSqlLimitResponse.

        SQL限流总数

        :return: The count of this ListSqlLimitResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ListSqlLimitResponse.

        SQL限流总数

        :param count: The count of this ListSqlLimitResponse.
        :type count: int
        """
        self._count = count

    @property
    def sql_limit_objects(self):
        r"""Gets the sql_limit_objects of this ListSqlLimitResponse.

        SQL限流详情

        :return: The sql_limit_objects of this ListSqlLimitResponse.
        :rtype: list[:class:`huaweicloudsdkrds.v3.SqlLimitObject`]
        """
        return self._sql_limit_objects

    @sql_limit_objects.setter
    def sql_limit_objects(self, sql_limit_objects):
        r"""Sets the sql_limit_objects of this ListSqlLimitResponse.

        SQL限流详情

        :param sql_limit_objects: The sql_limit_objects of this ListSqlLimitResponse.
        :type sql_limit_objects: list[:class:`huaweicloudsdkrds.v3.SqlLimitObject`]
        """
        self._sql_limit_objects = sql_limit_objects

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
        if not isinstance(other, ListSqlLimitResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
