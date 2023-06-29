# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateServerReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'description': 'str',
        'maintain_status': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'description': 'description',
        'maintain_status': 'maintain_status'
    }

    def __init__(self, name=None, description=None, maintain_status=None):
        """UpdateServerReq

        The model defined in huaweicloud sdk

        :param name: 服务器名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-空格组成，不能全为空格, 首位不为空 2. 长度范围1~64个字符
        :type name: str
        :param description: 服务器描述
        :type description: str
        :param maintain_status: 服务器维护状态标识 * &#x60;true&#x60; - 添加标记 * &#x60;false&#x60; - 移除标记
        :type maintain_status: bool
        """
        
        

        self._name = None
        self._description = None
        self._maintain_status = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if description is not None:
            self.description = description
        if maintain_status is not None:
            self.maintain_status = maintain_status

    @property
    def name(self):
        """Gets the name of this UpdateServerReq.

        服务器名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-空格组成，不能全为空格, 首位不为空 2. 长度范围1~64个字符

        :return: The name of this UpdateServerReq.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateServerReq.

        服务器名称，名称需满足如下规则: 1. 由中文，英文大小写，数字，_-空格组成，不能全为空格, 首位不为空 2. 长度范围1~64个字符

        :param name: The name of this UpdateServerReq.
        :type name: str
        """
        self._name = name

    @property
    def description(self):
        """Gets the description of this UpdateServerReq.

        服务器描述

        :return: The description of this UpdateServerReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateServerReq.

        服务器描述

        :param description: The description of this UpdateServerReq.
        :type description: str
        """
        self._description = description

    @property
    def maintain_status(self):
        """Gets the maintain_status of this UpdateServerReq.

        服务器维护状态标识 * `true` - 添加标记 * `false` - 移除标记

        :return: The maintain_status of this UpdateServerReq.
        :rtype: bool
        """
        return self._maintain_status

    @maintain_status.setter
    def maintain_status(self, maintain_status):
        """Sets the maintain_status of this UpdateServerReq.

        服务器维护状态标识 * `true` - 添加标记 * `false` - 移除标记

        :param maintain_status: The maintain_status of this UpdateServerReq.
        :type maintain_status: bool
        """
        self._maintain_status = maintain_status

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
        if not isinstance(other, UpdateServerReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
