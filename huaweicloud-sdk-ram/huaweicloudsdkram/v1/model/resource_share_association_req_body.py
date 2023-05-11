# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourceShareAssociationReqBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'principals': 'list[str]',
        'resource_urns': 'list[str]'
    }

    attribute_map = {
        'principals': 'principals',
        'resource_urns': 'resource_urns'
    }

    def __init__(self, principals=None, resource_urns=None):
        """ResourceShareAssociationReqBody

        The model defined in huaweicloud sdk

        :param principals: 指定与资源共享实例关联的一个或多个资源使用者的列表。
        :type principals: list[str]
        :param resource_urns: 指定与资源共享实例关联的一个或多个共享资源URN的列表。
        :type resource_urns: list[str]
        """
        
        

        self._principals = None
        self._resource_urns = None
        self.discriminator = None

        if principals is not None:
            self.principals = principals
        if resource_urns is not None:
            self.resource_urns = resource_urns

    @property
    def principals(self):
        """Gets the principals of this ResourceShareAssociationReqBody.

        指定与资源共享实例关联的一个或多个资源使用者的列表。

        :return: The principals of this ResourceShareAssociationReqBody.
        :rtype: list[str]
        """
        return self._principals

    @principals.setter
    def principals(self, principals):
        """Sets the principals of this ResourceShareAssociationReqBody.

        指定与资源共享实例关联的一个或多个资源使用者的列表。

        :param principals: The principals of this ResourceShareAssociationReqBody.
        :type principals: list[str]
        """
        self._principals = principals

    @property
    def resource_urns(self):
        """Gets the resource_urns of this ResourceShareAssociationReqBody.

        指定与资源共享实例关联的一个或多个共享资源URN的列表。

        :return: The resource_urns of this ResourceShareAssociationReqBody.
        :rtype: list[str]
        """
        return self._resource_urns

    @resource_urns.setter
    def resource_urns(self, resource_urns):
        """Sets the resource_urns of this ResourceShareAssociationReqBody.

        指定与资源共享实例关联的一个或多个共享资源URN的列表。

        :param resource_urns: The resource_urns of this ResourceShareAssociationReqBody.
        :type resource_urns: list[str]
        """
        self._resource_urns = resource_urns

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
        if not isinstance(other, ResourceShareAssociationReqBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
