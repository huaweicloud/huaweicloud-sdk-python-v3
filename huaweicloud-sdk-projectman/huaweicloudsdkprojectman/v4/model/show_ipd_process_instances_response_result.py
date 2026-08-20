# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowIpdProcessInstancesResponseResult:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'total': 'int',
        'process_instances': 'list[ShowIpdProcessInstancesResponseResultProcessInstances]'
    }

    attribute_map = {
        'total': 'total',
        'process_instances': 'process_instances'
    }

    def __init__(self, total=None, process_instances=None):
        r"""ShowIpdProcessInstancesResponseResult

        The model defined in huaweicloud sdk

        :param total: 总数。
        :type total: int
        :param process_instances: 评审单列表。
        :type process_instances: list[:class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultProcessInstances`]
        """
        
        

        self._total = None
        self._process_instances = None
        self.discriminator = None

        if total is not None:
            self.total = total
        if process_instances is not None:
            self.process_instances = process_instances

    @property
    def total(self):
        r"""Gets the total of this ShowIpdProcessInstancesResponseResult.

        总数。

        :return: The total of this ShowIpdProcessInstancesResponseResult.
        :rtype: int
        """
        return self._total

    @total.setter
    def total(self, total):
        r"""Sets the total of this ShowIpdProcessInstancesResponseResult.

        总数。

        :param total: The total of this ShowIpdProcessInstancesResponseResult.
        :type total: int
        """
        self._total = total

    @property
    def process_instances(self):
        r"""Gets the process_instances of this ShowIpdProcessInstancesResponseResult.

        评审单列表。

        :return: The process_instances of this ShowIpdProcessInstancesResponseResult.
        :rtype: list[:class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultProcessInstances`]
        """
        return self._process_instances

    @process_instances.setter
    def process_instances(self, process_instances):
        r"""Sets the process_instances of this ShowIpdProcessInstancesResponseResult.

        评审单列表。

        :param process_instances: The process_instances of this ShowIpdProcessInstancesResponseResult.
        :type process_instances: list[:class:`huaweicloudsdkprojectman.v4.ShowIpdProcessInstancesResponseResultProcessInstances`]
        """
        self._process_instances = process_instances

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ShowIpdProcessInstancesResponseResult):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
