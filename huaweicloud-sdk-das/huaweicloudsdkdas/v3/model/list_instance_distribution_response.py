# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceDistributionResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'engine_distribution': 'list[InstanceEngineDistributionListEngineDistribution]'
    }

    attribute_map = {
        'total': 'total',
        'engine_distribution': 'engine_distribution'
    }

    def __init__(self, total=None, engine_distribution=None):
        """ListInstanceDistributionResponse

        The model defined in huaweicloud sdk

        :param total: 总数
        :type total: int
        :param engine_distribution: 引擎分布
        :type engine_distribution: list[:class:`huaweicloudsdkdas.v3.InstanceEngineDistributionListEngineDistribution`]
        """
        
        super(ListInstanceDistributionResponse, self).__init__()

        self._total = None
        self._engine_distribution = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if engine_distribution is not None:
            self.engine_distribution = engine_distribution

    @property
    def total(self):
        """Gets the total of this ListInstanceDistributionResponse.

        总数

        :return: The total of this ListInstanceDistributionResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        """Sets the total of this ListInstanceDistributionResponse.

        总数

        :param total: The total of this ListInstanceDistributionResponse.
        :type total: int
        """
        self._total = total

    @property
    def engine_distribution(self):
        """Gets the engine_distribution of this ListInstanceDistributionResponse.

        引擎分布

        :return: The engine_distribution of this ListInstanceDistributionResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.InstanceEngineDistributionListEngineDistribution`]
        """
        return self._engine_distribution

    @engine_distribution.setter
    def engine_distribution(self, engine_distribution):
        """Sets the engine_distribution of this ListInstanceDistributionResponse.

        引擎分布

        :param engine_distribution: The engine_distribution of this ListInstanceDistributionResponse.
        :type engine_distribution: list[:class:`huaweicloudsdkdas.v3.InstanceEngineDistributionListEngineDistribution`]
        """
        self._engine_distribution = engine_distribution

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
        if not isinstance(other, ListInstanceDistributionResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
