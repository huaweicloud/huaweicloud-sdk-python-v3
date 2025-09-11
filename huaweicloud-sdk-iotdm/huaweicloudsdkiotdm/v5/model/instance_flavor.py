# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class InstanceFlavor:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_type': 'str',
        'type': 'str',
        'status': 'str',
        'charge_modes': 'list[str]'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'type': 'type',
        'status': 'status',
        'charge_modes': 'charge_modes'
    }

    def __init__(self, instance_type=None, type=None, status=None, charge_modes=None):
        r"""InstanceFlavor

        The model defined in huaweicloud sdk

        :param instance_type: **参数说明**：创建的实例类型。实例类型说明参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 
        :type instance_type: str
        :param type: **参数说明**：设备接入实例的规格名称。详情请参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)中的规格编码。 
        :type type: str
        :param status: **参数说明**：实例规格的在售状态。 **取值范围**： - normal：在售 - sellout：已售罄 
        :type status: str
        :param charge_modes: **参数说明**：实例规格支持的付费方式列表。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费
        :type charge_modes: list[str]
        """
        
        

        self._instance_type = None
        self._type = None
        self._status = None
        self._charge_modes = None
        self.discriminator = None

        self.instance_type = instance_type
        self.type = type
        self.status = status
        self.charge_modes = charge_modes

    @property
    def instance_type(self):
        r"""Gets the instance_type of this InstanceFlavor.

        **参数说明**：创建的实例类型。实例类型说明参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :return: The instance_type of this InstanceFlavor.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this InstanceFlavor.

        **参数说明**：创建的实例类型。实例类型说明参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :param instance_type: The instance_type of this InstanceFlavor.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def type(self):
        r"""Gets the type of this InstanceFlavor.

        **参数说明**：设备接入实例的规格名称。详情请参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)中的规格编码。 

        :return: The type of this InstanceFlavor.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this InstanceFlavor.

        **参数说明**：设备接入实例的规格名称。详情请参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)中的规格编码。 

        :param type: The type of this InstanceFlavor.
        :type type: str
        """
        self._type = type

    @property
    def status(self):
        r"""Gets the status of this InstanceFlavor.

        **参数说明**：实例规格的在售状态。 **取值范围**： - normal：在售 - sellout：已售罄 

        :return: The status of this InstanceFlavor.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this InstanceFlavor.

        **参数说明**：实例规格的在售状态。 **取值范围**： - normal：在售 - sellout：已售罄 

        :param status: The status of this InstanceFlavor.
        :type status: str
        """
        self._status = status

    @property
    def charge_modes(self):
        r"""Gets the charge_modes of this InstanceFlavor.

        **参数说明**：实例规格支持的付费方式列表。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费

        :return: The charge_modes of this InstanceFlavor.
        :rtype: list[str]
        """
        return self._charge_modes

    @charge_modes.setter
    def charge_modes(self, charge_modes):
        r"""Sets the charge_modes of this InstanceFlavor.

        **参数说明**：实例规格支持的付费方式列表。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费

        :param charge_modes: The charge_modes of this InstanceFlavor.
        :type charge_modes: list[str]
        """
        self._charge_modes = charge_modes

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
        if not isinstance(other, InstanceFlavor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
