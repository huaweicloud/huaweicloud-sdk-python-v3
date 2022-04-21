# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeypairDetail:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'name': 'str',
        'id': 'int',
        'type': 'str',
        'scope': 'str',
        'public_key': 'str',
        'fingerprint': 'str',
        'is_key_protection': 'bool',
        'deleted': 'bool',
        'description': 'str',
        'user_id': 'str',
        'create_time': 'int',
        'delete_time': 'int',
        'update_time': 'int',
        'frozen_state': 'int'
    }

    attribute_map = {
        'name': 'name',
        'id': 'id',
        'type': 'type',
        'scope': 'scope',
        'public_key': 'public_key',
        'fingerprint': 'fingerprint',
        'is_key_protection': 'is_key_protection',
        'deleted': 'deleted',
        'description': 'description',
        'user_id': 'user_id',
        'create_time': 'create_time',
        'delete_time': 'delete_time',
        'update_time': 'update_time',
        'frozen_state': 'frozen_state'
    }

    def __init__(self, name=None, id=None, type=None, scope=None, public_key=None, fingerprint=None, is_key_protection=None, deleted=None, description=None, user_id=None, create_time=None, delete_time=None, update_time=None, frozen_state=None):
        """KeypairDetail

        The model defined in huaweicloud sdk

        :param name: SSH密钥对的名称
        :type name: str
        :param id: SSH密钥对的ID
        :type id: int
        :param type: SSH密钥对的类型
        :type type: str
        :param scope: 租户级或者用户级
        :type scope: str
        :param public_key: SSH密钥对对应的publicKey信息
        :type public_key: str
        :param fingerprint: SSH密钥对应指纹信息
        :type fingerprint: str
        :param is_key_protection: 是否托管密钥
        :type is_key_protection: bool
        :param deleted: SSH密钥对删除的标记
        :type deleted: bool
        :param description: SSH密钥对的描述信息
        :type description: str
        :param user_id: SSH密钥对所属的用户信息
        :type user_id: str
        :param create_time: SSH密钥对创建的时间，时间戳，即从1970年1月1日至该时间的总秒数
        :type create_time: int
        :param delete_time: SSH密钥对删除的时间，时间戳，即从1970年1月1日至该时间的总秒数
        :type delete_time: int
        :param update_time: SSH密钥对的更新时间，时间戳，即从1970年1月1日至该时间的总秒数
        :type update_time: int
        :param frozen_state: 冻结状态 - 0：正常状态 - 1：普通冻结 - 2：公安冻结 - 3：普通冻结及公安冻结 - 4：违规冻结 - 5：普通冻结及违规冻结 - 6：公安冻结及违规冻结 - 7：普通冻结、公安冻结及违规冻结 - 8：未实名认证冻结 - 9：普通冻结及未实名认证冻结 - 10：公安冻结及未实名认证冻结
        :type frozen_state: int
        """
        
        

        self._name = None
        self._id = None
        self._type = None
        self._scope = None
        self._public_key = None
        self._fingerprint = None
        self._is_key_protection = None
        self._deleted = None
        self._description = None
        self._user_id = None
        self._create_time = None
        self._delete_time = None
        self._update_time = None
        self._frozen_state = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if id is not None:
            self.id = id
        if type is not None:
            self.type = type
        if scope is not None:
            self.scope = scope
        if public_key is not None:
            self.public_key = public_key
        if fingerprint is not None:
            self.fingerprint = fingerprint
        if is_key_protection is not None:
            self.is_key_protection = is_key_protection
        if deleted is not None:
            self.deleted = deleted
        if description is not None:
            self.description = description
        if user_id is not None:
            self.user_id = user_id
        if create_time is not None:
            self.create_time = create_time
        if delete_time is not None:
            self.delete_time = delete_time
        if update_time is not None:
            self.update_time = update_time
        if frozen_state is not None:
            self.frozen_state = frozen_state

    @property
    def name(self):
        """Gets the name of this KeypairDetail.

        SSH密钥对的名称

        :return: The name of this KeypairDetail.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this KeypairDetail.

        SSH密钥对的名称

        :param name: The name of this KeypairDetail.
        :type name: str
        """
        self._name = name

    @property
    def id(self):
        """Gets the id of this KeypairDetail.

        SSH密钥对的ID

        :return: The id of this KeypairDetail.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this KeypairDetail.

        SSH密钥对的ID

        :param id: The id of this KeypairDetail.
        :type id: int
        """
        self._id = id

    @property
    def type(self):
        """Gets the type of this KeypairDetail.

        SSH密钥对的类型

        :return: The type of this KeypairDetail.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this KeypairDetail.

        SSH密钥对的类型

        :param type: The type of this KeypairDetail.
        :type type: str
        """
        self._type = type

    @property
    def scope(self):
        """Gets the scope of this KeypairDetail.

        租户级或者用户级

        :return: The scope of this KeypairDetail.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this KeypairDetail.

        租户级或者用户级

        :param scope: The scope of this KeypairDetail.
        :type scope: str
        """
        self._scope = scope

    @property
    def public_key(self):
        """Gets the public_key of this KeypairDetail.

        SSH密钥对对应的publicKey信息

        :return: The public_key of this KeypairDetail.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this KeypairDetail.

        SSH密钥对对应的publicKey信息

        :param public_key: The public_key of this KeypairDetail.
        :type public_key: str
        """
        self._public_key = public_key

    @property
    def fingerprint(self):
        """Gets the fingerprint of this KeypairDetail.

        SSH密钥对应指纹信息

        :return: The fingerprint of this KeypairDetail.
        :rtype: str
        """
        return self._fingerprint

    @fingerprint.setter
    def fingerprint(self, fingerprint):
        """Sets the fingerprint of this KeypairDetail.

        SSH密钥对应指纹信息

        :param fingerprint: The fingerprint of this KeypairDetail.
        :type fingerprint: str
        """
        self._fingerprint = fingerprint

    @property
    def is_key_protection(self):
        """Gets the is_key_protection of this KeypairDetail.

        是否托管密钥

        :return: The is_key_protection of this KeypairDetail.
        :rtype: bool
        """
        return self._is_key_protection

    @is_key_protection.setter
    def is_key_protection(self, is_key_protection):
        """Sets the is_key_protection of this KeypairDetail.

        是否托管密钥

        :param is_key_protection: The is_key_protection of this KeypairDetail.
        :type is_key_protection: bool
        """
        self._is_key_protection = is_key_protection

    @property
    def deleted(self):
        """Gets the deleted of this KeypairDetail.

        SSH密钥对删除的标记

        :return: The deleted of this KeypairDetail.
        :rtype: bool
        """
        return self._deleted

    @deleted.setter
    def deleted(self, deleted):
        """Sets the deleted of this KeypairDetail.

        SSH密钥对删除的标记

        :param deleted: The deleted of this KeypairDetail.
        :type deleted: bool
        """
        self._deleted = deleted

    @property
    def description(self):
        """Gets the description of this KeypairDetail.

        SSH密钥对的描述信息

        :return: The description of this KeypairDetail.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this KeypairDetail.

        SSH密钥对的描述信息

        :param description: The description of this KeypairDetail.
        :type description: str
        """
        self._description = description

    @property
    def user_id(self):
        """Gets the user_id of this KeypairDetail.

        SSH密钥对所属的用户信息

        :return: The user_id of this KeypairDetail.
        :rtype: str
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this KeypairDetail.

        SSH密钥对所属的用户信息

        :param user_id: The user_id of this KeypairDetail.
        :type user_id: str
        """
        self._user_id = user_id

    @property
    def create_time(self):
        """Gets the create_time of this KeypairDetail.

        SSH密钥对创建的时间，时间戳，即从1970年1月1日至该时间的总秒数

        :return: The create_time of this KeypairDetail.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this KeypairDetail.

        SSH密钥对创建的时间，时间戳，即从1970年1月1日至该时间的总秒数

        :param create_time: The create_time of this KeypairDetail.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def delete_time(self):
        """Gets the delete_time of this KeypairDetail.

        SSH密钥对删除的时间，时间戳，即从1970年1月1日至该时间的总秒数

        :return: The delete_time of this KeypairDetail.
        :rtype: int
        """
        return self._delete_time

    @delete_time.setter
    def delete_time(self, delete_time):
        """Sets the delete_time of this KeypairDetail.

        SSH密钥对删除的时间，时间戳，即从1970年1月1日至该时间的总秒数

        :param delete_time: The delete_time of this KeypairDetail.
        :type delete_time: int
        """
        self._delete_time = delete_time

    @property
    def update_time(self):
        """Gets the update_time of this KeypairDetail.

        SSH密钥对的更新时间，时间戳，即从1970年1月1日至该时间的总秒数

        :return: The update_time of this KeypairDetail.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        """Sets the update_time of this KeypairDetail.

        SSH密钥对的更新时间，时间戳，即从1970年1月1日至该时间的总秒数

        :param update_time: The update_time of this KeypairDetail.
        :type update_time: int
        """
        self._update_time = update_time

    @property
    def frozen_state(self):
        """Gets the frozen_state of this KeypairDetail.

        冻结状态 - 0：正常状态 - 1：普通冻结 - 2：公安冻结 - 3：普通冻结及公安冻结 - 4：违规冻结 - 5：普通冻结及违规冻结 - 6：公安冻结及违规冻结 - 7：普通冻结、公安冻结及违规冻结 - 8：未实名认证冻结 - 9：普通冻结及未实名认证冻结 - 10：公安冻结及未实名认证冻结

        :return: The frozen_state of this KeypairDetail.
        :rtype: int
        """
        return self._frozen_state

    @frozen_state.setter
    def frozen_state(self, frozen_state):
        """Sets the frozen_state of this KeypairDetail.

        冻结状态 - 0：正常状态 - 1：普通冻结 - 2：公安冻结 - 3：普通冻结及公安冻结 - 4：违规冻结 - 5：普通冻结及违规冻结 - 6：公安冻结及违规冻结 - 7：普通冻结、公安冻结及违规冻结 - 8：未实名认证冻结 - 9：普通冻结及未实名认证冻结 - 10：公安冻结及未实名认证冻结

        :param frozen_state: The frozen_state of this KeypairDetail.
        :type frozen_state: int
        """
        self._frozen_state = frozen_state

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
        if not isinstance(other, KeypairDetail):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
