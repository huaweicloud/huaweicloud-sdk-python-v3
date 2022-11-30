# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmnInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'smn_notified_content': 'str',
        'smn_subscription_status': 'str',
        'smn_subscription_type': 'str'
    }

    attribute_map = {
        'smn_notified_content': 'smn_notified_content',
        'smn_subscription_status': 'smn_subscription_status',
        'smn_subscription_type': 'smn_subscription_type'
    }

    def __init__(self, smn_notified_content=None, smn_subscription_status=None, smn_subscription_type=None):
        """SmnInfo

        The model defined in huaweicloud sdk

        :param smn_notified_content: smn发送消息的内容
        :type smn_notified_content: str
        :param smn_subscription_status: smn的订阅的状态
        :type smn_subscription_status: str
        :param smn_subscription_type: smn的订阅类型
        :type smn_subscription_type: str
        """
        
        

        self._smn_notified_content = None
        self._smn_subscription_status = None
        self._smn_subscription_type = None
        self.discriminator = None

        if smn_notified_content is not None:
            self.smn_notified_content = smn_notified_content
        if smn_subscription_status is not None:
            self.smn_subscription_status = smn_subscription_status
        if smn_subscription_type is not None:
            self.smn_subscription_type = smn_subscription_type

    @property
    def smn_notified_content(self):
        """Gets the smn_notified_content of this SmnInfo.

        smn发送消息的内容

        :return: The smn_notified_content of this SmnInfo.
        :rtype: str
        """
        return self._smn_notified_content

    @smn_notified_content.setter
    def smn_notified_content(self, smn_notified_content):
        """Sets the smn_notified_content of this SmnInfo.

        smn发送消息的内容

        :param smn_notified_content: The smn_notified_content of this SmnInfo.
        :type smn_notified_content: str
        """
        self._smn_notified_content = smn_notified_content

    @property
    def smn_subscription_status(self):
        """Gets the smn_subscription_status of this SmnInfo.

        smn的订阅的状态

        :return: The smn_subscription_status of this SmnInfo.
        :rtype: str
        """
        return self._smn_subscription_status

    @smn_subscription_status.setter
    def smn_subscription_status(self, smn_subscription_status):
        """Sets the smn_subscription_status of this SmnInfo.

        smn的订阅的状态

        :param smn_subscription_status: The smn_subscription_status of this SmnInfo.
        :type smn_subscription_status: str
        """
        self._smn_subscription_status = smn_subscription_status

    @property
    def smn_subscription_type(self):
        """Gets the smn_subscription_type of this SmnInfo.

        smn的订阅类型

        :return: The smn_subscription_type of this SmnInfo.
        :rtype: str
        """
        return self._smn_subscription_type

    @smn_subscription_type.setter
    def smn_subscription_type(self, smn_subscription_type):
        """Sets the smn_subscription_type of this SmnInfo.

        smn的订阅类型

        :param smn_subscription_type: The smn_subscription_type of this SmnInfo.
        :type smn_subscription_type: str
        """
        self._smn_subscription_type = smn_subscription_type

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
        if not isinstance(other, SmnInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
