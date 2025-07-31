# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGlobalAssetScanTaskRequest:

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
        'category': 'str',
        'body': 'CreateGlobalAssetScanTaskRequestInfo'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'category': 'category',
        'body': 'body'
    }

    def __init__(self, enterprise_project_id=None, category=None, body=None):
        r"""CreateGlobalAssetScanTaskRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param category: **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件  **默认取值**: 不涉及 
        :type category: str
        :param body: Body of the CreateGlobalAssetScanTaskRequest
        :type body: :class:`huaweicloudsdkhss.v5.CreateGlobalAssetScanTaskRequestInfo`
        """
        
        

        self._enterprise_project_id = None
        self._category = None
        self._body = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.category = category
        if body is not None:
            self.body = body

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this CreateGlobalAssetScanTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this CreateGlobalAssetScanTaskRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this CreateGlobalAssetScanTaskRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this CreateGlobalAssetScanTaskRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def category(self):
        r"""Gets the category of this CreateGlobalAssetScanTaskRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件  **默认取值**: 不涉及 

        :return: The category of this CreateGlobalAssetScanTaskRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this CreateGlobalAssetScanTaskRequest.

        **参数解释**: 事件类别 **约束限制**: 不涉及 **取值范围**: - host：主机安全事件 - container：容器安全事件  **默认取值**: 不涉及 

        :param category: The category of this CreateGlobalAssetScanTaskRequest.
        :type category: str
        """
        self._category = category

    @property
    def body(self):
        r"""Gets the body of this CreateGlobalAssetScanTaskRequest.

        :return: The body of this CreateGlobalAssetScanTaskRequest.
        :rtype: :class:`huaweicloudsdkhss.v5.CreateGlobalAssetScanTaskRequestInfo`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this CreateGlobalAssetScanTaskRequest.

        :param body: The body of this CreateGlobalAssetScanTaskRequest.
        :type body: :class:`huaweicloudsdkhss.v5.CreateGlobalAssetScanTaskRequestInfo`
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
        if not isinstance(other, CreateGlobalAssetScanTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
