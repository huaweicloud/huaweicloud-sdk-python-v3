# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateBandwidthOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'count': 'int',
        'name': 'str',
        'size': 'int',
        'public_border_group': 'str'
    }

    attribute_map = {
        'count': 'count',
        'name': 'name',
        'size': 'size',
        'public_border_group': 'public_border_group'
    }

    def __init__(self, count=None, name=None, size=None, public_border_group=None):
        """BatchCreateBandwidthOption

        The model defined in huaweicloud sdk

        :param count: 取值范围：正整数  功能说明：批创的共享带宽的个数  说明： 如果传入的参数为小数（如 2.2）或者字符类型（如“2”），会自动强制转换为整数。
        :type count: int
        :param name: 取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  功能说明：带宽名称
        :type name: str
        :param size: 功能说明：带宽大小。共享带宽的大小有最小值限制，默认为2M，可能因局点不同而不同。  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。
        :type size: int
        :param public_border_group: 功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能插入与该字段相同的publicip
        :type public_border_group: str
        """
        
        

        self._count = None
        self._name = None
        self._size = None
        self._public_border_group = None
        self.discriminator = None

        self.count = count
        self.name = name
        self.size = size
        if public_border_group is not None:
            self.public_border_group = public_border_group

    @property
    def count(self):
        """Gets the count of this BatchCreateBandwidthOption.

        取值范围：正整数  功能说明：批创的共享带宽的个数  说明： 如果传入的参数为小数（如 2.2）或者字符类型（如“2”），会自动强制转换为整数。

        :return: The count of this BatchCreateBandwidthOption.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """Sets the count of this BatchCreateBandwidthOption.

        取值范围：正整数  功能说明：批创的共享带宽的个数  说明： 如果传入的参数为小数（如 2.2）或者字符类型（如“2”），会自动强制转换为整数。

        :param count: The count of this BatchCreateBandwidthOption.
        :type count: int
        """
        self._count = count

    @property
    def name(self):
        """Gets the name of this BatchCreateBandwidthOption.

        取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  功能说明：带宽名称

        :return: The name of this BatchCreateBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BatchCreateBandwidthOption.

        取值范围：1-64，支持数字、字母、中文、_(下划线)、-（中划线）、.（点）  功能说明：带宽名称

        :param name: The name of this BatchCreateBandwidthOption.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this BatchCreateBandwidthOption.

        功能说明：带宽大小。共享带宽的大小有最小值限制，默认为2M，可能因局点不同而不同。  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this BatchCreateBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this BatchCreateBandwidthOption.

        功能说明：带宽大小。共享带宽的大小有最小值限制，默认为2M，可能因局点不同而不同。  取值范围：默认5Mbit/s~2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示）。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this BatchCreateBandwidthOption.
        :type size: int
        """
        self._size = size

    @property
    def public_border_group(self):
        """Gets the public_border_group of this BatchCreateBandwidthOption.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能插入与该字段相同的publicip

        :return: The public_border_group of this BatchCreateBandwidthOption.
        :rtype: str
        """
        return self._public_border_group

    @public_border_group.setter
    def public_border_group(self, public_border_group):
        """Sets the public_border_group of this BatchCreateBandwidthOption.

        功能说明：表示中心站点资源或者边缘站点资源 取值范围： center、边缘站点名称 约束：共享带宽只能插入与该字段相同的publicip

        :param public_border_group: The public_border_group of this BatchCreateBandwidthOption.
        :type public_border_group: str
        """
        self._public_border_group = public_border_group

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
        if not isinstance(other, BatchCreateBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
