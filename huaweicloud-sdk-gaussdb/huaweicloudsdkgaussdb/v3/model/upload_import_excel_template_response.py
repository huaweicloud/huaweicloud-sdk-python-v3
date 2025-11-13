# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UploadImportExcelTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'bool',
        'processed_rows': 'int',
        'error_tables': 'list[ErrorTable]',
        'success_tables': 'list[SuccessTable]',
        'error_count': 'int',
        'success_count': 'int'
    }

    attribute_map = {
        'success': 'success',
        'processed_rows': 'processed_rows',
        'error_tables': 'error_tables',
        'success_tables': 'success_tables',
        'error_count': 'error_count',
        'success_count': 'success_count'
    }

    def __init__(self, success=None, processed_rows=None, error_tables=None, success_tables=None, error_count=None, success_count=None):
        r"""UploadImportExcelTemplateResponse

        The model defined in huaweicloud sdk

        :param success: **参数解释**：  Excel导入返回状态。  **取值范围**：  - true: 导入成功。 - false： 导入失败。
        :type success: bool
        :param processed_rows: **参数解释**：  已处理的行数。   **取值范围**：  不涉及。
        :type processed_rows: int
        :param error_tables: **参数解释**：  导入失败返回的错误列表。 
        :type error_tables: list[:class:`huaweicloudsdkgaussdb.v3.ErrorTable`]
        :param success_tables: **参数解释**：  Excel导入验证成功的列表。 
        :type success_tables: list[:class:`huaweicloudsdkgaussdb.v3.SuccessTable`]
        :param error_count: **参数解释**：  Excel导入验证失败的行数。   **取值范围**：  不涉及。
        :type error_count: int
        :param success_count: **参数解释**：  Excel导入验证成功的行数。   **取值范围**：  不涉及。
        :type success_count: int
        """
        
        super().__init__()

        self._success = None
        self._processed_rows = None
        self._error_tables = None
        self._success_tables = None
        self._error_count = None
        self._success_count = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if processed_rows is not None:
            self.processed_rows = processed_rows
        if error_tables is not None:
            self.error_tables = error_tables
        if success_tables is not None:
            self.success_tables = success_tables
        if error_count is not None:
            self.error_count = error_count
        if success_count is not None:
            self.success_count = success_count

    @property
    def success(self):
        r"""Gets the success of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入返回状态。  **取值范围**：  - true: 导入成功。 - false： 导入失败。

        :return: The success of this UploadImportExcelTemplateResponse.
        :rtype: bool
        """
        return self._success

    @success.setter
    def success(self, success):
        r"""Sets the success of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入返回状态。  **取值范围**：  - true: 导入成功。 - false： 导入失败。

        :param success: The success of this UploadImportExcelTemplateResponse.
        :type success: bool
        """
        self._success = success

    @property
    def processed_rows(self):
        r"""Gets the processed_rows of this UploadImportExcelTemplateResponse.

        **参数解释**：  已处理的行数。   **取值范围**：  不涉及。

        :return: The processed_rows of this UploadImportExcelTemplateResponse.
        :rtype: int
        """
        return self._processed_rows

    @processed_rows.setter
    def processed_rows(self, processed_rows):
        r"""Sets the processed_rows of this UploadImportExcelTemplateResponse.

        **参数解释**：  已处理的行数。   **取值范围**：  不涉及。

        :param processed_rows: The processed_rows of this UploadImportExcelTemplateResponse.
        :type processed_rows: int
        """
        self._processed_rows = processed_rows

    @property
    def error_tables(self):
        r"""Gets the error_tables of this UploadImportExcelTemplateResponse.

        **参数解释**：  导入失败返回的错误列表。 

        :return: The error_tables of this UploadImportExcelTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.ErrorTable`]
        """
        return self._error_tables

    @error_tables.setter
    def error_tables(self, error_tables):
        r"""Sets the error_tables of this UploadImportExcelTemplateResponse.

        **参数解释**：  导入失败返回的错误列表。 

        :param error_tables: The error_tables of this UploadImportExcelTemplateResponse.
        :type error_tables: list[:class:`huaweicloudsdkgaussdb.v3.ErrorTable`]
        """
        self._error_tables = error_tables

    @property
    def success_tables(self):
        r"""Gets the success_tables of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入验证成功的列表。 

        :return: The success_tables of this UploadImportExcelTemplateResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdb.v3.SuccessTable`]
        """
        return self._success_tables

    @success_tables.setter
    def success_tables(self, success_tables):
        r"""Sets the success_tables of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入验证成功的列表。 

        :param success_tables: The success_tables of this UploadImportExcelTemplateResponse.
        :type success_tables: list[:class:`huaweicloudsdkgaussdb.v3.SuccessTable`]
        """
        self._success_tables = success_tables

    @property
    def error_count(self):
        r"""Gets the error_count of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入验证失败的行数。   **取值范围**：  不涉及。

        :return: The error_count of this UploadImportExcelTemplateResponse.
        :rtype: int
        """
        return self._error_count

    @error_count.setter
    def error_count(self, error_count):
        r"""Sets the error_count of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入验证失败的行数。   **取值范围**：  不涉及。

        :param error_count: The error_count of this UploadImportExcelTemplateResponse.
        :type error_count: int
        """
        self._error_count = error_count

    @property
    def success_count(self):
        r"""Gets the success_count of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入验证成功的行数。   **取值范围**：  不涉及。

        :return: The success_count of this UploadImportExcelTemplateResponse.
        :rtype: int
        """
        return self._success_count

    @success_count.setter
    def success_count(self, success_count):
        r"""Sets the success_count of this UploadImportExcelTemplateResponse.

        **参数解释**：  Excel导入验证成功的行数。   **取值范围**：  不涉及。

        :param success_count: The success_count of this UploadImportExcelTemplateResponse.
        :type success_count: int
        """
        self._success_count = success_count

    def to_dict(self):
        import warnings
        warnings.warn("UploadImportExcelTemplateResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, UploadImportExcelTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
