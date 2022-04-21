# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowApiVersionLinksParams:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'rel': 'str',
        'href': 'str'
    }

    attribute_map = {
        'rel': 'rel',
        'href': 'href'
    }

    def __init__(self, rel=None, href=None):
        """ShowApiVersionLinksParams

        The model defined in huaweicloud sdk

        :param rel: 链接的描述
        :type rel: str
        :param href: 版本号查询链接
        :type href: str
        """
        
        

        self._rel = None
        self._href = None
        self.discriminator = None

        self.rel = rel
        self.href = href

    @property
    def rel(self):
        """Gets the rel of this ShowApiVersionLinksParams.

        链接的描述

        :return: The rel of this ShowApiVersionLinksParams.
        :rtype: str
        """
        return self._rel

    @rel.setter
    def rel(self, rel):
        """Sets the rel of this ShowApiVersionLinksParams.

        链接的描述

        :param rel: The rel of this ShowApiVersionLinksParams.
        :type rel: str
        """
        self._rel = rel

    @property
    def href(self):
        """Gets the href of this ShowApiVersionLinksParams.

        版本号查询链接

        :return: The href of this ShowApiVersionLinksParams.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href):
        """Sets the href of this ShowApiVersionLinksParams.

        版本号查询链接

        :param href: The href of this ShowApiVersionLinksParams.
        :type href: str
        """
        self._href = href

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
        if not isinstance(other, ShowApiVersionLinksParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
