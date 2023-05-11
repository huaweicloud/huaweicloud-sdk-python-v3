# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Conversion:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'measure_id': 'int',
        'ref_measure_id': 'int',
        'conversion_ratio': 'int',
        'measure_type': 'int'
    }

    attribute_map = {
        'measure_id': 'measure_id',
        'ref_measure_id': 'ref_measure_id',
        'conversion_ratio': 'conversion_ratio',
        'measure_type': 'measure_type'
    }

    def __init__(self, measure_id=None, ref_measure_id=None, conversion_ratio=None, measure_type=None):
        """Conversion

        The model defined in huaweicloud sdk

        :param measure_id: 度量单位ID。 例如：10表示GB。
        :type measure_id: int
        :param ref_measure_id: 转换后的度量单位ID。 例如：11表示MB。
        :type ref_measure_id: int
        :param conversion_ratio: 度量单位和转换后的度量单位之间的转换比率。 例如： 度量单位为GB，转换度量单位为MB时，转换比率为1024，两者之间的转换公式为：1GB&#x3D;1024MB。
        :type conversion_ratio: int
        :param measure_type: 度量类型。 1：货币2：时长3：流量4：数量7：容量9：行数10：周期11：频率12：个数16：带宽速率17：容量时长18：查询速率19：带宽速率（1000进制）20：性能测试用量21：面积22：视频23：吞吐量25：测试类型
        :type measure_type: int
        """
        
        

        self._measure_id = None
        self._ref_measure_id = None
        self._conversion_ratio = None
        self._measure_type = None
        self.discriminator = None

        if measure_id is not None:
            self.measure_id = measure_id
        if ref_measure_id is not None:
            self.ref_measure_id = ref_measure_id
        if conversion_ratio is not None:
            self.conversion_ratio = conversion_ratio
        if measure_type is not None:
            self.measure_type = measure_type

    @property
    def measure_id(self):
        """Gets the measure_id of this Conversion.

        度量单位ID。 例如：10表示GB。

        :return: The measure_id of this Conversion.
        :rtype: int
        """
        return self._measure_id

    @measure_id.setter
    def measure_id(self, measure_id):
        """Sets the measure_id of this Conversion.

        度量单位ID。 例如：10表示GB。

        :param measure_id: The measure_id of this Conversion.
        :type measure_id: int
        """
        self._measure_id = measure_id

    @property
    def ref_measure_id(self):
        """Gets the ref_measure_id of this Conversion.

        转换后的度量单位ID。 例如：11表示MB。

        :return: The ref_measure_id of this Conversion.
        :rtype: int
        """
        return self._ref_measure_id

    @ref_measure_id.setter
    def ref_measure_id(self, ref_measure_id):
        """Sets the ref_measure_id of this Conversion.

        转换后的度量单位ID。 例如：11表示MB。

        :param ref_measure_id: The ref_measure_id of this Conversion.
        :type ref_measure_id: int
        """
        self._ref_measure_id = ref_measure_id

    @property
    def conversion_ratio(self):
        """Gets the conversion_ratio of this Conversion.

        度量单位和转换后的度量单位之间的转换比率。 例如： 度量单位为GB，转换度量单位为MB时，转换比率为1024，两者之间的转换公式为：1GB=1024MB。

        :return: The conversion_ratio of this Conversion.
        :rtype: int
        """
        return self._conversion_ratio

    @conversion_ratio.setter
    def conversion_ratio(self, conversion_ratio):
        """Sets the conversion_ratio of this Conversion.

        度量单位和转换后的度量单位之间的转换比率。 例如： 度量单位为GB，转换度量单位为MB时，转换比率为1024，两者之间的转换公式为：1GB=1024MB。

        :param conversion_ratio: The conversion_ratio of this Conversion.
        :type conversion_ratio: int
        """
        self._conversion_ratio = conversion_ratio

    @property
    def measure_type(self):
        """Gets the measure_type of this Conversion.

        度量类型。 1：货币2：时长3：流量4：数量7：容量9：行数10：周期11：频率12：个数16：带宽速率17：容量时长18：查询速率19：带宽速率（1000进制）20：性能测试用量21：面积22：视频23：吞吐量25：测试类型

        :return: The measure_type of this Conversion.
        :rtype: int
        """
        return self._measure_type

    @measure_type.setter
    def measure_type(self, measure_type):
        """Sets the measure_type of this Conversion.

        度量类型。 1：货币2：时长3：流量4：数量7：容量9：行数10：周期11：频率12：个数16：带宽速率17：容量时长18：查询速率19：带宽速率（1000进制）20：性能测试用量21：面积22：视频23：吞吐量25：测试类型

        :param measure_type: The measure_type of this Conversion.
        :type measure_type: int
        """
        self._measure_type = measure_type

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
        if not isinstance(other, Conversion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
