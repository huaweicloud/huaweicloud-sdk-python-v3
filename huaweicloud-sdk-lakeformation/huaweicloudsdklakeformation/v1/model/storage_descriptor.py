# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StorageDescriptor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'columns': 'list[Column]',
        'location': 'str',
        'compressed': 'bool',
        'input_format': 'str',
        'output_format': 'str',
        'number_of_buckets': 'int',
        'bucket_columns': 'list[str]',
        'sort_columns': 'list[Order]',
        'serde_info': 'SerDeInfo',
        'parameters': 'dict(str, str)',
        'skewed_info': 'SkewedInfo',
        'stored_as_sub_directories': 'bool'
    }

    attribute_map = {
        'columns': 'columns',
        'location': 'location',
        'compressed': 'compressed',
        'input_format': 'input_format',
        'output_format': 'output_format',
        'number_of_buckets': 'number_of_buckets',
        'bucket_columns': 'bucket_columns',
        'sort_columns': 'sort_columns',
        'serde_info': 'serde_info',
        'parameters': 'parameters',
        'skewed_info': 'skewed_info',
        'stored_as_sub_directories': 'stored_as_sub_directories'
    }

    def __init__(self, columns=None, location=None, compressed=None, input_format=None, output_format=None, number_of_buckets=None, bucket_columns=None, sort_columns=None, serde_info=None, parameters=None, skewed_info=None, stored_as_sub_directories=None):
        r"""StorageDescriptor

        The model defined in huaweicloud sdk

        :param columns: 分区列以外的所有字段
        :type columns: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        :param location: 存储路径
        :type location: str
        :param compressed: 是否启用数据压缩
        :type compressed: bool
        :param input_format: 输入格式
        :type input_format: str
        :param output_format: 输出格式
        :type output_format: str
        :param number_of_buckets: 分桶的桶数量
        :type number_of_buckets: int
        :param bucket_columns: 分桶字段
        :type bucket_columns: list[str]
        :param sort_columns: 指定表中的每个存储桶的排序顺序的列表
        :type sort_columns: list[:class:`huaweicloudsdklakeformation.v1.Order`]
        :param serde_info: 
        :type serde_info: :class:`huaweicloudsdklakeformation.v1.SerDeInfo`
        :param parameters: 存储描述符的参数。 key最小长度为1，最大长度为255. value最大长度为4000
        :type parameters: dict(str, str)
        :param skewed_info: 
        :type skewed_info: :class:`huaweicloudsdklakeformation.v1.SkewedInfo`
        :param stored_as_sub_directories: 数据是否会存放在子目录中
        :type stored_as_sub_directories: bool
        """
        
        

        self._columns = None
        self._location = None
        self._compressed = None
        self._input_format = None
        self._output_format = None
        self._number_of_buckets = None
        self._bucket_columns = None
        self._sort_columns = None
        self._serde_info = None
        self._parameters = None
        self._skewed_info = None
        self._stored_as_sub_directories = None
        self.discriminator = None

        self.columns = columns
        if location is not None:
            self.location = location
        self.compressed = compressed
        if input_format is not None:
            self.input_format = input_format
        if output_format is not None:
            self.output_format = output_format
        if number_of_buckets is not None:
            self.number_of_buckets = number_of_buckets
        if bucket_columns is not None:
            self.bucket_columns = bucket_columns
        if sort_columns is not None:
            self.sort_columns = sort_columns
        self.serde_info = serde_info
        self.parameters = parameters
        if skewed_info is not None:
            self.skewed_info = skewed_info
        if stored_as_sub_directories is not None:
            self.stored_as_sub_directories = stored_as_sub_directories

    @property
    def columns(self):
        r"""Gets the columns of this StorageDescriptor.

        分区列以外的所有字段

        :return: The columns of this StorageDescriptor.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        r"""Sets the columns of this StorageDescriptor.

        分区列以外的所有字段

        :param columns: The columns of this StorageDescriptor.
        :type columns: list[:class:`huaweicloudsdklakeformation.v1.Column`]
        """
        self._columns = columns

    @property
    def location(self):
        r"""Gets the location of this StorageDescriptor.

        存储路径

        :return: The location of this StorageDescriptor.
        :rtype: str
        """
        return self._location

    @location.setter
    def location(self, location):
        r"""Sets the location of this StorageDescriptor.

        存储路径

        :param location: The location of this StorageDescriptor.
        :type location: str
        """
        self._location = location

    @property
    def compressed(self):
        r"""Gets the compressed of this StorageDescriptor.

        是否启用数据压缩

        :return: The compressed of this StorageDescriptor.
        :rtype: bool
        """
        return self._compressed

    @compressed.setter
    def compressed(self, compressed):
        r"""Sets the compressed of this StorageDescriptor.

        是否启用数据压缩

        :param compressed: The compressed of this StorageDescriptor.
        :type compressed: bool
        """
        self._compressed = compressed

    @property
    def input_format(self):
        r"""Gets the input_format of this StorageDescriptor.

        输入格式

        :return: The input_format of this StorageDescriptor.
        :rtype: str
        """
        return self._input_format

    @input_format.setter
    def input_format(self, input_format):
        r"""Sets the input_format of this StorageDescriptor.

        输入格式

        :param input_format: The input_format of this StorageDescriptor.
        :type input_format: str
        """
        self._input_format = input_format

    @property
    def output_format(self):
        r"""Gets the output_format of this StorageDescriptor.

        输出格式

        :return: The output_format of this StorageDescriptor.
        :rtype: str
        """
        return self._output_format

    @output_format.setter
    def output_format(self, output_format):
        r"""Sets the output_format of this StorageDescriptor.

        输出格式

        :param output_format: The output_format of this StorageDescriptor.
        :type output_format: str
        """
        self._output_format = output_format

    @property
    def number_of_buckets(self):
        r"""Gets the number_of_buckets of this StorageDescriptor.

        分桶的桶数量

        :return: The number_of_buckets of this StorageDescriptor.
        :rtype: int
        """
        return self._number_of_buckets

    @number_of_buckets.setter
    def number_of_buckets(self, number_of_buckets):
        r"""Sets the number_of_buckets of this StorageDescriptor.

        分桶的桶数量

        :param number_of_buckets: The number_of_buckets of this StorageDescriptor.
        :type number_of_buckets: int
        """
        self._number_of_buckets = number_of_buckets

    @property
    def bucket_columns(self):
        r"""Gets the bucket_columns of this StorageDescriptor.

        分桶字段

        :return: The bucket_columns of this StorageDescriptor.
        :rtype: list[str]
        """
        return self._bucket_columns

    @bucket_columns.setter
    def bucket_columns(self, bucket_columns):
        r"""Sets the bucket_columns of this StorageDescriptor.

        分桶字段

        :param bucket_columns: The bucket_columns of this StorageDescriptor.
        :type bucket_columns: list[str]
        """
        self._bucket_columns = bucket_columns

    @property
    def sort_columns(self):
        r"""Gets the sort_columns of this StorageDescriptor.

        指定表中的每个存储桶的排序顺序的列表

        :return: The sort_columns of this StorageDescriptor.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Order`]
        """
        return self._sort_columns

    @sort_columns.setter
    def sort_columns(self, sort_columns):
        r"""Sets the sort_columns of this StorageDescriptor.

        指定表中的每个存储桶的排序顺序的列表

        :param sort_columns: The sort_columns of this StorageDescriptor.
        :type sort_columns: list[:class:`huaweicloudsdklakeformation.v1.Order`]
        """
        self._sort_columns = sort_columns

    @property
    def serde_info(self):
        r"""Gets the serde_info of this StorageDescriptor.

        :return: The serde_info of this StorageDescriptor.
        :rtype: :class:`huaweicloudsdklakeformation.v1.SerDeInfo`
        """
        return self._serde_info

    @serde_info.setter
    def serde_info(self, serde_info):
        r"""Sets the serde_info of this StorageDescriptor.

        :param serde_info: The serde_info of this StorageDescriptor.
        :type serde_info: :class:`huaweicloudsdklakeformation.v1.SerDeInfo`
        """
        self._serde_info = serde_info

    @property
    def parameters(self):
        r"""Gets the parameters of this StorageDescriptor.

        存储描述符的参数。 key最小长度为1，最大长度为255. value最大长度为4000

        :return: The parameters of this StorageDescriptor.
        :rtype: dict(str, str)
        """
        return self._parameters

    @parameters.setter
    def parameters(self, parameters):
        r"""Sets the parameters of this StorageDescriptor.

        存储描述符的参数。 key最小长度为1，最大长度为255. value最大长度为4000

        :param parameters: The parameters of this StorageDescriptor.
        :type parameters: dict(str, str)
        """
        self._parameters = parameters

    @property
    def skewed_info(self):
        r"""Gets the skewed_info of this StorageDescriptor.

        :return: The skewed_info of this StorageDescriptor.
        :rtype: :class:`huaweicloudsdklakeformation.v1.SkewedInfo`
        """
        return self._skewed_info

    @skewed_info.setter
    def skewed_info(self, skewed_info):
        r"""Sets the skewed_info of this StorageDescriptor.

        :param skewed_info: The skewed_info of this StorageDescriptor.
        :type skewed_info: :class:`huaweicloudsdklakeformation.v1.SkewedInfo`
        """
        self._skewed_info = skewed_info

    @property
    def stored_as_sub_directories(self):
        r"""Gets the stored_as_sub_directories of this StorageDescriptor.

        数据是否会存放在子目录中

        :return: The stored_as_sub_directories of this StorageDescriptor.
        :rtype: bool
        """
        return self._stored_as_sub_directories

    @stored_as_sub_directories.setter
    def stored_as_sub_directories(self, stored_as_sub_directories):
        r"""Sets the stored_as_sub_directories of this StorageDescriptor.

        数据是否会存放在子目录中

        :param stored_as_sub_directories: The stored_as_sub_directories of this StorageDescriptor.
        :type stored_as_sub_directories: bool
        """
        self._stored_as_sub_directories = stored_as_sub_directories

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
        if not isinstance(other, StorageDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
