# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DatapointResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'datapoint_name': 'str',
        'datapoint_values': 'list[str]'
    }

    attribute_map = {
        'datapoint_name': 'datapoint_name',
        'datapoint_values': 'datapoint_values'
    }

    def __init__(self, datapoint_name=None, datapoint_values=None):
        r"""DatapointResult

        The model defined in huaweicloud sdk

        :param datapoint_name: **参数解释**: 指标项名，实例指标用实例ID、节点指标用节点名称、组件指标用组件名称。 **取值范围**: 不涉及。
        :type datapoint_name: str
        :param datapoint_values: **参数解释**: 指标值集合。
        :type datapoint_values: list[str]
        """
        
        

        self._datapoint_name = None
        self._datapoint_values = None
        self.discriminator = None

        self.datapoint_name = datapoint_name
        self.datapoint_values = datapoint_values

    @property
    def datapoint_name(self):
        r"""Gets the datapoint_name of this DatapointResult.

        **参数解释**: 指标项名，实例指标用实例ID、节点指标用节点名称、组件指标用组件名称。 **取值范围**: 不涉及。

        :return: The datapoint_name of this DatapointResult.
        :rtype: str
        """
        return self._datapoint_name

    @datapoint_name.setter
    def datapoint_name(self, datapoint_name):
        r"""Sets the datapoint_name of this DatapointResult.

        **参数解释**: 指标项名，实例指标用实例ID、节点指标用节点名称、组件指标用组件名称。 **取值范围**: 不涉及。

        :param datapoint_name: The datapoint_name of this DatapointResult.
        :type datapoint_name: str
        """
        self._datapoint_name = datapoint_name

    @property
    def datapoint_values(self):
        r"""Gets the datapoint_values of this DatapointResult.

        **参数解释**: 指标值集合。

        :return: The datapoint_values of this DatapointResult.
        :rtype: list[str]
        """
        return self._datapoint_values

    @datapoint_values.setter
    def datapoint_values(self, datapoint_values):
        r"""Sets the datapoint_values of this DatapointResult.

        **参数解释**: 指标值集合。

        :param datapoint_values: The datapoint_values of this DatapointResult.
        :type datapoint_values: list[str]
        """
        self._datapoint_values = datapoint_values

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
        if not isinstance(other, DatapointResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
