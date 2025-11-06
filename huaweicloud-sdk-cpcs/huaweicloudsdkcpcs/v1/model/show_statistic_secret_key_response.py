# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowStatisticSecretKeyResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total_count': 'int',
        'invalid_count': 'int',
        'valid_count': 'int',
        'key_counts_by_service_type': 'list[VendorKeyStatistic]',
        'key_counts_by_algorithm': 'list[VendorKeyStatistic]',
        'key_counts_by_algorithm_and_cluster': 'list[VendorKeyStatistic]'
    }

    attribute_map = {
        'total_count': 'total_count',
        'invalid_count': 'invalid_count',
        'valid_count': 'valid_count',
        'key_counts_by_service_type': 'key_counts_by_service_type',
        'key_counts_by_algorithm': 'key_counts_by_algorithm',
        'key_counts_by_algorithm_and_cluster': 'key_counts_by_algorithm_and_cluster'
    }

    def __init__(self, total_count=None, invalid_count=None, valid_count=None, key_counts_by_service_type=None, key_counts_by_algorithm=None, key_counts_by_algorithm_and_cluster=None):
        r"""ShowStatisticSecretKeyResponse

        The model defined in huaweicloud sdk

        :param total_count: 总数量
        :type total_count: int
        :param invalid_count: 无效数量
        :type invalid_count: int
        :param valid_count: 有效数量
        :type valid_count: int
        :param key_counts_by_service_type: 密钥分布按服务类型统计
        :type key_counts_by_service_type: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        :param key_counts_by_algorithm: 密钥分布按算法统计
        :type key_counts_by_algorithm: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        :param key_counts_by_algorithm_and_cluster: 密钥分布按算法和集群统计
        :type key_counts_by_algorithm_and_cluster: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        
        super().__init__()

        self._total_count = None
        self._invalid_count = None
        self._valid_count = None
        self._key_counts_by_service_type = None
        self._key_counts_by_algorithm = None
        self._key_counts_by_algorithm_and_cluster = None
        self.discriminator = None

        if total_count is not None:
            self.total_count = total_count
        if invalid_count is not None:
            self.invalid_count = invalid_count
        if valid_count is not None:
            self.valid_count = valid_count
        if key_counts_by_service_type is not None:
            self.key_counts_by_service_type = key_counts_by_service_type
        if key_counts_by_algorithm is not None:
            self.key_counts_by_algorithm = key_counts_by_algorithm
        if key_counts_by_algorithm_and_cluster is not None:
            self.key_counts_by_algorithm_and_cluster = key_counts_by_algorithm_and_cluster

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowStatisticSecretKeyResponse.

        总数量

        :return: The total_count of this ShowStatisticSecretKeyResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowStatisticSecretKeyResponse.

        总数量

        :param total_count: The total_count of this ShowStatisticSecretKeyResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def invalid_count(self):
        r"""Gets the invalid_count of this ShowStatisticSecretKeyResponse.

        无效数量

        :return: The invalid_count of this ShowStatisticSecretKeyResponse.
        :rtype: int
        """
        return self._invalid_count

    @invalid_count.setter
    def invalid_count(self, invalid_count):
        r"""Sets the invalid_count of this ShowStatisticSecretKeyResponse.

        无效数量

        :param invalid_count: The invalid_count of this ShowStatisticSecretKeyResponse.
        :type invalid_count: int
        """
        self._invalid_count = invalid_count

    @property
    def valid_count(self):
        r"""Gets the valid_count of this ShowStatisticSecretKeyResponse.

        有效数量

        :return: The valid_count of this ShowStatisticSecretKeyResponse.
        :rtype: int
        """
        return self._valid_count

    @valid_count.setter
    def valid_count(self, valid_count):
        r"""Sets the valid_count of this ShowStatisticSecretKeyResponse.

        有效数量

        :param valid_count: The valid_count of this ShowStatisticSecretKeyResponse.
        :type valid_count: int
        """
        self._valid_count = valid_count

    @property
    def key_counts_by_service_type(self):
        r"""Gets the key_counts_by_service_type of this ShowStatisticSecretKeyResponse.

        密钥分布按服务类型统计

        :return: The key_counts_by_service_type of this ShowStatisticSecretKeyResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        return self._key_counts_by_service_type

    @key_counts_by_service_type.setter
    def key_counts_by_service_type(self, key_counts_by_service_type):
        r"""Sets the key_counts_by_service_type of this ShowStatisticSecretKeyResponse.

        密钥分布按服务类型统计

        :param key_counts_by_service_type: The key_counts_by_service_type of this ShowStatisticSecretKeyResponse.
        :type key_counts_by_service_type: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        self._key_counts_by_service_type = key_counts_by_service_type

    @property
    def key_counts_by_algorithm(self):
        r"""Gets the key_counts_by_algorithm of this ShowStatisticSecretKeyResponse.

        密钥分布按算法统计

        :return: The key_counts_by_algorithm of this ShowStatisticSecretKeyResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        return self._key_counts_by_algorithm

    @key_counts_by_algorithm.setter
    def key_counts_by_algorithm(self, key_counts_by_algorithm):
        r"""Sets the key_counts_by_algorithm of this ShowStatisticSecretKeyResponse.

        密钥分布按算法统计

        :param key_counts_by_algorithm: The key_counts_by_algorithm of this ShowStatisticSecretKeyResponse.
        :type key_counts_by_algorithm: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        self._key_counts_by_algorithm = key_counts_by_algorithm

    @property
    def key_counts_by_algorithm_and_cluster(self):
        r"""Gets the key_counts_by_algorithm_and_cluster of this ShowStatisticSecretKeyResponse.

        密钥分布按算法和集群统计

        :return: The key_counts_by_algorithm_and_cluster of this ShowStatisticSecretKeyResponse.
        :rtype: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        return self._key_counts_by_algorithm_and_cluster

    @key_counts_by_algorithm_and_cluster.setter
    def key_counts_by_algorithm_and_cluster(self, key_counts_by_algorithm_and_cluster):
        r"""Sets the key_counts_by_algorithm_and_cluster of this ShowStatisticSecretKeyResponse.

        密钥分布按算法和集群统计

        :param key_counts_by_algorithm_and_cluster: The key_counts_by_algorithm_and_cluster of this ShowStatisticSecretKeyResponse.
        :type key_counts_by_algorithm_and_cluster: list[:class:`huaweicloudsdkcpcs.v1.VendorKeyStatistic`]
        """
        self._key_counts_by_algorithm_and_cluster = key_counts_by_algorithm_and_cluster

    def to_dict(self):
        import warnings
        warnings.warn("ShowStatisticSecretKeyResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowStatisticSecretKeyResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
