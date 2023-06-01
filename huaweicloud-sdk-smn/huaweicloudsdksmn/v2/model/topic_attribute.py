# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopicAttribute:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_policy': 'AccessPolicy',
        'introduction': 'str'
    }

    attribute_map = {
        'access_policy': 'access_policy',
        'introduction': 'introduction'
    }

    def __init__(self, access_policy=None, introduction=None):
        """TopicAttribute

        The model defined in huaweicloud sdk

        :param access_policy: 
        :type access_policy: :class:`huaweicloudsdksmn.v2.AccessPolicy`
        :param introduction: topic的简介
        :type introduction: str
        """
        
        

        self._access_policy = None
        self._introduction = None
        self.discriminator = None

        if access_policy is not None:
            self.access_policy = access_policy
        if introduction is not None:
            self.introduction = introduction

    @property
    def access_policy(self):
        """Gets the access_policy of this TopicAttribute.

        :return: The access_policy of this TopicAttribute.
        :rtype: :class:`huaweicloudsdksmn.v2.AccessPolicy`
        """
        return self._access_policy

    @access_policy.setter
    def access_policy(self, access_policy):
        """Sets the access_policy of this TopicAttribute.

        :param access_policy: The access_policy of this TopicAttribute.
        :type access_policy: :class:`huaweicloudsdksmn.v2.AccessPolicy`
        """
        self._access_policy = access_policy

    @property
    def introduction(self):
        """Gets the introduction of this TopicAttribute.

        topic的简介

        :return: The introduction of this TopicAttribute.
        :rtype: str
        """
        return self._introduction

    @introduction.setter
    def introduction(self, introduction):
        """Sets the introduction of this TopicAttribute.

        topic的简介

        :param introduction: The introduction of this TopicAttribute.
        :type introduction: str
        """
        self._introduction = introduction

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
        if not isinstance(other, TopicAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
