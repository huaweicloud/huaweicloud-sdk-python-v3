# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListConfigurationAggregatorsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'configuration_aggregators': 'list[ConfigurationAggregatorResp]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'configuration_aggregators': 'configuration_aggregators',
        'page_info': 'page_info'
    }

    def __init__(self, configuration_aggregators=None, page_info=None):
        """ListConfigurationAggregatorsResponse

        The model defined in huaweicloud sdk

        :param configuration_aggregators: 资源聚合器列表。
        :type configuration_aggregators: list[:class:`huaweicloudsdkrms.v1.ConfigurationAggregatorResp`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        
        super(ListConfigurationAggregatorsResponse, self).__init__()

        self._configuration_aggregators = None
        self._page_info = None
        self.discriminator = None

        if configuration_aggregators is not None:
            self.configuration_aggregators = configuration_aggregators
        if page_info is not None:
            self.page_info = page_info

    @property
    def configuration_aggregators(self):
        """Gets the configuration_aggregators of this ListConfigurationAggregatorsResponse.

        资源聚合器列表。

        :return: The configuration_aggregators of this ListConfigurationAggregatorsResponse.
        :rtype: list[:class:`huaweicloudsdkrms.v1.ConfigurationAggregatorResp`]
        """
        return self._configuration_aggregators

    @configuration_aggregators.setter
    def configuration_aggregators(self, configuration_aggregators):
        """Sets the configuration_aggregators of this ListConfigurationAggregatorsResponse.

        资源聚合器列表。

        :param configuration_aggregators: The configuration_aggregators of this ListConfigurationAggregatorsResponse.
        :type configuration_aggregators: list[:class:`huaweicloudsdkrms.v1.ConfigurationAggregatorResp`]
        """
        self._configuration_aggregators = configuration_aggregators

    @property
    def page_info(self):
        """Gets the page_info of this ListConfigurationAggregatorsResponse.

        :return: The page_info of this ListConfigurationAggregatorsResponse.
        :rtype: :class:`huaweicloudsdkrms.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        """Sets the page_info of this ListConfigurationAggregatorsResponse.

        :param page_info: The page_info of this ListConfigurationAggregatorsResponse.
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
        if not isinstance(other, ListConfigurationAggregatorsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
