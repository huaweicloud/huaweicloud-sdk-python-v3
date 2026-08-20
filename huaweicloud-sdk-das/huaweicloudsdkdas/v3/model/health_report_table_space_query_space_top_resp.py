# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HealthReportTableSpaceQuerySpaceTopResp:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_data_list': 'list[HealthReportTableSpaceTopDataDto]',
        'collect_timestamp': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'top_data_list': 'top_data_list',
        'collect_timestamp': 'collect_timestamp',
        'total_count': 'total_count'
    }

    def __init__(self, top_data_list=None, collect_timestamp=None, total_count=None):
        r"""HealthReportTableSpaceQuerySpaceTopResp

        The model defined in huaweicloud sdk

        :param top_data_list: 库/表大小Top列表。
        :type top_data_list: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceTopDataDto`]
        :param collect_timestamp: 采集时间
        :type collect_timestamp: int
        :param total_count: 总大小。
        :type total_count: int
        """
        
        

        self._top_data_list = None
        self._collect_timestamp = None
        self._total_count = None
        self.discriminator = None

        if top_data_list is not None:
            self.top_data_list = top_data_list
        if collect_timestamp is not None:
            self.collect_timestamp = collect_timestamp
        if total_count is not None:
            self.total_count = total_count

    @property
    def top_data_list(self):
        r"""Gets the top_data_list of this HealthReportTableSpaceQuerySpaceTopResp.

        库/表大小Top列表。

        :return: The top_data_list of this HealthReportTableSpaceQuerySpaceTopResp.
        :rtype: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceTopDataDto`]
        """
        return self._top_data_list

    @top_data_list.setter
    def top_data_list(self, top_data_list):
        r"""Sets the top_data_list of this HealthReportTableSpaceQuerySpaceTopResp.

        库/表大小Top列表。

        :param top_data_list: The top_data_list of this HealthReportTableSpaceQuerySpaceTopResp.
        :type top_data_list: list[:class:`huaweicloudsdkdas.v3.HealthReportTableSpaceTopDataDto`]
        """
        self._top_data_list = top_data_list

    @property
    def collect_timestamp(self):
        r"""Gets the collect_timestamp of this HealthReportTableSpaceQuerySpaceTopResp.

        采集时间

        :return: The collect_timestamp of this HealthReportTableSpaceQuerySpaceTopResp.
        :rtype: int
        """
        return self._collect_timestamp

    @collect_timestamp.setter
    def collect_timestamp(self, collect_timestamp):
        r"""Sets the collect_timestamp of this HealthReportTableSpaceQuerySpaceTopResp.

        采集时间

        :param collect_timestamp: The collect_timestamp of this HealthReportTableSpaceQuerySpaceTopResp.
        :type collect_timestamp: int
        """
        self._collect_timestamp = collect_timestamp

    @property
    def total_count(self):
        r"""Gets the total_count of this HealthReportTableSpaceQuerySpaceTopResp.

        总大小。

        :return: The total_count of this HealthReportTableSpaceQuerySpaceTopResp.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this HealthReportTableSpaceQuerySpaceTopResp.

        总大小。

        :param total_count: The total_count of this HealthReportTableSpaceQuerySpaceTopResp.
        :type total_count: int
        """
        self._total_count = total_count

    def to_dict(self):
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
        if not isinstance(other, HealthReportTableSpaceQuerySpaceTopResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
