# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class StopGcTaskRequest:

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
        'gc_id': 'int'
    }

    attribute_map = {
        'instance_id': 'instance_id',
        'gc_id': 'gc_id'
    }

    def __init__(self, instance_id=None, gc_id=None):
        r"""StopGcTaskRequest

        The model defined in huaweicloud sdk

        :param instance_id: 企业仓库实例ID
        :type instance_id: str
        :param gc_id: 任务ID
        :type gc_id: int
        """
        
        

        self._instance_id = None
        self._gc_id = None
        self.discriminator = None

        self.instance_id = instance_id
        self.gc_id = gc_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this StopGcTaskRequest.

        企业仓库实例ID

        :return: The instance_id of this StopGcTaskRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this StopGcTaskRequest.

        企业仓库实例ID

        :param instance_id: The instance_id of this StopGcTaskRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def gc_id(self):
        r"""Gets the gc_id of this StopGcTaskRequest.

        任务ID

        :return: The gc_id of this StopGcTaskRequest.
        :rtype: int
        """
        return self._gc_id

    @gc_id.setter
    def gc_id(self, gc_id):
        r"""Sets the gc_id of this StopGcTaskRequest.

        任务ID

        :param gc_id: The gc_id of this StopGcTaskRequest.
        :type gc_id: int
        """
        self._gc_id = gc_id

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
        if not isinstance(other, StopGcTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
