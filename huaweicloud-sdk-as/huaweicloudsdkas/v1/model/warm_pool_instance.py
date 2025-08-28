# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class WarmPoolInstance:

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
        'instance_id': 'str',
        'name': 'str',
        'status': 'str'
    }

    attribute_map = {
        'id': 'id',
        'instance_id': 'instance_id',
        'name': 'name',
        'status': 'status'
    }

    def __init__(self, id=None, instance_id=None, name=None, status=None):
        r"""WarmPoolInstance

        The model defined in huaweicloud sdk

        :param id: 暖池实例ID
        :type id: str
        :param instance_id: 对应的虚拟机ID
        :type instance_id: str
        :param name: 暖池实例的名称
        :type name: str
        :param status: 暖池实例的状态
        :type status: str
        """
        
        

        self._id = None
        self._instance_id = None
        self._name = None
        self._status = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if instance_id is not None:
            self.instance_id = instance_id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status

    @property
    def id(self):
        r"""Gets the id of this WarmPoolInstance.

        暖池实例ID

        :return: The id of this WarmPoolInstance.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this WarmPoolInstance.

        暖池实例ID

        :param id: The id of this WarmPoolInstance.
        :type id: str
        """
        self._id = id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this WarmPoolInstance.

        对应的虚拟机ID

        :return: The instance_id of this WarmPoolInstance.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this WarmPoolInstance.

        对应的虚拟机ID

        :param instance_id: The instance_id of this WarmPoolInstance.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def name(self):
        r"""Gets the name of this WarmPoolInstance.

        暖池实例的名称

        :return: The name of this WarmPoolInstance.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this WarmPoolInstance.

        暖池实例的名称

        :param name: The name of this WarmPoolInstance.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        r"""Gets the status of this WarmPoolInstance.

        暖池实例的状态

        :return: The status of this WarmPoolInstance.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this WarmPoolInstance.

        暖池实例的状态

        :param status: The status of this WarmPoolInstance.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, WarmPoolInstance):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
