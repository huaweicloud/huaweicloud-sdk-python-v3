# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCacheDatasRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_uu_id': 'str',
        'type': 'str'
    }

    attribute_map = {
        'project_uu_id': 'projectUUId',
        'type': 'type'
    }

    def __init__(self, project_uu_id=None, type=None):
        r"""ListCacheDatasRequest

        The model defined in huaweicloud sdk

        :param project_uu_id: **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。
        :type project_uu_id: str
        :param type: **参数解释：** 字段类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： backlog。
        :type type: str
        """
        
        

        self._project_uu_id = None
        self._type = None
        self.discriminator = None

        if project_uu_id is not None:
            self.project_uu_id = project_uu_id
        if type is not None:
            self.type = type

    @property
    def project_uu_id(self):
        r"""Gets the project_uu_id of this ListCacheDatasRequest.

        **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :return: The project_uu_id of this ListCacheDatasRequest.
        :rtype: str
        """
        return self._project_uu_id

    @project_uu_id.setter
    def project_uu_id(self, project_uu_id):
        r"""Sets the project_uu_id of this ListCacheDatasRequest.

        **参数解释**： 项目的32位uuid，项目唯一标识，通过[查询项目列表](ListProjectsV4.xml)接口获取，响应消息体中的**project_id**字段的值就是项目ID。 **约束限制**： 32位的数字和字母组成的字符串。 **取值范围**： 不涉及。 **默认取值**： 不涉及。

        :param project_uu_id: The project_uu_id of this ListCacheDatasRequest.
        :type project_uu_id: str
        """
        self._project_uu_id = project_uu_id

    @property
    def type(self):
        r"""Gets the type of this ListCacheDatasRequest.

        **参数解释：** 字段类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： backlog。

        :return: The type of this ListCacheDatasRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ListCacheDatasRequest.

        **参数解释：** 字段类型。 **约束限制**： 不涉及。 **取值范围**： 不涉及。 **默认取值**： backlog。

        :param type: The type of this ListCacheDatasRequest.
        :type type: str
        """
        self._type = type

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
        if not isinstance(other, ListCacheDatasRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
