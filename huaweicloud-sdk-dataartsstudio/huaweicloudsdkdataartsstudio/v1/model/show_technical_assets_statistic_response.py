# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTechnicalAssetsStatisticResponse(SdkResponse):

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
        'datasource_statistics': 'list[DataSource]'
    }

    attribute_map = {
        'count': 'count',
        'datasource_statistics': 'datasource_statistics'
    }

    def __init__(self, count=None, datasource_statistics=None):
        r"""ShowTechnicalAssetsStatisticResponse

        The model defined in huaweicloud sdk

        :param count: 数据连接总数
        :type count: int
        :param datasource_statistics: 数据连接统计信息
        :type datasource_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.DataSource`]
        """
        
        super(ShowTechnicalAssetsStatisticResponse, self).__init__()

        self._count = None
        self._datasource_statistics = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if datasource_statistics is not None:
            self.datasource_statistics = datasource_statistics

    @property
    def count(self):
        r"""Gets the count of this ShowTechnicalAssetsStatisticResponse.

        数据连接总数

        :return: The count of this ShowTechnicalAssetsStatisticResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowTechnicalAssetsStatisticResponse.

        数据连接总数

        :param count: The count of this ShowTechnicalAssetsStatisticResponse.
        :type count: int
        """
        self._count = count

    @property
    def datasource_statistics(self):
        r"""Gets the datasource_statistics of this ShowTechnicalAssetsStatisticResponse.

        数据连接统计信息

        :return: The datasource_statistics of this ShowTechnicalAssetsStatisticResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.DataSource`]
        """
        return self._datasource_statistics

    @datasource_statistics.setter
    def datasource_statistics(self, datasource_statistics):
        r"""Sets the datasource_statistics of this ShowTechnicalAssetsStatisticResponse.

        数据连接统计信息

        :param datasource_statistics: The datasource_statistics of this ShowTechnicalAssetsStatisticResponse.
        :type datasource_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.DataSource`]
        """
        self._datasource_statistics = datasource_statistics

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
        if not isinstance(other, ShowTechnicalAssetsStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
