# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSqlResultWithJobResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_results': 'object'
    }

    attribute_map = {
        'sql_results': 'sql_results'
    }

    def __init__(self, sql_results=None):
        r"""ShowSqlResultWithJobResponse

        The model defined in huaweicloud sdk

        :param sql_results: SQL语句查询结果。
        :type sql_results: object
        """
        
        super(ShowSqlResultWithJobResponse, self).__init__()

        self._sql_results = None
        self.discriminator = None

        if sql_results is not None:
            self.sql_results = sql_results

    @property
    def sql_results(self):
        r"""Gets the sql_results of this ShowSqlResultWithJobResponse.

        SQL语句查询结果。

        :return: The sql_results of this ShowSqlResultWithJobResponse.
        :rtype: object
        """
        return self._sql_results

    @sql_results.setter
    def sql_results(self, sql_results):
        r"""Sets the sql_results of this ShowSqlResultWithJobResponse.

        SQL语句查询结果。

        :param sql_results: The sql_results of this ShowSqlResultWithJobResponse.
        :type sql_results: object
        """
        self._sql_results = sql_results

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
        if not isinstance(other, ShowSqlResultWithJobResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
