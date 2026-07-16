# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIServiceInstance:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'status': 'str',
        'endpoints': 'str'
    }

    attribute_map = {
        'id': 'id',
        'status': 'status',
        'endpoints': 'endpoints'
    }

    def __init__(self, id=None, status=None, endpoints=None):
        r"""AIServiceInstance

        The model defined in huaweicloud sdk

        :param id: **参数解释**：部署实例id。 **取值范围**：不涉及。
        :type id: str
        :param status: **参数解释**：部署实例状态。 **取值范围**：- CREATING - RUNNING  - FAILED  -DELETED - ERROR
        :type status: str
        :param endpoints: **参数解释**：调用方式信息。 **取值范围**：不涉及。
        :type endpoints: str
        """
        
        

        self._id = None
        self._status = None
        self._endpoints = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if status is not None:
            self.status = status
        if endpoints is not None:
            self.endpoints = endpoints

    @property
    def id(self):
        r"""Gets the id of this AIServiceInstance.

        **参数解释**：部署实例id。 **取值范围**：不涉及。

        :return: The id of this AIServiceInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AIServiceInstance.

        **参数解释**：部署实例id。 **取值范围**：不涉及。

        :param id: The id of this AIServiceInstance.
        :type id: str
        """
        self._id = id

    @property
    def status(self):
        r"""Gets the status of this AIServiceInstance.

        **参数解释**：部署实例状态。 **取值范围**：- CREATING - RUNNING  - FAILED  -DELETED - ERROR

        :return: The status of this AIServiceInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AIServiceInstance.

        **参数解释**：部署实例状态。 **取值范围**：- CREATING - RUNNING  - FAILED  -DELETED - ERROR

        :param status: The status of this AIServiceInstance.
        :type status: str
        """
        self._status = status

    @property
    def endpoints(self):
        r"""Gets the endpoints of this AIServiceInstance.

        **参数解释**：调用方式信息。 **取值范围**：不涉及。

        :return: The endpoints of this AIServiceInstance.
        :rtype: str
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        r"""Sets the endpoints of this AIServiceInstance.

        **参数解释**：调用方式信息。 **取值范围**：不涉及。

        :param endpoints: The endpoints of this AIServiceInstance.
        :type endpoints: str
        """
        self._endpoints = endpoints

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
        if not isinstance(other, AIServiceInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
