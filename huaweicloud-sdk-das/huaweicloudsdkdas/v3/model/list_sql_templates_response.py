# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSqlTemplatesResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'tpl_list': 'list[Tpl]'
    }

    attribute_map = {
        'tpl_list': 'tpl_list'
    }

    def __init__(self, tpl_list=None):
        r"""ListSqlTemplatesResponse

        The model defined in huaweicloud sdk

        :param tpl_list: SQL模板列表
        :type tpl_list: list[:class:`huaweicloudsdkdas.v3.Tpl`]
        """
        
        super().__init__()

        self._tpl_list = None
        self.discriminator = None

        if tpl_list is not None:
            self.tpl_list = tpl_list

    @property
    def tpl_list(self):
        r"""Gets the tpl_list of this ListSqlTemplatesResponse.

        SQL模板列表

        :return: The tpl_list of this ListSqlTemplatesResponse.
        :rtype: list[:class:`huaweicloudsdkdas.v3.Tpl`]
        """
        return self._tpl_list

    @tpl_list.setter
    def tpl_list(self, tpl_list):
        r"""Sets the tpl_list of this ListSqlTemplatesResponse.

        SQL模板列表

        :param tpl_list: The tpl_list of this ListSqlTemplatesResponse.
        :type tpl_list: list[:class:`huaweicloudsdkdas.v3.Tpl`]
        """
        self._tpl_list = tpl_list

    def to_dict(self):
        import warnings
        warnings.warn("ListSqlTemplatesResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListSqlTemplatesResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
