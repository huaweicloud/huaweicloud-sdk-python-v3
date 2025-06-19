# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowSparkJobRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_id': 'str'
    }

    attribute_map = {
        'batch_id': 'batch_id'
    }

    def __init__(self, batch_id=None):
        r"""ShowSparkJobRequest

        The model defined in huaweicloud sdk

        :param batch_id: 参数解释:  批处理作业的ID 示例: 0a324461-d9d9-45da-a52a-3b3c7a3d809e 约束限制:  无 取值范围: 无 默认取值: 无
        :type batch_id: str
        """
        
        

        self._batch_id = None
        self.discriminator = None

        self.batch_id = batch_id

    @property
    def batch_id(self):
        r"""Gets the batch_id of this ShowSparkJobRequest.

        参数解释:  批处理作业的ID 示例: 0a324461-d9d9-45da-a52a-3b3c7a3d809e 约束限制:  无 取值范围: 无 默认取值: 无

        :return: The batch_id of this ShowSparkJobRequest.
        :rtype: str
        """
        return self._batch_id

    @batch_id.setter
    def batch_id(self, batch_id):
        r"""Sets the batch_id of this ShowSparkJobRequest.

        参数解释:  批处理作业的ID 示例: 0a324461-d9d9-45da-a52a-3b3c7a3d809e 约束限制:  无 取值范围: 无 默认取值: 无

        :param batch_id: The batch_id of this ShowSparkJobRequest.
        :type batch_id: str
        """
        self._batch_id = batch_id

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
        if not isinstance(other, ShowSparkJobRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
