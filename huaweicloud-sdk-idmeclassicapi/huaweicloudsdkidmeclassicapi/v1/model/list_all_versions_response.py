# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAllVersionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'data': 'list[VersionModelQueryViewDTO]',
        'errors': 'list[str]',
        'page_info': 'PageInfoViewDTO'
    }

    attribute_map = {
        'result': 'result',
        'data': 'data',
        'errors': 'errors',
        'page_info': 'pageInfo'
    }

    def __init__(self, result=None, data=None, errors=None, page_info=None):
        r"""ListAllVersionsResponse

        The model defined in huaweicloud sdk

        :param result: **参数解释：**  请求结果。  **取值范围：**  - SUCCESS：请求成功。 - FAIL：请求失败。  **默认取值：**  不涉及。 
        :type result: str
        :param data: **参数解释：**  请求数据。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type data: list[:class:`huaweicloudsdkidmeclassicapi.v1.VersionModelQueryViewDTO`]
        :param errors: **参数解释：**  异常信息。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 
        :type errors: list[str]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkidmeclassicapi.v1.PageInfoViewDTO`
        """
        
        super(ListAllVersionsResponse, self).__init__()

        self._result = None
        self._data = None
        self._errors = None
        self._page_info = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if data is not None:
            self.data = data
        if errors is not None:
            self.errors = errors
        if page_info is not None:
            self.page_info = page_info

    @property
    def result(self):
        r"""Gets the result of this ListAllVersionsResponse.

        **参数解释：**  请求结果。  **取值范围：**  - SUCCESS：请求成功。 - FAIL：请求失败。  **默认取值：**  不涉及。 

        :return: The result of this ListAllVersionsResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this ListAllVersionsResponse.

        **参数解释：**  请求结果。  **取值范围：**  - SUCCESS：请求成功。 - FAIL：请求失败。  **默认取值：**  不涉及。 

        :param result: The result of this ListAllVersionsResponse.
        :type result: str
        """
        self._result = result

    @property
    def data(self):
        r"""Gets the data of this ListAllVersionsResponse.

        **参数解释：**  请求数据。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The data of this ListAllVersionsResponse.
        :rtype: list[:class:`huaweicloudsdkidmeclassicapi.v1.VersionModelQueryViewDTO`]
        """
        return self._data

    @data.setter
    def data(self, data):
        r"""Sets the data of this ListAllVersionsResponse.

        **参数解释：**  请求数据。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param data: The data of this ListAllVersionsResponse.
        :type data: list[:class:`huaweicloudsdkidmeclassicapi.v1.VersionModelQueryViewDTO`]
        """
        self._data = data

    @property
    def errors(self):
        r"""Gets the errors of this ListAllVersionsResponse.

        **参数解释：**  异常信息。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :return: The errors of this ListAllVersionsResponse.
        :rtype: list[str]
        """
        return self._errors

    @errors.setter
    def errors(self, errors):
        r"""Sets the errors of this ListAllVersionsResponse.

        **参数解释：**  异常信息。  **取值范围：**  不涉及。  **默认取值：**  不涉及。 

        :param errors: The errors of this ListAllVersionsResponse.
        :type errors: list[str]
        """
        self._errors = errors

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAllVersionsResponse.

        :return: The page_info of this ListAllVersionsResponse.
        :rtype: :class:`huaweicloudsdkidmeclassicapi.v1.PageInfoViewDTO`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAllVersionsResponse.

        :param page_info: The page_info of this ListAllVersionsResponse.
        :type page_info: :class:`huaweicloudsdkidmeclassicapi.v1.PageInfoViewDTO`
        """
        self._page_info = page_info

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
        if not isinstance(other, ListAllVersionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
