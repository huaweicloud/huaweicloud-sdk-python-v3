# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AIApplicationListItem:

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
        'name': 'str',
        'status': 'str',
        'managed_instance_id': 'str'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'managed_instance_id': 'managed_instance_id'
    }

    def __init__(self, id=None, name=None, status=None, managed_instance_id=None):
        r"""AIApplicationListItem

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param status: 
        :type status: str
        :param managed_instance_id: 关联的PG实例ID。
        :type managed_instance_id: str
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._managed_instance_id = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if managed_instance_id is not None:
            self.managed_instance_id = managed_instance_id

    @property
    def id(self):
        r"""Gets the id of this AIApplicationListItem.

        :return: The id of this AIApplicationListItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this AIApplicationListItem.

        :param id: The id of this AIApplicationListItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this AIApplicationListItem.

        :return: The name of this AIApplicationListItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AIApplicationListItem.

        :param name: The name of this AIApplicationListItem.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this AIApplicationListItem.

        :return: The status of this AIApplicationListItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this AIApplicationListItem.

        :param status: The status of this AIApplicationListItem.
        :type status: str
        """
        self._status = status

    @property
    def managed_instance_id(self):
        r"""Gets the managed_instance_id of this AIApplicationListItem.

        关联的PG实例ID。

        :return: The managed_instance_id of this AIApplicationListItem.
        :rtype: str
        """
        return self._managed_instance_id

    @managed_instance_id.setter
    def managed_instance_id(self, managed_instance_id):
        r"""Sets the managed_instance_id of this AIApplicationListItem.

        关联的PG实例ID。

        :param managed_instance_id: The managed_instance_id of this AIApplicationListItem.
        :type managed_instance_id: str
        """
        self._managed_instance_id = managed_instance_id

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
        if not isinstance(other, AIApplicationListItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
