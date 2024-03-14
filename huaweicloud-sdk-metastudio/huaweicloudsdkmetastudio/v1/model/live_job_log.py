# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LiveJobLog:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'interaction_records_url': 'str'
    }

    attribute_map = {
        'interaction_records_url': 'interaction_records_url'
    }

    def __init__(self, interaction_records_url=None):
        """LiveJobLog

        The model defined in huaweicloud sdk

        :param interaction_records_url: 直播互动记录文件地址
        :type interaction_records_url: str
        """
        
        

        self._interaction_records_url = None
        self.discriminator = None

        if interaction_records_url is not None:
            self.interaction_records_url = interaction_records_url

    @property
    def interaction_records_url(self):
        """Gets the interaction_records_url of this LiveJobLog.

        直播互动记录文件地址

        :return: The interaction_records_url of this LiveJobLog.
        :rtype: str
        """
        return self._interaction_records_url

    @interaction_records_url.setter
    def interaction_records_url(self, interaction_records_url):
        """Sets the interaction_records_url of this LiveJobLog.

        直播互动记录文件地址

        :param interaction_records_url: The interaction_records_url of this LiveJobLog.
        :type interaction_records_url: str
        """
        self._interaction_records_url = interaction_records_url

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
        if not isinstance(other, LiveJobLog):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
