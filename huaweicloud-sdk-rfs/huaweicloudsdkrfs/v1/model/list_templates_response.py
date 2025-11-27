# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'templates': 'list[Template]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'templates': 'templates',
        'page_info': 'page_info'
    }

    def __init__(self, templates=None, page_info=None):
        r"""ListTemplatesResponse

        The model defined in huaweicloud sdk

        :param templates: 模板列表
        :type templates: list[:class:`huaweicloudsdkrfs.v1.Template`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkrfs.v1.PageInfo`
        """
        
        super().__init__()

        self._templates = None
        self._page_info = None
        self.discriminator = None

        if templates is not None:
            self.templates = templates
        if page_info is not None:
            self.page_info = page_info

    @property
    def templates(self):
        r"""Gets the templates of this ListTemplatesResponse.

        模板列表

        :return: The templates of this ListTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkrfs.v1.Template`]
        """
        return self._templates

    @templates.setter
    def templates(self, templates):
        r"""Sets the templates of this ListTemplatesResponse.

        模板列表

        :param templates: The templates of this ListTemplatesResponse.
        :type templates: list[:class:`huaweicloudsdkrfs.v1.Template`]
        """
        self._templates = templates

    @property
    def page_info(self):
        r"""Gets the page_info of this ListTemplatesResponse.

        :return: The page_info of this ListTemplatesResponse.
        :rtype: :class:`huaweicloudsdkrfs.v1.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListTemplatesResponse.

        :param page_info: The page_info of this ListTemplatesResponse.
        :type page_info: :class:`huaweicloudsdkrfs.v1.PageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListTemplatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
