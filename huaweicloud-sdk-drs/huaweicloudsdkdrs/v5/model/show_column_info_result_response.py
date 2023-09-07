# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowColumnInfoResultResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'results': 'list[DbObjectColumnInfo]',
        'total_count': 'int'
    }

    attribute_map = {
        'results': 'results',
        'total_count': 'total_count'
    }

    def __init__(self, results=None, total_count=None):
        """ShowColumnInfoResultResponse

        The model defined in huaweicloud sdk

        :param results: 指定数据库表列信息
        :type results: list[:class:`huaweicloudsdkdrs.v5.DbObjectColumnInfo`]
        :param total_count: 列表中的项目总数，与分页无关
        :type total_count: int
        """
        
        super(ShowColumnInfoResultResponse, self).__init__()

        self._results = None
        self._total_count = None
        self.discriminator = None

        if results is not None:
            self.results = results
        if total_count is not None:
            self.total_count = total_count

    @property
    def results(self):
        """Gets the results of this ShowColumnInfoResultResponse.

        指定数据库表列信息

        :return: The results of this ShowColumnInfoResultResponse.
        :rtype: list[:class:`huaweicloudsdkdrs.v5.DbObjectColumnInfo`]
        """
        return self._results

    @results.setter
    def results(self, results):
        """Sets the results of this ShowColumnInfoResultResponse.

        指定数据库表列信息

        :param results: The results of this ShowColumnInfoResultResponse.
        :type results: list[:class:`huaweicloudsdkdrs.v5.DbObjectColumnInfo`]
        """
        self._results = results

    @property
    def total_count(self):
        """Gets the total_count of this ShowColumnInfoResultResponse.

        列表中的项目总数，与分页无关

        :return: The total_count of this ShowColumnInfoResultResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this ShowColumnInfoResultResponse.

        列表中的项目总数，与分页无关

        :param total_count: The total_count of this ShowColumnInfoResultResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, ShowColumnInfoResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
