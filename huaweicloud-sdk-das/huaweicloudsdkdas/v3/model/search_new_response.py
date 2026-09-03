# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SearchNewResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'sql_item_dto_list': 'list[SqlItemDto]',
        'total': 'int'
    }

    attribute_map = {
        'sql_item_dto_list': 'sql_item_dto_list',
        'total': 'total'
    }

    def __init__(self, sql_item_dto_list=None, total=None):
        r"""SearchNewResponse

        The model defined in huaweicloud sdk

        :param sql_item_dto_list: SQL列表
        :type sql_item_dto_list: list[:class:`huaweicloudsdkdas.v3.SqlItemDto`]
        :param total: 总数
        :type total: int
        """
        
        super().__init__()

        self._sql_item_dto_list = None
        self._total = None
        self.discriminator = None

        if sql_item_dto_list is not None:
            self.sql_item_dto_list = sql_item_dto_list
        if total is not None:
            self.total = total

    @property
    def sql_item_dto_list(self):
        r"""Gets the sql_item_dto_list of this SearchNewResponse.

        SQL列表

        :return: The sql_item_dto_list of this SearchNewResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.SqlItemDto`]
        """
        return self._sql_item_dto_list

    @sql_item_dto_list.setter
    def sql_item_dto_list(self, sql_item_dto_list):
        r"""Sets the sql_item_dto_list of this SearchNewResponse.

        SQL列表

        :param sql_item_dto_list: The sql_item_dto_list of this SearchNewResponse.
        :type sql_item_dto_list: list[:class:`huaweicloudsdkdas.v3.SqlItemDto`]
        """
        self._sql_item_dto_list = sql_item_dto_list

    @property
    def total(self):
        r"""Gets the total of this SearchNewResponse.

        总数

        :return: The total of this SearchNewResponse.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this SearchNewResponse.

        总数

        :param total: The total of this SearchNewResponse.
        :type total: int
        """
        self._total = total

    def to_dict(self):
        import warnings
        warnings.warn("SearchNewResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, SearchNewResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
