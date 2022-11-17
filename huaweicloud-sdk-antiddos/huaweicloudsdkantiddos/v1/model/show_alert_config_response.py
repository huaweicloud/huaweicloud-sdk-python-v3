# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowAlertConfigResponse(SdkResponse):

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
        'display_name': 'str',
        'warn_config': 'AlertConfigRespWarnConfig'
    }

    attribute_map = {
        'topic_urn': 'topic_urn',
        'display_name': 'display_name',
        'warn_config': 'warn_config'
    }

    def __init__(self, topic_urn=None, display_name=None, warn_config=None):
        """ShowAlertConfigResponse

        The model defined in huaweicloud sdk

        :param topic_urn: 告警群组的唯一标识
        :type topic_urn: str
        :param display_name: 告警群组描述
        :type display_name: str
        :param warn_config: 
        :type warn_config: :class:`huaweicloudsdkantiddos.v1.AlertConfigRespWarnConfig`
        """
        
        super(ShowAlertConfigResponse, self).__init__()

        self._topic_urn = None
        self._display_name = None
        self._warn_config = None
        self.discriminator = None

        if topic_urn is not None:
            self.topic_urn = topic_urn
        if display_name is not None:
            self.display_name = display_name
        if warn_config is not None:
            self.warn_config = warn_config

    @property
    def topic_urn(self):
        """Gets the topic_urn of this ShowAlertConfigResponse.

        告警群组的唯一标识

        :return: The topic_urn of this ShowAlertConfigResponse.
        :rtype: str
        """
        return self._topic_urn

    @topic_urn.setter
    def topic_urn(self, topic_urn):
        """Sets the topic_urn of this ShowAlertConfigResponse.

        告警群组的唯一标识

        :param topic_urn: The topic_urn of this ShowAlertConfigResponse.
        :type topic_urn: str
        """
        self._topic_urn = topic_urn

    @property
    def display_name(self):
        """Gets the display_name of this ShowAlertConfigResponse.

        告警群组描述

        :return: The display_name of this ShowAlertConfigResponse.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ShowAlertConfigResponse.

        告警群组描述

        :param display_name: The display_name of this ShowAlertConfigResponse.
        :type display_name: str
        """
        self._display_name = display_name

    @property
    def warn_config(self):
        """Gets the warn_config of this ShowAlertConfigResponse.

        :return: The warn_config of this ShowAlertConfigResponse.
        :rtype: :class:`huaweicloudsdkantiddos.v1.AlertConfigRespWarnConfig`
        """
        return self._warn_config

    @warn_config.setter
    def warn_config(self, warn_config):
        """Sets the warn_config of this ShowAlertConfigResponse.

        :param warn_config: The warn_config of this ShowAlertConfigResponse.
        :type warn_config: :class:`huaweicloudsdkantiddos.v1.AlertConfigRespWarnConfig`
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
        if not isinstance(other, ShowAlertConfigResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
