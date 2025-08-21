# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateApplicationViewRequestBodyComponentList:

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
        'parent_name': 'str'
    }

    attribute_map = {
        'name': 'name',
        'parent_name': 'parent_name'
    }

    def __init__(self, name=None, parent_name=None):
        r"""BatchCreateApplicationViewRequestBodyComponentList

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 组件名称。 **约束限制：** 不涉及。 **取值范围：** 由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。
        :type name: str
        :param parent_name: **参数解释：** 父节点名称。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度3到50个字符。 **默认取值：** 不涉及。
        :type parent_name: str
        """
        
        

        self._name = None
        self._parent_name = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if parent_name is not None:
            self.parent_name = parent_name

    @property
    def name(self):
        r"""Gets the name of this BatchCreateApplicationViewRequestBodyComponentList.

        **参数解释：** 组件名称。 **约束限制：** 不涉及。 **取值范围：** 由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :return: The name of this BatchCreateApplicationViewRequestBodyComponentList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this BatchCreateApplicationViewRequestBodyComponentList.

        **参数解释：** 组件名称。 **约束限制：** 不涉及。 **取值范围：** 由中文、英文字母、数字、中划线、下划线组成，长度在3~50个字符之间。 **默认取值：** 不涉及。

        :param name: The name of this BatchCreateApplicationViewRequestBodyComponentList.
        :type name: str
        """
        self._name = name

    @property
    def parent_name(self):
        r"""Gets the parent_name of this BatchCreateApplicationViewRequestBodyComponentList.

        **参数解释：** 父节点名称。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度3到50个字符。 **默认取值：** 不涉及。

        :return: The parent_name of this BatchCreateApplicationViewRequestBodyComponentList.
        :rtype: str
        """
        return self._parent_name

    @parent_name.setter
    def parent_name(self, parent_name):
        r"""Sets the parent_name of this BatchCreateApplicationViewRequestBodyComponentList.

        **参数解释：** 父节点名称。 **约束限制：** 不涉及。 **取值范围：** 字符串，长度3到50个字符。 **默认取值：** 不涉及。

        :param parent_name: The parent_name of this BatchCreateApplicationViewRequestBodyComponentList.
        :type parent_name: str
        """
        self._parent_name = parent_name

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
        if not isinstance(other, BatchCreateApplicationViewRequestBodyComponentList):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
