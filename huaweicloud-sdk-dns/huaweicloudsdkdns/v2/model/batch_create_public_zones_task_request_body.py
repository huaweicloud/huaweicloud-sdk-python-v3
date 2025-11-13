# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreatePublicZonesTaskRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'zone_names': 'list[str]',
        'enterprise_project_id': 'str'
    }

    attribute_map = {
        'zone_names': 'zone_names',
        'enterprise_project_id': 'enterprise_project_id'
    }

    def __init__(self, zone_names=None, enterprise_project_id=None):
        r"""BatchCreatePublicZonesTaskRequestBody

        The model defined in huaweicloud sdk

        :param zone_names: **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 由多个以点分隔的字符串组成，可包含字母、数字、汉字、中划线，中划线不能在开头或末尾，单个字符串不超过63个字符，域名总长度不超过254个字符。 **默认取值：** 不涉及。
        :type zone_names: list[str]
        :param enterprise_project_id: **参数解释：** 域名所属的企业项目ID。可以使用该字段过滤企业项目下的域名。 **约束限制：** 不涉及。 **取值范围：** 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 **默认取值：** 不涉及。
        :type enterprise_project_id: str
        """
        
        

        self._zone_names = None
        self._enterprise_project_id = None
        self.discriminator = None

        self.zone_names = zone_names
        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id

    @property
    def zone_names(self):
        r"""Gets the zone_names of this BatchCreatePublicZonesTaskRequestBody.

        **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 由多个以点分隔的字符串组成，可包含字母、数字、汉字、中划线，中划线不能在开头或末尾，单个字符串不超过63个字符，域名总长度不超过254个字符。 **默认取值：** 不涉及。

        :return: The zone_names of this BatchCreatePublicZonesTaskRequestBody.
        :rtype: list[str]
        """
        return self._zone_names

    @zone_names.setter
    def zone_names(self, zone_names):
        r"""Sets the zone_names of this BatchCreatePublicZonesTaskRequestBody.

        **参数解释：** 域名。 **约束限制：** 不涉及。 **取值范围：** 由多个以点分隔的字符串组成，可包含字母、数字、汉字、中划线，中划线不能在开头或末尾，单个字符串不超过63个字符，域名总长度不超过254个字符。 **默认取值：** 不涉及。

        :param zone_names: The zone_names of this BatchCreatePublicZonesTaskRequestBody.
        :type zone_names: list[str]
        """
        self._zone_names = zone_names

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this BatchCreatePublicZonesTaskRequestBody.

        **参数解释：** 域名所属的企业项目ID。可以使用该字段过滤企业项目下的域名。 **约束限制：** 不涉及。 **取值范围：** 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 **默认取值：** 不涉及。

        :return: The enterprise_project_id of this BatchCreatePublicZonesTaskRequestBody.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this BatchCreatePublicZonesTaskRequestBody.

        **参数解释：** 域名所属的企业项目ID。可以使用该字段过滤企业项目下的域名。 **约束限制：** 不涉及。 **取值范围：** 最大长度36字节，带“-”连字符的UUID格式，或者是字符串“0”。“0”表示默认企业项目。 **默认取值：** 不涉及。

        :param enterprise_project_id: The enterprise_project_id of this BatchCreatePublicZonesTaskRequestBody.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

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
        if not isinstance(other, BatchCreatePublicZonesTaskRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
