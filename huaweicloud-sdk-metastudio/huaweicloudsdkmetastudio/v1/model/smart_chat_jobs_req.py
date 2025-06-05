# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SmartChatJobsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'extend_param': 'str'
    }

    attribute_map = {
        'extend_param': 'extend_param'
    }

    def __init__(self, extend_param=None):
        r"""SmartChatJobsReq

        The model defined in huaweicloud sdk

        :param extend_param: 扩展参数，按照Json格式携带。 * city：所在城市 * client_id：客户端ID
        :type extend_param: str
        """
        
        

        self._extend_param = None
        self.discriminator = None

        if extend_param is not None:
            self.extend_param = extend_param

    @property
    def extend_param(self):
        r"""Gets the extend_param of this SmartChatJobsReq.

        扩展参数，按照Json格式携带。 * city：所在城市 * client_id：客户端ID

        :return: The extend_param of this SmartChatJobsReq.
        :rtype: str
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        r"""Sets the extend_param of this SmartChatJobsReq.

        扩展参数，按照Json格式携带。 * city：所在城市 * client_id：客户端ID

        :param extend_param: The extend_param of this SmartChatJobsReq.
        :type extend_param: str
        """
        self._extend_param = extend_param

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
        if not isinstance(other, SmartChatJobsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
