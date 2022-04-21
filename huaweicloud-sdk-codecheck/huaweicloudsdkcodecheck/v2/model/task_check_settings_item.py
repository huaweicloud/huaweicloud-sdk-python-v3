# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TaskCheckSettingsItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'cfg_key': 'str',
        'status': 'str',
        'cfg_value': 'str'
    }

    attribute_map = {
        'cfg_key': 'cfg_key',
        'status': 'status',
        'cfg_value': 'cfg_value'
    }

    def __init__(self, cfg_key=None, status=None, cfg_value=None):
        """TaskCheckSettingsItem

        The model defined in huaweicloud sdk

        :param cfg_key: 检查参数对应的key值
        :type cfg_key: str
        :param status: 参数状态
        :type status: str
        :param cfg_value: 检查参数值
        :type cfg_value: str
        """
        
        

        self._cfg_key = None
        self._status = None
        self._cfg_value = None
        self.discriminator = None

        self.cfg_key = cfg_key
        self.status = status
        if cfg_value is not None:
            self.cfg_value = cfg_value

    @property
    def cfg_key(self):
        """Gets the cfg_key of this TaskCheckSettingsItem.

        检查参数对应的key值

        :return: The cfg_key of this TaskCheckSettingsItem.
        :rtype: str
        """
        return self._cfg_key

    @cfg_key.setter
    def cfg_key(self, cfg_key):
        """Sets the cfg_key of this TaskCheckSettingsItem.

        检查参数对应的key值

        :param cfg_key: The cfg_key of this TaskCheckSettingsItem.
        :type cfg_key: str
        """
        self._cfg_key = cfg_key

    @property
    def status(self):
        """Gets the status of this TaskCheckSettingsItem.

        参数状态

        :return: The status of this TaskCheckSettingsItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaskCheckSettingsItem.

        参数状态

        :param status: The status of this TaskCheckSettingsItem.
        :type status: str
        """
        self._status = status

    @property
    def cfg_value(self):
        """Gets the cfg_value of this TaskCheckSettingsItem.

        检查参数值

        :return: The cfg_value of this TaskCheckSettingsItem.
        :rtype: str
        """
        return self._cfg_value

    @cfg_value.setter
    def cfg_value(self, cfg_value):
        """Sets the cfg_value of this TaskCheckSettingsItem.

        检查参数值

        :param cfg_value: The cfg_value of this TaskCheckSettingsItem.
        :type cfg_value: str
        """
        self._cfg_value = cfg_value

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
        if not isinstance(other, TaskCheckSettingsItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
