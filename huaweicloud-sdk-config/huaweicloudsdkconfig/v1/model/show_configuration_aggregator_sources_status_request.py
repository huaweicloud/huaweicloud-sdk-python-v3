# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowConfigurationAggregatorSourcesStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aggregator_id': 'str',
        'update_status': 'str',
        'limit': 'int',
        'marker': 'str'
    }

    attribute_map = {
        'aggregator_id': 'aggregator_id',
        'update_status': 'update_status',
        'limit': 'limit',
        'marker': 'marker'
    }

    def __init__(self, aggregator_id=None, update_status=None, limit=None, marker=None):
        r"""ShowConfigurationAggregatorSourcesStatusRequest

        The model defined in huaweicloud sdk

        :param aggregator_id: 资源聚合器ID。
        :type aggregator_id: str
        :param update_status: 聚合帐号的状态。
        :type update_status: str
        :param limit: 最大的返回数量
        :type limit: int
        :param marker: 分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页
        :type marker: str
        """
        
        

        self._aggregator_id = None
        self._update_status = None
        self._limit = None
        self._marker = None
        self.discriminator = None

        self.aggregator_id = aggregator_id
        if update_status is not None:
            self.update_status = update_status
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker

    @property
    def aggregator_id(self):
        r"""Gets the aggregator_id of this ShowConfigurationAggregatorSourcesStatusRequest.

        资源聚合器ID。

        :return: The aggregator_id of this ShowConfigurationAggregatorSourcesStatusRequest.
        :rtype: str
        """
        return self._aggregator_id

    @aggregator_id.setter
    def aggregator_id(self, aggregator_id):
        r"""Sets the aggregator_id of this ShowConfigurationAggregatorSourcesStatusRequest.

        资源聚合器ID。

        :param aggregator_id: The aggregator_id of this ShowConfigurationAggregatorSourcesStatusRequest.
        :type aggregator_id: str
        """
        self._aggregator_id = aggregator_id

    @property
    def update_status(self):
        r"""Gets the update_status of this ShowConfigurationAggregatorSourcesStatusRequest.

        聚合帐号的状态。

        :return: The update_status of this ShowConfigurationAggregatorSourcesStatusRequest.
        :rtype: str
        """
        return self._update_status

    @update_status.setter
    def update_status(self, update_status):
        r"""Sets the update_status of this ShowConfigurationAggregatorSourcesStatusRequest.

        聚合帐号的状态。

        :param update_status: The update_status of this ShowConfigurationAggregatorSourcesStatusRequest.
        :type update_status: str
        """
        self._update_status = update_status

    @property
    def limit(self):
        r"""Gets the limit of this ShowConfigurationAggregatorSourcesStatusRequest.

        最大的返回数量

        :return: The limit of this ShowConfigurationAggregatorSourcesStatusRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ShowConfigurationAggregatorSourcesStatusRequest.

        最大的返回数量

        :param limit: The limit of this ShowConfigurationAggregatorSourcesStatusRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ShowConfigurationAggregatorSourcesStatusRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :return: The marker of this ShowConfigurationAggregatorSourcesStatusRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ShowConfigurationAggregatorSourcesStatusRequest.

        分页参数，通过上一个请求中返回的marker信息作为输入，获取当前页

        :param marker: The marker of this ShowConfigurationAggregatorSourcesStatusRequest.
        :type marker: str
        """
        self._marker = marker

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
        if not isinstance(other, ShowConfigurationAggregatorSourcesStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
