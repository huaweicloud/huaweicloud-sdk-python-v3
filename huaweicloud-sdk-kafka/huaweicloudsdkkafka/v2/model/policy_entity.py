# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PolicyEntity:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'owner': 'bool',
        'user_name': 'str',
        'access_policy': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'user_name': 'user_name',
        'access_policy': 'access_policy'
    }

    def __init__(self, owner=None, user_name=None, access_policy=None):
        """PolicyEntity

        The model defined in huaweicloud sdk

        :param owner: 是否为创建topic时所选择的用户。
        :type owner: bool
        :param user_name: 用户名。
        :type user_name: str
        :param access_policy: 权限类型。 - all：拥有发布、订阅权限; - pub：拥有发布权限; - sub：拥有订阅权限。
        :type access_policy: str
        """
        
        

        self._owner = None
        self._user_name = None
        self._access_policy = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if user_name is not None:
            self.user_name = user_name
        if access_policy is not None:
            self.access_policy = access_policy

    @property
    def owner(self):
        """Gets the owner of this PolicyEntity.

        是否为创建topic时所选择的用户。

        :return: The owner of this PolicyEntity.
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this PolicyEntity.

        是否为创建topic时所选择的用户。

        :param owner: The owner of this PolicyEntity.
        :type owner: bool
        """
        self._owner = owner

    @property
    def user_name(self):
        """Gets the user_name of this PolicyEntity.

        用户名。

        :return: The user_name of this PolicyEntity.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        """Sets the user_name of this PolicyEntity.

        用户名。

        :param user_name: The user_name of this PolicyEntity.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def access_policy(self):
        """Gets the access_policy of this PolicyEntity.

        权限类型。 - all：拥有发布、订阅权限; - pub：拥有发布权限; - sub：拥有订阅权限。

        :return: The access_policy of this PolicyEntity.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this PolicyEntity.

        权限类型。 - all：拥有发布、订阅权限; - pub：拥有发布权限; - sub：拥有订阅权限。

        :param access_policy: The access_policy of this PolicyEntity.
        :type access_policy: str
        """
        self._access_policy = access_policy

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
        if not isinstance(other, PolicyEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
