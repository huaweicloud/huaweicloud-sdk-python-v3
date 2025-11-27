# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListServerlessAssetDetailRequest:

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
        'asset_id': 'str'
    }

    attribute_map = {
        'enterprise_project_id': 'enterprise_project_id',
        'category': 'category',
        'asset_id': 'asset_id'
    }

    def __init__(self, enterprise_project_id=None, category=None, asset_id=None):
        r"""ListServerlessAssetDetailRequest

        The model defined in huaweicloud sdk

        :param enterprise_project_id: **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 
        :type enterprise_project_id: str
        :param category: **参数解释**： 资产维度 **约束限制**： 不涉及 **取值范围**： - container : 容器维度 **默认取值**： container
        :type category: str
        :param asset_id: **参数解释**: 资产ID，基于参数category决定维度（比如category&#x3D;container时，asset_id为容器id） **约束限制**： 不涉及 **取值范围**: 字符长度0-255位 **默认取值**： 不涉及 
        :type asset_id: str
        """
        
        

        self._enterprise_project_id = None
        self._category = None
        self._asset_id = None
        self.discriminator = None

        if enterprise_project_id is not None:
            self.enterprise_project_id = enterprise_project_id
        self.category = category
        self.asset_id = asset_id

    @property
    def enterprise_project_id(self):
        r"""Gets the enterprise_project_id of this ListServerlessAssetDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :return: The enterprise_project_id of this ListServerlessAssetDetailRequest.
        :rtype: str
        """
        return self._enterprise_project_id

    @enterprise_project_id.setter
    def enterprise_project_id(self, enterprise_project_id):
        r"""Sets the enterprise_project_id of this ListServerlessAssetDetailRequest.

        **参数解释**: 企业项目ID，用于过滤不同企业项目下的资产。获取方式请参见[获取企业项目ID](hss_02_0027.xml)。 如需查询所有企业项目下的资产请传参“all_granted_eps”。 **约束限制**: 开通企业项目功能后才需要配置企业项目ID参数。 **取值范围**: 字符长度1-256位 **默认取值**: 0，表示默认企业项目（default）。 

        :param enterprise_project_id: The enterprise_project_id of this ListServerlessAssetDetailRequest.
        :type enterprise_project_id: str
        """
        self._enterprise_project_id = enterprise_project_id

    @property
    def category(self):
        r"""Gets the category of this ListServerlessAssetDetailRequest.

        **参数解释**： 资产维度 **约束限制**： 不涉及 **取值范围**： - container : 容器维度 **默认取值**： container

        :return: The category of this ListServerlessAssetDetailRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListServerlessAssetDetailRequest.

        **参数解释**： 资产维度 **约束限制**： 不涉及 **取值范围**： - container : 容器维度 **默认取值**： container

        :param category: The category of this ListServerlessAssetDetailRequest.
        :type category: str
        """
        self._category = category

    @property
    def asset_id(self):
        r"""Gets the asset_id of this ListServerlessAssetDetailRequest.

        **参数解释**: 资产ID，基于参数category决定维度（比如category=container时，asset_id为容器id） **约束限制**： 不涉及 **取值范围**: 字符长度0-255位 **默认取值**： 不涉及 

        :return: The asset_id of this ListServerlessAssetDetailRequest.
        :rtype: str
        """
        return self._asset_id

    @asset_id.setter
    def asset_id(self, asset_id):
        r"""Sets the asset_id of this ListServerlessAssetDetailRequest.

        **参数解释**: 资产ID，基于参数category决定维度（比如category=container时，asset_id为容器id） **约束限制**： 不涉及 **取值范围**: 字符长度0-255位 **默认取值**： 不涉及 

        :param asset_id: The asset_id of this ListServerlessAssetDetailRequest.
        :type asset_id: str
        """
        self._asset_id = asset_id

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
        if not isinstance(other, ListServerlessAssetDetailRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
