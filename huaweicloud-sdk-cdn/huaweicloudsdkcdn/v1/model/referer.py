# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Referer:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'referer_type': 'int',
        'referer_list': 'str',
        'include_empty': 'bool'
    }

    attribute_map = {
        'referer_type': 'referer_type',
        'referer_list': 'referer_list',
        'include_empty': 'include_empty'
    }

    def __init__(self, referer_type=None, referer_list=None, include_empty=None):
        r"""Referer

        The model defined in huaweicloud sdk

        :param referer_type: Referer类型。取值：0代表不设置Referer过滤；1代表黑名单；2代表白名单。默认取值为0。
        :type referer_type: int
        :param referer_list: 请输入域名或IP地址，以“;”进行分割，域名、IP地址可以混合输入，支持泛域名添加。输入的域名、IP地址总数不超过400个。当设置防盗链时，此项必填。
        :type referer_list: str
        :param include_empty: 是否包含空Referer。如果是黑名单并开启该选项，则表示无referer不允许访问。如果是白名单并开启该选项，则表示无referer允许访问。ttrue:包含，false：不包含，默认值false。
        :type include_empty: bool
        """
        
        

        self._referer_type = None
        self._referer_list = None
        self._include_empty = None
        self.discriminator = None

        self.referer_type = referer_type
        if referer_list is not None:
            self.referer_list = referer_list
        if include_empty is not None:
            self.include_empty = include_empty

    @property
    def referer_type(self):
        r"""Gets the referer_type of this Referer.

        Referer类型。取值：0代表不设置Referer过滤；1代表黑名单；2代表白名单。默认取值为0。

        :return: The referer_type of this Referer.
        :rtype: int
        """
        return self._referer_type

    @referer_type.setter
    def referer_type(self, referer_type):
        r"""Sets the referer_type of this Referer.

        Referer类型。取值：0代表不设置Referer过滤；1代表黑名单；2代表白名单。默认取值为0。

        :param referer_type: The referer_type of this Referer.
        :type referer_type: int
        """
        self._referer_type = referer_type

    @property
    def referer_list(self):
        r"""Gets the referer_list of this Referer.

        请输入域名或IP地址，以“;”进行分割，域名、IP地址可以混合输入，支持泛域名添加。输入的域名、IP地址总数不超过400个。当设置防盗链时，此项必填。

        :return: The referer_list of this Referer.
        :rtype: str
        """
        return self._referer_list

    @referer_list.setter
    def referer_list(self, referer_list):
        r"""Sets the referer_list of this Referer.

        请输入域名或IP地址，以“;”进行分割，域名、IP地址可以混合输入，支持泛域名添加。输入的域名、IP地址总数不超过400个。当设置防盗链时，此项必填。

        :param referer_list: The referer_list of this Referer.
        :type referer_list: str
        """
        self._referer_list = referer_list

    @property
    def include_empty(self):
        r"""Gets the include_empty of this Referer.

        是否包含空Referer。如果是黑名单并开启该选项，则表示无referer不允许访问。如果是白名单并开启该选项，则表示无referer允许访问。ttrue:包含，false：不包含，默认值false。

        :return: The include_empty of this Referer.
        :rtype: bool
        """
        return self._include_empty

    @include_empty.setter
    def include_empty(self, include_empty):
        r"""Sets the include_empty of this Referer.

        是否包含空Referer。如果是黑名单并开启该选项，则表示无referer不允许访问。如果是白名单并开启该选项，则表示无referer允许访问。ttrue:包含，false：不包含，默认值false。

        :param include_empty: The include_empty of this Referer.
        :type include_empty: bool
        """
        self._include_empty = include_empty

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
        if not isinstance(other, Referer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
