# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Params:

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
        'type': 'str',
        'required': 'bool',
        'constraints': 'list[Constraints]',
        'deletion': 'bool',
        'defaults': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'title': 'title',
        'type': 'type',
        'required': 'required',
        'constraints': 'constraints',
        'deletion': 'deletion',
        'defaults': 'defaults'
    }

    def __init__(self, name=None, title=None, type=None, required=None, constraints=None, deletion=None, defaults=None):
        r"""Params

        The model defined in huaweicloud sdk

        :param name: 参数名
        :type name: str
        :param title: 名称
        :type title: str
        :param type: 类型
        :type type: str
        :param required: 必填
        :type required: bool
        :param constraints: 简要构建信息列表
        :type constraints: list[:class:`huaweicloudsdkcodeartsbuild.v3.Constraints`]
        :param deletion: 删除
        :type deletion: bool
        :param defaults: 默认
        :type defaults: bool
        """
        
        

        self._name = None
        self._title = None
        self._type = None
        self._required = None
        self._constraints = None
        self._deletion = None
        self._defaults = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if title is not None:
            self.title = title
        if type is not None:
            self.type = type
        if required is not None:
            self.required = required
        if constraints is not None:
            self.constraints = constraints
        if deletion is not None:
            self.deletion = deletion
        if defaults is not None:
            self.defaults = defaults

    @property
    def name(self):
        r"""Gets the name of this Params.

        参数名

        :return: The name of this Params.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this Params.

        参数名

        :param name: The name of this Params.
        :type name: str
        """
        self._name = name

    @property
    def title(self):
        r"""Gets the title of this Params.

        名称

        :return: The title of this Params.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        r"""Sets the title of this Params.

        名称

        :param title: The title of this Params.
        :type title: str
        """
        self._title = title

    @property
    def type(self):
        r"""Gets the type of this Params.

        类型

        :return: The type of this Params.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this Params.

        类型

        :param type: The type of this Params.
        :type type: str
        """
        self._type = type

    @property
    def required(self):
        r"""Gets the required of this Params.

        必填

        :return: The required of this Params.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this Params.

        必填

        :param required: The required of this Params.
        :type required: bool
        """
        self._required = required

    @property
    def constraints(self):
        r"""Gets the constraints of this Params.

        简要构建信息列表

        :return: The constraints of this Params.
        :rtype: list[:class:`huaweicloudsdkcodeartsbuild.v3.Constraints`]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints):
        r"""Sets the constraints of this Params.

        简要构建信息列表

        :param constraints: The constraints of this Params.
        :type constraints: list[:class:`huaweicloudsdkcodeartsbuild.v3.Constraints`]
        """
        self._constraints = constraints

    @property
    def deletion(self):
        r"""Gets the deletion of this Params.

        删除

        :return: The deletion of this Params.
        :rtype: bool
        """
        return self._deletion

    @deletion.setter
    def deletion(self, deletion):
        r"""Sets the deletion of this Params.

        删除

        :param deletion: The deletion of this Params.
        :type deletion: bool
        """
        self._deletion = deletion

    @property
    def defaults(self):
        r"""Gets the defaults of this Params.

        默认

        :return: The defaults of this Params.
        :rtype: bool
        """
        return self._defaults

    @defaults.setter
    def defaults(self, defaults):
        r"""Sets the defaults of this Params.

        默认

        :param defaults: The defaults of this Params.
        :type defaults: bool
        """
        self._defaults = defaults

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
        if not isinstance(other, Params):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
