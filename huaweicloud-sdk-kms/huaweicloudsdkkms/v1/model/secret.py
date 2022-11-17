# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Secret:

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
        'state': 'str',
        'kms_key_id': 'str',
        'description': 'str',
        'create_time': 'int',
        'update_time': 'int',
        'scheduled_delete_time': 'int'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'state': 'state',
        'kms_key_id': 'kms_key_id',
        'description': 'description',
        'create_time': 'create_time',
        'update_time': 'update_time',
        'scheduled_delete_time': 'scheduled_delete_time'
    }

    def __init__(self, id=None, name=None, state=None, kms_key_id=None, description=None, create_time=None, update_time=None, scheduled_delete_time=None):
        """Secret

        The model defined in huaweicloud sdk

        :param id: 凭据的资源标识符。
        :type id: str
        :param name: 凭据名称。
        :type name: str
        :param state: 凭据状态，取值如下：  ENABLED：表示启用状态  DISABLED：表示禁用状态  PENDING_DELETE：表示待删除状态  FROZEN：表示冻结状态状态 
        :type state: str
        :param kms_key_id: 用于加密凭据值的KMS主密钥的ID值。 
        :type kms_key_id: str
        :param description: 凭据的描述信息。
        :type description: str
        :param create_time: 凭据创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 
        :type create_time: int
        :param update_time: 凭据上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type update_time: int
        :param scheduled_delete_time: 凭据计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。  凭据不在删除计划中时，本项值为null。 
        :type scheduled_delete_time: int
        """
        
        

        self._id = None
        self._name = None
        self._state = None
        self._kms_key_id = None
        self._description = None
        self._create_time = None
        self._update_time = None
        self._scheduled_delete_time = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if state is not None:
            self.state = state
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        if description is not None:
            self.description = description
        if create_time is not None:
            self.create_time = create_time
        if update_time is not None:
            self.update_time = update_time
        if scheduled_delete_time is not None:
            self.scheduled_delete_time = scheduled_delete_time

    @property
    def id(self):
        """Gets the id of this Secret.

        凭据的资源标识符。

        :return: The id of this Secret.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Secret.

        凭据的资源标识符。

        :param id: The id of this Secret.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this Secret.

        凭据名称。

        :return: The name of this Secret.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Secret.

        凭据名称。

        :param name: The name of this Secret.
        :type name: str
        """
        self._name = name

    @property
    def state(self):
        """Gets the state of this Secret.

        凭据状态，取值如下：  ENABLED：表示启用状态  DISABLED：表示禁用状态  PENDING_DELETE：表示待删除状态  FROZEN：表示冻结状态状态 

        :return: The state of this Secret.
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Secret.

        凭据状态，取值如下：  ENABLED：表示启用状态  DISABLED：表示禁用状态  PENDING_DELETE：表示待删除状态  FROZEN：表示冻结状态状态 

        :param state: The state of this Secret.
        :type state: str
        """
        self._state = state

    @property
    def kms_key_id(self):
        """Gets the kms_key_id of this Secret.

        用于加密凭据值的KMS主密钥的ID值。 

        :return: The kms_key_id of this Secret.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """Sets the kms_key_id of this Secret.

        用于加密凭据值的KMS主密钥的ID值。 

        :param kms_key_id: The kms_key_id of this Secret.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def description(self):
        """Gets the description of this Secret.

        凭据的描述信息。

        :return: The description of this Secret.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Secret.

        凭据的描述信息。

        :param description: The description of this Secret.
        :type description: str
        """
        self._description = description

    @property
    def create_time(self):
        """Gets the create_time of this Secret.

        凭据创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 

        :return: The create_time of this Secret.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this Secret.

        凭据创建时间，时间戳，即从1970年1月1日至该时间的总秒数。 

        :param create_time: The create_time of this Secret.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def update_time(self):
        """Gets the update_time of this Secret.

        凭据上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The update_time of this Secret.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this Secret.

        凭据上次更新时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param update_time: The update_time of this Secret.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def scheduled_delete_time(self):
        """Gets the scheduled_delete_time of this Secret.

        凭据计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。  凭据不在删除计划中时，本项值为null。 

        :return: The scheduled_delete_time of this Secret.
        :rtype: int
        """
        return self._scheduled_delete_time

    @scheduled_delete_time.setter
    def scheduled_delete_time(self, scheduled_delete_time):
        """Sets the scheduled_delete_time of this Secret.

        凭据计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。  凭据不在删除计划中时，本项值为null。 

        :param scheduled_delete_time: The scheduled_delete_time of this Secret.
        :type scheduled_delete_time: int
        """
        self._scheduled_delete_time = scheduled_delete_time

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
        if not isinstance(other, Secret):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
