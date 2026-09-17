# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListRapidGrowthTablesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tables': 'list[RapidGrowthTableInfo]',
        'threshold': 'int',
        'last_diagnose_timestamp': 'int',
        'first2_last_timestamp': 'int',
        'second2_last_timestamp': 'int'
    }

    attribute_map = {
        'tables': 'tables',
        'threshold': 'threshold',
        'last_diagnose_timestamp': 'last_diagnose_timestamp',
        'first2_last_timestamp': 'first2_last_timestamp',
        'second2_last_timestamp': 'second2_last_timestamp'
    }

    def __init__(self, tables=None, threshold=None, last_diagnose_timestamp=None, first2_last_timestamp=None, second2_last_timestamp=None):
        r"""ListRapidGrowthTablesResponse

        The model defined in huaweicloud sdk

        :param tables: 异常增长表信息列表
        :type tables: list[:class:`huaweicloudsdkdas.v3.RapidGrowthTableInfo`]
        :param threshold: 诊断阈值
        :type threshold: int
        :param last_diagnose_timestamp: 上次诊断时间
        :type last_diagnose_timestamp: int
        :param first2_last_timestamp: 最近一次诊断时间
        :type first2_last_timestamp: int
        :param second2_last_timestamp: 最近第二次诊断时间
        :type second2_last_timestamp: int
        """
        
        super().__init__()

        self._tables = None
        self._threshold = None
        self._last_diagnose_timestamp = None
        self._first2_last_timestamp = None
        self._second2_last_timestamp = None
        self.discriminator = None

        if tables is not None:
            self.tables = tables
        if threshold is not None:
            self.threshold = threshold
        if last_diagnose_timestamp is not None:
            self.last_diagnose_timestamp = last_diagnose_timestamp
        if first2_last_timestamp is not None:
            self.first2_last_timestamp = first2_last_timestamp
        if second2_last_timestamp is not None:
            self.second2_last_timestamp = second2_last_timestamp

    @property
    def tables(self):
        r"""Gets the tables of this ListRapidGrowthTablesResponse.

        异常增长表信息列表

        :return: The tables of this ListRapidGrowthTablesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.RapidGrowthTableInfo`]
        """
        return self._tables

    @tables.setter
    def tables(self, tables):
        r"""Sets the tables of this ListRapidGrowthTablesResponse.

        异常增长表信息列表

        :param tables: The tables of this ListRapidGrowthTablesResponse.
        :type tables: list[:class:`huaweicloudsdkdas.v3.RapidGrowthTableInfo`]
        """
        self._tables = tables

    @property
    def threshold(self):
        r"""Gets the threshold of this ListRapidGrowthTablesResponse.

        诊断阈值

        :return: The threshold of this ListRapidGrowthTablesResponse.
        :rtype: int
        """
        return self._threshold

    @threshold.setter
    def threshold(self, threshold):
        r"""Sets the threshold of this ListRapidGrowthTablesResponse.

        诊断阈值

        :param threshold: The threshold of this ListRapidGrowthTablesResponse.
        :type threshold: int
        """
        self._threshold = threshold

    @property
    def last_diagnose_timestamp(self):
        r"""Gets the last_diagnose_timestamp of this ListRapidGrowthTablesResponse.

        上次诊断时间

        :return: The last_diagnose_timestamp of this ListRapidGrowthTablesResponse.
        :rtype: int
        """
        return self._last_diagnose_timestamp

    @last_diagnose_timestamp.setter
    def last_diagnose_timestamp(self, last_diagnose_timestamp):
        r"""Sets the last_diagnose_timestamp of this ListRapidGrowthTablesResponse.

        上次诊断时间

        :param last_diagnose_timestamp: The last_diagnose_timestamp of this ListRapidGrowthTablesResponse.
        :type last_diagnose_timestamp: int
        """
        self._last_diagnose_timestamp = last_diagnose_timestamp

    @property
    def first2_last_timestamp(self):
        r"""Gets the first2_last_timestamp of this ListRapidGrowthTablesResponse.

        最近一次诊断时间

        :return: The first2_last_timestamp of this ListRapidGrowthTablesResponse.
        :rtype: int
        """
        return self._first2_last_timestamp

    @first2_last_timestamp.setter
    def first2_last_timestamp(self, first2_last_timestamp):
        r"""Sets the first2_last_timestamp of this ListRapidGrowthTablesResponse.

        最近一次诊断时间

        :param first2_last_timestamp: The first2_last_timestamp of this ListRapidGrowthTablesResponse.
        :type first2_last_timestamp: int
        """
        self._first2_last_timestamp = first2_last_timestamp

    @property
    def second2_last_timestamp(self):
        r"""Gets the second2_last_timestamp of this ListRapidGrowthTablesResponse.

        最近第二次诊断时间

        :return: The second2_last_timestamp of this ListRapidGrowthTablesResponse.
        :rtype: int
        """
        return self._second2_last_timestamp

    @second2_last_timestamp.setter
    def second2_last_timestamp(self, second2_last_timestamp):
        r"""Sets the second2_last_timestamp of this ListRapidGrowthTablesResponse.

        最近第二次诊断时间

        :param second2_last_timestamp: The second2_last_timestamp of this ListRapidGrowthTablesResponse.
        :type second2_last_timestamp: int
        """
        self._second2_last_timestamp = second2_last_timestamp

    def to_dict(self):
        import warnings
        warnings.warn("ListRapidGrowthTablesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListRapidGrowthTablesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
