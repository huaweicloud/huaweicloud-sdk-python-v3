# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestSetCohostBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'is_cohost': 'int'
    }

    attribute_map = {
        'is_cohost': 'isCohost'
    }

    def __init__(self, is_cohost=None):
        r"""RestSetCohostBody

        The model defined in huaweicloud sdk

        :param is_cohost: - 0：撤销联席主持人 - 1：设置联席主持人
        :type is_cohost: int
        """
        
        

        self._is_cohost = None
        self.discriminator = None

        self.is_cohost = is_cohost

    @property
    def is_cohost(self):
        r"""Gets the is_cohost of this RestSetCohostBody.

        - 0：撤销联席主持人 - 1：设置联席主持人

        :return: The is_cohost of this RestSetCohostBody.
        :rtype: int
        """
        return self._is_cohost

    @is_cohost.setter
    def is_cohost(self, is_cohost):
        r"""Sets the is_cohost of this RestSetCohostBody.

        - 0：撤销联席主持人 - 1：设置联席主持人

        :param is_cohost: The is_cohost of this RestSetCohostBody.
        :type is_cohost: int
        """
        self._is_cohost = is_cohost

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
        if not isinstance(other, RestSetCohostBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
