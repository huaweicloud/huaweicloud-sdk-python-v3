# coding: utf-8

import pprint
import re

import six





class BandWidthRules:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'admin_state_up': 'bool',
        'egress_size': 'int',
        'egress_guarented_size': 'int',
        'publicip_info': 'list[PublicipInfoResp]'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'admin_state_up': 'admin_state_up',
        'egress_size': 'egress_size',
        'egress_guarented_size': 'egress_guarented_size',
        'publicip_info': 'publicip_info'
    }

    def __init__(self, id=None, name=None, admin_state_up=None, egress_size=None, egress_guarented_size=None, publicip_info=None):
        """BandWidthRules - a model defined in huaweicloud sdk"""
        
        

        self._id = None
        self._name = None
        self._admin_state_up = None
        self._egress_size = None
        self._egress_guarented_size = None
        self._publicip_info = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if admin_state_up is not None:
            self.admin_state_up = admin_state_up
        if egress_size is not None:
            self.egress_size = egress_size
        if egress_guarented_size is not None:
            self.egress_guarented_size = egress_guarented_size
        if publicip_info is not None:
            self.publicip_info = publicip_info

    @property
    def id(self):
        """Gets the id of this BandWidthRules.

        带宽规则ID

        :return: The id of this BandWidthRules.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BandWidthRules.

        带宽规则ID

        :param id: The id of this BandWidthRules.
        :type: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this BandWidthRules.

        带宽规则名称

        :return: The name of this BandWidthRules.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BandWidthRules.

        带宽规则名称

        :param name: The name of this BandWidthRules.
        :type: str
        """
        self._name = name

    @property
    def admin_state_up(self):
        """Gets the admin_state_up of this BandWidthRules.

        配置状态，为False时配置不生效。

        :return: The admin_state_up of this BandWidthRules.
        :rtype: bool
        """
        return self._admin_state_up

    @admin_state_up.setter
    def admin_state_up(self, admin_state_up):
        """Sets the admin_state_up of this BandWidthRules.

        配置状态，为False时配置不生效。

        :param admin_state_up: The admin_state_up of this BandWidthRules.
        :type: bool
        """
        self._admin_state_up = admin_state_up

    @property
    def egress_size(self):
        """Gets the egress_size of this BandWidthRules.

        出网带宽最大值，单位M bps。取值范围[0,n]，其中n为所属带宽的带宽大小（size字段）。0表示设置为最大带宽。

        :return: The egress_size of this BandWidthRules.
        :rtype: int
        """
        return self._egress_size

    @egress_size.setter
    def egress_size(self, egress_size):
        """Sets the egress_size of this BandWidthRules.

        出网带宽最大值，单位M bps。取值范围[0,n]，其中n为所属带宽的带宽大小（size字段）。0表示设置为最大带宽。

        :param egress_size: The egress_size of this BandWidthRules.
        :type: int
        """
        self._egress_size = egress_size

    @property
    def egress_guarented_size(self):
        """Gets the egress_guarented_size of this BandWidthRules.

        出网保障带宽大小，单位M bps。取值范围[0,x]，其中x为所属带宽剩余的保障额。

        :return: The egress_guarented_size of this BandWidthRules.
        :rtype: int
        """
        return self._egress_guarented_size

    @egress_guarented_size.setter
    def egress_guarented_size(self, egress_guarented_size):
        """Sets the egress_guarented_size of this BandWidthRules.

        出网保障带宽大小，单位M bps。取值范围[0,x]，其中x为所属带宽剩余的保障额。

        :param egress_guarented_size: The egress_guarented_size of this BandWidthRules.
        :type: int
        """
        self._egress_guarented_size = egress_guarented_size

    @property
    def publicip_info(self):
        """Gets the publicip_info of this BandWidthRules.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :return: The publicip_info of this BandWidthRules.
        :rtype: list[PublicipInfoResp]
        """
        return self._publicip_info

    @publicip_info.setter
    def publicip_info(self, publicip_info):
        """Sets the publicip_info of this BandWidthRules.

        功能说明：带宽对应的弹性公网IP信息  约束：WHOLE类型的带宽支持多个弹性公网IP，PER类型的带宽只能对应一个弹性公网IP

        :param publicip_info: The publicip_info of this BandWidthRules.
        :type: list[PublicipInfoResp]
        """
        self._publicip_info = publicip_info

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, BandWidthRules):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
