# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Dubbo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service': 'str',
        'version': 'str',
        'group': 'str',
        'methods': 'list[DubboMethod]'
    }

    attribute_map = {
        'service': 'service',
        'version': 'version',
        'group': 'group',
        'methods': 'methods'
    }

    def __init__(self, service=None, version=None, group=None, methods=None):
        r"""Dubbo

        The model defined in huaweicloud sdk

        :param service: 服务名。
        :type service: str
        :param version: 版本号。
        :type version: str
        :param group: 分组。
        :type group: str
        :param methods: dubbo方法列表。
        :type methods: list[:class:`huaweicloudsdkcse.v1.DubboMethod`]
        """
        
        

        self._service = None
        self._version = None
        self._group = None
        self._methods = None
        self.discriminator = None

        if service is not None:
            self.service = service
        if version is not None:
            self.version = version
        if group is not None:
            self.group = group
        if methods is not None:
            self.methods = methods

    @property
    def service(self):
        r"""Gets the service of this Dubbo.

        服务名。

        :return: The service of this Dubbo.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        r"""Sets the service of this Dubbo.

        服务名。

        :param service: The service of this Dubbo.
        :type service: str
        """
        self._service = service

    @property
    def version(self):
        r"""Gets the version of this Dubbo.

        版本号。

        :return: The version of this Dubbo.
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        r"""Sets the version of this Dubbo.

        版本号。

        :param version: The version of this Dubbo.
        :type version: str
        """
        self._version = version

    @property
    def group(self):
        r"""Gets the group of this Dubbo.

        分组。

        :return: The group of this Dubbo.
        :rtype: str
        """
        return self._group

    @group.setter
    def group(self, group):
        r"""Sets the group of this Dubbo.

        分组。

        :param group: The group of this Dubbo.
        :type group: str
        """
        self._group = group

    @property
    def methods(self):
        r"""Gets the methods of this Dubbo.

        dubbo方法列表。

        :return: The methods of this Dubbo.
        :rtype: list[:class:`huaweicloudsdkcse.v1.DubboMethod`]
        """
        return self._methods

    @methods.setter
    def methods(self, methods):
        r"""Sets the methods of this Dubbo.

        dubbo方法列表。

        :param methods: The methods of this Dubbo.
        :type methods: list[:class:`huaweicloudsdkcse.v1.DubboMethod`]
        """
        self._methods = methods

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
        if not isinstance(other, Dubbo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
