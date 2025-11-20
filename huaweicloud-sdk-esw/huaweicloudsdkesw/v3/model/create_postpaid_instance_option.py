# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreatePostpaidInstanceOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'availability_zones': 'AvailabilityZones',
        'charge_infos': 'PostPaidChargeInfos',
        'flavor_ref': 'str',
        'ha_mode': 'str',
        'name': 'str',
        'tunnel_info': 'TunnelInfoOption',
        'description': 'str'
    }

    attribute_map = {
        'availability_zones': 'availability_zones',
        'charge_infos': 'charge_infos',
        'flavor_ref': 'flavor_ref',
        'ha_mode': 'ha_mode',
        'name': 'name',
        'tunnel_info': 'tunnel_info',
        'description': 'description'
    }

    def __init__(self, availability_zones=None, charge_infos=None, flavor_ref=None, ha_mode=None, name=None, tunnel_info=None, description=None):
        r"""CreatePostpaidInstanceOption

        The model defined in huaweicloud sdk

        :param availability_zones: 
        :type availability_zones: :class:`huaweicloudsdkesw.v3.AvailabilityZones`
        :param charge_infos: 
        :type charge_infos: :class:`huaweicloudsdkesw.v3.PostPaidChargeInfos`
        :param flavor_ref: - 参数解释：ESW实例规格。 - 约束限制：不涉及。 - 取值范围：参考flavor list接口响应。 - 默认取值：不涉及。
        :type flavor_ref: str
        :param ha_mode: - 参数解释：ESW实例的高可用模式。 - 约束限制：当前只支持设置ha。 - 取值范围：ha。 - 默认取值：不涉及。
        :type ha_mode: str
        :param name: - 参数解释：ESW实例名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type name: str
        :param tunnel_info: 
        :type tunnel_info: :class:`huaweicloudsdkesw.v3.TunnelInfoOption`
        :param description: - 参数解释：ESW实例描述信息。 - 约束限制：   - 长度范围为0~255个字符。   - 不能包含“&lt;”和“&gt;”。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type description: str
        """
        
        

        self._availability_zones = None
        self._charge_infos = None
        self._flavor_ref = None
        self._ha_mode = None
        self._name = None
        self._tunnel_info = None
        self._description = None
        self.discriminator = None

        self.availability_zones = availability_zones
        self.charge_infos = charge_infos
        self.flavor_ref = flavor_ref
        self.ha_mode = ha_mode
        self.name = name
        self.tunnel_info = tunnel_info
        if description is not None:
            self.description = description

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this CreatePostpaidInstanceOption.

        :return: The availability_zones of this CreatePostpaidInstanceOption.
        :rtype: :class:`huaweicloudsdkesw.v3.AvailabilityZones`
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this CreatePostpaidInstanceOption.

        :param availability_zones: The availability_zones of this CreatePostpaidInstanceOption.
        :type availability_zones: :class:`huaweicloudsdkesw.v3.AvailabilityZones`
        """
        self._availability_zones = availability_zones

    @property
    def charge_infos(self):
        r"""Gets the charge_infos of this CreatePostpaidInstanceOption.

        :return: The charge_infos of this CreatePostpaidInstanceOption.
        :rtype: :class:`huaweicloudsdkesw.v3.PostPaidChargeInfos`
        """
        return self._charge_infos

    @charge_infos.setter
    def charge_infos(self, charge_infos):
        r"""Sets the charge_infos of this CreatePostpaidInstanceOption.

        :param charge_infos: The charge_infos of this CreatePostpaidInstanceOption.
        :type charge_infos: :class:`huaweicloudsdkesw.v3.PostPaidChargeInfos`
        """
        self._charge_infos = charge_infos

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例规格。 - 约束限制：不涉及。 - 取值范围：参考flavor list接口响应。 - 默认取值：不涉及。

        :return: The flavor_ref of this CreatePostpaidInstanceOption.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例规格。 - 约束限制：不涉及。 - 取值范围：参考flavor list接口响应。 - 默认取值：不涉及。

        :param flavor_ref: The flavor_ref of this CreatePostpaidInstanceOption.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例的高可用模式。 - 约束限制：当前只支持设置ha。 - 取值范围：ha。 - 默认取值：不涉及。

        :return: The ha_mode of this CreatePostpaidInstanceOption.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例的高可用模式。 - 约束限制：当前只支持设置ha。 - 取值范围：ha。 - 默认取值：不涉及。

        :param ha_mode: The ha_mode of this CreatePostpaidInstanceOption.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def name(self):
        r"""Gets the name of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The name of this CreatePostpaidInstanceOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param name: The name of this CreatePostpaidInstanceOption.
        :type name: str
        """
        self._name = name

    @property
    def tunnel_info(self):
        r"""Gets the tunnel_info of this CreatePostpaidInstanceOption.

        :return: The tunnel_info of this CreatePostpaidInstanceOption.
        :rtype: :class:`huaweicloudsdkesw.v3.TunnelInfoOption`
        """
        return self._tunnel_info

    @tunnel_info.setter
    def tunnel_info(self, tunnel_info):
        r"""Sets the tunnel_info of this CreatePostpaidInstanceOption.

        :param tunnel_info: The tunnel_info of this CreatePostpaidInstanceOption.
        :type tunnel_info: :class:`huaweicloudsdkesw.v3.TunnelInfoOption`
        """
        self._tunnel_info = tunnel_info

    @property
    def description(self):
        r"""Gets the description of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例描述信息。 - 约束限制：   - 长度范围为0~255个字符。   - 不能包含“<”和“>”。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The description of this CreatePostpaidInstanceOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this CreatePostpaidInstanceOption.

        - 参数解释：ESW实例描述信息。 - 约束限制：   - 长度范围为0~255个字符。   - 不能包含“<”和“>”。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param description: The description of this CreatePostpaidInstanceOption.
        :type description: str
        """
        self._description = description

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CreatePostpaidInstanceOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
