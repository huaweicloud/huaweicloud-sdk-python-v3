# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowWdrSnapshotRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'start_time': 'int',
        'end_time': 'int'
    }

    attribute_map = {
        'start_time': 'start_time',
        'end_time': 'end_time'
    }

    def __init__(self, start_time=None, end_time=None):
        r"""ShowWdrSnapshotRequestBody

        The model defined in huaweicloud sdk

        :param start_time: 开始时间（Unix timestamp），单位：毫秒
        :type start_time: int
        :param end_time: 结束时间（Unix timestamp），单位：毫秒
        :type end_time: int
        """
        
        

        self._start_time = None
        self._end_time = None
        self.discriminator = None

        if start_time is not None:
            self.start_time = start_time
        if end_time is not None:
            self.end_time = end_time

    @property
    def start_time(self):
        r"""Gets the start_time of this ShowWdrSnapshotRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :return: The start_time of this ShowWdrSnapshotRequestBody.
        :rtype: int
        """
        return self._start_time

    @start_time.setter
    def start_time(self, start_time):
        r"""Sets the start_time of this ShowWdrSnapshotRequestBody.

        开始时间（Unix timestamp），单位：毫秒

        :param start_time: The start_time of this ShowWdrSnapshotRequestBody.
        :type start_time: int
        """
        self._start_time = start_time

    @property
    def end_time(self):
        r"""Gets the end_time of this ShowWdrSnapshotRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :return: The end_time of this ShowWdrSnapshotRequestBody.
        :rtype: int
        """
        return self._end_time

    @end_time.setter
    def end_time(self, end_time):
        r"""Sets the end_time of this ShowWdrSnapshotRequestBody.

        结束时间（Unix timestamp），单位：毫秒

        :param end_time: The end_time of this ShowWdrSnapshotRequestBody.
        :type end_time: int
        """
        self._end_time = end_time

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
        if not isinstance(other, ShowWdrSnapshotRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
