# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateAccessConfigRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'access_config_name': 'str',
        'access_config_type': 'str',
        'access_config_detail': 'AccessConfigDeatilCreate',
        'log_info': 'AccessConfigBaseLogInfoCreate',
        'host_group_info': 'AccessConfigHostGroupIdListCreate',
        'access_config_tag': 'list[AccessConfigTag]'
    }

    attribute_map = {
        'access_config_name': 'access_config_name',
        'access_config_type': 'access_config_type',
        'access_config_detail': 'access_config_detail',
        'log_info': 'log_info',
        'host_group_info': 'host_group_info',
        'access_config_tag': 'access_config_tag'
    }

    def __init__(self, access_config_name=None, access_config_type=None, access_config_detail=None, log_info=None, host_group_info=None, access_config_tag=None):
        """CreateAccessConfigRequestBody

        The model defined in huaweicloud sdk

        :param access_config_name: 日志接入名称
        :type access_config_name: str
        :param access_config_type: 日志接入类型。AGENT：主机接入类型
        :type access_config_type: str
        :param access_config_detail: 
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilCreate`
        :param log_info: 
        :type log_info: :class:`huaweicloudsdklts.v2.AccessConfigBaseLogInfoCreate`
        :param host_group_info: 
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdListCreate`
        :param access_config_tag: 
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        
        

        self._access_config_name = None
        self._access_config_type = None
        self._access_config_detail = None
        self._log_info = None
        self._host_group_info = None
        self._access_config_tag = None
        self.discriminator = None

        self.access_config_name = access_config_name
        self.access_config_type = access_config_type
        self.access_config_detail = access_config_detail
        self.log_info = log_info
        if host_group_info is not None:
            self.host_group_info = host_group_info
        if access_config_tag is not None:
            self.access_config_tag = access_config_tag

    @property
    def access_config_name(self):
        """Gets the access_config_name of this CreateAccessConfigRequestBody.

        日志接入名称

        :return: The access_config_name of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_name

    @access_config_name.setter
    def access_config_name(self, access_config_name):
        """Sets the access_config_name of this CreateAccessConfigRequestBody.

        日志接入名称

        :param access_config_name: The access_config_name of this CreateAccessConfigRequestBody.
        :type access_config_name: str
        """
        self._access_config_name = access_config_name

    @property
    def access_config_type(self):
        """Gets the access_config_type of this CreateAccessConfigRequestBody.

        日志接入类型。AGENT：主机接入类型

        :return: The access_config_type of this CreateAccessConfigRequestBody.
        :rtype: str
        """
        return self._access_config_type

    @access_config_type.setter
    def access_config_type(self, access_config_type):
        """Sets the access_config_type of this CreateAccessConfigRequestBody.

        日志接入类型。AGENT：主机接入类型

        :param access_config_type: The access_config_type of this CreateAccessConfigRequestBody.
        :type access_config_type: str
        """
        self._access_config_type = access_config_type

    @property
    def access_config_detail(self):
        """Gets the access_config_detail of this CreateAccessConfigRequestBody.

        :return: The access_config_detail of this CreateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigDeatilCreate`
        """
        return self._access_config_detail

    @access_config_detail.setter
    def access_config_detail(self, access_config_detail):
        """Sets the access_config_detail of this CreateAccessConfigRequestBody.

        :param access_config_detail: The access_config_detail of this CreateAccessConfigRequestBody.
        :type access_config_detail: :class:`huaweicloudsdklts.v2.AccessConfigDeatilCreate`
        """
        self._access_config_detail = access_config_detail

    @property
    def log_info(self):
        """Gets the log_info of this CreateAccessConfigRequestBody.

        :return: The log_info of this CreateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigBaseLogInfoCreate`
        """
        return self._log_info

    @log_info.setter
    def log_info(self, log_info):
        """Sets the log_info of this CreateAccessConfigRequestBody.

        :param log_info: The log_info of this CreateAccessConfigRequestBody.
        :type log_info: :class:`huaweicloudsdklts.v2.AccessConfigBaseLogInfoCreate`
        """
        self._log_info = log_info

    @property
    def host_group_info(self):
        """Gets the host_group_info of this CreateAccessConfigRequestBody.

        :return: The host_group_info of this CreateAccessConfigRequestBody.
        :rtype: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdListCreate`
        """
        return self._host_group_info

    @host_group_info.setter
    def host_group_info(self, host_group_info):
        """Sets the host_group_info of this CreateAccessConfigRequestBody.

        :param host_group_info: The host_group_info of this CreateAccessConfigRequestBody.
        :type host_group_info: :class:`huaweicloudsdklts.v2.AccessConfigHostGroupIdListCreate`
        """
        self._host_group_info = host_group_info

    @property
    def access_config_tag(self):
        """Gets the access_config_tag of this CreateAccessConfigRequestBody.

        :return: The access_config_tag of this CreateAccessConfigRequestBody.
        :rtype: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        return self._access_config_tag

    @access_config_tag.setter
    def access_config_tag(self, access_config_tag):
        """Sets the access_config_tag of this CreateAccessConfigRequestBody.

        :param access_config_tag: The access_config_tag of this CreateAccessConfigRequestBody.
        :type access_config_tag: list[:class:`huaweicloudsdklts.v2.AccessConfigTag`]
        """
        self._access_config_tag = access_config_tag

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
        if not isinstance(other, CreateAccessConfigRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
