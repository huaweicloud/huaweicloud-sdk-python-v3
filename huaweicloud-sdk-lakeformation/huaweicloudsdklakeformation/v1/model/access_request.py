# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AccessRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource': 'ResourceInput',
        'principal': 'list[Principal]',
        'action': 'str'
    }

    attribute_map = {
        'resource': 'resource',
        'principal': 'principal',
        'action': 'action'
    }

    def __init__(self, resource=None, principal=None, action=None):
        r"""AccessRequest

        The model defined in huaweicloud sdk

        :param resource: 
        :type resource: :class:`huaweicloudsdklakeformation.v1.ResourceInput`
        :param principal: 授权主体信息
        :type principal: list[:class:`huaweicloudsdklakeformation.v1.Principal`]
        :param action: 权限信息,ALL,CREATE,ALTER,DROP,DESCRIBE,EXEC,CREATE_DATABASE,LIST_DATABASE,CREATE_TABLE,LIST_TABLE,CREATE_FUNC,LIST_FUNC,REGISTER_MODEL,LIST_MODEL,INSERT,UPDATE,DELETE,SELECT,READ,WRITE,OPERATE,USE
        :type action: str
        """
        
        

        self._resource = None
        self._principal = None
        self._action = None
        self.discriminator = None

        self.resource = resource
        self.principal = principal
        self.action = action

    @property
    def resource(self):
        r"""Gets the resource of this AccessRequest.

        :return: The resource of this AccessRequest.
        :rtype: :class:`huaweicloudsdklakeformation.v1.ResourceInput`
        """
        return self._resource

    @resource.setter
    def resource(self, resource):
        r"""Sets the resource of this AccessRequest.

        :param resource: The resource of this AccessRequest.
        :type resource: :class:`huaweicloudsdklakeformation.v1.ResourceInput`
        """
        self._resource = resource

    @property
    def principal(self):
        r"""Gets the principal of this AccessRequest.

        授权主体信息

        :return: The principal of this AccessRequest.
        :rtype: list[:class:`huaweicloudsdklakeformation.v1.Principal`]
        """
        return self._principal

    @principal.setter
    def principal(self, principal):
        r"""Sets the principal of this AccessRequest.

        授权主体信息

        :param principal: The principal of this AccessRequest.
        :type principal: list[:class:`huaweicloudsdklakeformation.v1.Principal`]
        """
        self._principal = principal

    @property
    def action(self):
        r"""Gets the action of this AccessRequest.

        权限信息,ALL,CREATE,ALTER,DROP,DESCRIBE,EXEC,CREATE_DATABASE,LIST_DATABASE,CREATE_TABLE,LIST_TABLE,CREATE_FUNC,LIST_FUNC,REGISTER_MODEL,LIST_MODEL,INSERT,UPDATE,DELETE,SELECT,READ,WRITE,OPERATE,USE

        :return: The action of this AccessRequest.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this AccessRequest.

        权限信息,ALL,CREATE,ALTER,DROP,DESCRIBE,EXEC,CREATE_DATABASE,LIST_DATABASE,CREATE_TABLE,LIST_TABLE,CREATE_FUNC,LIST_FUNC,REGISTER_MODEL,LIST_MODEL,INSERT,UPDATE,DELETE,SELECT,READ,WRITE,OPERATE,USE

        :param action: The action of this AccessRequest.
        :type action: str
        """
        self._action = action

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
        if not isinstance(other, AccessRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
