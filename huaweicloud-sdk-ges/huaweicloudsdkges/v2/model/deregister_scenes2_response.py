# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeregisterScenes2Response(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'success': 'list[str]',
        'failure': 'list[str]'
    }

    attribute_map = {
        'success': 'success',
        'failure': 'failure'
    }

    def __init__(self, success=None, failure=None):
        """DeregisterScenes2Response

        The model defined in huaweicloud sdk

        :param success: 取消订阅成功的SceneApplication。
        :type success: list[str]
        :param failure: 取消订阅失败的SceneApplication。
        :type failure: list[str]
        """
        
        super(DeregisterScenes2Response, self).__init__()

        self._success = None
        self._failure = None
        self.discriminator = None

        if success is not None:
            self.success = success
        if failure is not None:
            self.failure = failure

    @property
    def success(self):
        """Gets the success of this DeregisterScenes2Response.

        取消订阅成功的SceneApplication。

        :return: The success of this DeregisterScenes2Response.
        :rtype: list[str]
        """
        return self._success

    @success.setter
    def success(self, success):
        """Sets the success of this DeregisterScenes2Response.

        取消订阅成功的SceneApplication。

        :param success: The success of this DeregisterScenes2Response.
        :type success: list[str]
        """
        self._success = success

    @property
    def failure(self):
        """Gets the failure of this DeregisterScenes2Response.

        取消订阅失败的SceneApplication。

        :return: The failure of this DeregisterScenes2Response.
        :rtype: list[str]
        """
        return self._failure

    @failure.setter
    def failure(self, failure):
        """Sets the failure of this DeregisterScenes2Response.

        取消订阅失败的SceneApplication。

        :param failure: The failure of this DeregisterScenes2Response.
        :type failure: list[str]
        """
        self._failure = failure

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
        if not isinstance(other, DeregisterScenes2Response):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
