# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MdParam:

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
        'temperature': 'float',
        'step_params': 'MdStepParam'
    }

    attribute_map = {
        'timestep_size': 'timestep_size',
        'temperature': 'temperature',
        'step_params': 'step_params'
    }

    def __init__(self, timestep_size=None, temperature=None, step_params=None):
        r"""MdParam

        The model defined in huaweicloud sdk

        :param timestep_size: MD模拟的时间步长，单位fs，取值范围：大于0，小于等于5
        :type timestep_size: float
        :param temperature: MD模拟的温度，单位K
        :type temperature: float
        :param step_params: 
        :type step_params: :class:`huaweicloudsdkeihealth.v1.MdStepParam`
        """
        
        

        self._timestep_size = None
        self._temperature = None
        self._step_params = None
        self.discriminator = None

        if timestep_size is not None:
            self.timestep_size = timestep_size
        if temperature is not None:
            self.temperature = temperature
        if step_params is not None:
            self.step_params = step_params

    @property
    def timestep_size(self):
        r"""Gets the timestep_size of this MdParam.

        MD模拟的时间步长，单位fs，取值范围：大于0，小于等于5

        :return: The timestep_size of this MdParam.
        :rtype: float
        """
        return self._timestep_size

    @timestep_size.setter
    def timestep_size(self, timestep_size):
        r"""Sets the timestep_size of this MdParam.

        MD模拟的时间步长，单位fs，取值范围：大于0，小于等于5

        :param timestep_size: The timestep_size of this MdParam.
        :type timestep_size: float
        """
        self._timestep_size = timestep_size

    @property
    def temperature(self):
        r"""Gets the temperature of this MdParam.

        MD模拟的温度，单位K

        :return: The temperature of this MdParam.
        :rtype: float
        """
        return self._temperature

    @temperature.setter
    def temperature(self, temperature):
        r"""Sets the temperature of this MdParam.

        MD模拟的温度，单位K

        :param temperature: The temperature of this MdParam.
        :type temperature: float
        """
        self._temperature = temperature

    @property
    def step_params(self):
        r"""Gets the step_params of this MdParam.

        :return: The step_params of this MdParam.
        :rtype: :class:`huaweicloudsdkeihealth.v1.MdStepParam`
        """
        return self._step_params

    @step_params.setter
    def step_params(self, step_params):
        r"""Sets the step_params of this MdParam.

        :param step_params: The step_params of this MdParam.
        :type step_params: :class:`huaweicloudsdkeihealth.v1.MdStepParam`
        """
        self._step_params = step_params

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
        if not isinstance(other, MdParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
