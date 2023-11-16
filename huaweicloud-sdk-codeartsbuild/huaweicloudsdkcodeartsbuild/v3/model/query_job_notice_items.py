# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class QueryJobNoticeItems:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'notice_type': 'str',
        'enable_map': 'dict(str, bool)',
        'param_config': 'str'
    }

    attribute_map = {
        'notice_type': 'notice_type',
        'enable_map': 'enable_map',
        'param_config': 'param_config'
    }

    def __init__(self, notice_type=None, enable_map=None, param_config=None):
        """QueryJobNoticeItems

        The model defined in huaweicloud sdk

        :param notice_type: 通知类型
        :type notice_type: str
        :param enable_map: 通知品种开启详情的表
        :type enable_map: dict(str, bool)
        :param param_config: 参数配置
        :type param_config: str
        """
        
        

        self._notice_type = None
        self._enable_map = None
        self._param_config = None
        self.discriminator = None

        if notice_type is not None:
            self.notice_type = notice_type
        if enable_map is not None:
            self.enable_map = enable_map
        if param_config is not None:
            self.param_config = param_config

    @property
    def notice_type(self):
        """Gets the notice_type of this QueryJobNoticeItems.

        通知类型

        :return: The notice_type of this QueryJobNoticeItems.
        :rtype: str
        """
        return self._notice_type

    @notice_type.setter
    def notice_type(self, notice_type):
        """Sets the notice_type of this QueryJobNoticeItems.

        通知类型

        :param notice_type: The notice_type of this QueryJobNoticeItems.
        :type notice_type: str
        """
        self._notice_type = notice_type

    @property
    def enable_map(self):
        """Gets the enable_map of this QueryJobNoticeItems.

        通知品种开启详情的表

        :return: The enable_map of this QueryJobNoticeItems.
        :rtype: dict(str, bool)
        """
        return self._enable_map

    @enable_map.setter
    def enable_map(self, enable_map):
        """Sets the enable_map of this QueryJobNoticeItems.

        通知品种开启详情的表

        :param enable_map: The enable_map of this QueryJobNoticeItems.
        :type enable_map: dict(str, bool)
        """
        self._enable_map = enable_map

    @property
    def param_config(self):
        """Gets the param_config of this QueryJobNoticeItems.

        参数配置

        :return: The param_config of this QueryJobNoticeItems.
        :rtype: str
        """
        return self._param_config

    @param_config.setter
    def param_config(self, param_config):
        """Sets the param_config of this QueryJobNoticeItems.

        参数配置

        :param param_config: The param_config of this QueryJobNoticeItems.
        :type param_config: str
        """
        self._param_config = param_config

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
        if not isinstance(other, QueryJobNoticeItems):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
