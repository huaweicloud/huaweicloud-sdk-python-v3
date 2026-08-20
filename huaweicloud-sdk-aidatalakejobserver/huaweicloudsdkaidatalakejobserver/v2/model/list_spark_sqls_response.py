# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSparkSqlsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'SparkMarkerPageInfo',
        'statements': 'list[ListSparkSqlResItem]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'statements': 'statements'
    }

    def __init__(self, page_info=None, statements=None):
        r"""ListSparkSqlsResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkMarkerPageInfo`
        :param statements: **参数解释**：详细的SparkSql作业列表，包含作业ID、状态、SQL内容等信息。
        :type statements: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkSqlResItem`]
        """
        
        super().__init__()

        self._page_info = None
        self._statements = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if statements is not None:
            self.statements = statements

    @property
    def page_info(self):
        r"""Gets the page_info of this ListSparkSqlsResponse.

        :return: The page_info of this ListSparkSqlsResponse.
        :rtype: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkMarkerPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListSparkSqlsResponse.

        :param page_info: The page_info of this ListSparkSqlsResponse.
        :type page_info: :class:`huaweicloudsdkaidatalakejobserver.v2.SparkMarkerPageInfo`
        """
        self._page_info = page_info

    @property
    def statements(self):
        r"""Gets the statements of this ListSparkSqlsResponse.

        **参数解释**：详细的SparkSql作业列表，包含作业ID、状态、SQL内容等信息。

        :return: The statements of this ListSparkSqlsResponse.
        :rtype: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkSqlResItem`]
        """
        return self._statements

    @statements.setter
    def statements(self, statements):
        r"""Sets the statements of this ListSparkSqlsResponse.

        **参数解释**：详细的SparkSql作业列表，包含作业ID、状态、SQL内容等信息。

        :param statements: The statements of this ListSparkSqlsResponse.
        :type statements: list[:class:`huaweicloudsdkaidatalakejobserver.v2.ListSparkSqlResItem`]
        """
        self._statements = statements

    def to_dict(self):
        import warnings
        warnings.warn("ListSparkSqlsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSparkSqlsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
