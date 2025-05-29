# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BuildParams:

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
        'title': 'str',
        'params': 'list[Params]'
    }

    attribute_map = {
        'name': 'name',
        'title': 'title',
        'params': 'params'
    }

    def __init__(self, name=None, title=None, params=None):
        r"""BuildParams

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param title: 名称
        :type title: str
        :param params: 简要构建信息列表
        :type params: list[:class:`huaweicloudsdkcodeartsbuild.v3.Params`]
        """
        
        

        self._name = None
        self._title = None
        self._params = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if params is not None:
            self.params = params

    @property
    def name(self):
        r"""Gets the name of this BuildParams.

        参数名

        :return: The name of this BuildParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BuildParams.

        参数名

        :param name: The name of this BuildParams.
        :type name: str
        """
        self._name = name

    @property
    def title(self):
        r"""Gets the title of this BuildParams.

        名称

        :return: The title of this BuildParams.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this BuildParams.

        名称

        :param title: The title of this BuildParams.
        :type title: str
        """
        self._title = title

    @property
    def params(self):
        r"""Gets the params of this BuildParams.

        简要构建信息列表

        :return: The params of this BuildParams.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Params`]
        """
        return self._params

    @params.setter
    def params(self, params):
        r"""Sets the params of this BuildParams.

        简要构建信息列表

        :param params: The params of this BuildParams.
        :type params: list[:class:`huaweicloudsdkcodeartsbuild.v3.Params`]
        """
        self._params = params

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
        if not isinstance(other, BuildParams):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
