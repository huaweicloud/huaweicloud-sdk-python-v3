# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateGraphReqGraphEncryption:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'enable': 'bool',
        'master_key_id': 'str'
    }

    attribute_map = {
        'enable': 'enable',
        'master_key_id': 'master_key_id'
    }

    def __init__(self, enable=None, master_key_id=None):
        """CreateGraphReqGraphEncryption

        The model defined in huaweicloud sdk

        :param enable: 是否启动加密特性。取值为“true”或者“false”。默认为“false”。
        :type enable: bool
        :param master_key_id: 与建图对应的project下，华为云数据加密服务创建的用户主密钥ID。
        :type master_key_id: str
        """
        
        

        self._enable = None
        self._master_key_id = None
        self.discriminator = None

        if enable is not None:
            self.enable = enable
        if master_key_id is not None:
            self.master_key_id = master_key_id

    @property
    def enable(self):
        """Gets the enable of this CreateGraphReqGraphEncryption.

        是否启动加密特性。取值为“true”或者“false”。默认为“false”。

        :return: The enable of this CreateGraphReqGraphEncryption.
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this CreateGraphReqGraphEncryption.

        是否启动加密特性。取值为“true”或者“false”。默认为“false”。

        :param enable: The enable of this CreateGraphReqGraphEncryption.
        :type enable: bool
        """
        self._enable = enable

    @property
    def master_key_id(self):
        """Gets the master_key_id of this CreateGraphReqGraphEncryption.

        与建图对应的project下，华为云数据加密服务创建的用户主密钥ID。

        :return: The master_key_id of this CreateGraphReqGraphEncryption.
        :rtype: str
        """
        return self._master_key_id

    @master_key_id.setter
    def master_key_id(self, master_key_id):
        """Sets the master_key_id of this CreateGraphReqGraphEncryption.

        与建图对应的project下，华为云数据加密服务创建的用户主密钥ID。

        :param master_key_id: The master_key_id of this CreateGraphReqGraphEncryption.
        :type master_key_id: str
        """
        self._master_key_id = master_key_id

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
        if not isinstance(other, CreateGraphReqGraphEncryption):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
