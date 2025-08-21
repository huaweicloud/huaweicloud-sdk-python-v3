# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RequiredAttributeDto:

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
        'is_required': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'is_required': 'is_required'
    }

    def __init__(self, name=None, is_required=None):
        r"""RequiredAttributeDto

        The model defined in huaweicloud sdk

        :param name: **参数解释：** 必填字段名称。 描述：Body 严重程度：Severity 指派给：AssigneeId 意见分类：ReviewCategories 意见模块：ReviewModules
        :type name: str
        :param is_required: **参数解释：** 是否必填。
        :type is_required: bool
        """
        
        

        self._name = None
        self._is_required = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if is_required is not None:
            self.is_required = is_required

    @property
    def name(self):
        r"""Gets the name of this RequiredAttributeDto.

        **参数解释：** 必填字段名称。 描述：Body 严重程度：Severity 指派给：AssigneeId 意见分类：ReviewCategories 意见模块：ReviewModules

        :return: The name of this RequiredAttributeDto.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this RequiredAttributeDto.

        **参数解释：** 必填字段名称。 描述：Body 严重程度：Severity 指派给：AssigneeId 意见分类：ReviewCategories 意见模块：ReviewModules

        :param name: The name of this RequiredAttributeDto.
        :type name: str
        """
        self._name = name

    @property
    def is_required(self):
        r"""Gets the is_required of this RequiredAttributeDto.

        **参数解释：** 是否必填。

        :return: The is_required of this RequiredAttributeDto.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        r"""Sets the is_required of this RequiredAttributeDto.

        **参数解释：** 是否必填。

        :param is_required: The is_required of this RequiredAttributeDto.
        :type is_required: bool
        """
        self._is_required = is_required

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
        if not isinstance(other, RequiredAttributeDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
