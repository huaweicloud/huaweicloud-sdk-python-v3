# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyInstanceConfigsReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'kafka_configs': 'list[ModifyInstanceConfig]'
    }

    attribute_map = {
        'kafka_configs': 'kafka_configs'
    }

    def __init__(self, kafka_configs=None):
        """ModifyInstanceConfigsReq

        The model defined in huaweicloud sdk

        :param kafka_configs: kafka待修改配置列表。
        :type kafka_configs: list[:class:`huaweicloudsdkkafka.v2.ModifyInstanceConfig`]
        """
        
        

        self._kafka_configs = None
        self.discriminator = None

        if kafka_configs is not None:
            self.kafka_configs = kafka_configs

    @property
    def kafka_configs(self):
        """Gets the kafka_configs of this ModifyInstanceConfigsReq.

        kafka待修改配置列表。

        :return: The kafka_configs of this ModifyInstanceConfigsReq.
        :rtype: list[:class:`huaweicloudsdkkafka.v2.ModifyInstanceConfig`]
        """
        return self._kafka_configs

    @kafka_configs.setter
    def kafka_configs(self, kafka_configs):
        """Sets the kafka_configs of this ModifyInstanceConfigsReq.

        kafka待修改配置列表。

        :param kafka_configs: The kafka_configs of this ModifyInstanceConfigsReq.
        :type kafka_configs: list[:class:`huaweicloudsdkkafka.v2.ModifyInstanceConfig`]
        """
        self._kafka_configs = kafka_configs

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
        if not isinstance(other, ModifyInstanceConfigsReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
