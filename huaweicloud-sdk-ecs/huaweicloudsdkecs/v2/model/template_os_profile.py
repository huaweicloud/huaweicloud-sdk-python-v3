# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TemplateOsProfile:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []
    sensitive_list.append('key_name')
    sensitive_list.append('user_data')

    openapi_types = {
        'key_name': 'str',
        'user_data': 'str',
        'iam_agency_name': 'str',
        'enable_monitoring_service': 'bool'
    }

    attribute_map = {
        'key_name': 'key_name',
        'user_data': 'user_data',
        'iam_agency_name': 'iam_agency_name',
        'enable_monitoring_service': 'enable_monitoring_service'
    }

    def __init__(self, key_name=None, user_data=None, iam_agency_name=None, enable_monitoring_service=None):
        r"""TemplateOsProfile

        The model defined in huaweicloud sdk

        :param key_name: 秘钥名称
        :type key_name: str
        :param user_data: 注入脚本，会导致请求过大，影响虚拟机表。1. 和密码的使用冲突 2. 超大文本问题。
        :type user_data: str
        :param iam_agency_name: 委托名称。实际需要多委托。
        :type iam_agency_name: str
        :param enable_monitoring_service: 开启主机监控服务
        :type enable_monitoring_service: bool
        """
        
        

        self._key_name = None
        self._user_data = None
        self._iam_agency_name = None
        self._enable_monitoring_service = None
        self.discriminator = None

        if key_name is not None:
            self.key_name = key_name
        if user_data is not None:
            self.user_data = user_data
        if iam_agency_name is not None:
            self.iam_agency_name = iam_agency_name
        if enable_monitoring_service is not None:
            self.enable_monitoring_service = enable_monitoring_service

    @property
    def key_name(self):
        r"""Gets the key_name of this TemplateOsProfile.

        秘钥名称

        :return: The key_name of this TemplateOsProfile.
        :rtype: str
        """
        return self._key_name

    @key_name.setter
    def key_name(self, key_name):
        r"""Sets the key_name of this TemplateOsProfile.

        秘钥名称

        :param key_name: The key_name of this TemplateOsProfile.
        :type key_name: str
        """
        self._key_name = key_name

    @property
    def user_data(self):
        r"""Gets the user_data of this TemplateOsProfile.

        注入脚本，会导致请求过大，影响虚拟机表。1. 和密码的使用冲突 2. 超大文本问题。

        :return: The user_data of this TemplateOsProfile.
        :rtype: str
        """
        return self._user_data

    @user_data.setter
    def user_data(self, user_data):
        r"""Sets the user_data of this TemplateOsProfile.

        注入脚本，会导致请求过大，影响虚拟机表。1. 和密码的使用冲突 2. 超大文本问题。

        :param user_data: The user_data of this TemplateOsProfile.
        :type user_data: str
        """
        self._user_data = user_data

    @property
    def iam_agency_name(self):
        r"""Gets the iam_agency_name of this TemplateOsProfile.

        委托名称。实际需要多委托。

        :return: The iam_agency_name of this TemplateOsProfile.
        :rtype: str
        """
        return self._iam_agency_name

    @iam_agency_name.setter
    def iam_agency_name(self, iam_agency_name):
        r"""Sets the iam_agency_name of this TemplateOsProfile.

        委托名称。实际需要多委托。

        :param iam_agency_name: The iam_agency_name of this TemplateOsProfile.
        :type iam_agency_name: str
        """
        self._iam_agency_name = iam_agency_name

    @property
    def enable_monitoring_service(self):
        r"""Gets the enable_monitoring_service of this TemplateOsProfile.

        开启主机监控服务

        :return: The enable_monitoring_service of this TemplateOsProfile.
        :rtype: bool
        """
        return self._enable_monitoring_service

    @enable_monitoring_service.setter
    def enable_monitoring_service(self, enable_monitoring_service):
        r"""Sets the enable_monitoring_service of this TemplateOsProfile.

        开启主机监控服务

        :param enable_monitoring_service: The enable_monitoring_service of this TemplateOsProfile.
        :type enable_monitoring_service: bool
        """
        self._enable_monitoring_service = enable_monitoring_service

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
        if not isinstance(other, TemplateOsProfile):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
