# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowTopDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'top_data_list': 'list[TopDataInfo]',
        'total_count': 'int',
        'collect_timestamp': 'int'
    }

    attribute_map = {
        'top_data_list': 'top_data_list',
        'total_count': 'total_count',
        'collect_timestamp': 'collect_timestamp'
    }

    def __init__(self, top_data_list=None, total_count=None, collect_timestamp=None):
        r"""ShowTopDataResponse

        The model defined in huaweicloud sdk

        :param top_data_list: Top库表数据列表
        :type top_data_list: list[:class:`huaweicloudsdkdas.v3.TopDataInfo`]
        :param total_count: 总数
        :type total_count: int
        :param collect_timestamp: 采集时间（Unix timestamp），单位：毫秒
        :type collect_timestamp: int
        """
        
        super().__init__()

        self._top_data_list = None
        self._total_count = None
        self._collect_timestamp = None
        self.discriminator = None

        if top_data_list is not None:
            self.top_data_list = top_data_list
        if total_count is not None:
            self.total_count = total_count
        if collect_timestamp is not None:
            self.collect_timestamp = collect_timestamp

    @property
    def top_data_list(self):
        r"""Gets the top_data_list of this ShowTopDataResponse.

        Top库表数据列表

        :return: The top_data_list of this ShowTopDataResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.TopDataInfo`]
        """
        return self._top_data_list

    @top_data_list.setter
    def top_data_list(self, top_data_list):
        r"""Sets the top_data_list of this ShowTopDataResponse.

        Top库表数据列表

        :param top_data_list: The top_data_list of this ShowTopDataResponse.
        :type top_data_list: list[:class:`huaweicloudsdkdas.v3.TopDataInfo`]
        """
        self._top_data_list = top_data_list

    @property
    def total_count(self):
        r"""Gets the total_count of this ShowTopDataResponse.

        总数

        :return: The total_count of this ShowTopDataResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this ShowTopDataResponse.

        总数

        :param total_count: The total_count of this ShowTopDataResponse.
        :type total_count: int
        """
        self._total_count = total_count

    @property
    def collect_timestamp(self):
        r"""Gets the collect_timestamp of this ShowTopDataResponse.

        采集时间（Unix timestamp），单位：毫秒

        :return: The collect_timestamp of this ShowTopDataResponse.
        :rtype: int
        """
        return self._collect_timestamp

    @collect_timestamp.setter
    def collect_timestamp(self, collect_timestamp):
        r"""Sets the collect_timestamp of this ShowTopDataResponse.

        采集时间（Unix timestamp），单位：毫秒

        :param collect_timestamp: The collect_timestamp of this ShowTopDataResponse.
        :type collect_timestamp: int
        """
        self._collect_timestamp = collect_timestamp

    def to_dict(self):
        import warnings
        warnings.warn("ShowTopDataResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowTopDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
