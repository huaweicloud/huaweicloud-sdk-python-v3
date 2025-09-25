# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ChangeImageWhiteListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'rule_type': 'str',
        'query_info': 'AddImageWhiteListsRequestBodyQueryInfo',
        'image_info': 'list[AddImageWhiteListsRequestBodyImageInfo]',
        'description': 'str'
    }

    attribute_map = {
        'rule_type': 'rule_type',
        'query_info': 'query_info',
        'image_info': 'image_info',
        'description': 'description'
    }

    def __init__(self, rule_type=None, query_info=None, image_info=None, description=None):
        r"""ChangeImageWhiteListRequestBody

        The model defined in huaweicloud sdk

        :param rule_type: **参数解释**： 白名单规则类型 **约束限制**: 不涉及 **取值范围**: - all_images：白名单应用于全部镜像。 - specific_image_types：白名单应用于指定镜像类型(仅用于指定仓库镜像类型)。 - specific_images：白名单应用于指定镜像。  **默认取值**: 不涉及 
        :type rule_type: str
        :param query_info: 
        :type query_info: :class:`huaweicloudsdkhss.v5.AddImageWhiteListsRequestBodyQueryInfo`
        :param image_info: 指定具体镜像
        :type image_info: list[:class:`huaweicloudsdkhss.v5.AddImageWhiteListsRequestBodyImageInfo`]
        :param description: 白名单的描述信息
        :type description: str
        """
        
        

        self._rule_type = None
        self._query_info = None
        self._image_info = None
        self._description = None
        self.discriminator = None

        if rule_type is not None:
            self.rule_type = rule_type
        if query_info is not None:
            self.query_info = query_info
        if image_info is not None:
            self.image_info = image_info
        if description is not None:
            self.description = description

    @property
    def rule_type(self):
        r"""Gets the rule_type of this ChangeImageWhiteListRequestBody.

        **参数解释**： 白名单规则类型 **约束限制**: 不涉及 **取值范围**: - all_images：白名单应用于全部镜像。 - specific_image_types：白名单应用于指定镜像类型(仅用于指定仓库镜像类型)。 - specific_images：白名单应用于指定镜像。  **默认取值**: 不涉及 

        :return: The rule_type of this ChangeImageWhiteListRequestBody.
        :rtype: str
        """
        return self._rule_type

    @rule_type.setter
    def rule_type(self, rule_type):
        r"""Sets the rule_type of this ChangeImageWhiteListRequestBody.

        **参数解释**： 白名单规则类型 **约束限制**: 不涉及 **取值范围**: - all_images：白名单应用于全部镜像。 - specific_image_types：白名单应用于指定镜像类型(仅用于指定仓库镜像类型)。 - specific_images：白名单应用于指定镜像。  **默认取值**: 不涉及 

        :param rule_type: The rule_type of this ChangeImageWhiteListRequestBody.
        :type rule_type: str
        """
        self._rule_type = rule_type

    @property
    def query_info(self):
        r"""Gets the query_info of this ChangeImageWhiteListRequestBody.

        :return: The query_info of this ChangeImageWhiteListRequestBody.
        :rtype: :class:`huaweicloudsdkhss.v5.AddImageWhiteListsRequestBodyQueryInfo`
        """
        return self._query_info

    @query_info.setter
    def query_info(self, query_info):
        r"""Sets the query_info of this ChangeImageWhiteListRequestBody.

        :param query_info: The query_info of this ChangeImageWhiteListRequestBody.
        :type query_info: :class:`huaweicloudsdkhss.v5.AddImageWhiteListsRequestBodyQueryInfo`
        """
        self._query_info = query_info

    @property
    def image_info(self):
        r"""Gets the image_info of this ChangeImageWhiteListRequestBody.

        指定具体镜像

        :return: The image_info of this ChangeImageWhiteListRequestBody.
        :rtype: list[:class:`huaweicloudsdkhss.v5.AddImageWhiteListsRequestBodyImageInfo`]
        """
        return self._image_info

    @image_info.setter
    def image_info(self, image_info):
        r"""Sets the image_info of this ChangeImageWhiteListRequestBody.

        指定具体镜像

        :param image_info: The image_info of this ChangeImageWhiteListRequestBody.
        :type image_info: list[:class:`huaweicloudsdkhss.v5.AddImageWhiteListsRequestBodyImageInfo`]
        """
        self._image_info = image_info

    @property
    def description(self):
        r"""Gets the description of this ChangeImageWhiteListRequestBody.

        白名单的描述信息

        :return: The description of this ChangeImageWhiteListRequestBody.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this ChangeImageWhiteListRequestBody.

        白名单的描述信息

        :param description: The description of this ChangeImageWhiteListRequestBody.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, ChangeImageWhiteListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
