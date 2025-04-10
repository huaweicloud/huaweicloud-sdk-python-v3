# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SwitchoverReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'post_process_config': 'str',
        'disaster_type': 'str'
    }

    attribute_map = {
        'post_process_config': 'post_process_config',
        'disaster_type': 'disaster_type'
    }

    def __init__(self, post_process_config=None, disaster_type=None):
        r"""SwitchoverReq

        The model defined in huaweicloud sdk

        :param post_process_config: 是否支持倒换失败自愈，为空时默认不自愈。
        :type post_process_config: str
        :param disaster_type: 容灾类型。
        :type disaster_type: str
        """
        
        

        self._post_process_config = None
        self._disaster_type = None
        self.discriminator = None

        if post_process_config is not None:
            self.post_process_config = post_process_config
        self.disaster_type = disaster_type

    @property
    def post_process_config(self):
        r"""Gets the post_process_config of this SwitchoverReq.

        是否支持倒换失败自愈，为空时默认不自愈。

        :return: The post_process_config of this SwitchoverReq.
        :rtype: str
        """
        return self._post_process_config

    @post_process_config.setter
    def post_process_config(self, post_process_config):
        r"""Sets the post_process_config of this SwitchoverReq.

        是否支持倒换失败自愈，为空时默认不自愈。

        :param post_process_config: The post_process_config of this SwitchoverReq.
        :type post_process_config: str
        """
        self._post_process_config = post_process_config

    @property
    def disaster_type(self):
        r"""Gets the disaster_type of this SwitchoverReq.

        容灾类型。

        :return: The disaster_type of this SwitchoverReq.
        :rtype: str
        """
        return self._disaster_type

    @disaster_type.setter
    def disaster_type(self, disaster_type):
        r"""Sets the disaster_type of this SwitchoverReq.

        容灾类型。

        :param disaster_type: The disaster_type of this SwitchoverReq.
        :type disaster_type: str
        """
        self._disaster_type = disaster_type

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
        if not isinstance(other, SwitchoverReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
