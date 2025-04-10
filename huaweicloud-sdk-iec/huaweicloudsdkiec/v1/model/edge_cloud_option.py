# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EdgeCloudOption:

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
        'id': 'str',
        'description': 'str',
        'coverage': 'Coverage',
        'stack': 'Stack'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'description': 'description',
        'coverage': 'coverage',
        'stack': 'stack'
    }

    def __init__(self, name=None, id=None, description=None, coverage=None, stack=None):
        r"""EdgeCloudOption

        The model defined in huaweicloud sdk

        :param name: 边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。
        :type name: str
        :param id: 已有边缘业务ID，该参数用于扩容边缘业务场景。 &gt;-  id与name不可同时为空，同时有值时部署计划无效； - 通过id扩容场景要求区域分布层级与原边缘业务一致； - 区域分布层级为站点级的边缘业务不支持扩容。
        :type id: str
        :param description: 描述，缺省值为空字符串。
        :type description: str
        :param coverage: 
        :type coverage: :class:`huaweicloudsdkiec.v1.Coverage`
        :param stack: 
        :type stack: :class:`huaweicloudsdkiec.v1.Stack`
        """
        
        

        self._name = None
        self._id = None
        self._description = None
        self._coverage = None
        self._stack = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if description is not None:
            self.description = description
        self.coverage = coverage
        self.stack = stack

    @property
    def name(self):
        r"""Gets the name of this EdgeCloudOption.

        边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。

        :return: The name of this EdgeCloudOption.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this EdgeCloudOption.

        边缘业务名称。 取值范围：只能由中文字符、大小写英文字母、数字及中划线、下划线组成，且长度为[1-32]个字符。

        :param name: The name of this EdgeCloudOption.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        r"""Gets the id of this EdgeCloudOption.

        已有边缘业务ID，该参数用于扩容边缘业务场景。 >-  id与name不可同时为空，同时有值时部署计划无效； - 通过id扩容场景要求区域分布层级与原边缘业务一致； - 区域分布层级为站点级的边缘业务不支持扩容。

        :return: The id of this EdgeCloudOption.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this EdgeCloudOption.

        已有边缘业务ID，该参数用于扩容边缘业务场景。 >-  id与name不可同时为空，同时有值时部署计划无效； - 通过id扩容场景要求区域分布层级与原边缘业务一致； - 区域分布层级为站点级的边缘业务不支持扩容。

        :param id: The id of this EdgeCloudOption.
        :type id: str
        """
        self._id = id

    @property
    def description(self):
        r"""Gets the description of this EdgeCloudOption.

        描述，缺省值为空字符串。

        :return: The description of this EdgeCloudOption.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        r"""Sets the description of this EdgeCloudOption.

        描述，缺省值为空字符串。

        :param description: The description of this EdgeCloudOption.
        :type description: str
        """
        self._description = description

    @property
    def coverage(self):
        r"""Gets the coverage of this EdgeCloudOption.

        :return: The coverage of this EdgeCloudOption.
        :rtype: :class:`huaweicloudsdkiec.v1.Coverage`
        """
        return self._coverage

    @coverage.setter
    def coverage(self, coverage):
        r"""Sets the coverage of this EdgeCloudOption.

        :param coverage: The coverage of this EdgeCloudOption.
        :type coverage: :class:`huaweicloudsdkiec.v1.Coverage`
        """
        self._coverage = coverage

    @property
    def stack(self):
        r"""Gets the stack of this EdgeCloudOption.

        :return: The stack of this EdgeCloudOption.
        :rtype: :class:`huaweicloudsdkiec.v1.Stack`
        """
        return self._stack

    @stack.setter
    def stack(self, stack):
        r"""Sets the stack of this EdgeCloudOption.

        :param stack: The stack of this EdgeCloudOption.
        :type stack: :class:`huaweicloudsdkiec.v1.Stack`
        """
        self._stack = stack

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
        if not isinstance(other, EdgeCloudOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
