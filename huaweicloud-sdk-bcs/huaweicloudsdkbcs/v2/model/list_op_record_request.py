# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListOpRecordRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'blockchain_id': 'str',
        'operation_status': 'str',
        'resource_type': 'str',
        'operation_type': 'str',
        'operation_id': 'str'
    }

    attribute_map = {
        'blockchain_id': 'blockchain_id',
        'operation_status': 'operation_status',
        'resource_type': 'resource_type',
        'operation_type': 'operation_type',
        'operation_id': 'operation_id'
    }

    def __init__(self, blockchain_id=None, operation_status=None, resource_type=None, operation_type=None, operation_id=None):
        """ListOpRecordRequest

        The model defined in huaweicloud sdk

        :param blockchain_id: 区块链ID
        :type blockchain_id: str
        :param operation_status: 操作状态, 可选数值如下（括号中为该数值对应的操作状态含义）：waiting(等待执行)，processing（处理中），finished（操作完成，成功），failed（操作失败），stop（操作中断）
        :type operation_status: str
        :param resource_type: 资源类型, 可选数值如下（括号中为该数值对应的资源类型含义）：BCSSVC01（BCS变更操作），BCSSVC02（UGBaaS变更操作），PLUGIN01（RestAPI插件变更操作），PLUGIN02（TC3插件变更操作），PLUGIN03（轻节点插件变更操作）
        :type resource_type: str
        :param operation_type: 操作类型, 可选数值如下（括号中为该数值对应的操作类型含义）：99（OpCreate）,00（OpDelete）,01（OpUpgrade）,91（OpUpgradeRb）,02（OpAddOrg）,03（OpScaleOrg）,04（OpJoinChannel）,05（OpJoinUnion）
        :type operation_type: str
        :param operation_id: 操作记录ID
        :type operation_id: str
        """
        
        

        self._blockchain_id = None
        self._operation_status = None
        self._resource_type = None
        self._operation_type = None
        self._operation_id = None
        self.discriminator = None

        if blockchain_id is not None:
            self.blockchain_id = blockchain_id
        if operation_status is not None:
            self.operation_status = operation_status
        if resource_type is not None:
            self.resource_type = resource_type
        if operation_type is not None:
            self.operation_type = operation_type
        if operation_id is not None:
            self.operation_id = operation_id

    @property
    def blockchain_id(self):
        """Gets the blockchain_id of this ListOpRecordRequest.

        区块链ID

        :return: The blockchain_id of this ListOpRecordRequest.
        :rtype: str
        """
        return self._blockchain_id

    @blockchain_id.setter
    def blockchain_id(self, blockchain_id):
        """Sets the blockchain_id of this ListOpRecordRequest.

        区块链ID

        :param blockchain_id: The blockchain_id of this ListOpRecordRequest.
        :type blockchain_id: str
        """
        self._blockchain_id = blockchain_id

    @property
    def operation_status(self):
        """Gets the operation_status of this ListOpRecordRequest.

        操作状态, 可选数值如下（括号中为该数值对应的操作状态含义）：waiting(等待执行)，processing（处理中），finished（操作完成，成功），failed（操作失败），stop（操作中断）

        :return: The operation_status of this ListOpRecordRequest.
        :rtype: str
        """
        return self._operation_status

    @operation_status.setter
    def operation_status(self, operation_status):
        """Sets the operation_status of this ListOpRecordRequest.

        操作状态, 可选数值如下（括号中为该数值对应的操作状态含义）：waiting(等待执行)，processing（处理中），finished（操作完成，成功），failed（操作失败），stop（操作中断）

        :param operation_status: The operation_status of this ListOpRecordRequest.
        :type operation_status: str
        """
        self._operation_status = operation_status

    @property
    def resource_type(self):
        """Gets the resource_type of this ListOpRecordRequest.

        资源类型, 可选数值如下（括号中为该数值对应的资源类型含义）：BCSSVC01（BCS变更操作），BCSSVC02（UGBaaS变更操作），PLUGIN01（RestAPI插件变更操作），PLUGIN02（TC3插件变更操作），PLUGIN03（轻节点插件变更操作）

        :return: The resource_type of this ListOpRecordRequest.
        :rtype: str
        """
        return self._resource_type

    @resource_type.setter
    def resource_type(self, resource_type):
        """Sets the resource_type of this ListOpRecordRequest.

        资源类型, 可选数值如下（括号中为该数值对应的资源类型含义）：BCSSVC01（BCS变更操作），BCSSVC02（UGBaaS变更操作），PLUGIN01（RestAPI插件变更操作），PLUGIN02（TC3插件变更操作），PLUGIN03（轻节点插件变更操作）

        :param resource_type: The resource_type of this ListOpRecordRequest.
        :type resource_type: str
        """
        self._resource_type = resource_type

    @property
    def operation_type(self):
        """Gets the operation_type of this ListOpRecordRequest.

        操作类型, 可选数值如下（括号中为该数值对应的操作类型含义）：99（OpCreate）,00（OpDelete）,01（OpUpgrade）,91（OpUpgradeRb）,02（OpAddOrg）,03（OpScaleOrg）,04（OpJoinChannel）,05（OpJoinUnion）

        :return: The operation_type of this ListOpRecordRequest.
        :rtype: str
        """
        return self._operation_type

    @operation_type.setter
    def operation_type(self, operation_type):
        """Sets the operation_type of this ListOpRecordRequest.

        操作类型, 可选数值如下（括号中为该数值对应的操作类型含义）：99（OpCreate）,00（OpDelete）,01（OpUpgrade）,91（OpUpgradeRb）,02（OpAddOrg）,03（OpScaleOrg）,04（OpJoinChannel）,05（OpJoinUnion）

        :param operation_type: The operation_type of this ListOpRecordRequest.
        :type operation_type: str
        """
        self._operation_type = operation_type

    @property
    def operation_id(self):
        """Gets the operation_id of this ListOpRecordRequest.

        操作记录ID

        :return: The operation_id of this ListOpRecordRequest.
        :rtype: str
        """
        return self._operation_id

    @operation_id.setter
    def operation_id(self, operation_id):
        """Sets the operation_id of this ListOpRecordRequest.

        操作记录ID

        :param operation_id: The operation_id of this ListOpRecordRequest.
        :type operation_id: str
        """
        self._operation_id = operation_id

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
        if not isinstance(other, ListOpRecordRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
