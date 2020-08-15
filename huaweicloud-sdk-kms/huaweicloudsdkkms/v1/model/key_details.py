# coding: utf-8

import pprint
import re

import six





class KeyDetails:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'key_id': 'str',
        'domain_id': 'str',
        'key_alias': 'str',
        'realm': 'str',
        'key_description': 'str',
        'creation_date': 'str',
        'scheduled_deletion_date': 'str',
        'key_state': 'str',
        'default_key_flag': 'str',
        'key_type': 'str',
        'expiration_time': 'str',
        'origin': 'str',
        'key_rotation_enabled': 'str',
        'sys_enterprise_project_id': 'str'
    }

    attribute_map = {
        'key_id': 'key_id',
        'domain_id': 'domain_id',
        'key_alias': 'key_alias',
        'realm': 'realm',
        'key_description': 'key_description',
        'creation_date': 'creation_date',
        'scheduled_deletion_date': 'scheduled_deletion_date',
        'key_state': 'key_state',
        'default_key_flag': 'default_key_flag',
        'key_type': 'key_type',
        'expiration_time': 'expiration_time',
        'origin': 'origin',
        'key_rotation_enabled': 'key_rotation_enabled',
        'sys_enterprise_project_id': 'sys_enterprise_project_id'
    }

    def __init__(self, key_id=None, domain_id=None, key_alias=None, realm=None, key_description=None, creation_date=None, scheduled_deletion_date=None, key_state=None, default_key_flag=None, key_type=None, expiration_time=None, origin=None, key_rotation_enabled=None, sys_enterprise_project_id=None):
        """KeyDetails - a model defined in huaweicloud sdk"""
        
        

        self._key_id = None
        self._domain_id = None
        self._key_alias = None
        self._realm = None
        self._key_description = None
        self._creation_date = None
        self._scheduled_deletion_date = None
        self._key_state = None
        self._default_key_flag = None
        self._key_type = None
        self._expiration_time = None
        self._origin = None
        self._key_rotation_enabled = None
        self._sys_enterprise_project_id = None
        self.discriminator = None

        if key_id is not None:
            self.key_id = key_id
        if domain_id is not None:
            self.domain_id = domain_id
        if key_alias is not None:
            self.key_alias = key_alias
        if realm is not None:
            self.realm = realm
        if key_description is not None:
            self.key_description = key_description
        if creation_date is not None:
            self.creation_date = creation_date
        if scheduled_deletion_date is not None:
            self.scheduled_deletion_date = scheduled_deletion_date
        if key_state is not None:
            self.key_state = key_state
        if default_key_flag is not None:
            self.default_key_flag = default_key_flag
        if key_type is not None:
            self.key_type = key_type
        if expiration_time is not None:
            self.expiration_time = expiration_time
        if origin is not None:
            self.origin = origin
        if key_rotation_enabled is not None:
            self.key_rotation_enabled = key_rotation_enabled
        if sys_enterprise_project_id is not None:
            self.sys_enterprise_project_id = sys_enterprise_project_id

    @property
    def key_id(self):
        """Gets the key_id of this KeyDetails.

        密钥ID。

        :return: The key_id of this KeyDetails.
        :rtype: str
        """
        return self._key_id

    @key_id.setter
    def key_id(self, key_id):
        """Sets the key_id of this KeyDetails.

        密钥ID。

        :param key_id: The key_id of this KeyDetails.
        :type: str
        """
        self._key_id = key_id

    @property
    def domain_id(self):
        """Gets the domain_id of this KeyDetails.

        用户域ID。

        :return: The domain_id of this KeyDetails.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeyDetails.

        用户域ID。

        :param domain_id: The domain_id of this KeyDetails.
        :type: str
        """
        self._domain_id = domain_id

    @property
    def key_alias(self):
        """Gets the key_alias of this KeyDetails.

        密钥别名。

        :return: The key_alias of this KeyDetails.
        :rtype: str
        """
        return self._key_alias

    @key_alias.setter
    def key_alias(self, key_alias):
        """Sets the key_alias of this KeyDetails.

        密钥别名。

        :param key_alias: The key_alias of this KeyDetails.
        :type: str
        """
        self._key_alias = key_alias

    @property
    def realm(self):
        """Gets the realm of this KeyDetails.

        密钥区域。

        :return: The realm of this KeyDetails.
        :rtype: str
        """
        return self._realm

    @realm.setter
    def realm(self, realm):
        """Sets the realm of this KeyDetails.

        密钥区域。

        :param realm: The realm of this KeyDetails.
        :type: str
        """
        self._realm = realm

    @property
    def key_description(self):
        """Gets the key_description of this KeyDetails.

        密钥描述。

        :return: The key_description of this KeyDetails.
        :rtype: str
        """
        return self._key_description

    @key_description.setter
    def key_description(self, key_description):
        """Sets the key_description of this KeyDetails.

        密钥描述。

        :param key_description: The key_description of this KeyDetails.
        :type: str
        """
        self._key_description = key_description

    @property
    def creation_date(self):
        """Gets the creation_date of this KeyDetails.

        密钥创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The creation_date of this KeyDetails.
        :rtype: str
        """
        return self._creation_date

    @creation_date.setter
    def creation_date(self, creation_date):
        """Sets the creation_date of this KeyDetails.

        密钥创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param creation_date: The creation_date of this KeyDetails.
        :type: str
        """
        self._creation_date = creation_date

    @property
    def scheduled_deletion_date(self):
        """Gets the scheduled_deletion_date of this KeyDetails.

        密钥计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The scheduled_deletion_date of this KeyDetails.
        :rtype: str
        """
        return self._scheduled_deletion_date

    @scheduled_deletion_date.setter
    def scheduled_deletion_date(self, scheduled_deletion_date):
        """Sets the scheduled_deletion_date of this KeyDetails.

        密钥计划删除时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param scheduled_deletion_date: The scheduled_deletion_date of this KeyDetails.
        :type: str
        """
        self._scheduled_deletion_date = scheduled_deletion_date

    @property
    def key_state(self):
        """Gets the key_state of this KeyDetails.

        密钥状态，满足正则匹配“^[1-5]{1}$”，枚举如下：  - “1”表示待激活状态  - “2”表示启用状态  - “3”表示禁用状态  - “4”表示计划删除状态  - “5”表示等待导入状态

        :return: The key_state of this KeyDetails.
        :rtype: str
        """
        return self._key_state

    @key_state.setter
    def key_state(self, key_state):
        """Sets the key_state of this KeyDetails.

        密钥状态，满足正则匹配“^[1-5]{1}$”，枚举如下：  - “1”表示待激活状态  - “2”表示启用状态  - “3”表示禁用状态  - “4”表示计划删除状态  - “5”表示等待导入状态

        :param key_state: The key_state of this KeyDetails.
        :type: str
        """
        self._key_state = key_state

    @property
    def default_key_flag(self):
        """Gets the default_key_flag of this KeyDetails.

        默认主密钥标识，默认主密钥标识为1，非默认标识为0。

        :return: The default_key_flag of this KeyDetails.
        :rtype: str
        """
        return self._default_key_flag

    @default_key_flag.setter
    def default_key_flag(self, default_key_flag):
        """Sets the default_key_flag of this KeyDetails.

        默认主密钥标识，默认主密钥标识为1，非默认标识为0。

        :param default_key_flag: The default_key_flag of this KeyDetails.
        :type: str
        """
        self._default_key_flag = default_key_flag

    @property
    def key_type(self):
        """Gets the key_type of this KeyDetails.

        密钥类型。

        :return: The key_type of this KeyDetails.
        :rtype: str
        """
        return self._key_type

    @key_type.setter
    def key_type(self, key_type):
        """Sets the key_type of this KeyDetails.

        密钥类型。

        :param key_type: The key_type of this KeyDetails.
        :type: str
        """
        self._key_type = key_type

    @property
    def expiration_time(self):
        """Gets the expiration_time of this KeyDetails.

        密钥材料失效时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The expiration_time of this KeyDetails.
        :rtype: str
        """
        return self._expiration_time

    @expiration_time.setter
    def expiration_time(self, expiration_time):
        """Sets the expiration_time of this KeyDetails.

        密钥材料失效时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param expiration_time: The expiration_time of this KeyDetails.
        :type: str
        """
        self._expiration_time = expiration_time

    @property
    def origin(self):
        """Gets the origin of this KeyDetails.

        密钥来源，默认为“kms”，枚举如下：  - kms表示密钥材料由kms生成kms表示密钥材料由kms生成  - external表示密钥材料由外部导入

        :return: The origin of this KeyDetails.
        :rtype: str
        """
        return self._origin

    @origin.setter
    def origin(self, origin):
        """Sets the origin of this KeyDetails.

        密钥来源，默认为“kms”，枚举如下：  - kms表示密钥材料由kms生成kms表示密钥材料由kms生成  - external表示密钥材料由外部导入

        :param origin: The origin of this KeyDetails.
        :type: str
        """
        self._origin = origin

    @property
    def key_rotation_enabled(self):
        """Gets the key_rotation_enabled of this KeyDetails.

        密钥轮换状态，默认为“false”，表示关闭密钥轮换功能。

        :return: The key_rotation_enabled of this KeyDetails.
        :rtype: str
        """
        return self._key_rotation_enabled

    @key_rotation_enabled.setter
    def key_rotation_enabled(self, key_rotation_enabled):
        """Sets the key_rotation_enabled of this KeyDetails.

        密钥轮换状态，默认为“false”，表示关闭密钥轮换功能。

        :param key_rotation_enabled: The key_rotation_enabled of this KeyDetails.
        :type: str
        """
        self._key_rotation_enabled = key_rotation_enabled

    @property
    def sys_enterprise_project_id(self):
        """Gets the sys_enterprise_project_id of this KeyDetails.

        企业项目ID，默认为“0”。  - 对于开通企业项目的用户，表示资源处于默认企业项目下。  - 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :return: The sys_enterprise_project_id of this KeyDetails.
        :rtype: str
        """
        return self._sys_enterprise_project_id

    @sys_enterprise_project_id.setter
    def sys_enterprise_project_id(self, sys_enterprise_project_id):
        """Sets the sys_enterprise_project_id of this KeyDetails.

        企业项目ID，默认为“0”。  - 对于开通企业项目的用户，表示资源处于默认企业项目下。  - 对于未开通企业项目的用户，表示资源未处于企业项目下。

        :param sys_enterprise_project_id: The sys_enterprise_project_id of this KeyDetails.
        :type: str
        """
        self._sys_enterprise_project_id = sys_enterprise_project_id

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
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, KeyDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
