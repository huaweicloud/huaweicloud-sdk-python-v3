# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdatePrePaidBandwidthOption:

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
        'size': 'int'
    }

    attribute_map = {
        'name': 'name',
        'size': 'size'
    }

    def __init__(self, name=None, size=None):
        """UpdatePrePaidBandwidthOption

        The model defined in huaweicloud sdk

        :param name: 功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），为空表示不修改名称  约束：和参数size必须有一个参数有值
        :type name: str
        :param size: 功能说明：带宽大小，包周期的带宽只能改大  取值范围：默认1Mbit/s～2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示），不带此参数时表示不修改大小。  约束：和参数name必须有一个参数有值。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。
        :type size: int
        """
        
        

        self._name = None
        self._size = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if size is not None:
            self.size = size

    @property
    def name(self):
        """Gets the name of this UpdatePrePaidBandwidthOption.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），为空表示不修改名称  约束：和参数size必须有一个参数有值

        :return: The name of this UpdatePrePaidBandwidthOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdatePrePaidBandwidthOption.

        功能说明：带宽名称  取值范围：1-64个字符，支持数字、字母、中文、_(下划线)、-（中划线）、.（点），为空表示不修改名称  约束：和参数size必须有一个参数有值

        :param name: The name of this UpdatePrePaidBandwidthOption.
        :type name: str
        """
        self._name = name

    @property
    def size(self):
        """Gets the size of this UpdatePrePaidBandwidthOption.

        功能说明：带宽大小，包周期的带宽只能改大  取值范围：默认1Mbit/s～2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示），不带此参数时表示不修改大小。  约束：和参数name必须有一个参数有值。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this UpdatePrePaidBandwidthOption.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this UpdatePrePaidBandwidthOption.

        功能说明：带宽大小，包周期的带宽只能改大  取值范围：默认1Mbit/s～2000Mbit/s（具体范围以各区域配置为准，请参见控制台对应页面显示），不带此参数时表示不修改大小。  约束：和参数name必须有一个参数有值。  注意：调整带宽时的最小单位会根据带宽范围不同存在差异。  小于等于300Mbit/s：默认最小单位为1Mbit/s。  300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。  大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this UpdatePrePaidBandwidthOption.
        :type size: int
        """
        self._size = size

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
        if not isinstance(other, UpdatePrePaidBandwidthOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
