# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOtaModulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modules': 'list[OtaModuleInfo]',
        'page': 'PageInfo'
    }

    attribute_map = {
        'modules': 'modules',
        'page': 'page'
    }

    def __init__(self, modules=None, page=None):
        r"""ListOtaModulesResponse

        The model defined in huaweicloud sdk

        :param modules: 模块列表
        :type modules: list[:class:`huaweicloudsdkiotda.v5.OtaModuleInfo`]
        :param page: 
        :type page: :class:`huaweicloudsdkiotda.v5.PageInfo`
        """
        
        super().__init__()

        self._modules = None
        self._page = None
        self.discriminator = None

        if modules is not None:
            self.modules = modules
        if page is not None:
            self.page = page

    @property
    def modules(self):
        r"""Gets the modules of this ListOtaModulesResponse.

        模块列表

        :return: The modules of this ListOtaModulesResponse.
        :rtype: list[:class:`huaweicloudsdkiotda.v5.OtaModuleInfo`]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        r"""Sets the modules of this ListOtaModulesResponse.

        模块列表

        :param modules: The modules of this ListOtaModulesResponse.
        :type modules: list[:class:`huaweicloudsdkiotda.v5.OtaModuleInfo`]
        """
        self._modules = modules

    @property
    def page(self):
        r"""Gets the page of this ListOtaModulesResponse.

        :return: The page of this ListOtaModulesResponse.
        :rtype: :class:`huaweicloudsdkiotda.v5.PageInfo`
        """
        return self._page

    @page.setter
    def page(self, page):
        r"""Sets the page of this ListOtaModulesResponse.

        :param page: The page of this ListOtaModulesResponse.
        :type page: :class:`huaweicloudsdkiotda.v5.PageInfo`
        """
        self._page = page

    def to_dict(self):
        import warnings
        warnings.warn("ListOtaModulesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListOtaModulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
