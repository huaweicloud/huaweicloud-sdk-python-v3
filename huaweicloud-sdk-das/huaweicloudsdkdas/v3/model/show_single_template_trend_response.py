# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSingleTemplateTrendResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestamps': 'list[int]',
        'trend_data_list': 'list[SingleSqlTplCmp]'
    }

    attribute_map = {
        'timestamps': 'timestamps',
        'trend_data_list': 'trend_data_list'
    }

    def __init__(self, timestamps=None, trend_data_list=None):
        r"""ShowSingleTemplateTrendResponse

        The model defined in huaweicloud sdk

        :param timestamps: 趋势图的时间戳
        :type timestamps: list[int]
        :param trend_data_list: SQL趋势列表
        :type trend_data_list: list[:class:`huaweicloudsdkdas.v3.SingleSqlTplCmp`]
        """
        
        super().__init__()

        self._timestamps = None
        self._trend_data_list = None
        self.discriminator = None

        if timestamps is not None:
            self.timestamps = timestamps
        if trend_data_list is not None:
            self.trend_data_list = trend_data_list

    @property
    def timestamps(self):
        r"""Gets the timestamps of this ShowSingleTemplateTrendResponse.

        趋势图的时间戳

        :return: The timestamps of this ShowSingleTemplateTrendResponse.
        :rtype: list[int]
        """
        return self._timestamps

    @timestamps.setter
    def timestamps(self, timestamps):
        r"""Sets the timestamps of this ShowSingleTemplateTrendResponse.

        趋势图的时间戳

        :param timestamps: The timestamps of this ShowSingleTemplateTrendResponse.
        :type timestamps: list[int]
        """
        self._timestamps = timestamps

    @property
    def trend_data_list(self):
        r"""Gets the trend_data_list of this ShowSingleTemplateTrendResponse.

        SQL趋势列表

        :return: The trend_data_list of this ShowSingleTemplateTrendResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SingleSqlTplCmp`]
        """
        return self._trend_data_list

    @trend_data_list.setter
    def trend_data_list(self, trend_data_list):
        r"""Sets the trend_data_list of this ShowSingleTemplateTrendResponse.

        SQL趋势列表

        :param trend_data_list: The trend_data_list of this ShowSingleTemplateTrendResponse.
        :type trend_data_list: list[:class:`huaweicloudsdkdas.v3.SingleSqlTplCmp`]
        """
        self._trend_data_list = trend_data_list

    def to_dict(self):
        import warnings
        warnings.warn("ShowSingleTemplateTrendResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ShowSingleTemplateTrendResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
