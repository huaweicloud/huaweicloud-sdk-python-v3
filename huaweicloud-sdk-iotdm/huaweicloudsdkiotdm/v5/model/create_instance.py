# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstance:

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
        'flavor': 'Flavor',
        'name': 'str',
        'charge_info': 'ChargeInfo',
        'description': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'additional_params': 'AdditionalParams'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'flavor': 'flavor',
        'name': 'name',
        'charge_info': 'charge_info',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'additional_params': 'additional_params'
    }

    def __init__(self, instance_type=None, flavor=None, name=None, charge_info=None, description=None, enterprise_project_id=None, tags=None, additional_params=None):
        r"""CreateInstance

        The model defined in huaweicloud sdk

        :param instance_type: **参数说明**：创建的实例类型。实例类型说明参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 
        :type instance_type: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        :param name: **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 
        :type name: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkiotdm.v5.ChargeInfo`
        :param description: **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 
        :type description: str
        :param enterprise_project_id: **参数说明**：企业项目Id。此字段填写明确的企业项目Id或者0(表示默认企业项目Id)时支持企业项目特性。可以企业项目管理服务中获取。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 
        :type enterprise_project_id: str
        :param tags: **参数说明**：设备接入实例的标签信息。 
        :type tags: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        :param additional_params: 
        :type additional_params: :class:`huaweicloudsdkiotdm.v5.AdditionalParams`
        """
        
        

        self._instance_type = None
        self._flavor = None
        self._name = None
        self._charge_info = None
        self._description = None
        self._enterprise_project_id = None
        self._tags = None
        self._additional_params = None
        self.discriminator = None

        self.instance_type = instance_type
        self.flavor = flavor
        self.name = name
        self.charge_info = charge_info
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if additional_params is not None:
            self.additional_params = additional_params

    @property
    def instance_type(self):
        r"""Gets the instance_type of this CreateInstance.

        **参数说明**：创建的实例类型。实例类型说明参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :return: The instance_type of this CreateInstance.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this CreateInstance.

        **参数说明**：创建的实例类型。实例类型说明参见[[产品规格说明](https://support.huaweicloud.com/productdesc-iothub/iot_04_0014.html)](tag:hws)[[产品规格说明](https://support.huaweicloud.com/intl/zh-cn/productdesc-iothub/iot_04_0014.html)](tag:hws_hk)。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :param instance_type: The instance_type of this CreateInstance.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateInstance.

        :return: The flavor of this CreateInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateInstance.

        :param flavor: The flavor of this CreateInstance.
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        self._flavor = flavor

    @property
    def name(self):
        r"""Gets the name of this CreateInstance.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :return: The name of this CreateInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstance.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :param name: The name of this CreateInstance.
        :type name: str
        """
        self._name = name

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateInstance.

        :return: The charge_info of this CreateInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateInstance.

        :param charge_info: The charge_info of this CreateInstance.
        :type charge_info: :class:`huaweicloudsdkiotdm.v5.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def description(self):
        r"""Gets the description of this CreateInstance.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 

        :return: The description of this CreateInstance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstance.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 

        :param description: The description of this CreateInstance.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstance.

        **参数说明**：企业项目Id。此字段填写明确的企业项目Id或者0(表示默认企业项目Id)时支持企业项目特性。可以企业项目管理服务中获取。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :return: The enterprise_project_id of this CreateInstance.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstance.

        **参数说明**：企业项目Id。此字段填写明确的企业项目Id或者0(表示默认企业项目Id)时支持企业项目特性。可以企业项目管理服务中获取。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :param enterprise_project_id: The enterprise_project_id of this CreateInstance.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateInstance.

        **参数说明**：设备接入实例的标签信息。 

        :return: The tags of this CreateInstance.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateInstance.

        **参数说明**：设备接入实例的标签信息。 

        :param tags: The tags of this CreateInstance.
        :type tags: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        """
        self._tags = tags

    @property
    def additional_params(self):
        r"""Gets the additional_params of this CreateInstance.

        :return: The additional_params of this CreateInstance.
        :rtype: :class:`huaweicloudsdkiotdm.v5.AdditionalParams`
        """
        return self._additional_params

    @additional_params.setter
    def additional_params(self, additional_params):
        r"""Sets the additional_params of this CreateInstance.

        :param additional_params: The additional_params of this CreateInstance.
        :type additional_params: :class:`huaweicloudsdkiotdm.v5.AdditionalParams`
        """
        self._additional_params = additional_params

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
        if not isinstance(other, CreateInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
