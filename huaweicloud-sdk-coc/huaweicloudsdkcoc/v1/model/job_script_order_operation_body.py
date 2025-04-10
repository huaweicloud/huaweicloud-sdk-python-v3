# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class JobScriptOrderOperationBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'batch_index': 'int',
        'instance_id': 'int',
        'operation_type': 'str'
    }

    attribute_map = {
        'batch_index': 'batch_index',
        'instance_id': 'instance_id',
        'operation_type': 'operation_type'
    }

    def __init__(self, batch_index=None, instance_id=None, operation_type=None):
        r"""JobScriptOrderOperationBody

        The model defined in huaweicloud sdk

        :param batch_index: 适用于批次操作时
        :type batch_index: int
        :param instance_id: 适用于实例操作时 非script_execute_instance_do中iD，需要新增字段
        :type instance_id: int
        :param operation_type: 操作类型：取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单 CANCEL_INSTANCE：取消实例 SKIP_BATCH：跳过批次 CANCEL_ORDER：取消整个工单 PAUSE_ORDER：暂停整个工单 CONTINUE_ORDER：继续整个工单
        :type operation_type: str
        """
        
        

        self._batch_index = None
        self._instance_id = None
        self._operation_type = None
        self.discriminator = None

        if batch_index is not None:
            self.batch_index = batch_index
        if instance_id is not None:
            self.instance_id = instance_id
        self.operation_type = operation_type

    @property
    def batch_index(self):
        r"""Gets the batch_index of this JobScriptOrderOperationBody.

        适用于批次操作时

        :return: The batch_index of this JobScriptOrderOperationBody.
        :rtype: int
        """
        return self._batch_index

    @batch_index.setter
    def batch_index(self, batch_index):
        r"""Sets the batch_index of this JobScriptOrderOperationBody.

        适用于批次操作时

        :param batch_index: The batch_index of this JobScriptOrderOperationBody.
        :type batch_index: int
        """
        self._batch_index = batch_index

    @property
    def instance_id(self):
        r"""Gets the instance_id of this JobScriptOrderOperationBody.

        适用于实例操作时 非script_execute_instance_do中iD，需要新增字段

        :return: The instance_id of this JobScriptOrderOperationBody.
        :rtype: int
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this JobScriptOrderOperationBody.

        适用于实例操作时 非script_execute_instance_do中iD，需要新增字段

        :param instance_id: The instance_id of this JobScriptOrderOperationBody.
        :type instance_id: int
        """
        self._instance_id = instance_id

    @property
    def operation_type(self):
        r"""Gets the operation_type of this JobScriptOrderOperationBody.

        操作类型：取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单 CANCEL_INSTANCE：取消实例 SKIP_BATCH：跳过批次 CANCEL_ORDER：取消整个工单 PAUSE_ORDER：暂停整个工单 CONTINUE_ORDER：继续整个工单

        :return: The operation_type of this JobScriptOrderOperationBody.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        r"""Sets the operation_type of this JobScriptOrderOperationBody.

        操作类型：取消实例、跳过批次、取消整个工单、暂停整个工单、继续整个工单 CANCEL_INSTANCE：取消实例 SKIP_BATCH：跳过批次 CANCEL_ORDER：取消整个工单 PAUSE_ORDER：暂停整个工单 CONTINUE_ORDER：继续整个工单

        :param operation_type: The operation_type of this JobScriptOrderOperationBody.
        :type operation_type: str
        """
        self._operation_type = operation_type

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
        if not isinstance(other, JobScriptOrderOperationBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
