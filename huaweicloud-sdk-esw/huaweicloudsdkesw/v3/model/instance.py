# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Instance:

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
        'project_id': 'str',
        'region': 'str',
        'flavor_ref': 'str',
        'ha_mode': 'str',
        'status': 'str',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'description': 'str',
        'tunnel_info': 'TunnelInfoResult',
        'charge_infos': 'PostPaidChargeInfos',
        'availability_zones': 'AvailabilityZones'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'project_id': 'project_id',
        'region': 'region',
        'flavor_ref': 'flavor_ref',
        'ha_mode': 'ha_mode',
        'status': 'status',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'description': 'description',
        'tunnel_info': 'tunnel_info',
        'charge_infos': 'charge_infos',
        'availability_zones': 'availability_zones'
    }

    def __init__(self, id=None, name=None, project_id=None, region=None, flavor_ref=None, ha_mode=None, status=None, created_at=None, updated_at=None, description=None, tunnel_info=None, charge_infos=None, availability_zones=None):
        r"""Instance

        The model defined in huaweicloud sdk

        :param id: - 参数解释：ESW实例的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type id: str
        :param name: - 参数解释：ESW实例名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type name: str
        :param project_id: - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type project_id: str
        :param region: - 参数解释：ESW实例所属region的ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type region: str
        :param flavor_ref: - 参数解释：ESW实例规格。 - 约束限制：不涉及。 - 取值范围：参考flavor list接口响应。 - 默认取值：不涉及。
        :type flavor_ref: str
        :param ha_mode: - 参数解释：ESW实例的高可用模式。 - 约束限制：当前只支持设置ha。 - 取值范围：ha。 - 默认取值：不涉及。
        :type ha_mode: str
        :param status: - 参数解释：ESW实例的状态。 - 约束限制：不涉及。 - 取值范围：   - active：运行中   - failed：创建失败   - abnormal：异常   - build：创建中   - frozen：已冻结 - 默认取值：不涉及。
        :type status: str
        :param created_at: - 参数解释：ESW实例创建时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type created_at: datetime
        :param updated_at: - 参数解释：ESW实例更新时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type updated_at: datetime
        :param description: - 参数解释：ESW实例描述信息。 - 约束限制：   - 长度范围为0~255个字符。   - 不能包含“&lt;”和“&gt;”。 - 取值范围：不涉及。 - 默认取值：不涉及。
        :type description: str
        :param tunnel_info: 
        :type tunnel_info: :class:`huaweicloudsdkesw.v3.TunnelInfoResult`
        :param charge_infos: 
        :type charge_infos: :class:`huaweicloudsdkesw.v3.PostPaidChargeInfos`
        :param availability_zones: 
        :type availability_zones: :class:`huaweicloudsdkesw.v3.AvailabilityZones`
        """
        
        

        self._id = None
        self._name = None
        self._project_id = None
        self._region = None
        self._flavor_ref = None
        self._ha_mode = None
        self._status = None
        self._created_at = None
        self._updated_at = None
        self._description = None
        self._tunnel_info = None
        self._charge_infos = None
        self._availability_zones = None
        self.discriminator = None

        self.id = id
        self.name = name
        self.project_id = project_id
        self.region = region
        self.flavor_ref = flavor_ref
        self.ha_mode = ha_mode
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at
        self.description = description
        self.tunnel_info = tunnel_info
        self.charge_infos = charge_infos
        self.availability_zones = availability_zones

    @property
    def id(self):
        r"""Gets the id of this Instance.

        - 参数解释：ESW实例的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The id of this Instance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this Instance.

        - 参数解释：ESW实例的唯一标识。 - 约束限制：带“-”的UUID格式。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param id: The id of this Instance.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this Instance.

        - 参数解释：ESW实例名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The name of this Instance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Instance.

        - 参数解释：ESW实例名称。 - 约束限制：   - 长度范围为1~64个字符。   - 名称由中文、英文字母、数字、下划线（_）、中划线（-）、点（.）组成。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param name: The name of this Instance.
        :type name: str
        """
        self._name = name

    @property
    def project_id(self):
        r"""Gets the project_id of this Instance.

        - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The project_id of this Instance.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this Instance.

        - 参数解释：ESW实例所属项目ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param project_id: The project_id of this Instance.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def region(self):
        r"""Gets the region of this Instance.

        - 参数解释：ESW实例所属region的ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The region of this Instance.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        r"""Sets the region of this Instance.

        - 参数解释：ESW实例所属region的ID。 - 约束限制：不涉及。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param region: The region of this Instance.
        :type region: str
        """
        self._region = region

    @property
    def flavor_ref(self):
        r"""Gets the flavor_ref of this Instance.

        - 参数解释：ESW实例规格。 - 约束限制：不涉及。 - 取值范围：参考flavor list接口响应。 - 默认取值：不涉及。

        :return: The flavor_ref of this Instance.
        :rtype: str
        """
        return self._flavor_ref

    @flavor_ref.setter
    def flavor_ref(self, flavor_ref):
        r"""Sets the flavor_ref of this Instance.

        - 参数解释：ESW实例规格。 - 约束限制：不涉及。 - 取值范围：参考flavor list接口响应。 - 默认取值：不涉及。

        :param flavor_ref: The flavor_ref of this Instance.
        :type flavor_ref: str
        """
        self._flavor_ref = flavor_ref

    @property
    def ha_mode(self):
        r"""Gets the ha_mode of this Instance.

        - 参数解释：ESW实例的高可用模式。 - 约束限制：当前只支持设置ha。 - 取值范围：ha。 - 默认取值：不涉及。

        :return: The ha_mode of this Instance.
        :rtype: str
        """
        return self._ha_mode

    @ha_mode.setter
    def ha_mode(self, ha_mode):
        r"""Sets the ha_mode of this Instance.

        - 参数解释：ESW实例的高可用模式。 - 约束限制：当前只支持设置ha。 - 取值范围：ha。 - 默认取值：不涉及。

        :param ha_mode: The ha_mode of this Instance.
        :type ha_mode: str
        """
        self._ha_mode = ha_mode

    @property
    def status(self):
        r"""Gets the status of this Instance.

        - 参数解释：ESW实例的状态。 - 约束限制：不涉及。 - 取值范围：   - active：运行中   - failed：创建失败   - abnormal：异常   - build：创建中   - frozen：已冻结 - 默认取值：不涉及。

        :return: The status of this Instance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Instance.

        - 参数解释：ESW实例的状态。 - 约束限制：不涉及。 - 取值范围：   - active：运行中   - failed：创建失败   - abnormal：异常   - build：创建中   - frozen：已冻结 - 默认取值：不涉及。

        :param status: The status of this Instance.
        :type status: str
        """
        self._status = status

    @property
    def created_at(self):
        r"""Gets the created_at of this Instance.

        - 参数解释：ESW实例创建时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The created_at of this Instance.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this Instance.

        - 参数解释：ESW实例创建时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param created_at: The created_at of this Instance.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this Instance.

        - 参数解释：ESW实例更新时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The updated_at of this Instance.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this Instance.

        - 参数解释：ESW实例更新时间。 - 约束限制：UTC时间，格式为yyyy-MM-ddTHH:mm:ss。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param updated_at: The updated_at of this Instance.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def description(self):
        r"""Gets the description of this Instance.

        - 参数解释：ESW实例描述信息。 - 约束限制：   - 长度范围为0~255个字符。   - 不能包含“<”和“>”。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :return: The description of this Instance.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this Instance.

        - 参数解释：ESW实例描述信息。 - 约束限制：   - 长度范围为0~255个字符。   - 不能包含“<”和“>”。 - 取值范围：不涉及。 - 默认取值：不涉及。

        :param description: The description of this Instance.
        :type description: str
        """
        self._description = description

    @property
    def tunnel_info(self):
        r"""Gets the tunnel_info of this Instance.

        :return: The tunnel_info of this Instance.
        :rtype: :class:`huaweicloudsdkesw.v3.TunnelInfoResult`
        """
        return self._tunnel_info

    @tunnel_info.setter
    def tunnel_info(self, tunnel_info):
        r"""Sets the tunnel_info of this Instance.

        :param tunnel_info: The tunnel_info of this Instance.
        :type tunnel_info: :class:`huaweicloudsdkesw.v3.TunnelInfoResult`
        """
        self._tunnel_info = tunnel_info

    @property
    def charge_infos(self):
        r"""Gets the charge_infos of this Instance.

        :return: The charge_infos of this Instance.
        :rtype: :class:`huaweicloudsdkesw.v3.PostPaidChargeInfos`
        """
        return self._charge_infos

    @charge_infos.setter
    def charge_infos(self, charge_infos):
        r"""Sets the charge_infos of this Instance.

        :param charge_infos: The charge_infos of this Instance.
        :type charge_infos: :class:`huaweicloudsdkesw.v3.PostPaidChargeInfos`
        """
        self._charge_infos = charge_infos

    @property
    def availability_zones(self):
        r"""Gets the availability_zones of this Instance.

        :return: The availability_zones of this Instance.
        :rtype: :class:`huaweicloudsdkesw.v3.AvailabilityZones`
        """
        return self._availability_zones

    @availability_zones.setter
    def availability_zones(self, availability_zones):
        r"""Sets the availability_zones of this Instance.

        :param availability_zones: The availability_zones of this Instance.
        :type availability_zones: :class:`huaweicloudsdkesw.v3.AvailabilityZones`
        """
        self._availability_zones = availability_zones

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
        if not isinstance(other, Instance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
