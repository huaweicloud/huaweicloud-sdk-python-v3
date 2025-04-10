# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetBucketNotificationRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    xml_name = "NotificationConfiguration"

    sensitive_list = []

    openapi_types = {
        'topic_configuration': 'list[TopicConfiguration]',
        'function_stage_configuration': 'list[FunctionStageConfiguration]'
    }

    attribute_map = {
        'topic_configuration': 'TopicConfiguration',
        'function_stage_configuration': 'FunctionStageConfiguration'
    }

    def __init__(self, topic_configuration=None, function_stage_configuration=None):
        r"""SetBucketNotificationRequestBody

        The model defined in huaweicloud sdk

        :param topic_configuration: 
        :type topic_configuration: list[:class:`huaweicloudsdkobs.v1.TopicConfiguration`]
        :param function_stage_configuration: 
        :type function_stage_configuration: list[:class:`huaweicloudsdkobs.v1.FunctionStageConfiguration`]
        """
        
        

        self._topic_configuration = None
        self._function_stage_configuration = None
        self.discriminator = None

        if topic_configuration is not None:
            self.topic_configuration = topic_configuration
        if function_stage_configuration is not None:
            self.function_stage_configuration = function_stage_configuration

    @property
    def topic_configuration(self):
        r"""Gets the topic_configuration of this SetBucketNotificationRequestBody.

        :return: The topic_configuration of this SetBucketNotificationRequestBody.
        :rtype: list[:class:`huaweicloudsdkobs.v1.TopicConfiguration`]
        """
        return self._topic_configuration

    @topic_configuration.setter
    def topic_configuration(self, topic_configuration):
        r"""Sets the topic_configuration of this SetBucketNotificationRequestBody.

        :param topic_configuration: The topic_configuration of this SetBucketNotificationRequestBody.
        :type topic_configuration: list[:class:`huaweicloudsdkobs.v1.TopicConfiguration`]
        """
        self._topic_configuration = topic_configuration

    @property
    def function_stage_configuration(self):
        r"""Gets the function_stage_configuration of this SetBucketNotificationRequestBody.

        :return: The function_stage_configuration of this SetBucketNotificationRequestBody.
        :rtype: list[:class:`huaweicloudsdkobs.v1.FunctionStageConfiguration`]
        """
        return self._function_stage_configuration

    @function_stage_configuration.setter
    def function_stage_configuration(self, function_stage_configuration):
        r"""Sets the function_stage_configuration of this SetBucketNotificationRequestBody.

        :param function_stage_configuration: The function_stage_configuration of this SetBucketNotificationRequestBody.
        :type function_stage_configuration: list[:class:`huaweicloudsdkobs.v1.FunctionStageConfiguration`]
        """
        self._function_stage_configuration = function_stage_configuration

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
        if not isinstance(other, SetBucketNotificationRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
