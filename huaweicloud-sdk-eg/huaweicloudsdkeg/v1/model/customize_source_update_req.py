# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CustomizeSourceUpdateReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'description': 'str',
        'detail': 'object'
    }

    attribute_map = {
        'description': 'description',
        'detail': 'detail'
    }

    def __init__(self, description=None, detail=None):
        """CustomizeSourceUpdateReq

        The model defined in huaweicloud sdk

        :param description: 事件源描述
        :type description: str
        :param detail: json格式封装消息实例更新信息：如RabbitMQ实例的虚拟主机vhost字段、队列queue字段、用户密码
        :type detail: object
        """
        
        

        self._description = None
        self._detail = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if detail is not None:
            self.detail = detail

    @property
    def description(self):
        """Gets the description of this CustomizeSourceUpdateReq.

        事件源描述

        :return: The description of this CustomizeSourceUpdateReq.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CustomizeSourceUpdateReq.

        事件源描述

        :param description: The description of this CustomizeSourceUpdateReq.
        :type description: str
        """
        self._description = description

    @property
    def detail(self):
        """Gets the detail of this CustomizeSourceUpdateReq.

        json格式封装消息实例更新信息：如RabbitMQ实例的虚拟主机vhost字段、队列queue字段、用户密码

        :return: The detail of this CustomizeSourceUpdateReq.
        :rtype: object
        """
        return self._detail

    @detail.setter
    def detail(self, detail):
        """Sets the detail of this CustomizeSourceUpdateReq.

        json格式封装消息实例更新信息：如RabbitMQ实例的虚拟主机vhost字段、队列queue字段、用户密码

        :param detail: The detail of this CustomizeSourceUpdateReq.
        :type detail: object
        """
        self._detail = detail

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
        if not isinstance(other, CustomizeSourceUpdateReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
