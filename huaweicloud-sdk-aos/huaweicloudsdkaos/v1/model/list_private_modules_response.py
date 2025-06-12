# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListPrivateModulesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'modules': 'list[PrivateModuleSummary]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'modules': 'modules',
        'page_info': 'page_info'
    }

    def __init__(self, modules=None, page_info=None):
        r"""ListPrivateModulesResponse

        The model defined in huaweicloud sdk

        :param modules: 私有模块的列表。默认以创建时间升序排序。
        :type modules: list[:class:`huaweicloudsdkaos.v1.PrivateModuleSummary`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        
        super(ListPrivateModulesResponse, self).__init__()

        self._modules = None
        self._page_info = None
        self.discriminator = None

        if modules is not None:
            self.modules = modules
        if page_info is not None:
            self.page_info = page_info

    @property
    def modules(self):
        r"""Gets the modules of this ListPrivateModulesResponse.

        私有模块的列表。默认以创建时间升序排序。

        :return: The modules of this ListPrivateModulesResponse.
        :rtype: list[:class:`huaweicloudsdkaos.v1.PrivateModuleSummary`]
        """
        return self._modules

    @modules.setter
    def modules(self, modules):
        r"""Sets the modules of this ListPrivateModulesResponse.

        私有模块的列表。默认以创建时间升序排序。

        :param modules: The modules of this ListPrivateModulesResponse.
        :type modules: list[:class:`huaweicloudsdkaos.v1.PrivateModuleSummary`]
        """
        self._modules = modules

    @property
    def page_info(self):
        r"""Gets the page_info of this ListPrivateModulesResponse.

        :return: The page_info of this ListPrivateModulesResponse.
        :rtype: :class:`huaweicloudsdkaos.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListPrivateModulesResponse.

        :param page_info: The page_info of this ListPrivateModulesResponse.
        :type page_info: :class:`huaweicloudsdkaos.v1.PageInfo`
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
        if not isinstance(other, ListPrivateModulesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
