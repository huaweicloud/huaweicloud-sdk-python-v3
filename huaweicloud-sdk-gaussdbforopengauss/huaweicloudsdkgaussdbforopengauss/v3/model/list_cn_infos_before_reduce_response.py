# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListCnInfosBeforeReduceResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'instance_id': 'str',
        'max_reduction_num': 'int',
        'nodes': 'list[CnInfoBeforeReduce]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'max_reduction_num': 'max_reduction_num',
        'nodes': 'nodes'
    }

    def __init__(self, instance_id=None, max_reduction_num=None, nodes=None):
        """ListCnInfosBeforeReduceResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID。
        :type instance_id: str
        :param max_reduction_num: 单次缩容允许最大步长。
        :type max_reduction_num: int
        :param nodes: 节点信息列表。
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CnInfoBeforeReduce`]
        """
        
        super(ListCnInfosBeforeReduceResponse, self).__init__()

        self._instance_id = None
        self._max_reduction_num = None
        self._nodes = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if max_reduction_num is not None:
            self.max_reduction_num = max_reduction_num
        if nodes is not None:
            self.nodes = nodes

    @property
    def instance_id(self):
        """Gets the instance_id of this ListCnInfosBeforeReduceResponse.

        实例ID。

        :return: The instance_id of this ListCnInfosBeforeReduceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListCnInfosBeforeReduceResponse.

        实例ID。

        :param instance_id: The instance_id of this ListCnInfosBeforeReduceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def max_reduction_num(self):
        """Gets the max_reduction_num of this ListCnInfosBeforeReduceResponse.

        单次缩容允许最大步长。

        :return: The max_reduction_num of this ListCnInfosBeforeReduceResponse.
        :rtype: int
        """
        return self._max_reduction_num

    @max_reduction_num.setter
    def max_reduction_num(self, max_reduction_num):
        """Sets the max_reduction_num of this ListCnInfosBeforeReduceResponse.

        单次缩容允许最大步长。

        :param max_reduction_num: The max_reduction_num of this ListCnInfosBeforeReduceResponse.
        :type max_reduction_num: int
        """
        self._max_reduction_num = max_reduction_num

    @property
    def nodes(self):
        """Gets the nodes of this ListCnInfosBeforeReduceResponse.

        节点信息列表。

        :return: The nodes of this ListCnInfosBeforeReduceResponse.
        :rtype: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CnInfoBeforeReduce`]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        """Sets the nodes of this ListCnInfosBeforeReduceResponse.

        节点信息列表。

        :param nodes: The nodes of this ListCnInfosBeforeReduceResponse.
        :type nodes: list[:class:`huaweicloudsdkgaussdbforopengauss.v3.CnInfoBeforeReduce`]
        """
        self._nodes = nodes

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
        if not isinstance(other, ListCnInfosBeforeReduceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
