# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateNotificationOption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'topic_urn': 'str',
        'topic_scene': 'list[str]'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'topic_scene': 'topic_scene'
    }

    def __init__(self, topic_urn=None, topic_scene=None):
        """CreateNotificationOption

        The model defined in huaweicloud sdk

        :param topic_urn: SMN服务中Topic的唯一的资源标识。
        :type topic_urn: str
        :param topic_scene: 通知场景，有以下五种类型。SCALING_UP：扩容成功。SCALING_UP_FAIL：扩容失败。SCALING_DOWN：减容成功。SCALING_DOWN_FAIL：减容失败。SCALING_GROUP_ABNORMAL：伸缩组发生异常
        :type topic_scene: list[str]
        """
        
        

        self._topic_urn = None
        self._topic_scene = None
        self.discriminator = None

        self.topic_urn = topic_urn
        self.topic_scene = topic_scene

    @property
    def topic_urn(self):
        """Gets the topic_urn of this CreateNotificationOption.

        SMN服务中Topic的唯一的资源标识。

        :return: The topic_urn of this CreateNotificationOption.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this CreateNotificationOption.

        SMN服务中Topic的唯一的资源标识。

        :param topic_urn: The topic_urn of this CreateNotificationOption.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def topic_scene(self):
        """Gets the topic_scene of this CreateNotificationOption.

        通知场景，有以下五种类型。SCALING_UP：扩容成功。SCALING_UP_FAIL：扩容失败。SCALING_DOWN：减容成功。SCALING_DOWN_FAIL：减容失败。SCALING_GROUP_ABNORMAL：伸缩组发生异常

        :return: The topic_scene of this CreateNotificationOption.
        :rtype: list[str]
        """
        return self._topic_scene

    @topic_scene.setter
    def topic_scene(self, topic_scene):
        """Sets the topic_scene of this CreateNotificationOption.

        通知场景，有以下五种类型。SCALING_UP：扩容成功。SCALING_UP_FAIL：扩容失败。SCALING_DOWN：减容成功。SCALING_DOWN_FAIL：减容失败。SCALING_GROUP_ABNORMAL：伸缩组发生异常

        :param topic_scene: The topic_scene of this CreateNotificationOption.
        :type topic_scene: list[str]
        """
        self._topic_scene = topic_scene

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
        if not isinstance(other, CreateNotificationOption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
