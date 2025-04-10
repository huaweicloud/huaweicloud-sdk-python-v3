# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceResponse(SdkResponse):

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
        'charge_mode': 'str',
        'name': 'str',
        'flavor': 'Flavor',
        'status': 'str',
        'description': 'str',
        'access_infos': 'list[AccessInfo]',
        'create_time': 'str',
        'update_time': 'str',
        'enterprise_project_id': 'str',
        'tags': 'list[Tag]',
        'order_id': 'str',
        'operate_window': 'OperateWindow',
        'additional_params': 'AdditionalParamsResp'
    }

    attribute_map = {
        'instance_type': 'instance_type',
        'instance_id': 'instance_id',
        'charge_mode': 'charge_mode',
        'name': 'name',
        'flavor': 'flavor',
        'status': 'status',
        'description': 'description',
        'access_infos': 'access_infos',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'enterprise_project_id': 'enterprise_project_id',
        'tags': 'tags',
        'order_id': 'order_id',
        'operate_window': 'operate_window',
        'additional_params': 'additional_params'
    }

    def __init__(self, instance_type=None, instance_id=None, charge_mode=None, name=None, flavor=None, status=None, description=None, access_infos=None, create_time=None, update_time=None, enterprise_project_id=None, tags=None, order_id=None, operate_window=None, additional_params=None):
        r"""UpdateInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_type: **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 
        :type instance_type: str
        :param instance_id: **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 
        :type instance_id: str
        :param charge_mode: **参数说明**：实例的付费方式。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费 
        :type charge_mode: str
        :param name: **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 
        :type name: str
        :param flavor: 
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        :param status: **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 
        :type status: str
        :param description: **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 
        :type description: str
        :param access_infos: **参数说明**：设备接入实例的接入信息 
        :type access_infos: list[:class:`huaweicloudsdkiotdm.v5.AccessInfo`]
        :param create_time: **参数说明**：实例的创建时间。时间格式例如：2023-01-28T06:57:52Z 
        :type create_time: str
        :param update_time: **参数说明**：实例的最近一次更新的时间。时间格式例如：2023-01-28T06:57:52Z 
        :type update_time: str
        :param enterprise_project_id: **参数说明**：企业项目Id。
        :type enterprise_project_id: str
        :param tags: **参数说明**: 设备接入实例的标签信息。如果实例有标签，则会有该字段，否则该字段为空。 
        :type tags: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        :param order_id: **参数说明**：订单号，仅包年包月实例返回该参数。[查看订单详情请参考[[查询订单详情](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0075746564.html)。]](tag:hws)
        :type order_id: str
        :param operate_window: 
        :type operate_window: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        :param additional_params: 
        :type additional_params: :class:`huaweicloudsdkiotdm.v5.AdditionalParamsResp`
        """
        
        super(UpdateInstanceResponse, self).__init__()

        self._instance_type = None
        self._instance_id = None
        self._charge_mode = None
        self._name = None
        self._flavor = None
        self._status = None
        self._description = None
        self._access_infos = None
        self._create_time = None
        self._update_time = None
        self._enterprise_project_id = None
        self._tags = None
        self._order_id = None
        self._operate_window = None
        self._additional_params = None
        self.discriminator = None

        if instance_type is not None:
            self.instance_type = instance_type
        if instance_id is not None:
            self.instance_id = instance_id
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if name is not None:
            self.name = name
        if flavor is not None:
            self.flavor = flavor
        if status is not None:
            self.status = status
        if description is not None:
            self.description = description
        if access_infos is not None:
            self.access_infos = access_infos
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        if tags is not None:
            self.tags = tags
        if order_id is not None:
            self.order_id = order_id
        if operate_window is not None:
            self.operate_window = operate_window
        if additional_params is not None:
            self.additional_params = additional_params

    @property
    def instance_type(self):
        r"""Gets the instance_type of this UpdateInstanceResponse.

        **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :return: The instance_type of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._instance_type

    @instance_type.setter
    def instance_type(self, instance_type):
        r"""Sets the instance_type of this UpdateInstanceResponse.

        **参数说明**：实例类型。 **取值范围**： - standard：标准版实例 - enterprise：企业版实例 

        :param instance_type: The instance_type of this UpdateInstanceResponse.
        :type instance_type: str
        """
        self._instance_type = instance_type

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateInstanceResponse.

        **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :return: The instance_id of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateInstanceResponse.

        **参数说明**：实例ID。 **取值范围**：长度不超过36，由小写字母[a-f]、数字、连接符（-）的组成。 

        :param instance_id: The instance_id of this UpdateInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdateInstanceResponse.

        **参数说明**：实例的付费方式。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费 

        :return: The charge_mode of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdateInstanceResponse.

        **参数说明**：实例的付费方式。 **取值范围**： - prePaid：包年/包月 - postPaid：按需计费 

        :param charge_mode: The charge_mode of this UpdateInstanceResponse.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def name(self):
        r"""Gets the name of this UpdateInstanceResponse.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :return: The name of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateInstanceResponse.

        **参数说明**：实例名称 **取值范围**：由中文字符，英文字母、数字及“_”、“-”组成，且长度为[1-64]个字符。 

        :param name: The name of this UpdateInstanceResponse.
        :type name: str
        """
        self._name = name

    @property
    def flavor(self):
        r"""Gets the flavor of this UpdateInstanceResponse.

        :return: The flavor of this UpdateInstanceResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        return self._flavor

    @flavor.setter
    def flavor(self, flavor):
        r"""Sets the flavor of this UpdateInstanceResponse.

        :param flavor: The flavor of this UpdateInstanceResponse.
        :type flavor: :class:`huaweicloudsdkiotdm.v5.Flavor`
        """
        self._flavor = flavor

    @property
    def status(self):
        r"""Gets the status of this UpdateInstanceResponse.

        **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 

        :return: The status of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this UpdateInstanceResponse.

        **参数说明**：实例状态。 **取值范围**： - CREATING：实例正在创建 - ACTIVE：实例正常 - FROZEN：实例冻结 - MODIFYING：实例正在变更规格 - FAILED：实例创建失败 

        :param status: The status of this UpdateInstanceResponse.
        :type status: str
        """
        self._status = status

    @property
    def description(self):
        r"""Gets the description of this UpdateInstanceResponse.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 

        :return: The description of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateInstanceResponse.

        **参数说明**：设备接入实例的描述信息。 **取值范围**：由中文，字母，数字，句号，逗号，下划线（“_”），中划线（“-”），空格组成，且长度为[1-256]个字符。 

        :param description: The description of this UpdateInstanceResponse.
        :type description: str
        """
        self._description = description

    @property
    def access_infos(self):
        r"""Gets the access_infos of this UpdateInstanceResponse.

        **参数说明**：设备接入实例的接入信息 

        :return: The access_infos of this UpdateInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.AccessInfo`]
        """
        return self._access_infos

    @access_infos.setter
    def access_infos(self, access_infos):
        r"""Sets the access_infos of this UpdateInstanceResponse.

        **参数说明**：设备接入实例的接入信息 

        :param access_infos: The access_infos of this UpdateInstanceResponse.
        :type access_infos: list[:class:`huaweicloudsdkiotdm.v5.AccessInfo`]
        """
        self._access_infos = access_infos

    @property
    def create_time(self):
        r"""Gets the create_time of this UpdateInstanceResponse.

        **参数说明**：实例的创建时间。时间格式例如：2023-01-28T06:57:52Z 

        :return: The create_time of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        r"""Sets the create_time of this UpdateInstanceResponse.

        **参数说明**：实例的创建时间。时间格式例如：2023-01-28T06:57:52Z 

        :param create_time: The create_time of this UpdateInstanceResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def update_time(self):
        r"""Gets the update_time of this UpdateInstanceResponse.

        **参数说明**：实例的最近一次更新的时间。时间格式例如：2023-01-28T06:57:52Z 

        :return: The update_time of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this UpdateInstanceResponse.

        **参数说明**：实例的最近一次更新的时间。时间格式例如：2023-01-28T06:57:52Z 

        :param update_time: The update_time of this UpdateInstanceResponse.
        :type update_time: str
        """
        self._update_time = update_time

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this UpdateInstanceResponse.

        **参数说明**：企业项目Id。

        :return: The enterprise_project_id of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this UpdateInstanceResponse.

        **参数说明**：企业项目Id。

        :param enterprise_project_id: The enterprise_project_id of this UpdateInstanceResponse.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def tags(self):
        r"""Gets the tags of this UpdateInstanceResponse.

        **参数说明**: 设备接入实例的标签信息。如果实例有标签，则会有该字段，否则该字段为空。 

        :return: The tags of this UpdateInstanceResponse.
        :rtype: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this UpdateInstanceResponse.

        **参数说明**: 设备接入实例的标签信息。如果实例有标签，则会有该字段，否则该字段为空。 

        :param tags: The tags of this UpdateInstanceResponse.
        :type tags: list[:class:`huaweicloudsdkiotdm.v5.Tag`]
        """
        self._tags = tags

    @property
    def order_id(self):
        r"""Gets the order_id of this UpdateInstanceResponse.

        **参数说明**：订单号，仅包年包月实例返回该参数。[查看订单详情请参考[[查询订单详情](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0075746564.html)。]](tag:hws)

        :return: The order_id of this UpdateInstanceResponse.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        r"""Sets the order_id of this UpdateInstanceResponse.

        **参数说明**：订单号，仅包年包月实例返回该参数。[查看订单详情请参考[[查询订单详情](https://support.huaweicloud.com/api-bpconsole/zh-cn_topic_0075746564.html)。]](tag:hws)

        :param order_id: The order_id of this UpdateInstanceResponse.
        :type order_id: str
        """
        self._order_id = order_id

    @property
    def operate_window(self):
        r"""Gets the operate_window of this UpdateInstanceResponse.

        :return: The operate_window of this UpdateInstanceResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        """
        return self._operate_window

    @operate_window.setter
    def operate_window(self, operate_window):
        r"""Sets the operate_window of this UpdateInstanceResponse.

        :param operate_window: The operate_window of this UpdateInstanceResponse.
        :type operate_window: :class:`huaweicloudsdkiotdm.v5.OperateWindow`
        """
        self._operate_window = operate_window

    @property
    def additional_params(self):
        r"""Gets the additional_params of this UpdateInstanceResponse.

        :return: The additional_params of this UpdateInstanceResponse.
        :rtype: :class:`huaweicloudsdkiotdm.v5.AdditionalParamsResp`
        """
        return self._additional_params

    @additional_params.setter
    def additional_params(self, additional_params):
        r"""Sets the additional_params of this UpdateInstanceResponse.

        :param additional_params: The additional_params of this UpdateInstanceResponse.
        :type additional_params: :class:`huaweicloudsdkiotdm.v5.AdditionalParamsResp`
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
        if not isinstance(other, UpdateInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
