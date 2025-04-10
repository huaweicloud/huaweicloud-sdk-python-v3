# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowMqsInstanceTopicAccessPolicyRespPolicies:

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
        'access_policy': 'str',
        'app_name': 'str',
        'tag': 'str'
    }

    attribute_map = {
        'owner': 'owner',
        'user_name': 'user_name',
        'access_policy': 'access_policy',
        'app_name': 'app_name',
        'tag': 'tag'
    }

    def __init__(self, owner=None, user_name=None, access_policy=None, app_name=None, tag=None):
        r"""ShowMqsInstanceTopicAccessPolicyRespPolicies

        The model defined in huaweicloud sdk

        :param owner: 是否为创建topic时所选择的应用。
        :type owner: bool
        :param user_name: 应用ID。
        :type user_name: str
        :param access_policy: 权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅
        :type access_policy: str
        :param app_name: 应用名称。
        :type app_name: str
        :param tag: 权限类型对应的标签。
        :type tag: str
        """
        
        

        self._owner = None
        self._user_name = None
        self._access_policy = None
        self._app_name = None
        self._tag = None
        self.discriminator = None

        if owner is not None:
            self.owner = owner
        if user_name is not None:
            self.user_name = user_name
        if access_policy is not None:
            self.access_policy = access_policy
        if app_name is not None:
            self.app_name = app_name
        if tag is not None:
            self.tag = tag

    @property
    def owner(self):
        r"""Gets the owner of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        是否为创建topic时所选择的应用。

        :return: The owner of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        r"""Sets the owner of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        是否为创建topic时所选择的应用。

        :param owner: The owner of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :type owner: bool
        """
        self._owner = owner

    @property
    def user_name(self):
        r"""Gets the user_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        应用ID。

        :return: The user_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._user_name

    @user_name.setter
    def user_name(self, user_name):
        r"""Sets the user_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        应用ID。

        :param user_name: The user_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :type user_name: str
        """
        self._user_name = user_name

    @property
    def access_policy(self):
        r"""Gets the access_policy of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅

        :return: The access_policy of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        r"""Sets the access_policy of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅

        :param access_policy: The access_policy of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def app_name(self):
        r"""Gets the app_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        应用名称。

        :return: The app_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        r"""Sets the app_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        应用名称。

        :param app_name: The app_name of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def tag(self):
        r"""Gets the tag of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        权限类型对应的标签。

        :return: The tag of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        r"""Sets the tag of this ShowMqsInstanceTopicAccessPolicyRespPolicies.

        权限类型对应的标签。

        :param tag: The tag of this ShowMqsInstanceTopicAccessPolicyRespPolicies.
        :type tag: str
        """
        self._tag = tag

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
        if not isinstance(other, ShowMqsInstanceTopicAccessPolicyRespPolicies):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
