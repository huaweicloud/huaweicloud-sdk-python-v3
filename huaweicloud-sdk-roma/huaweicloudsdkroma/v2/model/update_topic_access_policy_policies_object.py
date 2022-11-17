# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateTopicAccessPolicyPoliciesObject:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'access_policy': 'str',
        'owner': 'bool',
        'tag': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'access_policy': 'access_policy',
        'owner': 'owner',
        'tag': 'tag'
    }

    def __init__(self, app_id=None, app_name=None, access_policy=None, owner=None, tag=None):
        """UpdateTopicAccessPolicyPoliciesObject

        The model defined in huaweicloud sdk

        :param app_id: 集成应用key。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param access_policy: 权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅
        :type access_policy: str
        :param owner: 是否为创建topic时所选择的应用。  默认为false。
        :type owner: bool
        :param tag: 权限类型对应的标签。  当权限类型是all时，发布和订阅的标签用符号“&amp;”隔开。  当有多个标签时，标签用符号“||”隔开。
        :type tag: str
        """
        
        

        self._app_id = None
        self._app_name = None
        self._access_policy = None
        self._owner = None
        self._tag = None
        self.discriminator = None

        self.app_id = app_id
        self.app_name = app_name
        self.access_policy = access_policy
        if owner is not None:
            self.owner = owner
        if tag is not None:
            self.tag = tag

    @property
    def app_id(self):
        """Gets the app_id of this UpdateTopicAccessPolicyPoliciesObject.

        集成应用key。

        :return: The app_id of this UpdateTopicAccessPolicyPoliciesObject.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this UpdateTopicAccessPolicyPoliciesObject.

        集成应用key。

        :param app_id: The app_id of this UpdateTopicAccessPolicyPoliciesObject.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this UpdateTopicAccessPolicyPoliciesObject.

        应用名称。

        :return: The app_name of this UpdateTopicAccessPolicyPoliciesObject.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this UpdateTopicAccessPolicyPoliciesObject.

        应用名称。

        :param app_name: The app_name of this UpdateTopicAccessPolicyPoliciesObject.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def access_policy(self):
        """Gets the access_policy of this UpdateTopicAccessPolicyPoliciesObject.

        权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅

        :return: The access_policy of this UpdateTopicAccessPolicyPoliciesObject.
        :rtype: str
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this UpdateTopicAccessPolicyPoliciesObject.

        权限类型。   - all：发布+订阅   - pub：发布   - sub：订阅

        :param access_policy: The access_policy of this UpdateTopicAccessPolicyPoliciesObject.
        :type access_policy: str
        """
        self._access_policy = access_policy

    @property
    def owner(self):
        """Gets the owner of this UpdateTopicAccessPolicyPoliciesObject.

        是否为创建topic时所选择的应用。  默认为false。

        :return: The owner of this UpdateTopicAccessPolicyPoliciesObject.
        :rtype: bool
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """Sets the owner of this UpdateTopicAccessPolicyPoliciesObject.

        是否为创建topic时所选择的应用。  默认为false。

        :param owner: The owner of this UpdateTopicAccessPolicyPoliciesObject.
        :type owner: bool
        """
        self._owner = owner

    @property
    def tag(self):
        """Gets the tag of this UpdateTopicAccessPolicyPoliciesObject.

        权限类型对应的标签。  当权限类型是all时，发布和订阅的标签用符号“&”隔开。  当有多个标签时，标签用符号“||”隔开。

        :return: The tag of this UpdateTopicAccessPolicyPoliciesObject.
        :rtype: str
        """
        return self._tag

    @tag.setter
    def tag(self, tag):
        """Sets the tag of this UpdateTopicAccessPolicyPoliciesObject.

        权限类型对应的标签。  当权限类型是all时，发布和订阅的标签用符号“&”隔开。  当有多个标签时，标签用符号“||”隔开。

        :param tag: The tag of this UpdateTopicAccessPolicyPoliciesObject.
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
        if not isinstance(other, UpdateTopicAccessPolicyPoliciesObject):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
