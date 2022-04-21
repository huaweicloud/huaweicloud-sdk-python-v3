# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetAccessConfigListRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'access_config_name_list': 'list[str]',
        'host_group_name_list': 'list[str]',
        'log_group_name_list': 'list[str]',
        'log_stream_name_list': 'list[str]',
        'access_config_tag_list': 'list[AccessConfigTag]'
    }

    attribute_map = {
        'access_config_name_list': 'access_config_name_list',
        'host_group_name_list': 'host_group_name_list',
        'log_group_name_list': 'log_group_name_list',
        'log_stream_name_list': 'log_stream_name_list',
        'access_config_tag_list': 'access_config_tag_list'
    }

    def __init__(self, access_config_name_list=None, host_group_name_list=None, log_group_name_list=None, log_stream_name_list=None, access_config_tag_list=None):
        """GetAccessConfigListRequestBody

        The model defined in huaweicloud sdk

        :param access_config_name_list: 接入配置名称列表
        :type access_config_name_list: list[str]
        :param host_group_name_list: 主机组名称列表
        :type host_group_name_list: list[str]
        :param log_group_name_list: 日志组名称列表
        :type log_group_name_list: list[str]
        :param log_stream_name_list: 日志流名称列表
        :type log_stream_name_list: list[str]
        :param access_config_tag_list: 
        :type access_config_tag_list: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        
        

        self._access_config_name_list = None
        self._host_group_name_list = None
        self._log_group_name_list = None
        self._log_stream_name_list = None
        self._access_config_tag_list = None
        self.discriminator = None

        self.access_config_name_list = access_config_name_list
        self.host_group_name_list = host_group_name_list
        self.log_group_name_list = log_group_name_list
        self.log_stream_name_list = log_stream_name_list
        self.access_config_tag_list = access_config_tag_list

    @property
    def access_config_name_list(self):
        """Gets the access_config_name_list of this GetAccessConfigListRequestBody.

        接入配置名称列表

        :return: The access_config_name_list of this GetAccessConfigListRequestBody.
        :rtype: list[str]
        """
        return self._access_config_name_list

    @access_config_name_list.setter
    def access_config_name_list(self, access_config_name_list):
        """Sets the access_config_name_list of this GetAccessConfigListRequestBody.

        接入配置名称列表

        :param access_config_name_list: The access_config_name_list of this GetAccessConfigListRequestBody.
        :type access_config_name_list: list[str]
        """
        self._access_config_name_list = access_config_name_list

    @property
    def host_group_name_list(self):
        """Gets the host_group_name_list of this GetAccessConfigListRequestBody.

        主机组名称列表

        :return: The host_group_name_list of this GetAccessConfigListRequestBody.
        :rtype: list[str]
        """
        return self._host_group_name_list

    @host_group_name_list.setter
    def host_group_name_list(self, host_group_name_list):
        """Sets the host_group_name_list of this GetAccessConfigListRequestBody.

        主机组名称列表

        :param host_group_name_list: The host_group_name_list of this GetAccessConfigListRequestBody.
        :type host_group_name_list: list[str]
        """
        self._host_group_name_list = host_group_name_list

    @property
    def log_group_name_list(self):
        """Gets the log_group_name_list of this GetAccessConfigListRequestBody.

        日志组名称列表

        :return: The log_group_name_list of this GetAccessConfigListRequestBody.
        :rtype: list[str]
        """
        return self._log_group_name_list

    @log_group_name_list.setter
    def log_group_name_list(self, log_group_name_list):
        """Sets the log_group_name_list of this GetAccessConfigListRequestBody.

        日志组名称列表

        :param log_group_name_list: The log_group_name_list of this GetAccessConfigListRequestBody.
        :type log_group_name_list: list[str]
        """
        self._log_group_name_list = log_group_name_list

    @property
    def log_stream_name_list(self):
        """Gets the log_stream_name_list of this GetAccessConfigListRequestBody.

        日志流名称列表

        :return: The log_stream_name_list of this GetAccessConfigListRequestBody.
        :rtype: list[str]
        """
        return self._log_stream_name_list

    @log_stream_name_list.setter
    def log_stream_name_list(self, log_stream_name_list):
        """Sets the log_stream_name_list of this GetAccessConfigListRequestBody.

        日志流名称列表

        :param log_stream_name_list: The log_stream_name_list of this GetAccessConfigListRequestBody.
        :type log_stream_name_list: list[str]
        """
        self._log_stream_name_list = log_stream_name_list

    @property
    def access_config_tag_list(self):
        """Gets the access_config_tag_list of this GetAccessConfigListRequestBody.


        :return: The access_config_tag_list of this GetAccessConfigListRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        return self._access_config_tag_list

    @access_config_tag_list.setter
    def access_config_tag_list(self, access_config_tag_list):
        """Sets the access_config_tag_list of this GetAccessConfigListRequestBody.


        :param access_config_tag_list: The access_config_tag_list of this GetAccessConfigListRequestBody.
        :type access_config_tag_list: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        self._access_config_tag_list = access_config_tag_list

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
        if not isinstance(other, GetAccessConfigListRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
