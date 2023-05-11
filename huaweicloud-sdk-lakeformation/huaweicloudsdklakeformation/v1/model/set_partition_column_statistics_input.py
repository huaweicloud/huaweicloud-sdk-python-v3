# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetPartitionColumnStatisticsInput:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'need_merge': 'bool',
        'statistics': 'list[PartitionColumnStatistics]'
    }

    attribute_map = {
        'need_merge': 'need_merge',
        'statistics': 'statistics'
    }

    def __init__(self, need_merge=None, statistics=None):
        """SetPartitionColumnStatisticsInput

        The model defined in huaweicloud sdk

        :param need_merge: 是否合入原有统计信息
        :type need_merge: bool
        :param statistics: 分区统计信息的统计列表
        :type statistics: list[:class:`huaweicloudsdklakeformation.v1.PartitionColumnStatistics`]
        """
        
        

        self._need_merge = None
        self._statistics = None
        self.discriminator = None

        self.need_merge = need_merge
        self.statistics = statistics

    @property
    def need_merge(self):
        """Gets the need_merge of this SetPartitionColumnStatisticsInput.

        是否合入原有统计信息

        :return: The need_merge of this SetPartitionColumnStatisticsInput.
        :rtype: bool
        """
        return self._need_merge

    @need_merge.setter
    def need_merge(self, need_merge):
        """Sets the need_merge of this SetPartitionColumnStatisticsInput.

        是否合入原有统计信息

        :param need_merge: The need_merge of this SetPartitionColumnStatisticsInput.
        :type need_merge: bool
        """
        self._need_merge = need_merge

    @property
    def statistics(self):
        """Gets the statistics of this SetPartitionColumnStatisticsInput.

        分区统计信息的统计列表

        :return: The statistics of this SetPartitionColumnStatisticsInput.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.PartitionColumnStatistics`]
        """
        return self._statistics

    @statistics.setter
    def statistics(self, statistics):
        """Sets the statistics of this SetPartitionColumnStatisticsInput.

        分区统计信息的统计列表

        :param statistics: The statistics of this SetPartitionColumnStatisticsInput.
        :type statistics: list[:class:`huaweicloudsdklakeformation.v1.PartitionColumnStatistics`]
        """
        self._statistics = statistics

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
        if not isinstance(other, SetPartitionColumnStatisticsInput):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
