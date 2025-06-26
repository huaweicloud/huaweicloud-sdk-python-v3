# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimulationEvaResultSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'score': 'float',
        'distance': 'float',
        'average_speed': 'float',
        'reach_time': 'float',
        'metrics': 'list[SimulationEvaResultMetricSrlz]'
    }

    attribute_map = {
        'score': 'score',
        'distance': 'distance',
        'average_speed': 'average_speed',
        'reach_time': 'reach_time',
        'metrics': 'metrics'
    }

    def __init__(self, score=None, distance=None, average_speed=None, reach_time=None, metrics=None):
        r"""SimulationEvaResultSrlz

        The model defined in huaweicloud sdk

        :param score: 得分
        :type score: float
        :param distance: 里程
        :type distance: float
        :param average_speed: 平均速度
        :type average_speed: float
        :param reach_time: 到达时间
        :type reach_time: float
        :param metrics: 评测指标
        :type metrics: list[:class:`huaweicloudsdkoctopus.v2.SimulationEvaResultMetricSrlz`]
        """
        
        

        self._score = None
        self._distance = None
        self._average_speed = None
        self._reach_time = None
        self._metrics = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if distance is not None:
            self.distance = distance
        if average_speed is not None:
            self.average_speed = average_speed
        if reach_time is not None:
            self.reach_time = reach_time
        if metrics is not None:
            self.metrics = metrics

    @property
    def score(self):
        r"""Gets the score of this SimulationEvaResultSrlz.

        得分

        :return: The score of this SimulationEvaResultSrlz.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this SimulationEvaResultSrlz.

        得分

        :param score: The score of this SimulationEvaResultSrlz.
        :type score: float
        """
        self._score = score

    @property
    def distance(self):
        r"""Gets the distance of this SimulationEvaResultSrlz.

        里程

        :return: The distance of this SimulationEvaResultSrlz.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        r"""Sets the distance of this SimulationEvaResultSrlz.

        里程

        :param distance: The distance of this SimulationEvaResultSrlz.
        :type distance: float
        """
        self._distance = distance

    @property
    def average_speed(self):
        r"""Gets the average_speed of this SimulationEvaResultSrlz.

        平均速度

        :return: The average_speed of this SimulationEvaResultSrlz.
        :rtype: float
        """
        return self._average_speed

    @average_speed.setter
    def average_speed(self, average_speed):
        r"""Sets the average_speed of this SimulationEvaResultSrlz.

        平均速度

        :param average_speed: The average_speed of this SimulationEvaResultSrlz.
        :type average_speed: float
        """
        self._average_speed = average_speed

    @property
    def reach_time(self):
        r"""Gets the reach_time of this SimulationEvaResultSrlz.

        到达时间

        :return: The reach_time of this SimulationEvaResultSrlz.
        :rtype: float
        """
        return self._reach_time

    @reach_time.setter
    def reach_time(self, reach_time):
        r"""Sets the reach_time of this SimulationEvaResultSrlz.

        到达时间

        :param reach_time: The reach_time of this SimulationEvaResultSrlz.
        :type reach_time: float
        """
        self._reach_time = reach_time

    @property
    def metrics(self):
        r"""Gets the metrics of this SimulationEvaResultSrlz.

        评测指标

        :return: The metrics of this SimulationEvaResultSrlz.
        :rtype: list[:class:`huaweicloudsdkoctopus.v2.SimulationEvaResultMetricSrlz`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this SimulationEvaResultSrlz.

        评测指标

        :param metrics: The metrics of this SimulationEvaResultSrlz.
        :type metrics: list[:class:`huaweicloudsdkoctopus.v2.SimulationEvaResultMetricSrlz`]
        """
        self._metrics = metrics

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
        if not isinstance(other, SimulationEvaResultSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
