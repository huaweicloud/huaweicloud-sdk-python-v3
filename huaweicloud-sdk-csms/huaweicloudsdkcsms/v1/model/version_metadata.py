# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class VersionMetadata:

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
        'create_time': 'int',
        'expire_time': 'int',
        'kms_key_id': 'str',
        'secret_name': 'str',
        'version_stages': 'list[str]'
    }

    attribute_map = {
        'id': 'id',
        'create_time': 'create_time',
        'expire_time': 'expire_time',
        'kms_key_id': 'kms_key_id',
        'secret_name': 'secret_name',
        'version_stages': 'version_stages'
    }

    def __init__(self, id=None, create_time=None, expire_time=None, kms_key_id=None, secret_name=None, version_stages=None):
        """VersionMetadata

        The model defined in huaweicloud sdk

        :param id: 凭据的版本号标识符，凭据对象下唯一。
        :type id: str
        :param create_time: 凭据版本创建时间，时间戳，即从1970年1月1日至该时间的总秒数。
        :type create_time: int
        :param expire_time: 凭据版本过期时间，时间戳，即从1970年1月1日至该时间的总秒数。默认为空，凭据订阅“版本过期”事件类型时，有效期判断所依据的值。
        :type expire_time: int
        :param kms_key_id: 加密版本凭据值的KMS主密钥ID。
        :type kms_key_id: str
        :param secret_name: 凭据名称。
        :type secret_name: str
        :param version_stages: 凭据版本被标记的状态列表。每个版本标签对于凭据对象下版本是唯一存在的，如果你创建版本时，指定的是同一凭据对象下的一个已经标记在其他版本上的状态，该标签将自动从其他版本上删除，并附加到此版本上。  如果未指定version_stage的值，则凭据管理服务会自动移动临时标签SYSCURRENT到此新版本。
        :type version_stages: list[str]
        """
        
        

        self._id = None
        self._create_time = None
        self._expire_time = None
        self._kms_key_id = None
        self._secret_name = None
        self._version_stages = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if create_time is not None:
            self.create_time = create_time
        if expire_time is not None:
            self.expire_time = expire_time
        if kms_key_id is not None:
            self.kms_key_id = kms_key_id
        if secret_name is not None:
            self.secret_name = secret_name
        if version_stages is not None:
            self.version_stages = version_stages

    @property
    def id(self):
        """Gets the id of this VersionMetadata.

        凭据的版本号标识符，凭据对象下唯一。

        :return: The id of this VersionMetadata.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this VersionMetadata.

        凭据的版本号标识符，凭据对象下唯一。

        :param id: The id of this VersionMetadata.
        :type id: str
        """
        self._id = id

    @property
    def create_time(self):
        """Gets the create_time of this VersionMetadata.

        凭据版本创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :return: The create_time of this VersionMetadata.
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this VersionMetadata.

        凭据版本创建时间，时间戳，即从1970年1月1日至该时间的总秒数。

        :param create_time: The create_time of this VersionMetadata.
        :type create_time: int
        """
        self._create_time = create_time

    @property
    def expire_time(self):
        """Gets the expire_time of this VersionMetadata.

        凭据版本过期时间，时间戳，即从1970年1月1日至该时间的总秒数。默认为空，凭据订阅“版本过期”事件类型时，有效期判断所依据的值。

        :return: The expire_time of this VersionMetadata.
        :rtype: int
        """
        return self._expire_time

    @expire_time.setter
    def expire_time(self, expire_time):
        """Sets the expire_time of this VersionMetadata.

        凭据版本过期时间，时间戳，即从1970年1月1日至该时间的总秒数。默认为空，凭据订阅“版本过期”事件类型时，有效期判断所依据的值。

        :param expire_time: The expire_time of this VersionMetadata.
        :type expire_time: int
        """
        self._expire_time = expire_time

    @property
    def kms_key_id(self):
        """Gets the kms_key_id of this VersionMetadata.

        加密版本凭据值的KMS主密钥ID。

        :return: The kms_key_id of this VersionMetadata.
        :rtype: str
        """
        return self._kms_key_id

    @kms_key_id.setter
    def kms_key_id(self, kms_key_id):
        """Sets the kms_key_id of this VersionMetadata.

        加密版本凭据值的KMS主密钥ID。

        :param kms_key_id: The kms_key_id of this VersionMetadata.
        :type kms_key_id: str
        """
        self._kms_key_id = kms_key_id

    @property
    def secret_name(self):
        """Gets the secret_name of this VersionMetadata.

        凭据名称。

        :return: The secret_name of this VersionMetadata.
        :rtype: str
        """
        return self._secret_name

    @secret_name.setter
    def secret_name(self, secret_name):
        """Sets the secret_name of this VersionMetadata.

        凭据名称。

        :param secret_name: The secret_name of this VersionMetadata.
        :type secret_name: str
        """
        self._secret_name = secret_name

    @property
    def version_stages(self):
        """Gets the version_stages of this VersionMetadata.

        凭据版本被标记的状态列表。每个版本标签对于凭据对象下版本是唯一存在的，如果你创建版本时，指定的是同一凭据对象下的一个已经标记在其他版本上的状态，该标签将自动从其他版本上删除，并附加到此版本上。  如果未指定version_stage的值，则凭据管理服务会自动移动临时标签SYSCURRENT到此新版本。

        :return: The version_stages of this VersionMetadata.
        :rtype: list[str]
        """
        return self._version_stages

    @version_stages.setter
    def version_stages(self, version_stages):
        """Sets the version_stages of this VersionMetadata.

        凭据版本被标记的状态列表。每个版本标签对于凭据对象下版本是唯一存在的，如果你创建版本时，指定的是同一凭据对象下的一个已经标记在其他版本上的状态，该标签将自动从其他版本上删除，并附加到此版本上。  如果未指定version_stage的值，则凭据管理服务会自动移动临时标签SYSCURRENT到此新版本。

        :param version_stages: The version_stages of this VersionMetadata.
        :type version_stages: list[str]
        """
        self._version_stages = version_stages

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
        if not isinstance(other, VersionMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
