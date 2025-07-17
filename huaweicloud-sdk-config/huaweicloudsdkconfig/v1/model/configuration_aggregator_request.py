# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationAggregatorRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregator_name': 'str',
        'aggregator_type': 'str',
        'account_aggregation_sources': 'AccountAggregationSource',
        'tags': 'list[ResourceTag]'
    }

    attribute_map = {
        'aggregator_name': 'aggregator_name',
        'aggregator_type': 'aggregator_type',
        'account_aggregation_sources': 'account_aggregation_sources',
        'tags': 'tags'
    }

    def __init__(self, aggregator_name=None, aggregator_type=None, account_aggregation_sources=None, tags=None):
        r"""ConfigurationAggregatorRequest

        The model defined in huaweicloud sdk

        :param aggregator_name: 资源聚合器名称。
        :type aggregator_name: str
        :param aggregator_type: 聚合器类型（ACCOUNT | ORGANIZATION）。
        :type aggregator_type: str
        :param account_aggregation_sources: 
        :type account_aggregation_sources: :class:`huaweicloudsdkconfig.v1.AccountAggregationSource`
        :param tags: 标签列表
        :type tags: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        
        

        self._aggregator_name = None
        self._aggregator_type = None
        self._account_aggregation_sources = None
        self._tags = None
        self.discriminator = None

        self.aggregator_name = aggregator_name
        self.aggregator_type = aggregator_type
        if account_aggregation_sources is not None:
            self.account_aggregation_sources = account_aggregation_sources
        if tags is not None:
            self.tags = tags

    @property
    def aggregator_name(self):
        r"""Gets the aggregator_name of this ConfigurationAggregatorRequest.

        资源聚合器名称。

        :return: The aggregator_name of this ConfigurationAggregatorRequest.
        :rtype: str
        """
        return self._aggregator_name

    @aggregator_name.setter
    def aggregator_name(self, aggregator_name):
        r"""Sets the aggregator_name of this ConfigurationAggregatorRequest.

        资源聚合器名称。

        :param aggregator_name: The aggregator_name of this ConfigurationAggregatorRequest.
        :type aggregator_name: str
        """
        self._aggregator_name = aggregator_name

    @property
    def aggregator_type(self):
        r"""Gets the aggregator_type of this ConfigurationAggregatorRequest.

        聚合器类型（ACCOUNT | ORGANIZATION）。

        :return: The aggregator_type of this ConfigurationAggregatorRequest.
        :rtype: str
        """
        return self._aggregator_type

    @aggregator_type.setter
    def aggregator_type(self, aggregator_type):
        r"""Sets the aggregator_type of this ConfigurationAggregatorRequest.

        聚合器类型（ACCOUNT | ORGANIZATION）。

        :param aggregator_type: The aggregator_type of this ConfigurationAggregatorRequest.
        :type aggregator_type: str
        """
        self._aggregator_type = aggregator_type

    @property
    def account_aggregation_sources(self):
        r"""Gets the account_aggregation_sources of this ConfigurationAggregatorRequest.

        :return: The account_aggregation_sources of this ConfigurationAggregatorRequest.
        :rtype: :class:`huaweicloudsdkconfig.v1.AccountAggregationSource`
        """
        return self._account_aggregation_sources

    @account_aggregation_sources.setter
    def account_aggregation_sources(self, account_aggregation_sources):
        r"""Sets the account_aggregation_sources of this ConfigurationAggregatorRequest.

        :param account_aggregation_sources: The account_aggregation_sources of this ConfigurationAggregatorRequest.
        :type account_aggregation_sources: :class:`huaweicloudsdkconfig.v1.AccountAggregationSource`
        """
        self._account_aggregation_sources = account_aggregation_sources

    @property
    def tags(self):
        r"""Gets the tags of this ConfigurationAggregatorRequest.

        标签列表

        :return: The tags of this ConfigurationAggregatorRequest.
        :rtype: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this ConfigurationAggregatorRequest.

        标签列表

        :param tags: The tags of this ConfigurationAggregatorRequest.
        :type tags: list[:class:`huaweicloudsdkconfig.v1.ResourceTag`]
        """
        self._tags = tags

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
        if not isinstance(other, ConfigurationAggregatorRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
