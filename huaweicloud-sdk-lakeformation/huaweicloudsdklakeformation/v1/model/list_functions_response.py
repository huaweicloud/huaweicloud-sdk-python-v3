# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListFunctionsResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'page_info': 'PagedInfo',
        'functions': 'list[Function]'
    }

    attribute_map = {
        'page_info': 'page_info',
        'functions': 'functions'
    }

    def __init__(self, page_info=None, functions=None):
        r"""ListFunctionsResponse

        The model defined in huaweicloud sdk

        :param page_info: 
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        :param functions: 
        :type functions: list[:class:`huaweicloudsdklakeformation.v1.Function`]
        """
        
        super().__init__()

        self._page_info = None
        self._functions = None
        self.discriminator = None

        if page_info is not None:
            self.page_info = page_info
        if functions is not None:
            self.functions = functions

    @property
    def page_info(self):
        r"""Gets the page_info of this ListFunctionsResponse.

        :return: The page_info of this ListFunctionsResponse.
        :rtype: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListFunctionsResponse.

        :param page_info: The page_info of this ListFunctionsResponse.
        :type page_info: :class:`huaweicloudsdklakeformation.v1.PagedInfo`
        """
        self._page_info = page_info

    @property
    def functions(self):
        r"""Gets the functions of this ListFunctionsResponse.

        :return: The functions of this ListFunctionsResponse.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Function`]
        """
        return self._functions

    @functions.setter
    def functions(self, functions):
        r"""Sets the functions of this ListFunctionsResponse.

        :param functions: The functions of this ListFunctionsResponse.
        :type functions: list[:class:`huaweicloudsdklakeformation.v1.Function`]
        """
        self._functions = functions

    def to_dict(self):
        import warnings
        warnings.warn("ListFunctionsResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListFunctionsResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
