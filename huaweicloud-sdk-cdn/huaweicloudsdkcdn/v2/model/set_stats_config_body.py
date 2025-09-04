# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SetStatsConfigBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'config_type': 'int',
        'resource_type': 'str',
        'resource_name': 'str',
        'config_info': 'object',
        'expired_time': 'int'
    }

    attribute_map = {
        'config_type': 'config_type',
        'resource_type': 'resource_type',
        'resource_name': 'resource_name',
        'config_info': 'config_info',
        'expired_time': 'expired_time'
    }

    def __init__(self, config_type=None, resource_type=None, resource_name=None, config_info=None, expired_time=None):
        r"""SetStatsConfigBody

        The model defined in huaweicloud sdk

        :param config_type: 配置类别.0：热点统计类
        :type config_type: int
        :param resource_type: 资源类型。domain:resource_name为域名，account:resource_name为账号
        :type resource_type: str
        :param resource_name: 资源名称为账号或域名。多个域名以英文逗号分隔
        :type resource_name: str
        :param config_info: 配置信息.top指标仅支持ua、refer、url、origin url
        :type config_info: :class:`huaweicloudsdkcdn.v2.object`
        :param expired_time: 统计配置失效时间，秒时间戳。不能超过当前时间点往后一年
        :type expired_time: int
        """
        
        

        self._config_type = None
        self._resource_type = None
        self._resource_name = None
        self._config_info = None
        self._expired_time = None
        self.discriminator = None

        if config_type is not None:
            self.config_type = config_type
        self.resource_type = resource_type
        self.resource_name = resource_name
        self.config_info = config_info
        if expired_time is not None:
            self.expired_time = expired_time

    @property
    def config_type(self):
        r"""Gets the config_type of this SetStatsConfigBody.

        配置类别.0：热点统计类

        :return: The config_type of this SetStatsConfigBody.
        :rtype: int
        """
        return self._config_type

    @config_type.setter
    def config_type(self, config_type):
        r"""Sets the config_type of this SetStatsConfigBody.

        配置类别.0：热点统计类

        :param config_type: The config_type of this SetStatsConfigBody.
        :type config_type: int
        """
        self._config_type = config_type

    @property
    def resource_type(self):
        r"""Gets the resource_type of this SetStatsConfigBody.

        资源类型。domain:resource_name为域名，account:resource_name为账号

        :return: The resource_type of this SetStatsConfigBody.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        r"""Sets the resource_type of this SetStatsConfigBody.

        资源类型。domain:resource_name为域名，account:resource_name为账号

        :param resource_type: The resource_type of this SetStatsConfigBody.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def resource_name(self):
        r"""Gets the resource_name of this SetStatsConfigBody.

        资源名称为账号或域名。多个域名以英文逗号分隔

        :return: The resource_name of this SetStatsConfigBody.
        :rtype: str
        """
        return self._resource_name

    @resource_name.setter
    def resource_name(self, resource_name):
        r"""Sets the resource_name of this SetStatsConfigBody.

        资源名称为账号或域名。多个域名以英文逗号分隔

        :param resource_name: The resource_name of this SetStatsConfigBody.
        :type resource_name: str
        """
        self._resource_name = resource_name

    @property
    def config_info(self):
        r"""Gets the config_info of this SetStatsConfigBody.

        配置信息.top指标仅支持ua、refer、url、origin url

        :return: The config_info of this SetStatsConfigBody.
        :rtype: :class:`huaweicloudsdkcdn.v2.object`
        """
        return self._config_info

    @config_info.setter
    def config_info(self, config_info):
        r"""Sets the config_info of this SetStatsConfigBody.

        配置信息.top指标仅支持ua、refer、url、origin url

        :param config_info: The config_info of this SetStatsConfigBody.
        :type config_info: :class:`huaweicloudsdkcdn.v2.object`
        """
        self._config_info = config_info

    @property
    def expired_time(self):
        r"""Gets the expired_time of this SetStatsConfigBody.

        统计配置失效时间，秒时间戳。不能超过当前时间点往后一年

        :return: The expired_time of this SetStatsConfigBody.
        :rtype: int
        """
        return self._expired_time

    @expired_time.setter
    def expired_time(self, expired_time):
        r"""Sets the expired_time of this SetStatsConfigBody.

        统计配置失效时间，秒时间戳。不能超过当前时间点往后一年

        :param expired_time: The expired_time of this SetStatsConfigBody.
        :type expired_time: int
        """
        self._expired_time = expired_time

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
        if not isinstance(other, SetStatsConfigBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
