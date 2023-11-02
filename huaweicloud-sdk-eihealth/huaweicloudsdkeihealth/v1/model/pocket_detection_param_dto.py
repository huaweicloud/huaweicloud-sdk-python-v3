# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PocketDetectionParamDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'timestep_size': 'float',
        'num_minimization_steps': 'int',
        'pre_equilibrium_time': 'int',
        'pocket_detection_time': 'int',
        'num_surface_points': 'int',
        'probe_radius': 'float'
    }

    attribute_map = {
        'timestep_size': 'timestep_size',
        'num_minimization_steps': 'num_minimization_steps',
        'pre_equilibrium_time': 'pre_equilibrium_time',
        'pocket_detection_time': 'pocket_detection_time',
        'num_surface_points': 'num_surface_points',
        'probe_radius': 'probe_radius'
    }

    def __init__(self, timestep_size=None, num_minimization_steps=None, pre_equilibrium_time=None, pocket_detection_time=None, num_surface_points=None, probe_radius=None):
        """PocketDetectionParamDto

        The model defined in huaweicloud sdk

        :param timestep_size: 时间步长，单位ps
        :type timestep_size: float
        :param num_minimization_steps: 最小化步数
        :type num_minimization_steps: int
        :param pre_equilibrium_time: 预平衡时长，单位ps
        :type pre_equilibrium_time: int
        :param pocket_detection_time: 口袋发现时长，单位ns
        :type pocket_detection_time: int
        :param num_surface_points: 表面原子离散点数量
        :type num_surface_points: int
        :param probe_radius: 探针半径，单位A
        :type probe_radius: float
        """
        
        

        self._timestep_size = None
        self._num_minimization_steps = None
        self._pre_equilibrium_time = None
        self._pocket_detection_time = None
        self._num_surface_points = None
        self._probe_radius = None
        self.discriminator = None

        if timestep_size is not None:
            self.timestep_size = timestep_size
        if num_minimization_steps is not None:
            self.num_minimization_steps = num_minimization_steps
        if pre_equilibrium_time is not None:
            self.pre_equilibrium_time = pre_equilibrium_time
        if pocket_detection_time is not None:
            self.pocket_detection_time = pocket_detection_time
        if num_surface_points is not None:
            self.num_surface_points = num_surface_points
        if probe_radius is not None:
            self.probe_radius = probe_radius

    @property
    def timestep_size(self):
        """Gets the timestep_size of this PocketDetectionParamDto.

        时间步长，单位ps

        :return: The timestep_size of this PocketDetectionParamDto.
        :rtype: float
        """
        return self._timestep_size

    @timestep_size.setter
    def timestep_size(self, timestep_size):
        """Sets the timestep_size of this PocketDetectionParamDto.

        时间步长，单位ps

        :param timestep_size: The timestep_size of this PocketDetectionParamDto.
        :type timestep_size: float
        """
        self._timestep_size = timestep_size

    @property
    def num_minimization_steps(self):
        """Gets the num_minimization_steps of this PocketDetectionParamDto.

        最小化步数

        :return: The num_minimization_steps of this PocketDetectionParamDto.
        :rtype: int
        """
        return self._num_minimization_steps

    @num_minimization_steps.setter
    def num_minimization_steps(self, num_minimization_steps):
        """Sets the num_minimization_steps of this PocketDetectionParamDto.

        最小化步数

        :param num_minimization_steps: The num_minimization_steps of this PocketDetectionParamDto.
        :type num_minimization_steps: int
        """
        self._num_minimization_steps = num_minimization_steps

    @property
    def pre_equilibrium_time(self):
        """Gets the pre_equilibrium_time of this PocketDetectionParamDto.

        预平衡时长，单位ps

        :return: The pre_equilibrium_time of this PocketDetectionParamDto.
        :rtype: int
        """
        return self._pre_equilibrium_time

    @pre_equilibrium_time.setter
    def pre_equilibrium_time(self, pre_equilibrium_time):
        """Sets the pre_equilibrium_time of this PocketDetectionParamDto.

        预平衡时长，单位ps

        :param pre_equilibrium_time: The pre_equilibrium_time of this PocketDetectionParamDto.
        :type pre_equilibrium_time: int
        """
        self._pre_equilibrium_time = pre_equilibrium_time

    @property
    def pocket_detection_time(self):
        """Gets the pocket_detection_time of this PocketDetectionParamDto.

        口袋发现时长，单位ns

        :return: The pocket_detection_time of this PocketDetectionParamDto.
        :rtype: int
        """
        return self._pocket_detection_time

    @pocket_detection_time.setter
    def pocket_detection_time(self, pocket_detection_time):
        """Sets the pocket_detection_time of this PocketDetectionParamDto.

        口袋发现时长，单位ns

        :param pocket_detection_time: The pocket_detection_time of this PocketDetectionParamDto.
        :type pocket_detection_time: int
        """
        self._pocket_detection_time = pocket_detection_time

    @property
    def num_surface_points(self):
        """Gets the num_surface_points of this PocketDetectionParamDto.

        表面原子离散点数量

        :return: The num_surface_points of this PocketDetectionParamDto.
        :rtype: int
        """
        return self._num_surface_points

    @num_surface_points.setter
    def num_surface_points(self, num_surface_points):
        """Sets the num_surface_points of this PocketDetectionParamDto.

        表面原子离散点数量

        :param num_surface_points: The num_surface_points of this PocketDetectionParamDto.
        :type num_surface_points: int
        """
        self._num_surface_points = num_surface_points

    @property
    def probe_radius(self):
        """Gets the probe_radius of this PocketDetectionParamDto.

        探针半径，单位A

        :return: The probe_radius of this PocketDetectionParamDto.
        :rtype: float
        """
        return self._probe_radius

    @probe_radius.setter
    def probe_radius(self, probe_radius):
        """Sets the probe_radius of this PocketDetectionParamDto.

        探针半径，单位A

        :param probe_radius: The probe_radius of this PocketDetectionParamDto.
        :type probe_radius: float
        """
        self._probe_radius = probe_radius

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
        if not isinstance(other, PocketDetectionParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
