# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateGlobalConnectionBandwidth:

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
        'description': 'str',
        'size': 'int',
        'charge_mode': 'str',
        'sla_level': 'str',
        'binding_service': 'str',
        'spec_code_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'size': 'size',
        'charge_mode': 'charge_mode',
        'sla_level': 'sla_level',
        'binding_service': 'binding_service',
        'spec_code_id': 'spec_code_id'
    }

    def __init__(self, name=None, description=None, size=None, charge_mode=None, sla_level=None, binding_service=None, spec_code_id=None):
        r"""UpdateGlobalConnectionBandwidth

        The model defined in huaweicloud sdk

        :param name: 实例名称。
        :type name: str
        :param description: 实例描述。不支持 &lt;&gt;。
        :type description: str
        :param size: 功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s
        :type size: int
        :param charge_mode: 功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费     95avr: 按传统型日95计费
        :type charge_mode: str
        :param sla_level: 功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银
        :type sla_level: str
        :param binding_service: 功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型
        :type binding_service: str
        :param spec_code_id: 功能说明：线路规格编码UUID。
        :type spec_code_id: str
        """
        
        

        self._name = None
        self._description = None
        self._size = None
        self._charge_mode = None
        self._sla_level = None
        self._binding_service = None
        self._spec_code_id = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if size is not None:
            self.size = size
        if charge_mode is not None:
            self.charge_mode = charge_mode
        if sla_level is not None:
            self.sla_level = sla_level
        if binding_service is not None:
            self.binding_service = binding_service
        if spec_code_id is not None:
            self.spec_code_id = spec_code_id

    @property
    def name(self):
        r"""Gets the name of this UpdateGlobalConnectionBandwidth.

        实例名称。

        :return: The name of this UpdateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateGlobalConnectionBandwidth.

        实例名称。

        :param name: The name of this UpdateGlobalConnectionBandwidth.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        r"""Gets the description of this UpdateGlobalConnectionBandwidth.

        实例描述。不支持 <>。

        :return: The description of this UpdateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateGlobalConnectionBandwidth.

        实例描述。不支持 <>。

        :param description: The description of this UpdateGlobalConnectionBandwidth.
        :type description: str
        """
        self._description = description

    @property
    def size(self):
        r"""Gets the size of this UpdateGlobalConnectionBandwidth.

        功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s

        :return: The size of this UpdateGlobalConnectionBandwidth.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        r"""Sets the size of this UpdateGlobalConnectionBandwidth.

        功能说明：全域互联带宽实例中的带宽值大小，单位Mbit/s。 取值范围：2-300Mbit/s

        :param size: The size of this UpdateGlobalConnectionBandwidth.
        :type size: int
        """
        self._size = size

    @property
    def charge_mode(self):
        r"""Gets the charge_mode of this UpdateGlobalConnectionBandwidth.

        功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费     95avr: 按传统型日95计费

        :return: The charge_mode of this UpdateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._charge_mode

    @charge_mode.setter
    def charge_mode(self, charge_mode):
        r"""Sets the charge_mode of this UpdateGlobalConnectionBandwidth.

        功能说明：描述计费类型，描述可选计费类型。默认开放按带宽计费，传统95计费租户白名单控制。 取值范围：     bwd: 按带宽计费     95: 按传统型95计费     95avr: 按传统型日95计费

        :param charge_mode: The charge_mode of this UpdateGlobalConnectionBandwidth.
        :type charge_mode: str
        """
        self._charge_mode = charge_mode

    @property
    def sla_level(self):
        r"""Gets the sla_level of this UpdateGlobalConnectionBandwidth.

        功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银

        :return: The sla_level of this UpdateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._sla_level

    @sla_level.setter
    def sla_level(self, sla_level):
        r"""Sets the sla_level of this UpdateGlobalConnectionBandwidth.

        功能说明：描述网络等级，从高到低分为铂金、金、银。默认金，其余租户白名单控制。 - Pt: 铂金 - Au: 金 - Ag: 银

        :param sla_level: The sla_level of this UpdateGlobalConnectionBandwidth.
        :type sla_level: str
        """
        self._sla_level = sla_level

    @property
    def binding_service(self):
        r"""Gets the binding_service of this UpdateGlobalConnectionBandwidth.

        功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型

        :return: The binding_service of this UpdateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._binding_service

    @binding_service.setter
    def binding_service(self, binding_service):
        r"""Sets the binding_service of this UpdateGlobalConnectionBandwidth.

        功能说明：绑定的服务类型。实例类型： - CC: 云连接 - GEIP: 全域弹性公网IP - GCN: 中心网络 - GSN: 分支网络 - ALL: 所有实例类型

        :param binding_service: The binding_service of this UpdateGlobalConnectionBandwidth.
        :type binding_service: str
        """
        self._binding_service = binding_service

    @property
    def spec_code_id(self):
        r"""Gets the spec_code_id of this UpdateGlobalConnectionBandwidth.

        功能说明：线路规格编码UUID。

        :return: The spec_code_id of this UpdateGlobalConnectionBandwidth.
        :rtype: str
        """
        return self._spec_code_id

    @spec_code_id.setter
    def spec_code_id(self, spec_code_id):
        r"""Sets the spec_code_id of this UpdateGlobalConnectionBandwidth.

        功能说明：线路规格编码UUID。

        :param spec_code_id: The spec_code_id of this UpdateGlobalConnectionBandwidth.
        :type spec_code_id: str
        """
        self._spec_code_id = spec_code_id

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
        if not isinstance(other, UpdateGlobalConnectionBandwidth):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
