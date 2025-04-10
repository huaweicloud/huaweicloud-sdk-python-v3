# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BandwidthInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'share_type': 'str',
        'charging_mode': 'str',
        'id': 'str'
    }

    attribute_map = {
        'size': 'size',
        'share_type': 'share_type',
        'charging_mode': 'charging_mode',
        'id': 'id'
    }

    def __init__(self, size=None, share_type=None, charging_mode=None, id=None):
        r"""BandwidthInfo

        The model defined in huaweicloud sdk

        :param size: 带宽（Mbit/s），按带宽分配取值范围为[1,2000]，按流量分配取值范围为[1,300]。  说明： - 若share_type是PER，该参数为必选项。若share_type是WHOLE，会忽略该参数。 - 具体范围以各区域配置为准，请参见控制台对应页面显示。 - 创建带宽时的最小单位会根据带宽取值范围不同存在差异。 - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。
        :type size: int
        :param share_type: 带宽的共享类型。共享类型枚举：PER：独享型。WHOLE：共享型。
        :type share_type: str
        :param charging_mode: 带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。字段为其它值，会导致创建云服务器失败。如果share_type是PER，该参数为必选项。如果share_type是WHOLE，会忽略该参数。
        :type charging_mode: str
        :param id: 带宽ID，使用共享型带宽时，可以选择之前创建的共享带宽来创建弹性IP。如果share_type是PER，会忽略该参数。如果share_type是WHOLE，该参数为必选项。
        :type id: str
        """
        
        

        self._size = None
        self._share_type = None
        self._charging_mode = None
        self._id = None
        self.discriminator = None

        if size is not None:
            self.size = size
        self.share_type = share_type
        if charging_mode is not None:
            self.charging_mode = charging_mode
        if id is not None:
            self.id = id

    @property
    def size(self):
        r"""Gets the size of this BandwidthInfo.

        带宽（Mbit/s），按带宽分配取值范围为[1,2000]，按流量分配取值范围为[1,300]。  说明： - 若share_type是PER，该参数为必选项。若share_type是WHOLE，会忽略该参数。 - 具体范围以各区域配置为准，请参见控制台对应页面显示。 - 创建带宽时的最小单位会根据带宽取值范围不同存在差异。 - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。

        :return: The size of this BandwidthInfo.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this BandwidthInfo.

        带宽（Mbit/s），按带宽分配取值范围为[1,2000]，按流量分配取值范围为[1,300]。  说明： - 若share_type是PER，该参数为必选项。若share_type是WHOLE，会忽略该参数。 - 具体范围以各区域配置为准，请参见控制台对应页面显示。 - 创建带宽时的最小单位会根据带宽取值范围不同存在差异。 - 小于等于300Mbit/s：默认最小单位为1Mbit/s。 - 300Mbit/s~1000Mbit/s：默认最小单位为50Mbit/s。 - 大于1000Mbit/s：默认最小单位为500Mbit/s。

        :param size: The size of this BandwidthInfo.
        :type size: int
        """
        self._size = size

    @property
    def share_type(self):
        r"""Gets the share_type of this BandwidthInfo.

        带宽的共享类型。共享类型枚举：PER：独享型。WHOLE：共享型。

        :return: The share_type of this BandwidthInfo.
        :rtype: str
        """
        return self._share_type

    @share_type.setter
    def share_type(self, share_type):
        r"""Sets the share_type of this BandwidthInfo.

        带宽的共享类型。共享类型枚举：PER：独享型。WHOLE：共享型。

        :param share_type: The share_type of this BandwidthInfo.
        :type share_type: str
        """
        self._share_type = share_type

    @property
    def charging_mode(self):
        r"""Gets the charging_mode of this BandwidthInfo.

        带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。字段为其它值，会导致创建云服务器失败。如果share_type是PER，该参数为必选项。如果share_type是WHOLE，会忽略该参数。

        :return: The charging_mode of this BandwidthInfo.
        :rtype: str
        """
        return self._charging_mode

    @charging_mode.setter
    def charging_mode(self, charging_mode):
        r"""Sets the charging_mode of this BandwidthInfo.

        带宽的计费类型。字段值为“bandwidth”，表示按带宽计费。字段值为“traffic”，表示按流量计费。字段为其它值，会导致创建云服务器失败。如果share_type是PER，该参数为必选项。如果share_type是WHOLE，会忽略该参数。

        :param charging_mode: The charging_mode of this BandwidthInfo.
        :type charging_mode: str
        """
        self._charging_mode = charging_mode

    @property
    def id(self):
        r"""Gets the id of this BandwidthInfo.

        带宽ID，使用共享型带宽时，可以选择之前创建的共享带宽来创建弹性IP。如果share_type是PER，会忽略该参数。如果share_type是WHOLE，该参数为必选项。

        :return: The id of this BandwidthInfo.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this BandwidthInfo.

        带宽ID，使用共享型带宽时，可以选择之前创建的共享带宽来创建弹性IP。如果share_type是PER，会忽略该参数。如果share_type是WHOLE，该参数为必选项。

        :param id: The id of this BandwidthInfo.
        :type id: str
        """
        self._id = id

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
        if not isinstance(other, BandwidthInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
