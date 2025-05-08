# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class OperateExecutionRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'execution_id': 'str',
        'operate_type': 'str'
    }

    attribute_map = {
        'execution_id': 'execution_id',
        'operate_type': 'operate_type'
    }

    def __init__(self, execution_id=None, operate_type=None):
        r"""OperateExecutionRequestBody

        The model defined in huaweicloud sdk

        :param execution_id: 工单id
        :type execution_id: str
        :param operate_type: 操作类型，枚举项RESUME,TERMINATE,RETRY,SKIP_BATCH
        :type operate_type: str
        """
        
        

        self._execution_id = None
        self._operate_type = None
        self.discriminator = None

        self.execution_id = execution_id
        self.operate_type = operate_type

    @property
    def execution_id(self):
        r"""Gets the execution_id of this OperateExecutionRequestBody.

        工单id

        :return: The execution_id of this OperateExecutionRequestBody.
        :rtype: str
        """
        return self._execution_id

    @execution_id.setter
    def execution_id(self, execution_id):
        r"""Sets the execution_id of this OperateExecutionRequestBody.

        工单id

        :param execution_id: The execution_id of this OperateExecutionRequestBody.
        :type execution_id: str
        """
        self._execution_id = execution_id

    @property
    def operate_type(self):
        r"""Gets the operate_type of this OperateExecutionRequestBody.

        操作类型，枚举项RESUME,TERMINATE,RETRY,SKIP_BATCH

        :return: The operate_type of this OperateExecutionRequestBody.
        :rtype: str
        """
        return self._operate_type

    @operate_type.setter
    def operate_type(self, operate_type):
        r"""Sets the operate_type of this OperateExecutionRequestBody.

        操作类型，枚举项RESUME,TERMINATE,RETRY,SKIP_BATCH

        :param operate_type: The operate_type of this OperateExecutionRequestBody.
        :type operate_type: str
        """
        self._operate_type = operate_type

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
        if not isinstance(other, OperateExecutionRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
