# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmResponseAdvancedConfigAutoSearchSearchParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'param_type': 'str',
        'lower_bound': 'str',
        'upper_bound': 'str',
        'discrete_points_num': 'str',
        'discrete_values': 'str'
    }

    attribute_map = {
        'name': 'name',
        'param_type': 'param_type',
        'lower_bound': 'lower_bound',
        'upper_bound': 'upper_bound',
        'discrete_points_num': 'discrete_points_num',
        'discrete_values': 'discrete_values'
    }

    def __init__(self, name=None, param_type=None, lower_bound=None, upper_bound=None, discrete_points_num=None, discrete_values=None):
        r"""AlgorithmResponseAdvancedConfigAutoSearchSearchParams

        The model defined in huaweicloud sdk

        :param name: 超参名称。
        :type name: str
        :param param_type: 参数类型。 - continuous：指定时表示这个超参是连续类型的。连续类型的超参在算法使用于训练作业时，控制台显示为输入框。 - discrete：指定时表示这个超参是离散类型的。离散类型的超参在算法使用于训练作业时，控制台显示为下拉选择框架。
        :type param_type: str
        :param lower_bound: 超参下界。
        :type lower_bound: str
        :param upper_bound: 超参上界。
        :type upper_bound: str
        :param discrete_points_num: 连续型超参离散化取值个数。
        :type discrete_points_num: str
        :param discrete_values: 离散型超参的取值列表。
        :type discrete_values: str
        """
        
        

        self._name = None
        self._param_type = None
        self._lower_bound = None
        self._upper_bound = None
        self._discrete_points_num = None
        self._discrete_values = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if param_type is not None:
            self.param_type = param_type
        if lower_bound is not None:
            self.lower_bound = lower_bound
        if upper_bound is not None:
            self.upper_bound = upper_bound
        if discrete_points_num is not None:
            self.discrete_points_num = discrete_points_num
        if discrete_values is not None:
            self.discrete_values = discrete_values

    @property
    def name(self):
        r"""Gets the name of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        超参名称。

        :return: The name of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        超参名称。

        :param name: The name of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :type name: str
        """
        self._name = name

    @property
    def param_type(self):
        r"""Gets the param_type of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        参数类型。 - continuous：指定时表示这个超参是连续类型的。连续类型的超参在算法使用于训练作业时，控制台显示为输入框。 - discrete：指定时表示这个超参是离散类型的。离散类型的超参在算法使用于训练作业时，控制台显示为下拉选择框架。

        :return: The param_type of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :rtype: str
        """
        return self._param_type

    @param_type.setter
    def param_type(self, param_type):
        r"""Sets the param_type of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        参数类型。 - continuous：指定时表示这个超参是连续类型的。连续类型的超参在算法使用于训练作业时，控制台显示为输入框。 - discrete：指定时表示这个超参是离散类型的。离散类型的超参在算法使用于训练作业时，控制台显示为下拉选择框架。

        :param param_type: The param_type of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :type param_type: str
        """
        self._param_type = param_type

    @property
    def lower_bound(self):
        r"""Gets the lower_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        超参下界。

        :return: The lower_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :rtype: str
        """
        return self._lower_bound

    @lower_bound.setter
    def lower_bound(self, lower_bound):
        r"""Sets the lower_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        超参下界。

        :param lower_bound: The lower_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :type lower_bound: str
        """
        self._lower_bound = lower_bound

    @property
    def upper_bound(self):
        r"""Gets the upper_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        超参上界。

        :return: The upper_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :rtype: str
        """
        return self._upper_bound

    @upper_bound.setter
    def upper_bound(self, upper_bound):
        r"""Sets the upper_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        超参上界。

        :param upper_bound: The upper_bound of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :type upper_bound: str
        """
        self._upper_bound = upper_bound

    @property
    def discrete_points_num(self):
        r"""Gets the discrete_points_num of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        连续型超参离散化取值个数。

        :return: The discrete_points_num of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :rtype: str
        """
        return self._discrete_points_num

    @discrete_points_num.setter
    def discrete_points_num(self, discrete_points_num):
        r"""Sets the discrete_points_num of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        连续型超参离散化取值个数。

        :param discrete_points_num: The discrete_points_num of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :type discrete_points_num: str
        """
        self._discrete_points_num = discrete_points_num

    @property
    def discrete_values(self):
        r"""Gets the discrete_values of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        离散型超参的取值列表。

        :return: The discrete_values of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :rtype: str
        """
        return self._discrete_values

    @discrete_values.setter
    def discrete_values(self, discrete_values):
        r"""Sets the discrete_values of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.

        离散型超参的取值列表。

        :param discrete_values: The discrete_values of this AlgorithmResponseAdvancedConfigAutoSearchSearchParams.
        :type discrete_values: str
        """
        self._discrete_values = discrete_values

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
        if not isinstance(other, AlgorithmResponseAdvancedConfigAutoSearchSearchParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
