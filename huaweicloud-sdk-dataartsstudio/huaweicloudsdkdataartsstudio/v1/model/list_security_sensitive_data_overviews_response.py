# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecuritySensitiveDataOverviewsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'secrecy_level_statistics': 'list[SensitiveDataSecrecyLevelOverviewQueryDTO]',
        'category_statistics': 'list[SensitiveDataCategoryOverviewQueryDTO]'
    }

    attribute_map = {
        'secrecy_level_statistics': 'secrecy_level_statistics',
        'category_statistics': 'category_statistics'
    }

    def __init__(self, secrecy_level_statistics=None, category_statistics=None):
        r"""ListSecuritySensitiveDataOverviewsResponse

        The model defined in huaweicloud sdk

        :param secrecy_level_statistics: 基于密级的概览统计
        :type secrecy_level_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataSecrecyLevelOverviewQueryDTO`]
        :param category_statistics: 基于分类的概览统计
        :type category_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataCategoryOverviewQueryDTO`]
        """
        
        super(ListSecuritySensitiveDataOverviewsResponse, self).__init__()

        self._secrecy_level_statistics = None
        self._category_statistics = None
        self.discriminator = None

        if secrecy_level_statistics is not None:
            self.secrecy_level_statistics = secrecy_level_statistics
        if category_statistics is not None:
            self.category_statistics = category_statistics

    @property
    def secrecy_level_statistics(self):
        r"""Gets the secrecy_level_statistics of this ListSecuritySensitiveDataOverviewsResponse.

        基于密级的概览统计

        :return: The secrecy_level_statistics of this ListSecuritySensitiveDataOverviewsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataSecrecyLevelOverviewQueryDTO`]
        """
        return self._secrecy_level_statistics

    @secrecy_level_statistics.setter
    def secrecy_level_statistics(self, secrecy_level_statistics):
        r"""Sets the secrecy_level_statistics of this ListSecuritySensitiveDataOverviewsResponse.

        基于密级的概览统计

        :param secrecy_level_statistics: The secrecy_level_statistics of this ListSecuritySensitiveDataOverviewsResponse.
        :type secrecy_level_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataSecrecyLevelOverviewQueryDTO`]
        """
        self._secrecy_level_statistics = secrecy_level_statistics

    @property
    def category_statistics(self):
        r"""Gets the category_statistics of this ListSecuritySensitiveDataOverviewsResponse.

        基于分类的概览统计

        :return: The category_statistics of this ListSecuritySensitiveDataOverviewsResponse.
        :rtype: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataCategoryOverviewQueryDTO`]
        """
        return self._category_statistics

    @category_statistics.setter
    def category_statistics(self, category_statistics):
        r"""Sets the category_statistics of this ListSecuritySensitiveDataOverviewsResponse.

        基于分类的概览统计

        :param category_statistics: The category_statistics of this ListSecuritySensitiveDataOverviewsResponse.
        :type category_statistics: list[:class:`huaweicloudsdkdataartsstudio.v1.SensitiveDataCategoryOverviewQueryDTO`]
        """
        self._category_statistics = category_statistics

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
        if not isinstance(other, ListSecuritySensitiveDataOverviewsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
