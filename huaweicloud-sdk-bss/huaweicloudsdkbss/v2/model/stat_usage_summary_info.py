# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StatUsageSummaryInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'actual_days': 'str',
        'band_width': 'str',
        'monthly_guaranteed_band_width': 'str',
        'monthly_peak_band_width': 'str',
        'band_width_measure_id': 'int'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'actual_days': 'actual_days',
        'band_width': 'band_width',
        'monthly_guaranteed_band_width': 'monthly_guaranteed_band_width',
        'monthly_peak_band_width': 'monthly_peak_band_width',
        'band_width_measure_id': 'band_width_measure_id'
    }

    def __init__(self, resource_id=None, actual_days=None, band_width=None, monthly_guaranteed_band_width=None, monthly_peak_band_width=None, band_width_measure_id=None):
        """StatUsageSummaryInfo

        The model defined in huaweicloud sdk

        :param resource_id: 资源ID。
        :type resource_id: str
        :param actual_days: 有效天数，精度最高返回小数点后20位。  说明： 计算方式为上报的点数/288所得出的值。其中288为一天的点数，5分钟为一个点数单位。计算95费用时，因95费用是按月定价，若实际不足月，则是使用官网价*折扣*actual_days/当月天数，来计算费用明细。
        :type actual_days: str
        :param band_width: 计费带宽的按月汇总。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。
        :type band_width: str
        :param monthly_guaranteed_band_width: 月保底带宽的按月汇总。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。该字段为预留值，当前始终为空；当场景为95增强时才返回数值。
        :type monthly_guaranteed_band_width: str
        :param monthly_peak_band_width: 月峰值带宽。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。该字段为预留值，当前始终为空；当场景为95增强时才返回数值。
        :type monthly_peak_band_width: str
        :param band_width_measure_id: 带宽单位，您可以调用查询度量单位列表接口获取。若所有带宽为空，则该字段为空。
        :type band_width_measure_id: int
        """
        
        

        self._resource_id = None
        self._actual_days = None
        self._band_width = None
        self._monthly_guaranteed_band_width = None
        self._monthly_peak_band_width = None
        self._band_width_measure_id = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if actual_days is not None:
            self.actual_days = actual_days
        if band_width is not None:
            self.band_width = band_width
        if monthly_guaranteed_band_width is not None:
            self.monthly_guaranteed_band_width = monthly_guaranteed_band_width
        if monthly_peak_band_width is not None:
            self.monthly_peak_band_width = monthly_peak_band_width
        if band_width_measure_id is not None:
            self.band_width_measure_id = band_width_measure_id

    @property
    def resource_id(self):
        """Gets the resource_id of this StatUsageSummaryInfo.

        资源ID。

        :return: The resource_id of this StatUsageSummaryInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this StatUsageSummaryInfo.

        资源ID。

        :param resource_id: The resource_id of this StatUsageSummaryInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def actual_days(self):
        """Gets the actual_days of this StatUsageSummaryInfo.

        有效天数，精度最高返回小数点后20位。  说明： 计算方式为上报的点数/288所得出的值。其中288为一天的点数，5分钟为一个点数单位。计算95费用时，因95费用是按月定价，若实际不足月，则是使用官网价*折扣*actual_days/当月天数，来计算费用明细。

        :return: The actual_days of this StatUsageSummaryInfo.
        :rtype: str
        """
        return self._actual_days

    @actual_days.setter
    def actual_days(self, actual_days):
        """Sets the actual_days of this StatUsageSummaryInfo.

        有效天数，精度最高返回小数点后20位。  说明： 计算方式为上报的点数/288所得出的值。其中288为一天的点数，5分钟为一个点数单位。计算95费用时，因95费用是按月定价，若实际不足月，则是使用官网价*折扣*actual_days/当月天数，来计算费用明细。

        :param actual_days: The actual_days of this StatUsageSummaryInfo.
        :type actual_days: str
        """
        self._actual_days = actual_days

    @property
    def band_width(self):
        """Gets the band_width of this StatUsageSummaryInfo.

        计费带宽的按月汇总。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。

        :return: The band_width of this StatUsageSummaryInfo.
        :rtype: str
        """
        return self._band_width

    @band_width.setter
    def band_width(self, band_width):
        """Sets the band_width of this StatUsageSummaryInfo.

        计费带宽的按月汇总。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。

        :param band_width: The band_width of this StatUsageSummaryInfo.
        :type band_width: str
        """
        self._band_width = band_width

    @property
    def monthly_guaranteed_band_width(self):
        """Gets the monthly_guaranteed_band_width of this StatUsageSummaryInfo.

        月保底带宽的按月汇总。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。该字段为预留值，当前始终为空；当场景为95增强时才返回数值。

        :return: The monthly_guaranteed_band_width of this StatUsageSummaryInfo.
        :rtype: str
        """
        return self._monthly_guaranteed_band_width

    @monthly_guaranteed_band_width.setter
    def monthly_guaranteed_band_width(self, monthly_guaranteed_band_width):
        """Sets the monthly_guaranteed_band_width of this StatUsageSummaryInfo.

        月保底带宽的按月汇总。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。该字段为预留值，当前始终为空；当场景为95增强时才返回数值。

        :param monthly_guaranteed_band_width: The monthly_guaranteed_band_width of this StatUsageSummaryInfo.
        :type monthly_guaranteed_band_width: str
        """
        self._monthly_guaranteed_band_width = monthly_guaranteed_band_width

    @property
    def monthly_peak_band_width(self):
        """Gets the monthly_peak_band_width of this StatUsageSummaryInfo.

        月峰值带宽。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。该字段为预留值，当前始终为空；当场景为95增强时才返回数值。

        :return: The monthly_peak_band_width of this StatUsageSummaryInfo.
        :rtype: str
        """
        return self._monthly_peak_band_width

    @monthly_peak_band_width.setter
    def monthly_peak_band_width(self, monthly_peak_band_width):
        """Sets the monthly_peak_band_width of this StatUsageSummaryInfo.

        月峰值带宽。  说明： 每月2日20点后可查询上月数据；若查询当月数据，则为空。该字段为预留值，当前始终为空；当场景为95增强时才返回数值。

        :param monthly_peak_band_width: The monthly_peak_band_width of this StatUsageSummaryInfo.
        :type monthly_peak_band_width: str
        """
        self._monthly_peak_band_width = monthly_peak_band_width

    @property
    def band_width_measure_id(self):
        """Gets the band_width_measure_id of this StatUsageSummaryInfo.

        带宽单位，您可以调用查询度量单位列表接口获取。若所有带宽为空，则该字段为空。

        :return: The band_width_measure_id of this StatUsageSummaryInfo.
        :rtype: int
        """
        return self._band_width_measure_id

    @band_width_measure_id.setter
    def band_width_measure_id(self, band_width_measure_id):
        """Sets the band_width_measure_id of this StatUsageSummaryInfo.

        带宽单位，您可以调用查询度量单位列表接口获取。若所有带宽为空，则该字段为空。

        :param band_width_measure_id: The band_width_measure_id of this StatUsageSummaryInfo.
        :type band_width_measure_id: int
        """
        self._band_width_measure_id = band_width_measure_id

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
        if not isinstance(other, StatUsageSummaryInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
