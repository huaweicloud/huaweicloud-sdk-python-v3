# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePipeSchemaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'columns': 'list[TableColumnForIsapPipe]',
        'watermark_column': 'str',
        'watermark_interval': 'float',
        'time_filter': 'str'
    }

    attribute_map = {
        'columns': 'columns',
        'watermark_column': 'watermark_column',
        'watermark_interval': 'watermark_interval',
        'time_filter': 'time_filter'
    }

    def __init__(self, columns=None, watermark_column=None, watermark_interval=None, time_filter=None):
        r"""UpdatePipeSchemaResponse

        The model defined in huaweicloud sdk

        :param columns: 管道列
        :type columns: list[:class:`huaweicloudsdksecmaster.v2.TableColumnForIsapPipe`]
        :param watermark_column: 管道水线列
        :type watermark_column: str
        :param watermark_interval: 管道水线间隔时长
        :type watermark_interval: float
        :param time_filter: 管道过滤列
        :type time_filter: str
        """
        
        super().__init__()

        self._columns = None
        self._watermark_column = None
        self._watermark_interval = None
        self._time_filter = None
        self.discriminator = None

        if columns is not None:
            self.columns = columns
        if watermark_column is not None:
            self.watermark_column = watermark_column
        if watermark_interval is not None:
            self.watermark_interval = watermark_interval
        if time_filter is not None:
            self.time_filter = time_filter

    @property
    def columns(self):
        r"""Gets the columns of this UpdatePipeSchemaResponse.

        管道列

        :return: The columns of this UpdatePipeSchemaResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v2.TableColumnForIsapPipe`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this UpdatePipeSchemaResponse.

        管道列

        :param columns: The columns of this UpdatePipeSchemaResponse.
        :type columns: list[:class:`huaweicloudsdksecmaster.v2.TableColumnForIsapPipe`]
        """
        self._columns = columns

    @property
    def watermark_column(self):
        r"""Gets the watermark_column of this UpdatePipeSchemaResponse.

        管道水线列

        :return: The watermark_column of this UpdatePipeSchemaResponse.
        :rtype: str
        """
        return self._watermark_column

    @watermark_column.setter
    def watermark_column(self, watermark_column):
        r"""Sets the watermark_column of this UpdatePipeSchemaResponse.

        管道水线列

        :param watermark_column: The watermark_column of this UpdatePipeSchemaResponse.
        :type watermark_column: str
        """
        self._watermark_column = watermark_column

    @property
    def watermark_interval(self):
        r"""Gets the watermark_interval of this UpdatePipeSchemaResponse.

        管道水线间隔时长

        :return: The watermark_interval of this UpdatePipeSchemaResponse.
        :rtype: float
        """
        return self._watermark_interval

    @watermark_interval.setter
    def watermark_interval(self, watermark_interval):
        r"""Sets the watermark_interval of this UpdatePipeSchemaResponse.

        管道水线间隔时长

        :param watermark_interval: The watermark_interval of this UpdatePipeSchemaResponse.
        :type watermark_interval: float
        """
        self._watermark_interval = watermark_interval

    @property
    def time_filter(self):
        r"""Gets the time_filter of this UpdatePipeSchemaResponse.

        管道过滤列

        :return: The time_filter of this UpdatePipeSchemaResponse.
        :rtype: str
        """
        return self._time_filter

    @time_filter.setter
    def time_filter(self, time_filter):
        r"""Sets the time_filter of this UpdatePipeSchemaResponse.

        管道过滤列

        :param time_filter: The time_filter of this UpdatePipeSchemaResponse.
        :type time_filter: str
        """
        self._time_filter = time_filter

    def to_dict(self):
        import warnings
        warnings.warn("UpdatePipeSchemaResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, UpdatePipeSchemaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
