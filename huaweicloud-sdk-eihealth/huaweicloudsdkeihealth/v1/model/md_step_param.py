# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MdStepParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'energy_minimization_steps': 'int',
        'nvt': 'float',
        'npt': 'float',
        'simulation_time': 'float'
    }

    attribute_map = {
        'energy_minimization_steps': 'energy_minimization_steps',
        'nvt': 'nvt',
        'npt': 'npt',
        'simulation_time': 'simulation_time'
    }

    def __init__(self, energy_minimization_steps=None, nvt=None, npt=None, simulation_time=None):
        r"""MdStepParam

        The model defined in huaweicloud sdk

        :param energy_minimization_steps: 能量最小化的步骤
        :type energy_minimization_steps: int
        :param nvt: 等温等体步骤模拟的时长，单位ps
        :type nvt: float
        :param npt: 等压等温步骤模拟的时长，单位ps
        :type npt: float
        :param simulation_time: 平衡步骤模拟的时长，单位ns
        :type simulation_time: float
        """
        
        

        self._energy_minimization_steps = None
        self._nvt = None
        self._npt = None
        self._simulation_time = None
        self.discriminator = None

        if energy_minimization_steps is not None:
            self.energy_minimization_steps = energy_minimization_steps
        if nvt is not None:
            self.nvt = nvt
        if npt is not None:
            self.npt = npt
        if simulation_time is not None:
            self.simulation_time = simulation_time

    @property
    def energy_minimization_steps(self):
        r"""Gets the energy_minimization_steps of this MdStepParam.

        能量最小化的步骤

        :return: The energy_minimization_steps of this MdStepParam.
        :rtype: int
        """
        return self._energy_minimization_steps

    @energy_minimization_steps.setter
    def energy_minimization_steps(self, energy_minimization_steps):
        r"""Sets the energy_minimization_steps of this MdStepParam.

        能量最小化的步骤

        :param energy_minimization_steps: The energy_minimization_steps of this MdStepParam.
        :type energy_minimization_steps: int
        """
        self._energy_minimization_steps = energy_minimization_steps

    @property
    def nvt(self):
        r"""Gets the nvt of this MdStepParam.

        等温等体步骤模拟的时长，单位ps

        :return: The nvt of this MdStepParam.
        :rtype: float
        """
        return self._nvt

    @nvt.setter
    def nvt(self, nvt):
        r"""Sets the nvt of this MdStepParam.

        等温等体步骤模拟的时长，单位ps

        :param nvt: The nvt of this MdStepParam.
        :type nvt: float
        """
        self._nvt = nvt

    @property
    def npt(self):
        r"""Gets the npt of this MdStepParam.

        等压等温步骤模拟的时长，单位ps

        :return: The npt of this MdStepParam.
        :rtype: float
        """
        return self._npt

    @npt.setter
    def npt(self, npt):
        r"""Sets the npt of this MdStepParam.

        等压等温步骤模拟的时长，单位ps

        :param npt: The npt of this MdStepParam.
        :type npt: float
        """
        self._npt = npt

    @property
    def simulation_time(self):
        r"""Gets the simulation_time of this MdStepParam.

        平衡步骤模拟的时长，单位ns

        :return: The simulation_time of this MdStepParam.
        :rtype: float
        """
        return self._simulation_time

    @simulation_time.setter
    def simulation_time(self, simulation_time):
        r"""Sets the simulation_time of this MdStepParam.

        平衡步骤模拟的时长，单位ns

        :param simulation_time: The simulation_time of this MdStepParam.
        :type simulation_time: float
        """
        self._simulation_time = simulation_time

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
        if not isinstance(other, MdStepParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
