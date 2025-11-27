# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CopyPolicyByIdRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enterprise_project_id': 'str',
        'src_policy_id': 'str',
        'dest_policy_name': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'src_policy_id': 'src_policy_id',
        'dest_policy_name': 'dest_policy_name'
    }

    def __init__(self, enterprise_project_id=None, src_policy_id=None, dest_policy_name=None):
        r"""CopyPolicyByIdRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0
        :type enterprise_project_id: str
        :param src_policy_id: **参数解释：** 源策略id，可以通过 查询 防护策略列表（ListPolicy）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及  **默认取值：** 不涉及
        :type src_policy_id: str
        :param dest_policy_name: **参数解释：** 复制出的新策略名称，用于标识复制后的防护策略，需符合命名规范（如无特殊字符、长度限制等）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及
        :type dest_policy_name: str
        """
        
        

        self._enterprise_project_id = None
        self._src_policy_id = None
        self._dest_policy_name = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.src_policy_id = src_policy_id
        self.dest_policy_name = dest_policy_name

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CopyPolicyByIdRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :return: The enterprise_project_id of this CopyPolicyByIdRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CopyPolicyByIdRequest.

        **参数解释：** 您可以通过调用企业项目管理服务（EPS）的查询企业项目列表接口（ListEnterpriseProject）查询企业项目ID。若需要查询当前用户所有企业项目绑定的资源信息，请传参all_granted_eps。 **约束限制：** 不涉及 **取值范围：**  - 0：代表default企业项目  - all_granted_eps：代表所有企业项目  - 其它企业项目ID：长度为36个字符 **默认取值：** 0

        :param enterprise_project_id: The enterprise_project_id of this CopyPolicyByIdRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def src_policy_id(self):
        r"""Gets the src_policy_id of this CopyPolicyByIdRequest.

        **参数解释：** 源策略id，可以通过 查询 防护策略列表（ListPolicy）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及  **默认取值：** 不涉及

        :return: The src_policy_id of this CopyPolicyByIdRequest.
        :rtype: str
        """
        return self._src_policy_id

    @src_policy_id.setter
    def src_policy_id(self, src_policy_id):
        r"""Sets the src_policy_id of this CopyPolicyByIdRequest.

        **参数解释：** 源策略id，可以通过 查询 防护策略列表（ListPolicy）接口获取 **约束限制：** 不涉及 **取值范围：** 不涉及  **默认取值：** 不涉及

        :param src_policy_id: The src_policy_id of this CopyPolicyByIdRequest.
        :type src_policy_id: str
        """
        self._src_policy_id = src_policy_id

    @property
    def dest_policy_name(self):
        r"""Gets the dest_policy_name of this CopyPolicyByIdRequest.

        **参数解释：** 复制出的新策略名称，用于标识复制后的防护策略，需符合命名规范（如无特殊字符、长度限制等）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :return: The dest_policy_name of this CopyPolicyByIdRequest.
        :rtype: str
        """
        return self._dest_policy_name

    @dest_policy_name.setter
    def dest_policy_name(self, dest_policy_name):
        r"""Sets the dest_policy_name of this CopyPolicyByIdRequest.

        **参数解释：** 复制出的新策略名称，用于标识复制后的防护策略，需符合命名规范（如无特殊字符、长度限制等）。 **约束限制：** 不涉及 **取值范围：** 不涉及 **默认取值：** 不涉及

        :param dest_policy_name: The dest_policy_name of this CopyPolicyByIdRequest.
        :type dest_policy_name: str
        """
        self._dest_policy_name = dest_policy_name

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
        if not isinstance(other, CopyPolicyByIdRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
