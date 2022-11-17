# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateKieReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'key': 'str',
        'labels': 'object',
        'value': 'str',
        'value_type': 'str',
        'status': 'str'
    }

    attribute_map = {
        'key': 'key',
        'labels': 'labels',
        'value': 'value',
        'value_type': 'value_type',
        'status': 'status'
    }

    def __init__(self, key=None, labels=None, value=None, value_type=None, status=None):
        """CreateKieReq

        The model defined in huaweicloud sdk

        :param key: 配置项的key。
        :type key: str
        :param labels: 配置项的标签
        :type labels: object
        :param value: 配置项的值。
        :type value: str
        :param value_type: 配置项value的类型。
        :type value_type: str
        :param status: 配置项的状态。
        :type status: str
        """
        
        

        self._key = None
        self._labels = None
        self._value = None
        self._value_type = None
        self._status = None
        self.discriminator = None

        if key is not None:
            self.key = key
        if labels is not None:
            self.labels = labels
        if value is not None:
            self.value = value
        if value_type is not None:
            self.value_type = value_type
        if status is not None:
            self.status = status

    @property
    def key(self):
        """Gets the key of this CreateKieReq.

        配置项的key。

        :return: The key of this CreateKieReq.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """Sets the key of this CreateKieReq.

        配置项的key。

        :param key: The key of this CreateKieReq.
        :type key: str
        """
        self._key = key

    @property
    def labels(self):
        """Gets the labels of this CreateKieReq.

        配置项的标签

        :return: The labels of this CreateKieReq.
        :rtype: object
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this CreateKieReq.

        配置项的标签

        :param labels: The labels of this CreateKieReq.
        :type labels: object
        """
        self._labels = labels

    @property
    def value(self):
        """Gets the value of this CreateKieReq.

        配置项的值。

        :return: The value of this CreateKieReq.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CreateKieReq.

        配置项的值。

        :param value: The value of this CreateKieReq.
        :type value: str
        """
        self._value = value

    @property
    def value_type(self):
        """Gets the value_type of this CreateKieReq.

        配置项value的类型。

        :return: The value_type of this CreateKieReq.
        :rtype: str
        """
        return self._value_type

    @value_type.setter
    def value_type(self, value_type):
        """Sets the value_type of this CreateKieReq.

        配置项value的类型。

        :param value_type: The value_type of this CreateKieReq.
        :type value_type: str
        """
        self._value_type = value_type

    @property
    def status(self):
        """Gets the status of this CreateKieReq.

        配置项的状态。

        :return: The status of this CreateKieReq.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CreateKieReq.

        配置项的状态。

        :param status: The status of this CreateKieReq.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, CreateKieReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
