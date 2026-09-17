# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowCategoryStatusRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'project_id': 'str',
        'categories': 'str'
    }

    attribute_map = {
        'project_id': 'project_id',
        'categories': 'categories'
    }

    def __init__(self, project_id=None, categories=None):
        r"""ShowCategoryStatusRequest

        The model defined in huaweicloud sdk

        :param project_id: 项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。
        :type project_id: str
        :param categories: **参数解释**： 工作项类型。 **约束限制**： 2~128个字符。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔，例如：IR,SR,AR。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。
        :type categories: str
        """
        
        

        self._project_id = None
        self._categories = None
        self.discriminator = None

        self.project_id = project_id
        self.categories = categories

    @property
    def project_id(self):
        r"""Gets the project_id of this ShowCategoryStatusRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :return: The project_id of this ShowCategoryStatusRequest.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ShowCategoryStatusRequest.

        项目32位ID，项目唯一标识。通过查询IPD项目列表获取，响应消息体中的id字段的值就是项目ID。

        :param project_id: The project_id of this ShowCategoryStatusRequest.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def categories(self):
        r"""Gets the categories of this ShowCategoryStatusRequest.

        **参数解释**： 工作项类型。 **约束限制**： 2~128个字符。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔，例如：IR,SR,AR。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。

        :return: The categories of this ShowCategoryStatusRequest.
        :rtype: str
        """
        return self._categories

    @categories.setter
    def categories(self, categories):
        r"""Sets the categories of this ShowCategoryStatusRequest.

        **参数解释**： 工作项类型。 **约束限制**： 2~128个字符。 **取值范围**： 支持多种工作项类型，使用英文逗号分隔，例如：IR,SR,AR。 - 系统设备类项目：RR、SF、IR、SR、AR、Task、Bug - 独立软件类项目：RR、SF、IR、US、Task、Bug - 云服务类项目：RR、Epic、FE、US、Task、Bug **默认取值**： 不涉及。

        :param categories: The categories of this ShowCategoryStatusRequest.
        :type categories: str
        """
        self._categories = categories

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
        if not isinstance(other, ShowCategoryStatusRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
