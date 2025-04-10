# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CheckResourceRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'resource': 'CheckResourceInfo'
    }

    attribute_map = {
        'action': 'action',
        'resource': 'resource'
    }

    def __init__(self, action=None, resource=None):
        r"""CheckResourceRequestBody

        The model defined in huaweicloud sdk

        :param action: 校验类型。 - createInstance：校验创建实例。 - createReadonlyNode：校验创建只读节点。 - resizeFlavor：校验规格变更。
        :type action: str
        :param resource: 
        :type resource: :class:`huaweicloudsdkgaussdb.v3.CheckResourceInfo`
        """
        
        

        self._action = None
        self._resource = None
        self.discriminator = None

        self.action = action
        self.resource = resource

    @property
    def action(self):
        r"""Gets the action of this CheckResourceRequestBody.

        校验类型。 - createInstance：校验创建实例。 - createReadonlyNode：校验创建只读节点。 - resizeFlavor：校验规格变更。

        :return: The action of this CheckResourceRequestBody.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this CheckResourceRequestBody.

        校验类型。 - createInstance：校验创建实例。 - createReadonlyNode：校验创建只读节点。 - resizeFlavor：校验规格变更。

        :param action: The action of this CheckResourceRequestBody.
        :type action: str
        """
        self._action = action

    @property
    def resource(self):
        r"""Gets the resource of this CheckResourceRequestBody.

        :return: The resource of this CheckResourceRequestBody.
        :rtype: :class:`huaweicloudsdkgaussdb.v3.CheckResourceInfo`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this CheckResourceRequestBody.

        :param resource: The resource of this CheckResourceRequestBody.
        :type resource: :class:`huaweicloudsdkgaussdb.v3.CheckResourceInfo`
        """
        self._resource = resource

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
        if not isinstance(other, CheckResourceRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
