# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeepLearingParam:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'initial_parameters': 'Initial',
        'optimize_parameters': 'Optimizer',
        'regular_parameters': 'Regular',
        'max_iterations': 'int',
        'early_stop_iterations': 'int',
        'batch_size': 'int',
        'dataset_split_parts': 'int',
        'restart_train': 'bool'
    }

    attribute_map = {
        'initial_parameters': 'initial_parameters',
        'optimize_parameters': 'optimize_parameters',
        'regular_parameters': 'regular_parameters',
        'max_iterations': 'max_iterations',
        'early_stop_iterations': 'early_stop_iterations',
        'batch_size': 'batch_size',
        'dataset_split_parts': 'dataset_split_parts',
        'restart_train': 'restart_train'
    }

    def __init__(self, initial_parameters=None, optimize_parameters=None, regular_parameters=None, max_iterations=None, early_stop_iterations=None, batch_size=None, dataset_split_parts=None, restart_train=None):
        """DeepLearingParam

        The model defined in huaweicloud sdk

        :param initial_parameters: 
        :type initial_parameters: :class:`huaweicloudsdkres.v1.Initial`
        :param optimize_parameters: 
        :type optimize_parameters: :class:`huaweicloudsdkres.v1.Optimizer`
        :param regular_parameters: 
        :type regular_parameters: :class:`huaweicloudsdkres.v1.Regular`
        :param max_iterations: 最大迭代轮数。
        :type max_iterations: int
        :param early_stop_iterations: 提前终止训练轮数。
        :type early_stop_iterations: int
        :param batch_size: 批量大小。
        :type batch_size: int
        :param dataset_split_parts: 训练数据集切分数量。
        :type dataset_split_parts: int
        :param restart_train: 重新训练。
        :type restart_train: bool
        """
        
        

        self._initial_parameters = None
        self._optimize_parameters = None
        self._regular_parameters = None
        self._max_iterations = None
        self._early_stop_iterations = None
        self._batch_size = None
        self._dataset_split_parts = None
        self._restart_train = None
        self.discriminator = None

        if initial_parameters is not None:
            self.initial_parameters = initial_parameters
        if optimize_parameters is not None:
            self.optimize_parameters = optimize_parameters
        if regular_parameters is not None:
            self.regular_parameters = regular_parameters
        if max_iterations is not None:
            self.max_iterations = max_iterations
        if early_stop_iterations is not None:
            self.early_stop_iterations = early_stop_iterations
        if batch_size is not None:
            self.batch_size = batch_size
        if dataset_split_parts is not None:
            self.dataset_split_parts = dataset_split_parts
        if restart_train is not None:
            self.restart_train = restart_train

    @property
    def initial_parameters(self):
        """Gets the initial_parameters of this DeepLearingParam.


        :return: The initial_parameters of this DeepLearingParam.
        :rtype: :class:`huaweicloudsdkres.v1.Initial`
        """
        return self._initial_parameters

    @initial_parameters.setter
    def initial_parameters(self, initial_parameters):
        """Sets the initial_parameters of this DeepLearingParam.


        :param initial_parameters: The initial_parameters of this DeepLearingParam.
        :type initial_parameters: :class:`huaweicloudsdkres.v1.Initial`
        """
        self._initial_parameters = initial_parameters

    @property
    def optimize_parameters(self):
        """Gets the optimize_parameters of this DeepLearingParam.


        :return: The optimize_parameters of this DeepLearingParam.
        :rtype: :class:`huaweicloudsdkres.v1.Optimizer`
        """
        return self._optimize_parameters

    @optimize_parameters.setter
    def optimize_parameters(self, optimize_parameters):
        """Sets the optimize_parameters of this DeepLearingParam.


        :param optimize_parameters: The optimize_parameters of this DeepLearingParam.
        :type optimize_parameters: :class:`huaweicloudsdkres.v1.Optimizer`
        """
        self._optimize_parameters = optimize_parameters

    @property
    def regular_parameters(self):
        """Gets the regular_parameters of this DeepLearingParam.


        :return: The regular_parameters of this DeepLearingParam.
        :rtype: :class:`huaweicloudsdkres.v1.Regular`
        """
        return self._regular_parameters

    @regular_parameters.setter
    def regular_parameters(self, regular_parameters):
        """Sets the regular_parameters of this DeepLearingParam.


        :param regular_parameters: The regular_parameters of this DeepLearingParam.
        :type regular_parameters: :class:`huaweicloudsdkres.v1.Regular`
        """
        self._regular_parameters = regular_parameters

    @property
    def max_iterations(self):
        """Gets the max_iterations of this DeepLearingParam.

        最大迭代轮数。

        :return: The max_iterations of this DeepLearingParam.
        :rtype: int
        """
        return self._max_iterations

    @max_iterations.setter
    def max_iterations(self, max_iterations):
        """Sets the max_iterations of this DeepLearingParam.

        最大迭代轮数。

        :param max_iterations: The max_iterations of this DeepLearingParam.
        :type max_iterations: int
        """
        self._max_iterations = max_iterations

    @property
    def early_stop_iterations(self):
        """Gets the early_stop_iterations of this DeepLearingParam.

        提前终止训练轮数。

        :return: The early_stop_iterations of this DeepLearingParam.
        :rtype: int
        """
        return self._early_stop_iterations

    @early_stop_iterations.setter
    def early_stop_iterations(self, early_stop_iterations):
        """Sets the early_stop_iterations of this DeepLearingParam.

        提前终止训练轮数。

        :param early_stop_iterations: The early_stop_iterations of this DeepLearingParam.
        :type early_stop_iterations: int
        """
        self._early_stop_iterations = early_stop_iterations

    @property
    def batch_size(self):
        """Gets the batch_size of this DeepLearingParam.

        批量大小。

        :return: The batch_size of this DeepLearingParam.
        :rtype: int
        """
        return self._batch_size

    @batch_size.setter
    def batch_size(self, batch_size):
        """Sets the batch_size of this DeepLearingParam.

        批量大小。

        :param batch_size: The batch_size of this DeepLearingParam.
        :type batch_size: int
        """
        self._batch_size = batch_size

    @property
    def dataset_split_parts(self):
        """Gets the dataset_split_parts of this DeepLearingParam.

        训练数据集切分数量。

        :return: The dataset_split_parts of this DeepLearingParam.
        :rtype: int
        """
        return self._dataset_split_parts

    @dataset_split_parts.setter
    def dataset_split_parts(self, dataset_split_parts):
        """Sets the dataset_split_parts of this DeepLearingParam.

        训练数据集切分数量。

        :param dataset_split_parts: The dataset_split_parts of this DeepLearingParam.
        :type dataset_split_parts: int
        """
        self._dataset_split_parts = dataset_split_parts

    @property
    def restart_train(self):
        """Gets the restart_train of this DeepLearingParam.

        重新训练。

        :return: The restart_train of this DeepLearingParam.
        :rtype: bool
        """
        return self._restart_train

    @restart_train.setter
    def restart_train(self, restart_train):
        """Sets the restart_train of this DeepLearingParam.

        重新训练。

        :param restart_train: The restart_train of this DeepLearingParam.
        :type restart_train: bool
        """
        self._restart_train = restart_train

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
        if not isinstance(other, DeepLearingParam):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
