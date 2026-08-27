# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelCost:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'input': 'float',
        'output': 'float',
        'cache_read': 'float',
        'cache_write': 'float'
    }

    attribute_map = {
        'input': 'input',
        'output': 'output',
        'cache_read': 'cache_read',
        'cache_write': 'cache_write'
    }

    def __init__(self, input=None, output=None, cache_read=None, cache_write=None):
        r"""ModelCost

        The model defined in huaweicloud sdk

        :param input: 每百万输入Token费用。
        :type input: float
        :param output: 每百万输出Token费用。
        :type output: float
        :param cache_read: 每百万缓存读取Token费用。
        :type cache_read: float
        :param cache_write: 每百万缓存写入Token费用。
        :type cache_write: float
        """
        
        

        self._input = None
        self._output = None
        self._cache_read = None
        self._cache_write = None
        self.discriminator = None

        if input is not None:
            self.input = input
        if output is not None:
            self.output = output
        if cache_read is not None:
            self.cache_read = cache_read
        if cache_write is not None:
            self.cache_write = cache_write

    @property
    def input(self):
        r"""Gets the input of this ModelCost.

        每百万输入Token费用。

        :return: The input of this ModelCost.
        :rtype: float
        """
        return self._input

    @input.setter
    def input(self, input):
        r"""Sets the input of this ModelCost.

        每百万输入Token费用。

        :param input: The input of this ModelCost.
        :type input: float
        """
        self._input = input

    @property
    def output(self):
        r"""Gets the output of this ModelCost.

        每百万输出Token费用。

        :return: The output of this ModelCost.
        :rtype: float
        """
        return self._output

    @output.setter
    def output(self, output):
        r"""Sets the output of this ModelCost.

        每百万输出Token费用。

        :param output: The output of this ModelCost.
        :type output: float
        """
        self._output = output

    @property
    def cache_read(self):
        r"""Gets the cache_read of this ModelCost.

        每百万缓存读取Token费用。

        :return: The cache_read of this ModelCost.
        :rtype: float
        """
        return self._cache_read

    @cache_read.setter
    def cache_read(self, cache_read):
        r"""Sets the cache_read of this ModelCost.

        每百万缓存读取Token费用。

        :param cache_read: The cache_read of this ModelCost.
        :type cache_read: float
        """
        self._cache_read = cache_read

    @property
    def cache_write(self):
        r"""Gets the cache_write of this ModelCost.

        每百万缓存写入Token费用。

        :return: The cache_write of this ModelCost.
        :rtype: float
        """
        return self._cache_write

    @cache_write.setter
    def cache_write(self, cache_write):
        r"""Sets the cache_write of this ModelCost.

        每百万缓存写入Token费用。

        :param cache_write: The cache_write of this ModelCost.
        :type cache_write: float
        """
        self._cache_write = cache_write

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
        if not isinstance(other, ModelCost):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
