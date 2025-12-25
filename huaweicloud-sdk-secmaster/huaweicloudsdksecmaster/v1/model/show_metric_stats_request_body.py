# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMetricStatsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataspace_id': 'str',
        'end_timestamp': 'int',
        'pipe_id': 'str',
        'start_timestamp': 'int'
    }

    attribute_map = {
        'dataspace_id': 'dataspace_id',
        'end_timestamp': 'end_timestamp',
        'pipe_id': 'pipe_id',
        'start_timestamp': 'start_timestamp'
    }

    def __init__(self, dataspace_id=None, end_timestamp=None, pipe_id=None, start_timestamp=None):
        r"""ShowMetricStatsRequestBody

        The model defined in huaweicloud sdk

        :param dataspace_id: 数据空间ID
        :type dataspace_id: str
        :param end_timestamp: 结束时间
        :type end_timestamp: int
        :param pipe_id: 数据管道ID
        :type pipe_id: str
        :param start_timestamp: 开始时间
        :type start_timestamp: int
        """
        
        

        self._dataspace_id = None
        self._end_timestamp = None
        self._pipe_id = None
        self._start_timestamp = None
        self.discriminator = None

        self.dataspace_id = dataspace_id
        self.end_timestamp = end_timestamp
        self.pipe_id = pipe_id
        self.start_timestamp = start_timestamp

    @property
    def dataspace_id(self):
        r"""Gets the dataspace_id of this ShowMetricStatsRequestBody.

        数据空间ID

        :return: The dataspace_id of this ShowMetricStatsRequestBody.
        :rtype: str
        """
        return self._dataspace_id

    @dataspace_id.setter
    def dataspace_id(self, dataspace_id):
        r"""Sets the dataspace_id of this ShowMetricStatsRequestBody.

        数据空间ID

        :param dataspace_id: The dataspace_id of this ShowMetricStatsRequestBody.
        :type dataspace_id: str
        """
        self._dataspace_id = dataspace_id

    @property
    def end_timestamp(self):
        r"""Gets the end_timestamp of this ShowMetricStatsRequestBody.

        结束时间

        :return: The end_timestamp of this ShowMetricStatsRequestBody.
        :rtype: int
        """
        return self._end_timestamp

    @end_timestamp.setter
    def end_timestamp(self, end_timestamp):
        r"""Sets the end_timestamp of this ShowMetricStatsRequestBody.

        结束时间

        :param end_timestamp: The end_timestamp of this ShowMetricStatsRequestBody.
        :type end_timestamp: int
        """
        self._end_timestamp = end_timestamp

    @property
    def pipe_id(self):
        r"""Gets the pipe_id of this ShowMetricStatsRequestBody.

        数据管道ID

        :return: The pipe_id of this ShowMetricStatsRequestBody.
        :rtype: str
        """
        return self._pipe_id

    @pipe_id.setter
    def pipe_id(self, pipe_id):
        r"""Sets the pipe_id of this ShowMetricStatsRequestBody.

        数据管道ID

        :param pipe_id: The pipe_id of this ShowMetricStatsRequestBody.
        :type pipe_id: str
        """
        self._pipe_id = pipe_id

    @property
    def start_timestamp(self):
        r"""Gets the start_timestamp of this ShowMetricStatsRequestBody.

        开始时间

        :return: The start_timestamp of this ShowMetricStatsRequestBody.
        :rtype: int
        """
        return self._start_timestamp

    @start_timestamp.setter
    def start_timestamp(self, start_timestamp):
        r"""Sets the start_timestamp of this ShowMetricStatsRequestBody.

        开始时间

        :param start_timestamp: The start_timestamp of this ShowMetricStatsRequestBody.
        :type start_timestamp: int
        """
        self._start_timestamp = start_timestamp

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
        if not isinstance(other, ShowMetricStatsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
