# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModelConfigDTO:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'categories': 'list[BaseCategory]',
        'category_layer_config': 'list[CategoryLayerDTO]',
        'feature_page_link_template': 'str'
    }

    attribute_map = {
        'categories': 'categories',
        'category_layer_config': 'category_layer_config',
        'feature_page_link_template': 'feature_page_link_template'
    }

    def __init__(self, categories=None, category_layer_config=None, feature_page_link_template=None):
        r"""ModelConfigDTO

        The model defined in huaweicloud sdk

        :param categories: **参数解释**： 工作项属性。 **取值范围**： 不涉及。
        :type categories: list[:class:`huaweicloudsdkprojectman.v4.BaseCategory`]
        :param category_layer_config: **参数解释**： 工作项层级关系。 **取值范围**： 不涉及。
        :type category_layer_config: list[:class:`huaweicloudsdkprojectman.v4.CategoryLayerDTO`]
        :param feature_page_link_template: **参数解释**： 工作项功能页面跳转链接模板。 **取值范围**： 不涉及。
        :type feature_page_link_template: str
        """
        
        

        self._categories = None
        self._category_layer_config = None
        self._feature_page_link_template = None
        self.discriminator = None

        if categories is not None:
            self.categories = categories
        if category_layer_config is not None:
            self.category_layer_config = category_layer_config
        if feature_page_link_template is not None:
            self.feature_page_link_template = feature_page_link_template

    @property
    def categories(self):
        r"""Gets the categories of this ModelConfigDTO.

        **参数解释**： 工作项属性。 **取值范围**： 不涉及。

        :return: The categories of this ModelConfigDTO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.BaseCategory`]
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ModelConfigDTO.

        **参数解释**： 工作项属性。 **取值范围**： 不涉及。

        :param categories: The categories of this ModelConfigDTO.
        :type categories: list[:class:`huaweicloudsdkprojectman.v4.BaseCategory`]
        """
        self._categories = categories

    @property
    def category_layer_config(self):
        r"""Gets the category_layer_config of this ModelConfigDTO.

        **参数解释**： 工作项层级关系。 **取值范围**： 不涉及。

        :return: The category_layer_config of this ModelConfigDTO.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.CategoryLayerDTO`]
        """
        return self._category_layer_config

    @category_layer_config.setter
    def category_layer_config(self, category_layer_config):
        r"""Sets the category_layer_config of this ModelConfigDTO.

        **参数解释**： 工作项层级关系。 **取值范围**： 不涉及。

        :param category_layer_config: The category_layer_config of this ModelConfigDTO.
        :type category_layer_config: list[:class:`huaweicloudsdkprojectman.v4.CategoryLayerDTO`]
        """
        self._category_layer_config = category_layer_config

    @property
    def feature_page_link_template(self):
        r"""Gets the feature_page_link_template of this ModelConfigDTO.

        **参数解释**： 工作项功能页面跳转链接模板。 **取值范围**： 不涉及。

        :return: The feature_page_link_template of this ModelConfigDTO.
        :rtype: str
        """
        return self._feature_page_link_template

    @feature_page_link_template.setter
    def feature_page_link_template(self, feature_page_link_template):
        r"""Sets the feature_page_link_template of this ModelConfigDTO.

        **参数解释**： 工作项功能页面跳转链接模板。 **取值范围**： 不涉及。

        :param feature_page_link_template: The feature_page_link_template of this ModelConfigDTO.
        :type feature_page_link_template: str
        """
        self._feature_page_link_template = feature_page_link_template

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
        if not isinstance(other, ModelConfigDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
