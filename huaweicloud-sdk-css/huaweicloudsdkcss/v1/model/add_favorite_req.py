# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddFavoriteReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'template': 'AddFavoriteReqTemplate'
    }

    attribute_map = {
        'name': 'name',
        'template': 'template'
    }

    def __init__(self, name=None, template=None):
        r"""AddFavoriteReq

        The model defined in huaweicloud sdk

        :param name: 配置文件名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。
        :type name: str
        :param template: 
        :type template: :class:`huaweicloudsdkcss.v1.AddFavoriteReqTemplate`
        """
        
        

        self._name = None
        self._template = None
        self.discriminator = None

        self.name = name
        self.template = template

    @property
    def name(self):
        r"""Gets the name of this AddFavoriteReq.

        配置文件名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :return: The name of this AddFavoriteReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddFavoriteReq.

        配置文件名称。4～32个字符，只能包含数字、字母、中划线和下划线，且必须以字母开头。

        :param name: The name of this AddFavoriteReq.
        :type name: str
        """
        self._name = name

    @property
    def template(self):
        r"""Gets the template of this AddFavoriteReq.

        :return: The template of this AddFavoriteReq.
        :rtype: :class:`huaweicloudsdkcss.v1.AddFavoriteReqTemplate`
        """
        return self._template

    @template.setter
    def template(self, template):
        r"""Sets the template of this AddFavoriteReq.

        :param template: The template of this AddFavoriteReq.
        :type template: :class:`huaweicloudsdkcss.v1.AddFavoriteReqTemplate`
        """
        self._template = template

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
        if not isinstance(other, AddFavoriteReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
