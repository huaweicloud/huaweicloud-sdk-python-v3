# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SimulationFilePathSrlz:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'evaluation_path': 'str',
        'visualization_path': 'str',
        'evaluation_log_path': 'str',
        'algorithm_pb_path': 'str',
        'algorithm_meta_path': 'str',
        'algorithm_log_path': 'str',
        'replay_path': 'str',
        'sim_osi_path': 'str',
        'osi_meta_path': 'str'
    }

    attribute_map = {
        'evaluation_path': 'evaluation_path',
        'visualization_path': 'visualization_path',
        'evaluation_log_path': 'evaluation_log_path',
        'algorithm_pb_path': 'algorithm_pb_path',
        'algorithm_meta_path': 'algorithm_meta_path',
        'algorithm_log_path': 'algorithm_log_path',
        'replay_path': 'replay_path',
        'sim_osi_path': 'sim_osi_path',
        'osi_meta_path': 'osi_meta_path'
    }

    def __init__(self, evaluation_path=None, visualization_path=None, evaluation_log_path=None, algorithm_pb_path=None, algorithm_meta_path=None, algorithm_log_path=None, replay_path=None, sim_osi_path=None, osi_meta_path=None):
        r"""SimulationFilePathSrlz

        The model defined in huaweicloud sdk

        :param evaluation_path: 评测osi文件路径
        :type evaluation_path: str
        :param visualization_path: 评测可视化pb文件路径
        :type visualization_path: str
        :param evaluation_log_path: 评测日志路径
        :type evaluation_log_path: str
        :param algorithm_pb_path: 算法pb文件路径
        :type algorithm_pb_path: str
        :param algorithm_meta_path: 算法pb文件元数据路径
        :type algorithm_meta_path: str
        :param algorithm_log_path: 算法日志路径
        :type algorithm_log_path: str
        :param replay_path: 回放文件路径
        :type replay_path: str
        :param sim_osi_path: 仿真pb文件路径
        :type sim_osi_path: str
        :param osi_meta_path: 仿真pb文件元数据路径
        :type osi_meta_path: str
        """
        
        

        self._evaluation_path = None
        self._visualization_path = None
        self._evaluation_log_path = None
        self._algorithm_pb_path = None
        self._algorithm_meta_path = None
        self._algorithm_log_path = None
        self._replay_path = None
        self._sim_osi_path = None
        self._osi_meta_path = None
        self.discriminator = None

        if evaluation_path is not None:
            self.evaluation_path = evaluation_path
        if visualization_path is not None:
            self.visualization_path = visualization_path
        if evaluation_log_path is not None:
            self.evaluation_log_path = evaluation_log_path
        if algorithm_pb_path is not None:
            self.algorithm_pb_path = algorithm_pb_path
        if algorithm_meta_path is not None:
            self.algorithm_meta_path = algorithm_meta_path
        if algorithm_log_path is not None:
            self.algorithm_log_path = algorithm_log_path
        if replay_path is not None:
            self.replay_path = replay_path
        if sim_osi_path is not None:
            self.sim_osi_path = sim_osi_path
        if osi_meta_path is not None:
            self.osi_meta_path = osi_meta_path

    @property
    def evaluation_path(self):
        r"""Gets the evaluation_path of this SimulationFilePathSrlz.

        评测osi文件路径

        :return: The evaluation_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._evaluation_path

    @evaluation_path.setter
    def evaluation_path(self, evaluation_path):
        r"""Sets the evaluation_path of this SimulationFilePathSrlz.

        评测osi文件路径

        :param evaluation_path: The evaluation_path of this SimulationFilePathSrlz.
        :type evaluation_path: str
        """
        self._evaluation_path = evaluation_path

    @property
    def visualization_path(self):
        r"""Gets the visualization_path of this SimulationFilePathSrlz.

        评测可视化pb文件路径

        :return: The visualization_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._visualization_path

    @visualization_path.setter
    def visualization_path(self, visualization_path):
        r"""Sets the visualization_path of this SimulationFilePathSrlz.

        评测可视化pb文件路径

        :param visualization_path: The visualization_path of this SimulationFilePathSrlz.
        :type visualization_path: str
        """
        self._visualization_path = visualization_path

    @property
    def evaluation_log_path(self):
        r"""Gets the evaluation_log_path of this SimulationFilePathSrlz.

        评测日志路径

        :return: The evaluation_log_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._evaluation_log_path

    @evaluation_log_path.setter
    def evaluation_log_path(self, evaluation_log_path):
        r"""Sets the evaluation_log_path of this SimulationFilePathSrlz.

        评测日志路径

        :param evaluation_log_path: The evaluation_log_path of this SimulationFilePathSrlz.
        :type evaluation_log_path: str
        """
        self._evaluation_log_path = evaluation_log_path

    @property
    def algorithm_pb_path(self):
        r"""Gets the algorithm_pb_path of this SimulationFilePathSrlz.

        算法pb文件路径

        :return: The algorithm_pb_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._algorithm_pb_path

    @algorithm_pb_path.setter
    def algorithm_pb_path(self, algorithm_pb_path):
        r"""Sets the algorithm_pb_path of this SimulationFilePathSrlz.

        算法pb文件路径

        :param algorithm_pb_path: The algorithm_pb_path of this SimulationFilePathSrlz.
        :type algorithm_pb_path: str
        """
        self._algorithm_pb_path = algorithm_pb_path

    @property
    def algorithm_meta_path(self):
        r"""Gets the algorithm_meta_path of this SimulationFilePathSrlz.

        算法pb文件元数据路径

        :return: The algorithm_meta_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._algorithm_meta_path

    @algorithm_meta_path.setter
    def algorithm_meta_path(self, algorithm_meta_path):
        r"""Sets the algorithm_meta_path of this SimulationFilePathSrlz.

        算法pb文件元数据路径

        :param algorithm_meta_path: The algorithm_meta_path of this SimulationFilePathSrlz.
        :type algorithm_meta_path: str
        """
        self._algorithm_meta_path = algorithm_meta_path

    @property
    def algorithm_log_path(self):
        r"""Gets the algorithm_log_path of this SimulationFilePathSrlz.

        算法日志路径

        :return: The algorithm_log_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._algorithm_log_path

    @algorithm_log_path.setter
    def algorithm_log_path(self, algorithm_log_path):
        r"""Sets the algorithm_log_path of this SimulationFilePathSrlz.

        算法日志路径

        :param algorithm_log_path: The algorithm_log_path of this SimulationFilePathSrlz.
        :type algorithm_log_path: str
        """
        self._algorithm_log_path = algorithm_log_path

    @property
    def replay_path(self):
        r"""Gets the replay_path of this SimulationFilePathSrlz.

        回放文件路径

        :return: The replay_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._replay_path

    @replay_path.setter
    def replay_path(self, replay_path):
        r"""Sets the replay_path of this SimulationFilePathSrlz.

        回放文件路径

        :param replay_path: The replay_path of this SimulationFilePathSrlz.
        :type replay_path: str
        """
        self._replay_path = replay_path

    @property
    def sim_osi_path(self):
        r"""Gets the sim_osi_path of this SimulationFilePathSrlz.

        仿真pb文件路径

        :return: The sim_osi_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._sim_osi_path

    @sim_osi_path.setter
    def sim_osi_path(self, sim_osi_path):
        r"""Sets the sim_osi_path of this SimulationFilePathSrlz.

        仿真pb文件路径

        :param sim_osi_path: The sim_osi_path of this SimulationFilePathSrlz.
        :type sim_osi_path: str
        """
        self._sim_osi_path = sim_osi_path

    @property
    def osi_meta_path(self):
        r"""Gets the osi_meta_path of this SimulationFilePathSrlz.

        仿真pb文件元数据路径

        :return: The osi_meta_path of this SimulationFilePathSrlz.
        :rtype: str
        """
        return self._osi_meta_path

    @osi_meta_path.setter
    def osi_meta_path(self, osi_meta_path):
        r"""Sets the osi_meta_path of this SimulationFilePathSrlz.

        仿真pb文件元数据路径

        :param osi_meta_path: The osi_meta_path of this SimulationFilePathSrlz.
        :type osi_meta_path: str
        """
        self._osi_meta_path = osi_meta_path

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
        if not isinstance(other, SimulationFilePathSrlz):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
