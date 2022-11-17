# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AlgorithmSpecifyParameters:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'latent_vector_length': 'int',
        'architecture': 'list[int]',
        'active_function': 'str',
        'value_keep_probability': 'float',
        'embed_size': 'list[int]',
        'mlp_architecture': 'list[int]',
        'max_order': 'int',
        'hash_sizes': 'list[int]',
        'hash_compensation': 'list[float]',
        'use_wide_part': 'bool',
        'structure_optimizer': 'Optimizer',
        'merge_multi_hot': 'bool',
        'fix_structure': 'bool'
    }

    attribute_map = {
        'latent_vector_length': 'latent_vector_length',
        'architecture': 'architecture',
        'active_function': 'active_function',
        'value_keep_probability': 'value_keep_probability',
        'embed_size': 'embed_size',
        'mlp_architecture': 'mlp_architecture',
        'max_order': 'max_order',
        'hash_sizes': 'hash_sizes',
        'hash_compensation': 'hash_compensation',
        'use_wide_part': 'use_wide_part',
        'structure_optimizer': 'structure_optimizer',
        'merge_multi_hot': 'merge_multi_hot',
        'fix_structure': 'fix_structure'
    }

    def __init__(self, latent_vector_length=None, architecture=None, active_function=None, value_keep_probability=None, embed_size=None, mlp_architecture=None, max_order=None, hash_sizes=None, hash_compensation=None, use_wide_part=None, structure_optimizer=None, merge_multi_hot=None, fix_structure=None):
        """AlgorithmSpecifyParameters

        The model defined in huaweicloud sdk

        :param latent_vector_length: 隐向量长度(DEEPFM需要提供此参数)。
        :type latent_vector_length: int
        :param architecture: 神经网络结构(DEEPFM需要提供此参数)。
        :type architecture: list[int]
        :param active_function: 激活函数(DEEPFM需要提供此参数,AutoGroup需要提供此参数)。
        :type active_function: str
        :param value_keep_probability: 神经元值保留概率(DEEPFM需要提供此参数,AutoGroup需要提供此参数)。
        :type value_keep_probability: float
        :param embed_size: 各阶隐向量长度(AutoGroup需要提供此参数)。
        :type embed_size: list[int]
        :param mlp_architecture: 神经网络结构(AutoGroup需要提供此参数)。
        :type mlp_architecture: list[int]
        :param max_order: 最大交互阶数(AutoGroup需要提供此参数)。
        :type max_order: int
        :param hash_sizes: 哈希长度(AutoGroup需要提供此参数)。
        :type hash_sizes: list[int]
        :param hash_compensation: 特征交互层惩罚项系数(AutoGroup需要提供此参数)。
        :type hash_compensation: list[float]
        :param use_wide_part: 使用线性部分(AutoGroup需要提供此参数)。
        :type use_wide_part: bool
        :param structure_optimizer: 
        :type structure_optimizer: :class:`huaweicloudsdkres.v1.Optimizer`
        :param merge_multi_hot: 融合多值特征(AutoGroup需要提供此参数)。
        :type merge_multi_hot: bool
        :param fix_structure: 固定哈希结构(AutoGroup需要提供此参数)。
        :type fix_structure: bool
        """
        
        

        self._latent_vector_length = None
        self._architecture = None
        self._active_function = None
        self._value_keep_probability = None
        self._embed_size = None
        self._mlp_architecture = None
        self._max_order = None
        self._hash_sizes = None
        self._hash_compensation = None
        self._use_wide_part = None
        self._structure_optimizer = None
        self._merge_multi_hot = None
        self._fix_structure = None
        self.discriminator = None

        if latent_vector_length is not None:
            self.latent_vector_length = latent_vector_length
        if architecture is not None:
            self.architecture = architecture
        if active_function is not None:
            self.active_function = active_function
        if value_keep_probability is not None:
            self.value_keep_probability = value_keep_probability
        if embed_size is not None:
            self.embed_size = embed_size
        if mlp_architecture is not None:
            self.mlp_architecture = mlp_architecture
        if max_order is not None:
            self.max_order = max_order
        if hash_sizes is not None:
            self.hash_sizes = hash_sizes
        if hash_compensation is not None:
            self.hash_compensation = hash_compensation
        if use_wide_part is not None:
            self.use_wide_part = use_wide_part
        if structure_optimizer is not None:
            self.structure_optimizer = structure_optimizer
        if merge_multi_hot is not None:
            self.merge_multi_hot = merge_multi_hot
        if fix_structure is not None:
            self.fix_structure = fix_structure

    @property
    def latent_vector_length(self):
        """Gets the latent_vector_length of this AlgorithmSpecifyParameters.

        隐向量长度(DEEPFM需要提供此参数)。

        :return: The latent_vector_length of this AlgorithmSpecifyParameters.
        :rtype: int
        """
        return self._latent_vector_length

    @latent_vector_length.setter
    def latent_vector_length(self, latent_vector_length):
        """Sets the latent_vector_length of this AlgorithmSpecifyParameters.

        隐向量长度(DEEPFM需要提供此参数)。

        :param latent_vector_length: The latent_vector_length of this AlgorithmSpecifyParameters.
        :type latent_vector_length: int
        """
        self._latent_vector_length = latent_vector_length

    @property
    def architecture(self):
        """Gets the architecture of this AlgorithmSpecifyParameters.

        神经网络结构(DEEPFM需要提供此参数)。

        :return: The architecture of this AlgorithmSpecifyParameters.
        :rtype: list[int]
        """
        return self._architecture

    @architecture.setter
    def architecture(self, architecture):
        """Sets the architecture of this AlgorithmSpecifyParameters.

        神经网络结构(DEEPFM需要提供此参数)。

        :param architecture: The architecture of this AlgorithmSpecifyParameters.
        :type architecture: list[int]
        """
        self._architecture = architecture

    @property
    def active_function(self):
        """Gets the active_function of this AlgorithmSpecifyParameters.

        激活函数(DEEPFM需要提供此参数,AutoGroup需要提供此参数)。

        :return: The active_function of this AlgorithmSpecifyParameters.
        :rtype: str
        """
        return self._active_function

    @active_function.setter
    def active_function(self, active_function):
        """Sets the active_function of this AlgorithmSpecifyParameters.

        激活函数(DEEPFM需要提供此参数,AutoGroup需要提供此参数)。

        :param active_function: The active_function of this AlgorithmSpecifyParameters.
        :type active_function: str
        """
        self._active_function = active_function

    @property
    def value_keep_probability(self):
        """Gets the value_keep_probability of this AlgorithmSpecifyParameters.

        神经元值保留概率(DEEPFM需要提供此参数,AutoGroup需要提供此参数)。

        :return: The value_keep_probability of this AlgorithmSpecifyParameters.
        :rtype: float
        """
        return self._value_keep_probability

    @value_keep_probability.setter
    def value_keep_probability(self, value_keep_probability):
        """Sets the value_keep_probability of this AlgorithmSpecifyParameters.

        神经元值保留概率(DEEPFM需要提供此参数,AutoGroup需要提供此参数)。

        :param value_keep_probability: The value_keep_probability of this AlgorithmSpecifyParameters.
        :type value_keep_probability: float
        """
        self._value_keep_probability = value_keep_probability

    @property
    def embed_size(self):
        """Gets the embed_size of this AlgorithmSpecifyParameters.

        各阶隐向量长度(AutoGroup需要提供此参数)。

        :return: The embed_size of this AlgorithmSpecifyParameters.
        :rtype: list[int]
        """
        return self._embed_size

    @embed_size.setter
    def embed_size(self, embed_size):
        """Sets the embed_size of this AlgorithmSpecifyParameters.

        各阶隐向量长度(AutoGroup需要提供此参数)。

        :param embed_size: The embed_size of this AlgorithmSpecifyParameters.
        :type embed_size: list[int]
        """
        self._embed_size = embed_size

    @property
    def mlp_architecture(self):
        """Gets the mlp_architecture of this AlgorithmSpecifyParameters.

        神经网络结构(AutoGroup需要提供此参数)。

        :return: The mlp_architecture of this AlgorithmSpecifyParameters.
        :rtype: list[int]
        """
        return self._mlp_architecture

    @mlp_architecture.setter
    def mlp_architecture(self, mlp_architecture):
        """Sets the mlp_architecture of this AlgorithmSpecifyParameters.

        神经网络结构(AutoGroup需要提供此参数)。

        :param mlp_architecture: The mlp_architecture of this AlgorithmSpecifyParameters.
        :type mlp_architecture: list[int]
        """
        self._mlp_architecture = mlp_architecture

    @property
    def max_order(self):
        """Gets the max_order of this AlgorithmSpecifyParameters.

        最大交互阶数(AutoGroup需要提供此参数)。

        :return: The max_order of this AlgorithmSpecifyParameters.
        :rtype: int
        """
        return self._max_order

    @max_order.setter
    def max_order(self, max_order):
        """Sets the max_order of this AlgorithmSpecifyParameters.

        最大交互阶数(AutoGroup需要提供此参数)。

        :param max_order: The max_order of this AlgorithmSpecifyParameters.
        :type max_order: int
        """
        self._max_order = max_order

    @property
    def hash_sizes(self):
        """Gets the hash_sizes of this AlgorithmSpecifyParameters.

        哈希长度(AutoGroup需要提供此参数)。

        :return: The hash_sizes of this AlgorithmSpecifyParameters.
        :rtype: list[int]
        """
        return self._hash_sizes

    @hash_sizes.setter
    def hash_sizes(self, hash_sizes):
        """Sets the hash_sizes of this AlgorithmSpecifyParameters.

        哈希长度(AutoGroup需要提供此参数)。

        :param hash_sizes: The hash_sizes of this AlgorithmSpecifyParameters.
        :type hash_sizes: list[int]
        """
        self._hash_sizes = hash_sizes

    @property
    def hash_compensation(self):
        """Gets the hash_compensation of this AlgorithmSpecifyParameters.

        特征交互层惩罚项系数(AutoGroup需要提供此参数)。

        :return: The hash_compensation of this AlgorithmSpecifyParameters.
        :rtype: list[float]
        """
        return self._hash_compensation

    @hash_compensation.setter
    def hash_compensation(self, hash_compensation):
        """Sets the hash_compensation of this AlgorithmSpecifyParameters.

        特征交互层惩罚项系数(AutoGroup需要提供此参数)。

        :param hash_compensation: The hash_compensation of this AlgorithmSpecifyParameters.
        :type hash_compensation: list[float]
        """
        self._hash_compensation = hash_compensation

    @property
    def use_wide_part(self):
        """Gets the use_wide_part of this AlgorithmSpecifyParameters.

        使用线性部分(AutoGroup需要提供此参数)。

        :return: The use_wide_part of this AlgorithmSpecifyParameters.
        :rtype: bool
        """
        return self._use_wide_part

    @use_wide_part.setter
    def use_wide_part(self, use_wide_part):
        """Sets the use_wide_part of this AlgorithmSpecifyParameters.

        使用线性部分(AutoGroup需要提供此参数)。

        :param use_wide_part: The use_wide_part of this AlgorithmSpecifyParameters.
        :type use_wide_part: bool
        """
        self._use_wide_part = use_wide_part

    @property
    def structure_optimizer(self):
        """Gets the structure_optimizer of this AlgorithmSpecifyParameters.

        :return: The structure_optimizer of this AlgorithmSpecifyParameters.
        :rtype: :class:`huaweicloudsdkres.v1.Optimizer`
        """
        return self._structure_optimizer

    @structure_optimizer.setter
    def structure_optimizer(self, structure_optimizer):
        """Sets the structure_optimizer of this AlgorithmSpecifyParameters.

        :param structure_optimizer: The structure_optimizer of this AlgorithmSpecifyParameters.
        :type structure_optimizer: :class:`huaweicloudsdkres.v1.Optimizer`
        """
        self._structure_optimizer = structure_optimizer

    @property
    def merge_multi_hot(self):
        """Gets the merge_multi_hot of this AlgorithmSpecifyParameters.

        融合多值特征(AutoGroup需要提供此参数)。

        :return: The merge_multi_hot of this AlgorithmSpecifyParameters.
        :rtype: bool
        """
        return self._merge_multi_hot

    @merge_multi_hot.setter
    def merge_multi_hot(self, merge_multi_hot):
        """Sets the merge_multi_hot of this AlgorithmSpecifyParameters.

        融合多值特征(AutoGroup需要提供此参数)。

        :param merge_multi_hot: The merge_multi_hot of this AlgorithmSpecifyParameters.
        :type merge_multi_hot: bool
        """
        self._merge_multi_hot = merge_multi_hot

    @property
    def fix_structure(self):
        """Gets the fix_structure of this AlgorithmSpecifyParameters.

        固定哈希结构(AutoGroup需要提供此参数)。

        :return: The fix_structure of this AlgorithmSpecifyParameters.
        :rtype: bool
        """
        return self._fix_structure

    @fix_structure.setter
    def fix_structure(self, fix_structure):
        """Sets the fix_structure of this AlgorithmSpecifyParameters.

        固定哈希结构(AutoGroup需要提供此参数)。

        :param fix_structure: The fix_structure of this AlgorithmSpecifyParameters.
        :type fix_structure: bool
        """
        self._fix_structure = fix_structure

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
        if not isinstance(other, AlgorithmSpecifyParameters):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
