# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class SupabaseApplicationApiKeyRecord:

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
        'remark': 'str',
        'status': 'str',
        'type': 'str',
        'created_user': 'str',
        'updated_user': 'str',
        'created_time': 'int',
        'updated_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'remark': 'remark',
        'status': 'status',
        'type': 'type',
        'created_user': 'created_user',
        'updated_user': 'updated_user',
        'created_time': 'created_time',
        'updated_time': 'updated_time'
    }

    def __init__(self, id=None, name=None, remark=None, status=None, type=None, created_user=None, updated_user=None, created_time=None, updated_time=None):
        r"""SupabaseApplicationApiKeyRecord

        The model defined in huaweicloud sdk

        :param id: 
        :type id: str
        :param name: 
        :type name: str
        :param remark: 
        :type remark: str
        :param status: 
        :type status: str
        :param type: 
        :type type: str
        :param created_user: 
        :type created_user: str
        :param updated_user: 
        :type updated_user: str
        :param created_time: 
        :type created_time: int
        :param updated_time: 
        :type updated_time: int
        """
        
        

        self._id = None
        self._name = None
        self._remark = None
        self._status = None
        self._type = None
        self._created_user = None
        self._updated_user = None
        self._created_time = None
        self._updated_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if remark is not None:
            self.remark = remark
        if status is not None:
            self.status = status
        if type is not None:
            self.type = type
        if created_user is not None:
            self.created_user = created_user
        if updated_user is not None:
            self.updated_user = updated_user
        if created_time is not None:
            self.created_time = created_time
        if updated_time is not None:
            self.updated_time = updated_time

    @property
    def id(self):
        r"""Gets the id of this SupabaseApplicationApiKeyRecord.

        :return: The id of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        r"""Sets the id of this SupabaseApplicationApiKeyRecord.

        :param id: The id of this SupabaseApplicationApiKeyRecord.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        r"""Gets the name of this SupabaseApplicationApiKeyRecord.

        :return: The name of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this SupabaseApplicationApiKeyRecord.

        :param name: The name of this SupabaseApplicationApiKeyRecord.
        :type name: str
        """
        self._name = name

    @property
    def remark(self):
        r"""Gets the remark of this SupabaseApplicationApiKeyRecord.

        :return: The remark of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._remark

    @remark.setter
    def remark(self, remark):
        r"""Sets the remark of this SupabaseApplicationApiKeyRecord.

        :param remark: The remark of this SupabaseApplicationApiKeyRecord.
        :type remark: str
        """
        self._remark = remark

    @property
    def status(self):
        r"""Gets the status of this SupabaseApplicationApiKeyRecord.

        :return: The status of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this SupabaseApplicationApiKeyRecord.

        :param status: The status of this SupabaseApplicationApiKeyRecord.
        :type status: str
        """
        self._status = status

    @property
    def type(self):
        r"""Gets the type of this SupabaseApplicationApiKeyRecord.

        :return: The type of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        r"""Sets the type of this SupabaseApplicationApiKeyRecord.

        :param type: The type of this SupabaseApplicationApiKeyRecord.
        :type type: str
        """
        self._type = type

    @property
    def created_user(self):
        r"""Gets the created_user of this SupabaseApplicationApiKeyRecord.

        :return: The created_user of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._created_user

    @created_user.setter
    def created_user(self, created_user):
        r"""Sets the created_user of this SupabaseApplicationApiKeyRecord.

        :param created_user: The created_user of this SupabaseApplicationApiKeyRecord.
        :type created_user: str
        """
        self._created_user = created_user

    @property
    def updated_user(self):
        r"""Gets the updated_user of this SupabaseApplicationApiKeyRecord.

        :return: The updated_user of this SupabaseApplicationApiKeyRecord.
        :rtype: str
        """
        return self._updated_user

    @updated_user.setter
    def updated_user(self, updated_user):
        r"""Sets the updated_user of this SupabaseApplicationApiKeyRecord.

        :param updated_user: The updated_user of this SupabaseApplicationApiKeyRecord.
        :type updated_user: str
        """
        self._updated_user = updated_user

    @property
    def created_time(self):
        r"""Gets the created_time of this SupabaseApplicationApiKeyRecord.

        :return: The created_time of this SupabaseApplicationApiKeyRecord.
        :rtype: int
        """
        return self._created_time

    @created_time.setter
    def created_time(self, created_time):
        r"""Sets the created_time of this SupabaseApplicationApiKeyRecord.

        :param created_time: The created_time of this SupabaseApplicationApiKeyRecord.
        :type created_time: int
        """
        self._created_time = created_time

    @property
    def updated_time(self):
        r"""Gets the updated_time of this SupabaseApplicationApiKeyRecord.

        :return: The updated_time of this SupabaseApplicationApiKeyRecord.
        :rtype: int
        """
        return self._updated_time

    @updated_time.setter
    def updated_time(self, updated_time):
        r"""Sets the updated_time of this SupabaseApplicationApiKeyRecord.

        :param updated_time: The updated_time of this SupabaseApplicationApiKeyRecord.
        :type updated_time: int
        """
        self._updated_time = updated_time

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
        if not isinstance(other, SupabaseApplicationApiKeyRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
