# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowBusinessAssetsStatisticResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'subject_area_group_statistics': 'list[L1Statistic]'
    }

    attribute_map = {
        'count': 'count',
        'subject_area_group_statistics': 'subject_area_group_statistics'
    }

    def __init__(self, count=None, subject_area_group_statistics=None):
        r"""ShowBusinessAssetsStatisticResponse

        The model defined in huaweicloud sdk

        :param count: 主题域分组的总数
        :type count: int
        :param subject_area_group_statistics: 主题域分组的统计信息
        :type subject_area_group_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.L1Statistic`]
        """
        
        super(ShowBusinessAssetsStatisticResponse, self).__init__()

        self._count = None
        self._subject_area_group_statistics = None
        self.discriminator = None

        if count is not None:
            self.count = count
        if subject_area_group_statistics is not None:
            self.subject_area_group_statistics = subject_area_group_statistics

    @property
    def count(self):
        r"""Gets the count of this ShowBusinessAssetsStatisticResponse.

        主题域分组的总数

        :return: The count of this ShowBusinessAssetsStatisticResponse.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        r"""Sets the count of this ShowBusinessAssetsStatisticResponse.

        主题域分组的总数

        :param count: The count of this ShowBusinessAssetsStatisticResponse.
        :type count: int
        """
        self._count = count

    @property
    def subject_area_group_statistics(self):
        r"""Gets the subject_area_group_statistics of this ShowBusinessAssetsStatisticResponse.

        主题域分组的统计信息

        :return: The subject_area_group_statistics of this ShowBusinessAssetsStatisticResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.L1Statistic`]
        """
        return self._subject_area_group_statistics

    @subject_area_group_statistics.setter
    def subject_area_group_statistics(self, subject_area_group_statistics):
        r"""Sets the subject_area_group_statistics of this ShowBusinessAssetsStatisticResponse.

        主题域分组的统计信息

        :param subject_area_group_statistics: The subject_area_group_statistics of this ShowBusinessAssetsStatisticResponse.
        :type subject_area_group_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.L1Statistic`]
        """
        self._subject_area_group_statistics = subject_area_group_statistics

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
        if not isinstance(other, ShowBusinessAssetsStatisticResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
