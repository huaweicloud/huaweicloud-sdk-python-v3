# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateInstanceResponse(SdkResponse):

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
        'instance_id': 'str',
        'name': 'str',
        'flavor': 'Flavor',
        'status': 'str',
        'charge_info': 'ChargeInfo',
        'description': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'order_id': 'str',
        'additional_params': 'AdditionalParams'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'name': 'name',
        'flavor': 'flavor',
        'status': 'status',
        'charge_info': 'charge_info',
        'description': 'description',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'order_id': 'order_id',
        'additional_params': 'additional_params'
    }

    def __init__(self, instance_type=None, instance_id=None, name=None, flavor=None, status=None, charge_info=None, description=None, enterprise_project_id=None, tags=None, order_id=None, additional_params=None):
        r"""CreateInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_type: **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 
        :type instance_type: str
        :param instance_id: **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 
        :type instance_id: str
        :param name: **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 
        :type name: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        :param status: **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 
        :type status: str
        :param charge_info: 
        :type charge_info: :class:`huaweicloudsdkiotdm.v5.ChargeInfo`
        :param description: **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[0-256]个字符。 
        :type description: str
        :param enterprise_project_id: **参数说明**：企业项目Id。
        :type enterprise_project_id: str
        :param tags: **参数说明**: 设备接入实例的标签信息。如果实例有标签，则会有该字段，否则该字段为空。 
        :type tags: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        :param order_id: **参数说明**：订单号，创建包年包月实例时返回该参数。[查看订单详情请参考[查询订单详情](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0075746564.html)。](tag:hws)\&quot; 
        :type order_id: str
        :param additional_params: 
        :type additional_params: :class:`huaweicloudsdkiotdm.v5.AdditionalParams`
        """
        
        super(CreateInstanceResponse, self).__init__()

        self._instance_type = None
        self._instance_id = None
        self._name = None
        self._flavor = None
        self._status = None
        self._charge_info = None
        self._description = None
        self._enterprise_project_id = None
        self._tags = None
        self._order_id = None
        self._additional_params = None
        self.discriminator = None

        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if charge_info is not None:
            self.charge_info = charge_info
        if description is not None:
            self.description = description
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if order_id is not None:
            self.order_id = order_id
        if additional_params is not None:
            self.additional_params = additional_params

    @property
    def instance_type(self):
        r"""Gets the instance_type of this CreateInstanceResponse.

        **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :return: The instance_type of this CreateInstanceResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this CreateInstanceResponse.

        **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :param instance_type: The instance_type of this CreateInstanceResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this CreateInstanceResponse.

        **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :return: The instance_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this CreateInstanceResponse.

        **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :param instance_id: The instance_id of this CreateInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this CreateInstanceResponse.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :return: The name of this CreateInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreateInstanceResponse.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :param name: The name of this CreateInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def flavor(self):
        r"""Gets the flavor of this CreateInstanceResponse.

        :return: The flavor of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this CreateInstanceResponse.

        :param flavor: The flavor of this CreateInstanceResponse.
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this CreateInstanceResponse.

        **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 

        :return: The status of this CreateInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this CreateInstanceResponse.

        **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 

        :param status: The status of this CreateInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def charge_info(self):
        r"""Gets the charge_info of this CreateInstanceResponse.

        :return: The charge_info of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.ChargeInfo`
        """
        return self._charge_info

    @charge_info.setter
    def charge_info(self, charge_info):
        r"""Sets the charge_info of this CreateInstanceResponse.

        :param charge_info: The charge_info of this CreateInstanceResponse.
        :type charge_info: :class:`huaweicloudsdkiotdm.v5.ChargeInfo`
        """
        self._charge_info = charge_info

    @property
    def description(self):
        r"""Gets the description of this CreateInstanceResponse.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[0-256]个字符。 

        :return: The description of this CreateInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreateInstanceResponse.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[0-256]个字符。 

        :param description: The description of this CreateInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateInstanceResponse.

        **参数说明**：企业项目Id。

        :return: The enterprise_project_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateInstanceResponse.

        **参数说明**：企业项目Id。

        :param enterprise_project_id: The enterprise_project_id of this CreateInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this CreateInstanceResponse.

        **参数说明**: 设备接入实例的标签信息。如果实例有标签，则会有该字段，否则该字段为空。 

        :return: The tags of this CreateInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this CreateInstanceResponse.

        **参数说明**: 设备接入实例的标签信息。如果实例有标签，则会有该字段，否则该字段为空。 

        :param tags: The tags of this CreateInstanceResponse.
        :type tags: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        """
        self._tags = tags

    @property
    def order_id(self):
        r"""Gets the order_id of this CreateInstanceResponse.

        **参数说明**：订单号，创建包年包月实例时返回该参数。[查看订单详情请参考[查询订单详情](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0075746564.html)。](tag:hws)\" 

        :return: The order_id of this CreateInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this CreateInstanceResponse.

        **参数说明**：订单号，创建包年包月实例时返回该参数。[查看订单详情请参考[查询订单详情](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0075746564.html)。](tag:hws)\" 

        :param order_id: The order_id of this CreateInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def additional_params(self):
        r"""Gets the additional_params of this CreateInstanceResponse.

        :return: The additional_params of this CreateInstanceResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.AdditionalParams`
        """
        return self._additional_params

    @additional_params.setter
    def additional_params(self, additional_params):
        r"""Sets the additional_params of this CreateInstanceResponse.

        :param additional_params: The additional_params of this CreateInstanceResponse.
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
        if not isinstance(other, CreateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
