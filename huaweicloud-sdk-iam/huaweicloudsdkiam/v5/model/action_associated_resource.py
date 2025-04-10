# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ActionAssociatedResource:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'urn_template': 'str',
        'required': 'bool',
        'condition_keys': 'list[str]'
    }

    attribute_map = {
        'urn_template': 'urn_template',
        'required': 'required',
        'condition_keys': 'condition_keys'
    }

    def __init__(self, urn_template=None, required=None, condition_keys=None):
        r"""ActionAssociatedResource

        The model defined in huaweicloud sdk

        :param urn_template: 统一资源名称模板，表示可以通过这类资源的统一资源名称对该授权项进行资源粒度的授权。
        :type urn_template: str
        :param required: 标识该资源类型是否是这个授权项必选的，即授权项一定涉及对这类资源的操作；例如subnet是vpc:subnets:get的必选资源类型；而ou是organizations::tagResource的可选资源类型，因为organizations::tagResource操作的资源还可能是account或者policy。
        :type required: bool
        :param condition_keys: 针对该授权项和资源的服务自定义条件属性以及部分全局属性，只有授权项和资源同时匹配时才会生效。
        :type condition_keys: list[str]
        """
        
        

        self._urn_template = None
        self._required = None
        self._condition_keys = None
        self.discriminator = None

        self.urn_template = urn_template
        self.required = required
        if condition_keys is not None:
            self.condition_keys = condition_keys

    @property
    def urn_template(self):
        r"""Gets the urn_template of this ActionAssociatedResource.

        统一资源名称模板，表示可以通过这类资源的统一资源名称对该授权项进行资源粒度的授权。

        :return: The urn_template of this ActionAssociatedResource.
        :rtype: str
        """
        return self._urn_template

    @urn_template.setter
    def urn_template(self, urn_template):
        r"""Sets the urn_template of this ActionAssociatedResource.

        统一资源名称模板，表示可以通过这类资源的统一资源名称对该授权项进行资源粒度的授权。

        :param urn_template: The urn_template of this ActionAssociatedResource.
        :type urn_template: str
        """
        self._urn_template = urn_template

    @property
    def required(self):
        r"""Gets the required of this ActionAssociatedResource.

        标识该资源类型是否是这个授权项必选的，即授权项一定涉及对这类资源的操作；例如subnet是vpc:subnets:get的必选资源类型；而ou是organizations::tagResource的可选资源类型，因为organizations::tagResource操作的资源还可能是account或者policy。

        :return: The required of this ActionAssociatedResource.
        :rtype: bool
        """
        return self._required

    @required.setter
    def required(self, required):
        r"""Sets the required of this ActionAssociatedResource.

        标识该资源类型是否是这个授权项必选的，即授权项一定涉及对这类资源的操作；例如subnet是vpc:subnets:get的必选资源类型；而ou是organizations::tagResource的可选资源类型，因为organizations::tagResource操作的资源还可能是account或者policy。

        :param required: The required of this ActionAssociatedResource.
        :type required: bool
        """
        self._required = required

    @property
    def condition_keys(self):
        r"""Gets the condition_keys of this ActionAssociatedResource.

        针对该授权项和资源的服务自定义条件属性以及部分全局属性，只有授权项和资源同时匹配时才会生效。

        :return: The condition_keys of this ActionAssociatedResource.
        :rtype: list[str]
        """
        return self._condition_keys

    @condition_keys.setter
    def condition_keys(self, condition_keys):
        r"""Sets the condition_keys of this ActionAssociatedResource.

        针对该授权项和资源的服务自定义条件属性以及部分全局属性，只有授权项和资源同时匹配时才会生效。

        :param condition_keys: The condition_keys of this ActionAssociatedResource.
        :type condition_keys: list[str]
        """
        self._condition_keys = condition_keys

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
        if not isinstance(other, ActionAssociatedResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
