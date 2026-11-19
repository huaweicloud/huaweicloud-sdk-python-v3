# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlPatchResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_patch_infos': 'list[SqlPatchInfosResult]',
        'total': 'int'
    }

    attribute_map = {
        'sql_patch_infos': 'sql_patch_infos',
        'total': 'total'
    }

    def __init__(self, sql_patch_infos=None, total=None):
        r"""ListSqlPatchResponse

        The model defined in huaweicloud sdk

        :param sql_patch_infos: **参数解释**: SQL Patch信息列表。
        :type sql_patch_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPatchInfosResult`]
        :param total: **参数解释**: 返回的SQL Patch数量。 **取值范围**: 不涉及。
        :type total: int
        """
        
        super().__init__()

        self._sql_patch_infos = None
        self._total = None
        self.discriminator = None

        if sql_patch_infos is not None:
            self.sql_patch_infos = sql_patch_infos
        if total is not None:
            self.total = total

    @property
    def sql_patch_infos(self):
        r"""Gets the sql_patch_infos of this ListSqlPatchResponse.

        **参数解释**: SQL Patch信息列表。

        :return: The sql_patch_infos of this ListSqlPatchResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPatchInfosResult`]
        """
        return self._sql_patch_infos

    @sql_patch_infos.setter
    def sql_patch_infos(self, sql_patch_infos):
        r"""Sets the sql_patch_infos of this ListSqlPatchResponse.

        **参数解释**: SQL Patch信息列表。

        :param sql_patch_infos: The sql_patch_infos of this ListSqlPatchResponse.
        :type sql_patch_infos: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.SqlPatchInfosResult`]
        """
        self._sql_patch_infos = sql_patch_infos

    @property
    def total(self):
        r"""Gets the total of this ListSqlPatchResponse.

        **参数解释**: 返回的SQL Patch数量。 **取值范围**: 不涉及。

        :return: The total of this ListSqlPatchResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ListSqlPatchResponse.

        **参数解释**: 返回的SQL Patch数量。 **取值范围**: 不涉及。

        :param total: The total of this ListSqlPatchResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("ListSqlPatchResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSqlPatchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
