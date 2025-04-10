# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAuthorizationSchemaV5Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'version': 'str',
        'actions': 'list[Action]',
        'resources': 'list[Resource]',
        'conditions': 'list[Condition]',
        'operations': 'list[Operation]'
    }

    attribute_map = {
        'version': 'version',
        'actions': 'actions',
        'resources': 'resources',
        'conditions': 'conditions',
        'operations': 'operations'
    }

    def __init__(self, version=None, actions=None, resources=None, conditions=None, operations=None):
        r"""GetAuthorizationSchemaV5Response

        The model defined in huaweicloud sdk

        :param version: 服务授权概要的版本号。
        :type version: str
        :param actions: 云服务支持的授权项列表。
        :type actions: list[:class:`huaweicloudsdkiam.v5.Action`]
        :param resources: 云服务支持的资源列表。
        :type resources: list[:class:`huaweicloudsdkiam.v5.Resource`]
        :param conditions: 云服务支持的条件键列表。
        :type conditions: list[:class:`huaweicloudsdkiam.v5.Condition`]
        :param operations: 云服务支持的操作列表。
        :type operations: list[:class:`huaweicloudsdkiam.v5.Operation`]
        """
        
        super(GetAuthorizationSchemaV5Response, self).__init__()

        self._version = None
        self._actions = None
        self._resources = None
        self._conditions = None
        self._operations = None
        self.discriminator = None

        if version is not None:
            self.version = version
        if actions is not None:
            self.actions = actions
        if resources is not None:
            self.resources = resources
        if conditions is not None:
            self.conditions = conditions
        if operations is not None:
            self.operations = operations

    @property
    def version(self):
        r"""Gets the version of this GetAuthorizationSchemaV5Response.

        服务授权概要的版本号。

        :return: The version of this GetAuthorizationSchemaV5Response.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this GetAuthorizationSchemaV5Response.

        服务授权概要的版本号。

        :param version: The version of this GetAuthorizationSchemaV5Response.
        :type version: str
        """
        self._version = version

    @property
    def actions(self):
        r"""Gets the actions of this GetAuthorizationSchemaV5Response.

        云服务支持的授权项列表。

        :return: The actions of this GetAuthorizationSchemaV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.Action`]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        r"""Sets the actions of this GetAuthorizationSchemaV5Response.

        云服务支持的授权项列表。

        :param actions: The actions of this GetAuthorizationSchemaV5Response.
        :type actions: list[:class:`huaweicloudsdkiam.v5.Action`]
        """
        self._actions = actions

    @property
    def resources(self):
        r"""Gets the resources of this GetAuthorizationSchemaV5Response.

        云服务支持的资源列表。

        :return: The resources of this GetAuthorizationSchemaV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.Resource`]
        """
        return self._resources

    @resources.setter
    def resources(self, resources):
        r"""Sets the resources of this GetAuthorizationSchemaV5Response.

        云服务支持的资源列表。

        :param resources: The resources of this GetAuthorizationSchemaV5Response.
        :type resources: list[:class:`huaweicloudsdkiam.v5.Resource`]
        """
        self._resources = resources

    @property
    def conditions(self):
        r"""Gets the conditions of this GetAuthorizationSchemaV5Response.

        云服务支持的条件键列表。

        :return: The conditions of this GetAuthorizationSchemaV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.Condition`]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        r"""Sets the conditions of this GetAuthorizationSchemaV5Response.

        云服务支持的条件键列表。

        :param conditions: The conditions of this GetAuthorizationSchemaV5Response.
        :type conditions: list[:class:`huaweicloudsdkiam.v5.Condition`]
        """
        self._conditions = conditions

    @property
    def operations(self):
        r"""Gets the operations of this GetAuthorizationSchemaV5Response.

        云服务支持的操作列表。

        :return: The operations of this GetAuthorizationSchemaV5Response.
        :rtype: list[:class:`huaweicloudsdkiam.v5.Operation`]
        """
        return self._operations

    @operations.setter
    def operations(self, operations):
        r"""Sets the operations of this GetAuthorizationSchemaV5Response.

        云服务支持的操作列表。

        :param operations: The operations of this GetAuthorizationSchemaV5Response.
        :type operations: list[:class:`huaweicloudsdkiam.v5.Operation`]
        """
        self._operations = operations

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
        if not isinstance(other, GetAuthorizationSchemaV5Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
