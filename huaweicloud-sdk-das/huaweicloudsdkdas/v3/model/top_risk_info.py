# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TopRiskInfo:

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
        'instance_name': 'str',
        'node_id': 'str',
        'metric_names': 'list[str]',
        'metric_values': 'list[float]'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'instance_name': 'instance_name',
        'node_id': 'node_id',
        'metric_names': 'metric_names',
        'metric_values': 'metric_values'
    }

    def __init__(self, instance_id=None, instance_name=None, node_id=None, metric_names=None, metric_values=None):
        r"""TopRiskInfo

        The model defined in huaweicloud sdk

        :param instance_id: 实例id。
        :type instance_id: str
        :param instance_name: 实例名称。
        :type instance_name: str
        :param node_id: 节点ID。
        :type node_id: str
        :param metric_names: 指标名称。
        :type metric_names: list[str]
        :param metric_values: 指标值,单位%。
        :type metric_values: list[float]
        """
        
        

        self._instance_id = None
        self._instance_name = None
        self._node_id = None
        self._metric_names = None
        self._metric_values = None
        self.discriminator = None

        self.instance_id = instance_id
        self.instance_name = instance_name
        self.node_id = node_id
        self.metric_names = metric_names
        self.metric_values = metric_values

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TopRiskInfo.

        实例id。

        :return: The instance_id of this TopRiskInfo.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TopRiskInfo.

        实例id。

        :param instance_id: The instance_id of this TopRiskInfo.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def instance_name(self):
        r"""Gets the instance_name of this TopRiskInfo.

        实例名称。

        :return: The instance_name of this TopRiskInfo.
        :rtype: str
        """
        return self._instance_name

    @instance_name.setter
    def instance_name(self, instance_name):
        r"""Sets the instance_name of this TopRiskInfo.

        实例名称。

        :param instance_name: The instance_name of this TopRiskInfo.
        :type instance_name: str
        """
        self._instance_name = instance_name

    @property
    def node_id(self):
        r"""Gets the node_id of this TopRiskInfo.

        节点ID。

        :return: The node_id of this TopRiskInfo.
        :rtype: str
        """
        return self._node_id

    @node_id.setter
    def node_id(self, node_id):
        r"""Sets the node_id of this TopRiskInfo.

        节点ID。

        :param node_id: The node_id of this TopRiskInfo.
        :type node_id: str
        """
        self._node_id = node_id

    @property
    def metric_names(self):
        r"""Gets the metric_names of this TopRiskInfo.

        指标名称。

        :return: The metric_names of this TopRiskInfo.
        :rtype: list[str]
        """
        return self._metric_names

    @metric_names.setter
    def metric_names(self, metric_names):
        r"""Sets the metric_names of this TopRiskInfo.

        指标名称。

        :param metric_names: The metric_names of this TopRiskInfo.
        :type metric_names: list[str]
        """
        self._metric_names = metric_names

    @property
    def metric_values(self):
        r"""Gets the metric_values of this TopRiskInfo.

        指标值,单位%。

        :return: The metric_values of this TopRiskInfo.
        :rtype: list[float]
        """
        return self._metric_values

    @metric_values.setter
    def metric_values(self, metric_values):
        r"""Sets the metric_values of this TopRiskInfo.

        指标值,单位%。

        :param metric_values: The metric_values of this TopRiskInfo.
        :type metric_values: list[float]
        """
        self._metric_values = metric_values

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
        if not isinstance(other, TopRiskInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
