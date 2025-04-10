# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAliasResponseBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'aliases': 'list[AliasEntity]',
        'page_info': 'PageInfo'
    }

    attribute_map = {
        'aliases': 'aliases',
        'page_info': 'page_info'
    }

    def __init__(self, aliases=None, page_info=None):
        r"""ListAliasResponseBody

        The model defined in huaweicloud sdk

        :param aliases: 密钥关联的所有别名
        :type aliases: list[:class:`huaweicloudsdkkms.v2.AliasEntity`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkkms.v2.PageInfo`
        """
        
        

        self._aliases = None
        self._page_info = None
        self.discriminator = None

        self.aliases = aliases
        self.page_info = page_info

    @property
    def aliases(self):
        r"""Gets the aliases of this ListAliasResponseBody.

        密钥关联的所有别名

        :return: The aliases of this ListAliasResponseBody.
        :rtype: list[:class:`huaweicloudsdkkms.v2.AliasEntity`]
        """
        return self._aliases

    @aliases.setter
    def aliases(self, aliases):
        r"""Sets the aliases of this ListAliasResponseBody.

        密钥关联的所有别名

        :param aliases: The aliases of this ListAliasResponseBody.
        :type aliases: list[:class:`huaweicloudsdkkms.v2.AliasEntity`]
        """
        self._aliases = aliases

    @property
    def page_info(self):
        r"""Gets the page_info of this ListAliasResponseBody.

        :return: The page_info of this ListAliasResponseBody.
        :rtype: :class:`huaweicloudsdkkms.v2.PageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListAliasResponseBody.

        :param page_info: The page_info of this ListAliasResponseBody.
        :type page_info: :class:`huaweicloudsdkkms.v2.PageInfo`
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
        if not isinstance(other, ListAliasResponseBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
