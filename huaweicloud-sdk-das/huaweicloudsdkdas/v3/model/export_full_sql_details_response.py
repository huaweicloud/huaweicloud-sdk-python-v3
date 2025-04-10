# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExportFullSqlDetailsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'full_sql_details': 'list[FullSqlDetail]',
        'total': 'int'
    }

    attribute_map = {
        'full_sql_details': 'full_sql_details',
        'total': 'total'
    }

    def __init__(self, full_sql_details=None, total=None):
        r"""ExportFullSqlDetailsResponse

        The model defined in huaweicloud sdk

        :param full_sql_details: 全量SQL明细列表。
        :type full_sql_details: list[:class:`huaweicloudsdkdas.v3.FullSqlDetail`]
        :param total: 总数。
        :type total: int
        """
        
        super(ExportFullSqlDetailsResponse, self).__init__()

        self._full_sql_details = None
        self._total = None
        self.discriminator = None

        if full_sql_details is not None:
            self.full_sql_details = full_sql_details
        if total is not None:
            self.total = total

    @property
    def full_sql_details(self):
        r"""Gets the full_sql_details of this ExportFullSqlDetailsResponse.

        全量SQL明细列表。

        :return: The full_sql_details of this ExportFullSqlDetailsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.FullSqlDetail`]
        """
        return self._full_sql_details

    @full_sql_details.setter
    def full_sql_details(self, full_sql_details):
        r"""Sets the full_sql_details of this ExportFullSqlDetailsResponse.

        全量SQL明细列表。

        :param full_sql_details: The full_sql_details of this ExportFullSqlDetailsResponse.
        :type full_sql_details: list[:class:`huaweicloudsdkdas.v3.FullSqlDetail`]
        """
        self._full_sql_details = full_sql_details

    @property
    def total(self):
        r"""Gets the total of this ExportFullSqlDetailsResponse.

        总数。

        :return: The total of this ExportFullSqlDetailsResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ExportFullSqlDetailsResponse.

        总数。

        :param total: The total of this ExportFullSqlDetailsResponse.
        :type total: int
        """
        self._total = total

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
        if not isinstance(other, ExportFullSqlDetailsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
