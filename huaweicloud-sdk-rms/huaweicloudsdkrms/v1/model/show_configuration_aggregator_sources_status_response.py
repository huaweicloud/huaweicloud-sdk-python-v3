# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigurationAggregatorSourcesStatusResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregated_source_statuses': 'list[AggregatedSourceStatus]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'aggregated_source_statuses': 'aggregated_source_statuses',
        'page_info': 'page_info'
    }

    def __init__(self, aggregated_source_statuses=None, page_info=None):
        """ShowConfigurationAggregatorSourcesStatusResponse

        The model defined in huaweicloud sdk

        :param aggregated_source_statuses: 资源聚合器状态列表。
        :type aggregated_source_statuses: list[:class:`huaweicloudsdkrms.v1.AggregatedSourceStatus`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        
        super(ShowConfigurationAggregatorSourcesStatusResponse, self).__init__()

        self._aggregated_source_statuses = None
        self._page_info = None
        self.discriminator = None

        if aggregated_source_statuses is not None:
            self.aggregated_source_statuses = aggregated_source_statuses
        if page_info is not None:
            self.page_info = page_info

    @property
    def aggregated_source_statuses(self):
        """Gets the aggregated_source_statuses of this ShowConfigurationAggregatorSourcesStatusResponse.

        资源聚合器状态列表。

        :return: The aggregated_source_statuses of this ShowConfigurationAggregatorSourcesStatusResponse.
        :rtype: list[:class:`huaweicloudsdkrms.v1.AggregatedSourceStatus`]
        """
        return self._aggregated_source_statuses

    @aggregated_source_statuses.setter
    def aggregated_source_statuses(self, aggregated_source_statuses):
        """Sets the aggregated_source_statuses of this ShowConfigurationAggregatorSourcesStatusResponse.

        资源聚合器状态列表。

        :param aggregated_source_statuses: The aggregated_source_statuses of this ShowConfigurationAggregatorSourcesStatusResponse.
        :type aggregated_source_statuses: list[:class:`huaweicloudsdkrms.v1.AggregatedSourceStatus`]
        """
        self._aggregated_source_statuses = aggregated_source_statuses

    @property
    def page_info(self):
        """Gets the page_info of this ShowConfigurationAggregatorSourcesStatusResponse.

        :return: The page_info of this ShowConfigurationAggregatorSourcesStatusResponse.
        :rtype: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ShowConfigurationAggregatorSourcesStatusResponse.

        :param page_info: The page_info of this ShowConfigurationAggregatorSourcesStatusResponse.
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        self._page_info = page_info

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
        if not isinstance(other, ShowConfigurationAggregatorSourcesStatusResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
