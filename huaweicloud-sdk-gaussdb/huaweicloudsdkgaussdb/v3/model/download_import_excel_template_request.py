# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DownloadImportExcelTemplateRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'x_language': 'str',
        'instance_id': 'str',
        'template_type': 'str'
    }

    attribute_map = {
        'x_language': 'X-Language',
        'instance_id': 'instance_id',
        'template_type': 'template_type'
    }

    def __init__(self, x_language=None, instance_id=None, template_type=None):
        r"""DownloadImportExcelTemplateRequest

        The model defined in huaweicloud sdk

        :param x_language: **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。
        :type x_language: str
        :param instance_id: **参数解释**：  HTAP标准版实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，长度为36个字符。  **默认取值**：  不涉及。
        :type instance_id: str
        :param template_type: **参数解释**：  具体选择哪一种模板进行下载。  **约束限制**：  不涉及。  **取值范围**：  import_async: Excel导入文件类型。  **默认取值**：  不涉及。
        :type template_type: str
        """
        
        

        self._x_language = None
        self._instance_id = None
        self._template_type = None
        self.discriminator = None

        if x_language is not None:
            self.x_language = x_language
        self.instance_id = instance_id
        self.template_type = template_type

    @property
    def x_language(self):
        r"""Gets the x_language of this DownloadImportExcelTemplateRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。

        :return: The x_language of this DownloadImportExcelTemplateRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this DownloadImportExcelTemplateRequest.

        **参数解释**：              请求语言类型。  **约束限制**：  不涉及。  **取值范围**： - en-us - zh-cn  **默认取值**：  en-us。

        :param x_language: The x_language of this DownloadImportExcelTemplateRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def instance_id(self):
        r"""Gets the instance_id of this DownloadImportExcelTemplateRequest.

        **参数解释**：  HTAP标准版实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，长度为36个字符。  **默认取值**：  不涉及。

        :return: The instance_id of this DownloadImportExcelTemplateRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this DownloadImportExcelTemplateRequest.

        **参数解释**：  HTAP标准版实例ID，此参数是实例的唯一标识。  **约束限制**：  不涉及。  **取值范围**：  只能由英文字母、数字组成，后缀为in17，长度为36个字符。  **默认取值**：  不涉及。

        :param instance_id: The instance_id of this DownloadImportExcelTemplateRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def template_type(self):
        r"""Gets the template_type of this DownloadImportExcelTemplateRequest.

        **参数解释**：  具体选择哪一种模板进行下载。  **约束限制**：  不涉及。  **取值范围**：  import_async: Excel导入文件类型。  **默认取值**：  不涉及。

        :return: The template_type of this DownloadImportExcelTemplateRequest.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this DownloadImportExcelTemplateRequest.

        **参数解释**：  具体选择哪一种模板进行下载。  **约束限制**：  不涉及。  **取值范围**：  import_async: Excel导入文件类型。  **默认取值**：  不涉及。

        :param template_type: The template_type of this DownloadImportExcelTemplateRequest.
        :type template_type: str
        """
        self._template_type = template_type

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
        if not isinstance(other, DownloadImportExcelTemplateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
