# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteLtsConfigsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_ids': 'list[str]',
        'log_type': 'str'
    }

    attribute_map = {
        'instance_ids': 'instance_ids',
        'log_type': 'log_type'
    }

    def __init__(self, instance_ids=None, log_type=None):
        """DeleteLtsConfigsRequestBody

        The model defined in huaweicloud sdk

        :param instance_ids: 需要解除关联的实例ID列表。
        :type instance_ids: list[str]
        :param log_type: 日志类型。slow_log表示慢日志。
        :type log_type: str
        """
        
        

        self._instance_ids = None
        self._log_type = None
        self.discriminator = None

        self.instance_ids = instance_ids
        self.log_type = log_type

    @property
    def instance_ids(self):
        """Gets the instance_ids of this DeleteLtsConfigsRequestBody.

        需要解除关联的实例ID列表。

        :return: The instance_ids of this DeleteLtsConfigsRequestBody.
        :rtype: list[str]
        """
        return self._instance_ids

    @instance_ids.setter
    def instance_ids(self, instance_ids):
        """Sets the instance_ids of this DeleteLtsConfigsRequestBody.

        需要解除关联的实例ID列表。

        :param instance_ids: The instance_ids of this DeleteLtsConfigsRequestBody.
        :type instance_ids: list[str]
        """
        self._instance_ids = instance_ids

    @property
    def log_type(self):
        """Gets the log_type of this DeleteLtsConfigsRequestBody.

        日志类型。slow_log表示慢日志。

        :return: The log_type of this DeleteLtsConfigsRequestBody.
        :rtype: str
        """
        return self._log_type

    @log_type.setter
    def log_type(self, log_type):
        """Sets the log_type of this DeleteLtsConfigsRequestBody.

        日志类型。slow_log表示慢日志。

        :param log_type: The log_type of this DeleteLtsConfigsRequestBody.
        :type log_type: str
        """
        self._log_type = log_type

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
        if not isinstance(other, DeleteLtsConfigsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
