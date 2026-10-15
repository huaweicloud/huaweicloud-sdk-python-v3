# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateRayFederationRequestBody:

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
        'display_name': 'str',
        'description': 'str',
        'ray_cluster_list': 'list[RayFederationRayClusterRequest]'
    }

    attribute_map = {
        'name': 'name',
        'display_name': 'display_name',
        'description': 'description',
        'ray_cluster_list': 'ray_cluster_list'
    }

    def __init__(self, name=None, display_name=None, description=None, ray_cluster_list=None):
        r"""UpdateRayFederationRequestBody

        The model defined in huaweicloud sdk

        :param name: **参数解释**：Ray联邦端点名称。 **约束限制**：不能修改。该字段将被忽略，仅用于响应一致性展示，更新对象由路径参数ray_federation_id标识。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。
        :type name: str
        :param display_name: **参数解释**：Ray联邦端点显示名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 **默认取值**：不涉及。
        :type display_name: str
        :param description: **参数解释**：Ray联邦端点描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~1024个字符。 **默认取值**：不涉及。
        :type description: str
        :param ray_cluster_list: **参数解释**：RayCluster端点列表。输入后，将覆盖原有列表。 **约束限制**：每个RayCluster只能属于一个Ray联邦端点。 **取值范围**：0~50个RayCluster端点。 **默认取值**：不涉及。
        :type ray_cluster_list: list[:class:`huaweicloudsdkaidatalake.v2.RayFederationRayClusterRequest`]
        """
        
        

        self._name = None
        self._display_name = None
        self._description = None
        self._ray_cluster_list = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if display_name is not None:
            self.display_name = display_name
        if description is not None:
            self.description = description
        if ray_cluster_list is not None:
            self.ray_cluster_list = ray_cluster_list

    @property
    def name(self):
        r"""Gets the name of this UpdateRayFederationRequestBody.

        **参数解释**：Ray联邦端点名称。 **约束限制**：不能修改。该字段将被忽略，仅用于响应一致性展示，更新对象由路径参数ray_federation_id标识。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。

        :return: The name of this UpdateRayFederationRequestBody.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this UpdateRayFederationRequestBody.

        **参数解释**：Ray联邦端点名称。 **约束限制**：不能修改。该字段将被忽略，仅用于响应一致性展示，更新对象由路径参数ray_federation_id标识。 **取值范围**：支持小写字母、数字、中划线，必须字母开头、字母或数字结尾，长度为1~63个字符。 **默认取值**：不涉及。

        :param name: The name of this UpdateRayFederationRequestBody.
        :type name: str
        """
        self._name = name

    @property
    def display_name(self):
        r"""Gets the display_name of this UpdateRayFederationRequestBody.

        **参数解释**：Ray联邦端点显示名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 **默认取值**：不涉及。

        :return: The display_name of this UpdateRayFederationRequestBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        r"""Sets the display_name of this UpdateRayFederationRequestBody.

        **参数解释**：Ray联邦端点显示名称。 **约束限制**：不涉及。 **取值范围**：长度为1~63个字符，支持字母、数字、中划线、汉字。 **默认取值**：不涉及。

        :param display_name: The display_name of this UpdateRayFederationRequestBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def description(self):
        r"""Gets the description of this UpdateRayFederationRequestBody.

        **参数解释**：Ray联邦端点描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~1024个字符。 **默认取值**：不涉及。

        :return: The description of this UpdateRayFederationRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this UpdateRayFederationRequestBody.

        **参数解释**：Ray联邦端点描述。 **约束限制**：不涉及。 **取值范围**：不允许输入感叹号、小于号、大于号、等号、与号、双引号、单引号、艾特符、井号、百分号、分号、左括号、右括号、竖线、星号、反斜杠。长度为0~1024个字符。 **默认取值**：不涉及。

        :param description: The description of this UpdateRayFederationRequestBody.
        :type description: str
        """
        self._description = description

    @property
    def ray_cluster_list(self):
        r"""Gets the ray_cluster_list of this UpdateRayFederationRequestBody.

        **参数解释**：RayCluster端点列表。输入后，将覆盖原有列表。 **约束限制**：每个RayCluster只能属于一个Ray联邦端点。 **取值范围**：0~50个RayCluster端点。 **默认取值**：不涉及。

        :return: The ray_cluster_list of this UpdateRayFederationRequestBody.
        :rtype: list[:class:`huaweicloudsdkaidatalake.v2.RayFederationRayClusterRequest`]
        """
        return self._ray_cluster_list

    @ray_cluster_list.setter
    def ray_cluster_list(self, ray_cluster_list):
        r"""Sets the ray_cluster_list of this UpdateRayFederationRequestBody.

        **参数解释**：RayCluster端点列表。输入后，将覆盖原有列表。 **约束限制**：每个RayCluster只能属于一个Ray联邦端点。 **取值范围**：0~50个RayCluster端点。 **默认取值**：不涉及。

        :param ray_cluster_list: The ray_cluster_list of this UpdateRayFederationRequestBody.
        :type ray_cluster_list: list[:class:`huaweicloudsdkaidatalake.v2.RayFederationRayClusterRequest`]
        """
        self._ray_cluster_list = ray_cluster_list

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
        if not isinstance(other, UpdateRayFederationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
