# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class FepParamDto:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'pre_equilibrium_time': 'float',
        'equilibrium_time': 'float',
        'num_pre_equilibrium_steps': 'int',
        'num_equilibrium_steps': 'int',
        'timestep_size': 'float',
        'num_lambda': 'int'
    }

    attribute_map = {
        'pre_equilibrium_time': 'pre_equilibrium_time',
        'equilibrium_time': 'equilibrium_time',
        'num_pre_equilibrium_steps': 'num_pre_equilibrium_steps',
        'num_equilibrium_steps': 'num_equilibrium_steps',
        'timestep_size': 'timestep_size',
        'num_lambda': 'num_lambda'
    }

    def __init__(self, pre_equilibrium_time=None, equilibrium_time=None, num_pre_equilibrium_steps=None, num_equilibrium_steps=None, timestep_size=None, num_lambda=None):
        r"""FepParamDto

        The model defined in huaweicloud sdk

        :param pre_equilibrium_time: 预平衡时长，单位ps，范围为0-200，不包含0，默认为100ps
        :type pre_equilibrium_time: float
        :param equilibrium_time: 平衡时长，单位ns，范围为0-10，不包含0，默认为1ns
        :type equilibrium_time: float
        :param num_pre_equilibrium_steps: 预平衡步数，默认为50000
        :type num_pre_equilibrium_steps: int
        :param num_equilibrium_steps: 平衡步数，默认为500000
        :type num_equilibrium_steps: int
        :param timestep_size: 时间步长，单位ps，取值范围：大于0，小于等于0.005
        :type timestep_size: float
        :param num_lambda: lambda个数
        :type num_lambda: int
        """
        
        

        self._pre_equilibrium_time = None
        self._equilibrium_time = None
        self._num_pre_equilibrium_steps = None
        self._num_equilibrium_steps = None
        self._timestep_size = None
        self._num_lambda = None
        self.discriminator = None

        if pre_equilibrium_time is not None:
            self.pre_equilibrium_time = pre_equilibrium_time
        if equilibrium_time is not None:
            self.equilibrium_time = equilibrium_time
        if num_pre_equilibrium_steps is not None:
            self.num_pre_equilibrium_steps = num_pre_equilibrium_steps
        if num_equilibrium_steps is not None:
            self.num_equilibrium_steps = num_equilibrium_steps
        if timestep_size is not None:
            self.timestep_size = timestep_size
        if num_lambda is not None:
            self.num_lambda = num_lambda

    @property
    def pre_equilibrium_time(self):
        r"""Gets the pre_equilibrium_time of this FepParamDto.

        预平衡时长，单位ps，范围为0-200，不包含0，默认为100ps

        :return: The pre_equilibrium_time of this FepParamDto.
        :rtype: float
        """
        return self._pre_equilibrium_time

    @pre_equilibrium_time.setter
    def pre_equilibrium_time(self, pre_equilibrium_time):
        r"""Sets the pre_equilibrium_time of this FepParamDto.

        预平衡时长，单位ps，范围为0-200，不包含0，默认为100ps

        :param pre_equilibrium_time: The pre_equilibrium_time of this FepParamDto.
        :type pre_equilibrium_time: float
        """
        self._pre_equilibrium_time = pre_equilibrium_time

    @property
    def equilibrium_time(self):
        r"""Gets the equilibrium_time of this FepParamDto.

        平衡时长，单位ns，范围为0-10，不包含0，默认为1ns

        :return: The equilibrium_time of this FepParamDto.
        :rtype: float
        """
        return self._equilibrium_time

    @equilibrium_time.setter
    def equilibrium_time(self, equilibrium_time):
        r"""Sets the equilibrium_time of this FepParamDto.

        平衡时长，单位ns，范围为0-10，不包含0，默认为1ns

        :param equilibrium_time: The equilibrium_time of this FepParamDto.
        :type equilibrium_time: float
        """
        self._equilibrium_time = equilibrium_time

    @property
    def num_pre_equilibrium_steps(self):
        r"""Gets the num_pre_equilibrium_steps of this FepParamDto.

        预平衡步数，默认为50000

        :return: The num_pre_equilibrium_steps of this FepParamDto.
        :rtype: int
        """
        return self._num_pre_equilibrium_steps

    @num_pre_equilibrium_steps.setter
    def num_pre_equilibrium_steps(self, num_pre_equilibrium_steps):
        r"""Sets the num_pre_equilibrium_steps of this FepParamDto.

        预平衡步数，默认为50000

        :param num_pre_equilibrium_steps: The num_pre_equilibrium_steps of this FepParamDto.
        :type num_pre_equilibrium_steps: int
        """
        self._num_pre_equilibrium_steps = num_pre_equilibrium_steps

    @property
    def num_equilibrium_steps(self):
        r"""Gets the num_equilibrium_steps of this FepParamDto.

        平衡步数，默认为500000

        :return: The num_equilibrium_steps of this FepParamDto.
        :rtype: int
        """
        return self._num_equilibrium_steps

    @num_equilibrium_steps.setter
    def num_equilibrium_steps(self, num_equilibrium_steps):
        r"""Sets the num_equilibrium_steps of this FepParamDto.

        平衡步数，默认为500000

        :param num_equilibrium_steps: The num_equilibrium_steps of this FepParamDto.
        :type num_equilibrium_steps: int
        """
        self._num_equilibrium_steps = num_equilibrium_steps

    @property
    def timestep_size(self):
        r"""Gets the timestep_size of this FepParamDto.

        时间步长，单位ps，取值范围：大于0，小于等于0.005

        :return: The timestep_size of this FepParamDto.
        :rtype: float
        """
        return self._timestep_size

    @timestep_size.setter
    def timestep_size(self, timestep_size):
        r"""Sets the timestep_size of this FepParamDto.

        时间步长，单位ps，取值范围：大于0，小于等于0.005

        :param timestep_size: The timestep_size of this FepParamDto.
        :type timestep_size: float
        """
        self._timestep_size = timestep_size

    @property
    def num_lambda(self):
        r"""Gets the num_lambda of this FepParamDto.

        lambda个数

        :return: The num_lambda of this FepParamDto.
        :rtype: int
        """
        return self._num_lambda

    @num_lambda.setter
    def num_lambda(self, num_lambda):
        r"""Sets the num_lambda of this FepParamDto.

        lambda个数

        :param num_lambda: The num_lambda of this FepParamDto.
        :type num_lambda: int
        """
        self._num_lambda = num_lambda

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
        if not isinstance(other, FepParamDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
