# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimulationEvaluationSrlz:

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
        'avg_speed': 'float',
        'distance': 'float',
        'reach_time': 'float',
        'metrics': 'list[SimulationEvaluationMetricSrlz]'
    }

    attribute_map = {
        'score': 'score',
        'avg_speed': 'avgSpeed',
        'distance': 'distance',
        'reach_time': 'reachTime',
        'metrics': 'metrics'
    }

    def __init__(self, score=None, avg_speed=None, distance=None, reach_time=None, metrics=None):
        r"""SimulationEvaluationSrlz

        The model defined in huaweicloud sdk

        :param score: 得分
        :type score: float
        :param avg_speed: 平均速度
        :type avg_speed: float
        :param distance: 里程
        :type distance: float
        :param reach_time: 到达时间
        :type reach_time: float
        :param metrics: 评测指标
        :type metrics: list[:class:`huaweicloudsdkoctopus.v2.SimulationEvaluationMetricSrlz`]
        """
        
        

        self._score = None
        self._avg_speed = None
        self._distance = None
        self._reach_time = None
        self._metrics = None
        self.discriminator = None

        if score is not None:
            self.score = score
        if avg_speed is not None:
            self.avg_speed = avg_speed
        if distance is not None:
            self.distance = distance
        if reach_time is not None:
            self.reach_time = reach_time
        if metrics is not None:
            self.metrics = metrics

    @property
    def score(self):
        r"""Gets the score of this SimulationEvaluationSrlz.

        得分

        :return: The score of this SimulationEvaluationSrlz.
        :rtype: float
        """
        return self._score

    @score.setter
    def score(self, score):
        r"""Sets the score of this SimulationEvaluationSrlz.

        得分

        :param score: The score of this SimulationEvaluationSrlz.
        :type score: float
        """
        self._score = score

    @property
    def avg_speed(self):
        r"""Gets the avg_speed of this SimulationEvaluationSrlz.

        平均速度

        :return: The avg_speed of this SimulationEvaluationSrlz.
        :rtype: float
        """
        return self._avg_speed

    @avg_speed.setter
    def avg_speed(self, avg_speed):
        r"""Sets the avg_speed of this SimulationEvaluationSrlz.

        平均速度

        :param avg_speed: The avg_speed of this SimulationEvaluationSrlz.
        :type avg_speed: float
        """
        self._avg_speed = avg_speed

    @property
    def distance(self):
        r"""Gets the distance of this SimulationEvaluationSrlz.

        里程

        :return: The distance of this SimulationEvaluationSrlz.
        :rtype: float
        """
        return self._distance

    @distance.setter
    def distance(self, distance):
        r"""Sets the distance of this SimulationEvaluationSrlz.

        里程

        :param distance: The distance of this SimulationEvaluationSrlz.
        :type distance: float
        """
        self._distance = distance

    @property
    def reach_time(self):
        r"""Gets the reach_time of this SimulationEvaluationSrlz.

        到达时间

        :return: The reach_time of this SimulationEvaluationSrlz.
        :rtype: float
        """
        return self._reach_time

    @reach_time.setter
    def reach_time(self, reach_time):
        r"""Sets the reach_time of this SimulationEvaluationSrlz.

        到达时间

        :param reach_time: The reach_time of this SimulationEvaluationSrlz.
        :type reach_time: float
        """
        self._reach_time = reach_time

    @property
    def metrics(self):
        r"""Gets the metrics of this SimulationEvaluationSrlz.

        评测指标

        :return: The metrics of this SimulationEvaluationSrlz.
        :rtype: list[:class:`huaweicloudsdkoctopus.v2.SimulationEvaluationMetricSrlz`]
        """
        return self._metrics

    @metrics.setter
    def metrics(self, metrics):
        r"""Sets the metrics of this SimulationEvaluationSrlz.

        评测指标

        :param metrics: The metrics of this SimulationEvaluationSrlz.
        :type metrics: list[:class:`huaweicloudsdkoctopus.v2.SimulationEvaluationMetricSrlz`]
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
        if not isinstance(other, SimulationEvaluationSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
