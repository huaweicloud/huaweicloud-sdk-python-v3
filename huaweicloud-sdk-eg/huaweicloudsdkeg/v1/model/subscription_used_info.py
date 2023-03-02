# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SubscriptionUsedInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'owner': 'str',
        'description': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'owner': 'owner',
        'description': 'description'
    }

    def __init__(self, resource_id=None, owner=None, description=None):
        """SubscriptionUsedInfo

        The model defined in huaweicloud sdk

        :param resource_id: 关联资源ID
        :type resource_id: str
        :param owner: 管理租户账号
        :type owner: str
        :param description: 描述
        :type description: str
        """
        
        

        self._resource_id = None
        self._owner = None
        self._description = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if owner is not None:
            self.owner = owner
        if description is not None:
            self.description = description

    @property
    def resource_id(self):
        """Gets the resource_id of this SubscriptionUsedInfo.

        关联资源ID

        :return: The resource_id of this SubscriptionUsedInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """Sets the resource_id of this SubscriptionUsedInfo.

        关联资源ID

        :param resource_id: The resource_id of this SubscriptionUsedInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def owner(self):
        """Gets the owner of this SubscriptionUsedInfo.

        管理租户账号

        :return: The owner of this SubscriptionUsedInfo.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this SubscriptionUsedInfo.

        管理租户账号

        :param owner: The owner of this SubscriptionUsedInfo.
        :type owner: str
        """
        self._owner = owner

    @property
    def description(self):
        """Gets the description of this SubscriptionUsedInfo.

        描述

        :return: The description of this SubscriptionUsedInfo.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionUsedInfo.

        描述

        :param description: The description of this SubscriptionUsedInfo.
        :type description: str
        """
        self._description = description

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
        if not isinstance(other, SubscriptionUsedInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
