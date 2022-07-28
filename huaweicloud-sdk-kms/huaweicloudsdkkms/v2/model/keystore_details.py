# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class KeystoreDetails:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'keystore_id': 'str',
        'domain_id': 'str',
        'keystore_alias': 'str',
        'keystore_type': 'str',
        'hsm_cluster_id': 'str',
        'create_time': 'str'
    }

    attribute_map = {
        'keystore_id': 'keystore_id',
        'domain_id': 'domain_id',
        'keystore_alias': 'keystore_alias',
        'keystore_type': 'keystore_type',
        'hsm_cluster_id': 'hsm_cluster_id',
        'create_time': 'create_time'
    }

    def __init__(self, keystore_id=None, domain_id=None, keystore_alias=None, keystore_type=None, hsm_cluster_id=None, create_time=None):
        """KeystoreDetails

        The model defined in huaweicloud sdk

        :param keystore_id: 密钥库ID
        :type keystore_id: str
        :param domain_id: 用户域ID
        :type domain_id: str
        :param keystore_alias: 密钥库别名
        :type keystore_alias: str
        :param keystore_type: 密钥库类型
        :type keystore_type: str
        :param hsm_cluster_id: DHSM集群id，要求集群当前未创建专属密钥库
        :type hsm_cluster_id: str
        :param create_time: 密钥库创建时间，UTC时间戳。
        :type create_time: str
        """
        
        

        self._keystore_id = None
        self._domain_id = None
        self._keystore_alias = None
        self._keystore_type = None
        self._hsm_cluster_id = None
        self._create_time = None
        self.discriminator = None

        if keystore_id is not None:
            self.keystore_id = keystore_id
        if domain_id is not None:
            self.domain_id = domain_id
        if keystore_alias is not None:
            self.keystore_alias = keystore_alias
        if keystore_type is not None:
            self.keystore_type = keystore_type
        if hsm_cluster_id is not None:
            self.hsm_cluster_id = hsm_cluster_id
        if create_time is not None:
            self.create_time = create_time

    @property
    def keystore_id(self):
        """Gets the keystore_id of this KeystoreDetails.

        密钥库ID

        :return: The keystore_id of this KeystoreDetails.
        :rtype: str
        """
        return self._keystore_id

    @keystore_id.setter
    def keystore_id(self, keystore_id):
        """Sets the keystore_id of this KeystoreDetails.

        密钥库ID

        :param keystore_id: The keystore_id of this KeystoreDetails.
        :type keystore_id: str
        """
        self._keystore_id = keystore_id

    @property
    def domain_id(self):
        """Gets the domain_id of this KeystoreDetails.

        用户域ID

        :return: The domain_id of this KeystoreDetails.
        :rtype: str
        """
        return self._domain_id

    @domain_id.setter
    def domain_id(self, domain_id):
        """Sets the domain_id of this KeystoreDetails.

        用户域ID

        :param domain_id: The domain_id of this KeystoreDetails.
        :type domain_id: str
        """
        self._domain_id = domain_id

    @property
    def keystore_alias(self):
        """Gets the keystore_alias of this KeystoreDetails.

        密钥库别名

        :return: The keystore_alias of this KeystoreDetails.
        :rtype: str
        """
        return self._keystore_alias

    @keystore_alias.setter
    def keystore_alias(self, keystore_alias):
        """Sets the keystore_alias of this KeystoreDetails.

        密钥库别名

        :param keystore_alias: The keystore_alias of this KeystoreDetails.
        :type keystore_alias: str
        """
        self._keystore_alias = keystore_alias

    @property
    def keystore_type(self):
        """Gets the keystore_type of this KeystoreDetails.

        密钥库类型

        :return: The keystore_type of this KeystoreDetails.
        :rtype: str
        """
        return self._keystore_type

    @keystore_type.setter
    def keystore_type(self, keystore_type):
        """Sets the keystore_type of this KeystoreDetails.

        密钥库类型

        :param keystore_type: The keystore_type of this KeystoreDetails.
        :type keystore_type: str
        """
        self._keystore_type = keystore_type

    @property
    def hsm_cluster_id(self):
        """Gets the hsm_cluster_id of this KeystoreDetails.

        DHSM集群id，要求集群当前未创建专属密钥库

        :return: The hsm_cluster_id of this KeystoreDetails.
        :rtype: str
        """
        return self._hsm_cluster_id

    @hsm_cluster_id.setter
    def hsm_cluster_id(self, hsm_cluster_id):
        """Sets the hsm_cluster_id of this KeystoreDetails.

        DHSM集群id，要求集群当前未创建专属密钥库

        :param hsm_cluster_id: The hsm_cluster_id of this KeystoreDetails.
        :type hsm_cluster_id: str
        """
        self._hsm_cluster_id = hsm_cluster_id

    @property
    def create_time(self):
        """Gets the create_time of this KeystoreDetails.

        密钥库创建时间，UTC时间戳。

        :return: The create_time of this KeystoreDetails.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this KeystoreDetails.

        密钥库创建时间，UTC时间戳。

        :param create_time: The create_time of this KeystoreDetails.
        :type create_time: str
        """
        self._create_time = create_time

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
        if not isinstance(other, KeystoreDetails):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
