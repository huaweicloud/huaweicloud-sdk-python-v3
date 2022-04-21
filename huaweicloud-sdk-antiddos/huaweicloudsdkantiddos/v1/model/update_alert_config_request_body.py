# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateAlertConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'display_name': 'str',
        'topic_urn': 'str',
        'warn_config': 'UpdateAlertConfigRequestBodyWarnConfig'
    }

    attribute_map = {
        'display_name': 'display_name',
        'topic_urn': 'topic_urn',
        'warn_config': 'warn_config'
    }

    def __init__(self, display_name=None, topic_urn=None, warn_config=None):
        """UpdateAlertConfigRequestBody

        The model defined in huaweicloud sdk

        :param display_name: 告警群组描述。
        :type display_name: str
        :param topic_urn: 告警群组的唯一标识。
        :type topic_urn: str
        :param warn_config: 
        :type warn_config: :class:`huaweicloudsdkantiddos.v1.UpdateAlertConfigRequestBodyWarnConfig`
        """
        
        

        self._display_name = None
        self._topic_urn = None
        self._warn_config = None
        self.discriminator = None

        self.display_name = display_name
        self.topic_urn = topic_urn
        self.warn_config = warn_config

    @property
    def display_name(self):
        """Gets the display_name of this UpdateAlertConfigRequestBody.

        告警群组描述。

        :return: The display_name of this UpdateAlertConfigRequestBody.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this UpdateAlertConfigRequestBody.

        告警群组描述。

        :param display_name: The display_name of this UpdateAlertConfigRequestBody.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def topic_urn(self):
        """Gets the topic_urn of this UpdateAlertConfigRequestBody.

        告警群组的唯一标识。

        :return: The topic_urn of this UpdateAlertConfigRequestBody.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this UpdateAlertConfigRequestBody.

        告警群组的唯一标识。

        :param topic_urn: The topic_urn of this UpdateAlertConfigRequestBody.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def warn_config(self):
        """Gets the warn_config of this UpdateAlertConfigRequestBody.


        :return: The warn_config of this UpdateAlertConfigRequestBody.
        :rtype: :class:`huaweicloudsdkantiddos.v1.UpdateAlertConfigRequestBodyWarnConfig`
        """
        return self._warn_config

    @warn_config.setter
    def warn_config(self, warn_config):
        """Sets the warn_config of this UpdateAlertConfigRequestBody.


        :param warn_config: The warn_config of this UpdateAlertConfigRequestBody.
        :type warn_config: :class:`huaweicloudsdkantiddos.v1.UpdateAlertConfigRequestBodyWarnConfig`
        """
        self._warn_config = warn_config

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
        if not isinstance(other, UpdateAlertConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
