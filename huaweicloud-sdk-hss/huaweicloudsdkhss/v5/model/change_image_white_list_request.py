# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeImageWhiteListRequest:

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
        'id': 'str',
        'global_image_type': 'str',
        'type': 'str',
        'body': 'ChangeImageWhiteListRequestBody'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'id': 'id',
        'global_image_type': 'global_image_type',
        'type': 'type',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, id=None, global_image_type=None, type=None, body=None):
        r"""ChangeImageWhiteListRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param id: **参数解释**： 白名单ID **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 
        :type id: str
        :param global_image_type: **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 
        :type global_image_type: str
        :param type: **参数解释**： 白名单类型 **约束限制**: 不涉及 **取值范围**: - vulnerability：漏洞白名单。  **默认取值**: 不涉及 
        :type type: str
        :param body: Body of the ChangeImageWhiteListRequest
        :type body: :class:`huaweicloudsdkhss.v5.ChangeImageWhiteListRequestBody`
        """
        
        

        self._enterprise_project_id = None
        self._id = None
        self._global_image_type = None
        self._type = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.id = id
        self.global_image_type = global_image_type
        self.type = type
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ChangeImageWhiteListRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ChangeImageWhiteListRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ChangeImageWhiteListRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ChangeImageWhiteListRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def id(self):
        r"""Gets the id of this ChangeImageWhiteListRequest.

        **参数解释**： 白名单ID **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :return: The id of this ChangeImageWhiteListRequest.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this ChangeImageWhiteListRequest.

        **参数解释**： 白名单ID **约束限制**： 不涉及 **取值范围**： 字符长度1-64位 **默认取值**： 不涉及 

        :param id: The id of this ChangeImageWhiteListRequest.
        :type id: str
        """
        self._id = id

    @property
    def global_image_type(self):
        r"""Gets the global_image_type of this ChangeImageWhiteListRequest.

        **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 

        :return: The global_image_type of this ChangeImageWhiteListRequest.
        :rtype: str
        """
        return self._global_image_type

    @global_image_type.setter
    def global_image_type(self, global_image_type):
        r"""Sets the global_image_type of this ChangeImageWhiteListRequest.

        **参数解释**： 镜像类型 **约束限制**: 不涉及 **取值范围**: - local：本地镜像。 - registry：仓库镜像。  **默认取值**: 不涉及 

        :param global_image_type: The global_image_type of this ChangeImageWhiteListRequest.
        :type global_image_type: str
        """
        self._global_image_type = global_image_type

    @property
    def type(self):
        r"""Gets the type of this ChangeImageWhiteListRequest.

        **参数解释**： 白名单类型 **约束限制**: 不涉及 **取值范围**: - vulnerability：漏洞白名单。  **默认取值**: 不涉及 

        :return: The type of this ChangeImageWhiteListRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this ChangeImageWhiteListRequest.

        **参数解释**： 白名单类型 **约束限制**: 不涉及 **取值范围**: - vulnerability：漏洞白名单。  **默认取值**: 不涉及 

        :param type: The type of this ChangeImageWhiteListRequest.
        :type type: str
        """
        self._type = type

    @property
    def body(self):
        r"""Gets the body of this ChangeImageWhiteListRequest.

        :return: The body of this ChangeImageWhiteListRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.ChangeImageWhiteListRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ChangeImageWhiteListRequest.

        :param body: The body of this ChangeImageWhiteListRequest.
        :type body: :class:`huaweicloudsdkhss.v5.ChangeImageWhiteListRequestBody`
        """
        self._body = body

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
        if not isinstance(other, ChangeImageWhiteListRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
