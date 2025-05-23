# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Spec:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'spec_code': 'str',
        'spec_type': 'SpecType',
        'resource_type': 'str',
        'stride': 'int',
        'unit': 'str',
        'min_stride_num': 'int',
        'max_stride_num': 'int',
        'usage_measure_id': 'int',
        'usage_factor': 'str',
        'stride_num_whitelist': 'list[int]'
    }

    attribute_map = {
        'spec_code': 'spec_code',
        'spec_type': 'spec_type',
        'resource_type': 'resource_type',
        'stride': 'stride',
        'unit': 'unit',
        'min_stride_num': 'min_stride_num',
        'max_stride_num': 'max_stride_num',
        'usage_measure_id': 'usage_measure_id',
        'usage_factor': 'usage_factor',
        'stride_num_whitelist': 'stride_num_whitelist'
    }

    def __init__(self, spec_code=None, spec_type=None, resource_type=None, stride=None, unit=None, min_stride_num=None, max_stride_num=None, usage_measure_id=None, usage_factor=None, stride_num_whitelist=None):
        r"""Spec

        The model defined in huaweicloud sdk

        :param spec_code: 资源规格，从规格列表查询获取。
        :type spec_code: str
        :param spec_type: 
        :type spec_type: :class:`huaweicloudsdkdataartsfabric.v1.SpecType`
        :param resource_type: 资源类型
        :type resource_type: str
        :param stride: 步长
        :type stride: int
        :param unit: 单位
        :type unit: str
        :param min_stride_num: 资源步数，最小为10000，步长为1。输入范围还需要满足规格列表接口的步长白名单
        :type min_stride_num: int
        :param max_stride_num: 资源步数，最小为10000，步长为1。输入范围还需要满足规格列表接口的步长白名单
        :type max_stride_num: int
        :param usage_measure_id: 使用量单位标识
        :type usage_measure_id: int
        :param usage_factor: 使用量因子
        :type usage_factor: str
        :param stride_num_whitelist: 步数白名单，返回时，步数必须是白名单中的值
        :type stride_num_whitelist: list[int]
        """
        
        

        self._spec_code = None
        self._spec_type = None
        self._resource_type = None
        self._stride = None
        self._unit = None
        self._min_stride_num = None
        self._max_stride_num = None
        self._usage_measure_id = None
        self._usage_factor = None
        self._stride_num_whitelist = None
        self.discriminator = None

        if spec_code is not None:
            self.spec_code = spec_code
        if spec_type is not None:
            self.spec_type = spec_type
        if resource_type is not None:
            self.resource_type = resource_type
        if stride is not None:
            self.stride = stride
        if unit is not None:
            self.unit = unit
        if min_stride_num is not None:
            self.min_stride_num = min_stride_num
        if max_stride_num is not None:
            self.max_stride_num = max_stride_num
        if usage_measure_id is not None:
            self.usage_measure_id = usage_measure_id
        if usage_factor is not None:
            self.usage_factor = usage_factor
        if stride_num_whitelist is not None:
            self.stride_num_whitelist = stride_num_whitelist

    @property
    def spec_code(self):
        r"""Gets the spec_code of this Spec.

        资源规格，从规格列表查询获取。

        :return: The spec_code of this Spec.
        :rtype: str
        """
        return self._spec_code

    @spec_code.setter
    def spec_code(self, spec_code):
        r"""Sets the spec_code of this Spec.

        资源规格，从规格列表查询获取。

        :param spec_code: The spec_code of this Spec.
        :type spec_code: str
        """
        self._spec_code = spec_code

    @property
    def spec_type(self):
        r"""Gets the spec_type of this Spec.

        :return: The spec_type of this Spec.
        :rtype: :class:`huaweicloudsdkdataartsfabric.v1.SpecType`
        """
        return self._spec_type

    @spec_type.setter
    def spec_type(self, spec_type):
        r"""Sets the spec_type of this Spec.

        :param spec_type: The spec_type of this Spec.
        :type spec_type: :class:`huaweicloudsdkdataartsfabric.v1.SpecType`
        """
        self._spec_type = spec_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this Spec.

        资源类型

        :return: The resource_type of this Spec.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this Spec.

        资源类型

        :param resource_type: The resource_type of this Spec.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def stride(self):
        r"""Gets the stride of this Spec.

        步长

        :return: The stride of this Spec.
        :rtype: int
        """
        return self._stride

    @stride.setter
    def stride(self, stride):
        r"""Sets the stride of this Spec.

        步长

        :param stride: The stride of this Spec.
        :type stride: int
        """
        self._stride = stride

    @property
    def unit(self):
        r"""Gets the unit of this Spec.

        单位

        :return: The unit of this Spec.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        r"""Sets the unit of this Spec.

        单位

        :param unit: The unit of this Spec.
        :type unit: str
        """
        self._unit = unit

    @property
    def min_stride_num(self):
        r"""Gets the min_stride_num of this Spec.

        资源步数，最小为10000，步长为1。输入范围还需要满足规格列表接口的步长白名单

        :return: The min_stride_num of this Spec.
        :rtype: int
        """
        return self._min_stride_num

    @min_stride_num.setter
    def min_stride_num(self, min_stride_num):
        r"""Sets the min_stride_num of this Spec.

        资源步数，最小为10000，步长为1。输入范围还需要满足规格列表接口的步长白名单

        :param min_stride_num: The min_stride_num of this Spec.
        :type min_stride_num: int
        """
        self._min_stride_num = min_stride_num

    @property
    def max_stride_num(self):
        r"""Gets the max_stride_num of this Spec.

        资源步数，最小为10000，步长为1。输入范围还需要满足规格列表接口的步长白名单

        :return: The max_stride_num of this Spec.
        :rtype: int
        """
        return self._max_stride_num

    @max_stride_num.setter
    def max_stride_num(self, max_stride_num):
        r"""Sets the max_stride_num of this Spec.

        资源步数，最小为10000，步长为1。输入范围还需要满足规格列表接口的步长白名单

        :param max_stride_num: The max_stride_num of this Spec.
        :type max_stride_num: int
        """
        self._max_stride_num = max_stride_num

    @property
    def usage_measure_id(self):
        r"""Gets the usage_measure_id of this Spec.

        使用量单位标识

        :return: The usage_measure_id of this Spec.
        :rtype: int
        """
        return self._usage_measure_id

    @usage_measure_id.setter
    def usage_measure_id(self, usage_measure_id):
        r"""Sets the usage_measure_id of this Spec.

        使用量单位标识

        :param usage_measure_id: The usage_measure_id of this Spec.
        :type usage_measure_id: int
        """
        self._usage_measure_id = usage_measure_id

    @property
    def usage_factor(self):
        r"""Gets the usage_factor of this Spec.

        使用量因子

        :return: The usage_factor of this Spec.
        :rtype: str
        """
        return self._usage_factor

    @usage_factor.setter
    def usage_factor(self, usage_factor):
        r"""Sets the usage_factor of this Spec.

        使用量因子

        :param usage_factor: The usage_factor of this Spec.
        :type usage_factor: str
        """
        self._usage_factor = usage_factor

    @property
    def stride_num_whitelist(self):
        r"""Gets the stride_num_whitelist of this Spec.

        步数白名单，返回时，步数必须是白名单中的值

        :return: The stride_num_whitelist of this Spec.
        :rtype: list[int]
        """
        return self._stride_num_whitelist

    @stride_num_whitelist.setter
    def stride_num_whitelist(self, stride_num_whitelist):
        r"""Sets the stride_num_whitelist of this Spec.

        步数白名单，返回时，步数必须是白名单中的值

        :param stride_num_whitelist: The stride_num_whitelist of this Spec.
        :type stride_num_whitelist: list[int]
        """
        self._stride_num_whitelist = stride_num_whitelist

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
        if not isinstance(other, Spec):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
