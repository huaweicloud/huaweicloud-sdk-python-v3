# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SyncLimitDataResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'result': 'str',
        'instance_id': 'str',
        'node_id': 'str',
        'total_count': 'int'
    }

    attribute_map = {
        'result': 'result',
        'instance_id': 'instance_id',
        'node_id': 'node_id',
        'total_count': 'total_count'
    }

    def __init__(self, result=None, instance_id=None, node_id=None, total_count=None):
        r"""SyncLimitDataResponse

        The model defined in huaweicloud sdk

        :param result: 同步结果，success成功，fail失败
        :type result: str
        :param instance_id: 同步数据的实例ID
        :type instance_id: str
        :param node_id: 同步数据的节点ID，集中式表示主节点ID，分布式表示CN节点ID
        :type node_id: str
        :param total_count: 同步的数据记录总数
        :type total_count: int
        """
        
        super(SyncLimitDataResponse, self).__init__()

        self._result = None
        self._instance_id = None
        self._node_id = None
        self._total_count = None
        self.discriminator = None

        if result is not None:
            self.result = result
        if instance_id is not None:
            self.instance_id = instance_id
        if node_id is not None:
            self.node_id = node_id
        if total_count is not None:
            self.total_count = total_count

    @property
    def result(self):
        r"""Gets the result of this SyncLimitDataResponse.

        同步结果，success成功，fail失败

        :return: The result of this SyncLimitDataResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this SyncLimitDataResponse.

        同步结果，success成功，fail失败

        :param result: The result of this SyncLimitDataResponse.
        :type result: str
        """
        self._result = result

    @property
    def instance_id(self):
        r"""Gets the instance_id of this SyncLimitDataResponse.

        同步数据的实例ID

        :return: The instance_id of this SyncLimitDataResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this SyncLimitDataResponse.

        同步数据的实例ID

        :param instance_id: The instance_id of this SyncLimitDataResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def node_id(self):
        r"""Gets the node_id of this SyncLimitDataResponse.

        同步数据的节点ID，集中式表示主节点ID，分布式表示CN节点ID

        :return: The node_id of this SyncLimitDataResponse.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this SyncLimitDataResponse.

        同步数据的节点ID，集中式表示主节点ID，分布式表示CN节点ID

        :param node_id: The node_id of this SyncLimitDataResponse.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def total_count(self):
        r"""Gets the total_count of this SyncLimitDataResponse.

        同步的数据记录总数

        :return: The total_count of this SyncLimitDataResponse.
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        r"""Sets the total_count of this SyncLimitDataResponse.

        同步的数据记录总数

        :param total_count: The total_count of this SyncLimitDataResponse.
        :type total_count: int
        """
        self._total_count = total_count

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
        if not isinstance(other, SyncLimitDataResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
