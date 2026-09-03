# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlTemplateComparisonsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_tpl_cmp_dto_list': 'list[SQLTplCmp]'
    }

    attribute_map = {
        'sql_tpl_cmp_dto_list': 'sql_tpl_cmp_dto_list'
    }

    def __init__(self, sql_tpl_cmp_dto_list=None):
        r"""ListSqlTemplateComparisonsResponse

        The model defined in huaweicloud sdk

        :param sql_tpl_cmp_dto_list: SQL模板对比列表
        :type sql_tpl_cmp_dto_list: list[:class:`huaweicloudsdkdas.v3.SQLTplCmp`]
        """
        
        super().__init__()

        self._sql_tpl_cmp_dto_list = None
        self.discriminator = None

        if sql_tpl_cmp_dto_list is not None:
            self.sql_tpl_cmp_dto_list = sql_tpl_cmp_dto_list

    @property
    def sql_tpl_cmp_dto_list(self):
        r"""Gets the sql_tpl_cmp_dto_list of this ListSqlTemplateComparisonsResponse.

        SQL模板对比列表

        :return: The sql_tpl_cmp_dto_list of this ListSqlTemplateComparisonsResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SQLTplCmp`]
        """
        return self._sql_tpl_cmp_dto_list

    @sql_tpl_cmp_dto_list.setter
    def sql_tpl_cmp_dto_list(self, sql_tpl_cmp_dto_list):
        r"""Sets the sql_tpl_cmp_dto_list of this ListSqlTemplateComparisonsResponse.

        SQL模板对比列表

        :param sql_tpl_cmp_dto_list: The sql_tpl_cmp_dto_list of this ListSqlTemplateComparisonsResponse.
        :type sql_tpl_cmp_dto_list: list[:class:`huaweicloudsdkdas.v3.SQLTplCmp`]
        """
        self._sql_tpl_cmp_dto_list = sql_tpl_cmp_dto_list

    def to_dict(self):
        import warnings
        warnings.warn("ListSqlTemplateComparisonsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSqlTemplateComparisonsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
