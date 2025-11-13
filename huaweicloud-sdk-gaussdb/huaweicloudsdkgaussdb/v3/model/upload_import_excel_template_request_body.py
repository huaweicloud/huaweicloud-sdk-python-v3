# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadImportExcelTemplateRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_type': 'str',
        'file': 'file',
        'is_instance_level': 'str',
        'selected_dbs': 'str',
        'is_support_regexp': 'str'
    }

    attribute_map = {
        'template_type': 'template_type',
        'file': 'file',
        'is_instance_level': 'is_instance_level',
        'selected_dbs': 'selected_dbs',
        'is_support_regexp': 'is_support_regexp'
    }

    def __init__(self, template_type=None, file=None, is_instance_level=None, selected_dbs=None, is_support_regexp=None):
        r"""UploadImportExcelTemplateRequestBody

        The model defined in huaweicloud sdk

        :param template_type: **参数解释**：  具体选择哪一种模板进行下载。  **约束限制**：  不涉及。  **取值范围**：  import_async: Excel导入文件类型。  **默认取值**：  不涉及。
        :type template_type: str
        :param file: **参数解释**：  Excel文件上传。  **约束限制**：  Excel文件。  **取值范围**：  .xlsx文件。  **默认取值**：  不涉及。
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        :param is_instance_level: **参数解释**：  判断是否是实例级同步。  **约束限制**：  不涉及。  **取值范围**：  - true：实例级同步。 - false: 非实例级同步。  **默认取值**：  false。
        :type is_instance_level: str
        :param selected_dbs: **参数解释**：  用户选中的数据库名，用英文\&quot;,\&quot;隔开。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。
        :type selected_dbs: str
        :param is_support_regexp: **参数解释**：  是否支持标配符。  **约束限制**：  不涉及。  **取值范围**：  - true: 支持标配符。 - false: 不支持标配符。  **默认取值**：  不涉及。
        :type is_support_regexp: str
        """
        
        

        self._template_type = None
        self._file = None
        self._is_instance_level = None
        self._selected_dbs = None
        self._is_support_regexp = None
        self.discriminator = None

        self.template_type = template_type
        self.file = file
        if is_instance_level is not None:
            self.is_instance_level = is_instance_level
        self.selected_dbs = selected_dbs
        if is_support_regexp is not None:
            self.is_support_regexp = is_support_regexp

    @property
    def template_type(self):
        r"""Gets the template_type of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  具体选择哪一种模板进行下载。  **约束限制**：  不涉及。  **取值范围**：  import_async: Excel导入文件类型。  **默认取值**：  不涉及。

        :return: The template_type of this UploadImportExcelTemplateRequestBody.
        :rtype: str
        """
        return self._template_type

    @template_type.setter
    def template_type(self, template_type):
        r"""Sets the template_type of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  具体选择哪一种模板进行下载。  **约束限制**：  不涉及。  **取值范围**：  import_async: Excel导入文件类型。  **默认取值**：  不涉及。

        :param template_type: The template_type of this UploadImportExcelTemplateRequestBody.
        :type template_type: str
        """
        self._template_type = template_type

    @property
    def file(self):
        r"""Gets the file of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  Excel文件上传。  **约束限制**：  Excel文件。  **取值范围**：  .xlsx文件。  **默认取值**：  不涉及。

        :return: The file of this UploadImportExcelTemplateRequestBody.
        :rtype: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        return self._file

    @file.setter
    def file(self, file):
        r"""Sets the file of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  Excel文件上传。  **约束限制**：  Excel文件。  **取值范围**：  .xlsx文件。  **默认取值**：  不涉及。

        :param file: The file of this UploadImportExcelTemplateRequestBody.
        :type file: :class:`huaweicloudsdkcore.http.formdata.FormFile`
        """
        self._file = file

    @property
    def is_instance_level(self):
        r"""Gets the is_instance_level of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  判断是否是实例级同步。  **约束限制**：  不涉及。  **取值范围**：  - true：实例级同步。 - false: 非实例级同步。  **默认取值**：  false。

        :return: The is_instance_level of this UploadImportExcelTemplateRequestBody.
        :rtype: str
        """
        return self._is_instance_level

    @is_instance_level.setter
    def is_instance_level(self, is_instance_level):
        r"""Sets the is_instance_level of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  判断是否是实例级同步。  **约束限制**：  不涉及。  **取值范围**：  - true：实例级同步。 - false: 非实例级同步。  **默认取值**：  false。

        :param is_instance_level: The is_instance_level of this UploadImportExcelTemplateRequestBody.
        :type is_instance_level: str
        """
        self._is_instance_level = is_instance_level

    @property
    def selected_dbs(self):
        r"""Gets the selected_dbs of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  用户选中的数据库名，用英文\",\"隔开。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :return: The selected_dbs of this UploadImportExcelTemplateRequestBody.
        :rtype: str
        """
        return self._selected_dbs

    @selected_dbs.setter
    def selected_dbs(self, selected_dbs):
        r"""Sets the selected_dbs of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  用户选中的数据库名，用英文\",\"隔开。  **约束限制**：  不涉及。  **取值范围**：  不涉及。  **默认取值**：  不涉及。

        :param selected_dbs: The selected_dbs of this UploadImportExcelTemplateRequestBody.
        :type selected_dbs: str
        """
        self._selected_dbs = selected_dbs

    @property
    def is_support_regexp(self):
        r"""Gets the is_support_regexp of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  是否支持标配符。  **约束限制**：  不涉及。  **取值范围**：  - true: 支持标配符。 - false: 不支持标配符。  **默认取值**：  不涉及。

        :return: The is_support_regexp of this UploadImportExcelTemplateRequestBody.
        :rtype: str
        """
        return self._is_support_regexp

    @is_support_regexp.setter
    def is_support_regexp(self, is_support_regexp):
        r"""Sets the is_support_regexp of this UploadImportExcelTemplateRequestBody.

        **参数解释**：  是否支持标配符。  **约束限制**：  不涉及。  **取值范围**：  - true: 支持标配符。 - false: 不支持标配符。  **默认取值**：  不涉及。

        :param is_support_regexp: The is_support_regexp of this UploadImportExcelTemplateRequestBody.
        :type is_support_regexp: str
        """
        self._is_support_regexp = is_support_regexp

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
        if not isinstance(other, UploadImportExcelTemplateRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
