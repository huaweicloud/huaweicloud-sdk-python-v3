# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CreateQueueRequestBodyProperties:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'compute_engine_spark_native_enabled': 'str'
    }

    attribute_map = {
        'compute_engine_spark_native_enabled': 'computeEngine.spark.nativeEnabled'
    }

    def __init__(self, compute_engine_spark_native_enabled=None):
        r"""CreateQueueRequestBodyProperties

        The model defined in huaweicloud sdk

        :param compute_engine_spark_native_enabled: 是否使用DLI Native。当前只涉及开启两种算子：Scan 和 Filter。修改现有队列的本属性，需要重启队列才会生效。
        :type compute_engine_spark_native_enabled: str
        """
        
        

        self._compute_engine_spark_native_enabled = None
        self.discriminator = None

        if compute_engine_spark_native_enabled is not None:
            self.compute_engine_spark_native_enabled = compute_engine_spark_native_enabled

    @property
    def compute_engine_spark_native_enabled(self):
        r"""Gets the compute_engine_spark_native_enabled of this CreateQueueRequestBodyProperties.

        是否使用DLI Native。当前只涉及开启两种算子：Scan 和 Filter。修改现有队列的本属性，需要重启队列才会生效。

        :return: The compute_engine_spark_native_enabled of this CreateQueueRequestBodyProperties.
        :rtype: str
        """
        return self._compute_engine_spark_native_enabled

    @compute_engine_spark_native_enabled.setter
    def compute_engine_spark_native_enabled(self, compute_engine_spark_native_enabled):
        r"""Sets the compute_engine_spark_native_enabled of this CreateQueueRequestBodyProperties.

        是否使用DLI Native。当前只涉及开启两种算子：Scan 和 Filter。修改现有队列的本属性，需要重启队列才会生效。

        :param compute_engine_spark_native_enabled: The compute_engine_spark_native_enabled of this CreateQueueRequestBodyProperties.
        :type compute_engine_spark_native_enabled: str
        """
        self._compute_engine_spark_native_enabled = compute_engine_spark_native_enabled

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
        if not isinstance(other, CreateQueueRequestBodyProperties):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
