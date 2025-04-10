# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConfigurationAggregatorResp:

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
        'aggregator_id': 'str',
        'aggregator_urn': 'str',
        'aggregator_type': 'str',
        'account_aggregation_sources': 'AccountAggregationSource',
        'updated_at': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'aggregator_name': 'aggregator_name',
        'aggregator_id': 'aggregator_id',
        'aggregator_urn': 'aggregator_urn',
        'aggregator_type': 'aggregator_type',
        'account_aggregation_sources': 'account_aggregation_sources',
        'updated_at': 'updated_at',
        'created_at': 'created_at'
    }

    def __init__(self, aggregator_name=None, aggregator_id=None, aggregator_urn=None, aggregator_type=None, account_aggregation_sources=None, updated_at=None, created_at=None):
        r"""ConfigurationAggregatorResp

        The model defined in huaweicloud sdk

        :param aggregator_name: 资源聚合器名称。
        :type aggregator_name: str
        :param aggregator_id: 资源聚合器ID。
        :type aggregator_id: str
        :param aggregator_urn: 资源聚合器标识符。
        :type aggregator_urn: str
        :param aggregator_type: 聚合器类型。
        :type aggregator_type: str
        :param account_aggregation_sources: 
        :type account_aggregation_sources: :class:`huaweicloudsdkrms.v1.AccountAggregationSource`
        :param updated_at: 资源聚合器更新时间。
        :type updated_at: str
        :param created_at: 资源聚合器创建时间。
        :type created_at: str
        """
        
        

        self._aggregator_name = None
        self._aggregator_id = None
        self._aggregator_urn = None
        self._aggregator_type = None
        self._account_aggregation_sources = None
        self._updated_at = None
        self._created_at = None
        self.discriminator = None

        if aggregator_name is not None:
            self.aggregator_name = aggregator_name
        if aggregator_id is not None:
            self.aggregator_id = aggregator_id
        if aggregator_urn is not None:
            self.aggregator_urn = aggregator_urn
        if aggregator_type is not None:
            self.aggregator_type = aggregator_type
        if account_aggregation_sources is not None:
            self.account_aggregation_sources = account_aggregation_sources
        if updated_at is not None:
            self.updated_at = updated_at
        if created_at is not None:
            self.created_at = created_at

    @property
    def aggregator_name(self):
        r"""Gets the aggregator_name of this ConfigurationAggregatorResp.

        资源聚合器名称。

        :return: The aggregator_name of this ConfigurationAggregatorResp.
        :rtype: str
        """
        return self._aggregator_name

    @aggregator_name.setter
    def aggregator_name(self, aggregator_name):
        r"""Sets the aggregator_name of this ConfigurationAggregatorResp.

        资源聚合器名称。

        :param aggregator_name: The aggregator_name of this ConfigurationAggregatorResp.
        :type aggregator_name: str
        """
        self._aggregator_name = aggregator_name

    @property
    def aggregator_id(self):
        r"""Gets the aggregator_id of this ConfigurationAggregatorResp.

        资源聚合器ID。

        :return: The aggregator_id of this ConfigurationAggregatorResp.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        r"""Sets the aggregator_id of this ConfigurationAggregatorResp.

        资源聚合器ID。

        :param aggregator_id: The aggregator_id of this ConfigurationAggregatorResp.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def aggregator_urn(self):
        r"""Gets the aggregator_urn of this ConfigurationAggregatorResp.

        资源聚合器标识符。

        :return: The aggregator_urn of this ConfigurationAggregatorResp.
        :rtype: str
        """
        return self._aggregator_urn

    @aggregator_urn.setter
    def aggregator_urn(self, aggregator_urn):
        r"""Sets the aggregator_urn of this ConfigurationAggregatorResp.

        资源聚合器标识符。

        :param aggregator_urn: The aggregator_urn of this ConfigurationAggregatorResp.
        :type aggregator_urn: str
        """
        self._aggregator_urn = aggregator_urn

    @property
    def aggregator_type(self):
        r"""Gets the aggregator_type of this ConfigurationAggregatorResp.

        聚合器类型。

        :return: The aggregator_type of this ConfigurationAggregatorResp.
        :rtype: str
        """
        return self._aggregator_type

    @aggregator_type.setter
    def aggregator_type(self, aggregator_type):
        r"""Sets the aggregator_type of this ConfigurationAggregatorResp.

        聚合器类型。

        :param aggregator_type: The aggregator_type of this ConfigurationAggregatorResp.
        :type aggregator_type: str
        """
        self._aggregator_type = aggregator_type

    @property
    def account_aggregation_sources(self):
        r"""Gets the account_aggregation_sources of this ConfigurationAggregatorResp.

        :return: The account_aggregation_sources of this ConfigurationAggregatorResp.
        :rtype: :class:`huaweicloudsdkrms.v1.AccountAggregationSource`
        """
        return self._account_aggregation_sources

    @account_aggregation_sources.setter
    def account_aggregation_sources(self, account_aggregation_sources):
        r"""Sets the account_aggregation_sources of this ConfigurationAggregatorResp.

        :param account_aggregation_sources: The account_aggregation_sources of this ConfigurationAggregatorResp.
        :type account_aggregation_sources: :class:`huaweicloudsdkrms.v1.AccountAggregationSource`
        """
        self._account_aggregation_sources = account_aggregation_sources

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ConfigurationAggregatorResp.

        资源聚合器更新时间。

        :return: The updated_at of this ConfigurationAggregatorResp.
        :rtype: str
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ConfigurationAggregatorResp.

        资源聚合器更新时间。

        :param updated_at: The updated_at of this ConfigurationAggregatorResp.
        :type updated_at: str
        """
        self._updated_at = updated_at

    @property
    def created_at(self):
        r"""Gets the created_at of this ConfigurationAggregatorResp.

        资源聚合器创建时间。

        :return: The created_at of this ConfigurationAggregatorResp.
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ConfigurationAggregatorResp.

        资源聚合器创建时间。

        :param created_at: The created_at of this ConfigurationAggregatorResp.
        :type created_at: str
        """
        self._created_at = created_at

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
        if not isinstance(other, ConfigurationAggregatorResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
