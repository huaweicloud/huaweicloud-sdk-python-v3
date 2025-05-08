# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class RestartInstanceResponse(SdkResponse):

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
        'nodes': 'list[str]',
        'result': 'str'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'nodes': 'nodes',
        'result': 'result'
    }

    def __init__(self, instance_id=None, nodes=None, result=None):
        r"""RestartInstanceResponse

        The model defined in huaweicloud sdk

        :param instance_id: 实例ID
        :type instance_id: str
        :param nodes: node列表
        :type nodes: list[str]
        :param result: 结果
        :type result: str
        """
        
        super(RestartInstanceResponse, self).__init__()

        self._instance_id = None
        self._nodes = None
        self._result = None
        self.discriminator = None

        if instance_id is not None:
            self.instance_id = instance_id
        if nodes is not None:
            self.nodes = nodes
        if result is not None:
            self.result = result

    @property
    def instance_id(self):
        r"""Gets the instance_id of this RestartInstanceResponse.

        实例ID

        :return: The instance_id of this RestartInstanceResponse.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this RestartInstanceResponse.

        实例ID

        :param instance_id: The instance_id of this RestartInstanceResponse.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def nodes(self):
        r"""Gets the nodes of this RestartInstanceResponse.

        node列表

        :return: The nodes of this RestartInstanceResponse.
        :rtype: list[str]
        """
        return self._nodes

    @nodes.setter
    def nodes(self, nodes):
        r"""Sets the nodes of this RestartInstanceResponse.

        node列表

        :param nodes: The nodes of this RestartInstanceResponse.
        :type nodes: list[str]
        """
        self._nodes = nodes

    @property
    def result(self):
        r"""Gets the result of this RestartInstanceResponse.

        结果

        :return: The result of this RestartInstanceResponse.
        :rtype: str
        """
        return self._result

    @result.setter
    def result(self, result):
        r"""Sets the result of this RestartInstanceResponse.

        结果

        :param result: The result of this RestartInstanceResponse.
        :type result: str
        """
        self._result = result

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
        if not isinstance(other, RestartInstanceResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
