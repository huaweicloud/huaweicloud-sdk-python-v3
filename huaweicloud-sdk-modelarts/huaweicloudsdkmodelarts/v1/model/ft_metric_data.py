# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FtMetricData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'format_version': 'str',
        'timestamp': 'str',
        'metrics': 'list[FtMetric]'
    }

    attribute_map = {
        'format_version': 'format_version',
        'timestamp': 'timestamp',
        'metrics': 'metrics'
    }

    def __init__(self, format_version=None, timestamp=None, metrics=None):
        r"""FtMetricData

        The model defined in huaweicloud sdk

        :param format_version: 固定值 \&quot;1.0\&quot;，标识数据格式版本
        :type format_version: str
        :param timestamp: 文件生成时间，ISO 8601 格式（如 2026-07-18T10:30:00Z）
        :type timestamp: str
        :param metrics: 
        :type metrics: list[:class:`huaweicloudsdkmodelarts.v1.FtMetric`]
        """
        
        

        self._format_version = None
        self._timestamp = None
        self._metrics = None
        self.discriminator = None

        self.format_version = format_version
        if timestamp is not None:
            self.timestamp = timestamp
        self.metrics = metrics

    @property
    def format_version(self):
        r"""Gets the format_version of this FtMetricData.

        固定值 \"1.0\"，标识数据格式版本

        :return: The format_version of this FtMetricData.
        :rtype: str
        """
        return self._format_version

    @format_version.setter
    def format_version(self, format_version):
        r"""Sets the format_version of this FtMetricData.

        固定值 \"1.0\"，标识数据格式版本

        :param format_version: The format_version of this FtMetricData.
        :type format_version: str
        """
        self._format_version = format_version

    @property
    def timestamp(self):
        r"""Gets the timestamp of this FtMetricData.

        文件生成时间，ISO 8601 格式（如 2026-07-18T10:30:00Z）

        :return: The timestamp of this FtMetricData.
        :rtype: str
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        r"""Sets the timestamp of this FtMetricData.

        文件生成时间，ISO 8601 格式（如 2026-07-18T10:30:00Z）

        :param timestamp: The timestamp of this FtMetricData.
        :type timestamp: str
        """
        self._timestamp = timestamp

    @property
    def metrics(self):
        r"""Gets the metrics of this FtMetricData.

        :return: The metrics of this FtMetricData.
        :rtype: list[:class:`huaweicloudsdkmodelarts.v1.FtMetric`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this FtMetricData.

        :param metrics: The metrics of this FtMetricData.
        :type metrics: list[:class:`huaweicloudsdkmodelarts.v1.FtMetric`]
        """
        self._metrics = metrics

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
        if not isinstance(other, FtMetricData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
