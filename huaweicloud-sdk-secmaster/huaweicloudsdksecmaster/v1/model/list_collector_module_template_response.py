# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCollectorModuleTemplateResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'common': 'list[ModuleTemplateVo]',
        'list': 'list[ModuleTemplateVo]'
    }

    attribute_map = {
        'common': 'common',
        'list': 'list'
    }

    def __init__(self, common=None, list=None):
        r"""ListCollectorModuleTemplateResponse

        The model defined in huaweicloud sdk

        :param common: 常用解析模板数组
        :type common: list[:class:`huaweicloudsdksecmaster.v1.ModuleTemplateVo`]
        :param list: 列出解析模板数组
        :type list: list[:class:`huaweicloudsdksecmaster.v1.ModuleTemplateVo`]
        """
        
        super().__init__()

        self._common = None
        self._list = None
        self.discriminator = None

        if common is not None:
            self.common = common
        if list is not None:
            self.list = list

    @property
    def common(self):
        r"""Gets the common of this ListCollectorModuleTemplateResponse.

        常用解析模板数组

        :return: The common of this ListCollectorModuleTemplateResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ModuleTemplateVo`]
        """
        return self._common

    @common.setter
    def common(self, common):
        r"""Sets the common of this ListCollectorModuleTemplateResponse.

        常用解析模板数组

        :param common: The common of this ListCollectorModuleTemplateResponse.
        :type common: list[:class:`huaweicloudsdksecmaster.v1.ModuleTemplateVo`]
        """
        self._common = common

    @property
    def list(self):
        r"""Gets the list of this ListCollectorModuleTemplateResponse.

        列出解析模板数组

        :return: The list of this ListCollectorModuleTemplateResponse.
        :rtype: list[:class:`huaweicloudsdksecmaster.v1.ModuleTemplateVo`]
        """
        return self._list

    @list.setter
    def list(self, list):
        r"""Sets the list of this ListCollectorModuleTemplateResponse.

        列出解析模板数组

        :param list: The list of this ListCollectorModuleTemplateResponse.
        :type list: list[:class:`huaweicloudsdksecmaster.v1.ModuleTemplateVo`]
        """
        self._list = list

    def to_dict(self):
        import warnings
        warnings.warn("ListCollectorModuleTemplateResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListCollectorModuleTemplateResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
