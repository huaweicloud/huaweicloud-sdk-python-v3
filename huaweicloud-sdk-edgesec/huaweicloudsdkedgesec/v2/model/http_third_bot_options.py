# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class HttpThirdBotOptions:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'river_config': 'HttpRiverConfig'
    }

    attribute_map = {
        'river_config': 'river_config'
    }

    def __init__(self, river_config=None):
        r"""HttpThirdBotOptions

        The model defined in huaweicloud sdk

        :param river_config: 
        :type river_config: :class:`huaweicloudsdkedgesec.v2.HttpRiverConfig`
        """
        
        

        self._river_config = None
        self.discriminator = None

        if river_config is not None:
            self.river_config = river_config

    @property
    def river_config(self):
        r"""Gets the river_config of this HttpThirdBotOptions.

        :return: The river_config of this HttpThirdBotOptions.
        :rtype: :class:`huaweicloudsdkedgesec.v2.HttpRiverConfig`
        """
        return self._river_config

    @river_config.setter
    def river_config(self, river_config):
        r"""Sets the river_config of this HttpThirdBotOptions.

        :param river_config: The river_config of this HttpThirdBotOptions.
        :type river_config: :class:`huaweicloudsdkedgesec.v2.HttpRiverConfig`
        """
        self._river_config = river_config

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
        if not isinstance(other, HttpThirdBotOptions):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
