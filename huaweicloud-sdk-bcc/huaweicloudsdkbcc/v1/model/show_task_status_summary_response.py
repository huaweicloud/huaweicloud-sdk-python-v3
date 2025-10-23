# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTaskStatusSummaryResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'filter': 'ShowTaskStatusSummaryResponseBodyFilter',
        'summary': 'ShowTaskStatusSummaryResponseBodySummary',
        'count': 'int',
        'datapoints': 'list[ShowTaskStatusSummaryResponseBodyDatapoints]'
    }

    attribute_map = {
        'filter': 'filter',
        'summary': 'summary',
        'count': 'count',
        'datapoints': 'datapoints'
    }

    def __init__(self, filter=None, summary=None, count=None, datapoints=None):
        r"""ShowTaskStatusSummaryResponse

        The model defined in huaweicloud sdk

        :param filter: 
        :type filter: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodyFilter`
        :param summary: 
        :type summary: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodySummary`
        :param count: 打点数据的条数
        :type count: int
        :param datapoints: 打点数据
        :type datapoints: list[:class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodyDatapoints`]
        """
        
        super(ShowTaskStatusSummaryResponse, self).__init__()

        self._filter = None
        self._summary = None
        self._count = None
        self._datapoints = None
        self.discriminator = None

        if filter is not None:
            self.filter = filter
        if summary is not None:
            self.summary = summary
        if count is not None:
            self.count = count
        if datapoints is not None:
            self.datapoints = datapoints

    @property
    def filter(self):
        r"""Gets the filter of this ShowTaskStatusSummaryResponse.

        :return: The filter of this ShowTaskStatusSummaryResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodyFilter`
        """
        return self._filter

    @filter.setter
    def filter(self, filter):
        r"""Sets the filter of this ShowTaskStatusSummaryResponse.

        :param filter: The filter of this ShowTaskStatusSummaryResponse.
        :type filter: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodyFilter`
        """
        self._filter = filter

    @property
    def summary(self):
        r"""Gets the summary of this ShowTaskStatusSummaryResponse.

        :return: The summary of this ShowTaskStatusSummaryResponse.
        :rtype: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodySummary`
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        r"""Sets the summary of this ShowTaskStatusSummaryResponse.

        :param summary: The summary of this ShowTaskStatusSummaryResponse.
        :type summary: :class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodySummary`
        """
        self._summary = summary

    @property
    def count(self):
        r"""Gets the count of this ShowTaskStatusSummaryResponse.

        打点数据的条数

        :return: The count of this ShowTaskStatusSummaryResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowTaskStatusSummaryResponse.

        打点数据的条数

        :param count: The count of this ShowTaskStatusSummaryResponse.
        :type count: int
        """
        self._count = count

    @property
    def datapoints(self):
        r"""Gets the datapoints of this ShowTaskStatusSummaryResponse.

        打点数据

        :return: The datapoints of this ShowTaskStatusSummaryResponse.
        :rtype: list[:class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodyDatapoints`]
        """
        return self._datapoints

    @datapoints.setter
    def datapoints(self, datapoints):
        r"""Sets the datapoints of this ShowTaskStatusSummaryResponse.

        打点数据

        :param datapoints: The datapoints of this ShowTaskStatusSummaryResponse.
        :type datapoints: list[:class:`huaweicloudsdkbcc.v1.ShowTaskStatusSummaryResponseBodyDatapoints`]
        """
        self._datapoints = datapoints

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
        if not isinstance(other, ShowTaskStatusSummaryResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
