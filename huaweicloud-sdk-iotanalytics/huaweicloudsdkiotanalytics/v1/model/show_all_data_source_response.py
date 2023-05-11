# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAllDataSourceResponse(SdkResponse):

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
        'datasources': 'list[DatasourceRestDTO]'
    }

    attribute_map = {
        'count': 'count',
        'datasources': 'datasources'
    }

    def __init__(self, count=None, datasources=None):
        """ShowAllDataSourceResponse

        The model defined in huaweicloud sdk

        :param count: 总数
        :type count: int
        :param datasources: 数据源列表
        :type datasources: list[:class:`huaweicloudsdkiotanalytics.v1.DatasourceRestDTO`]
        """
        
        super(ShowAllDataSourceResponse, self).__init__()

        self._count = None
        self._datasources = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if datasources is not None:
            self.datasources = datasources

    @property
    def count(self):
        """Gets the count of this ShowAllDataSourceResponse.

        总数

        :return: The count of this ShowAllDataSourceResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this ShowAllDataSourceResponse.

        总数

        :param count: The count of this ShowAllDataSourceResponse.
        :type count: int
        """
        self._count = count

    @property
    def datasources(self):
        """Gets the datasources of this ShowAllDataSourceResponse.

        数据源列表

        :return: The datasources of this ShowAllDataSourceResponse.
        :rtype: list[:class:`huaweicloudsdkiotanalytics.v1.DatasourceRestDTO`]
        """
        return self._datasources

    @datasources.setter
    def datasources(self, datasources):
        """Sets the datasources of this ShowAllDataSourceResponse.

        数据源列表

        :param datasources: The datasources of this ShowAllDataSourceResponse.
        :type datasources: list[:class:`huaweicloudsdkiotanalytics.v1.DatasourceRestDTO`]
        """
        self._datasources = datasources

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
        if not isinstance(other, ShowAllDataSourceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
