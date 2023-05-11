# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Cluster:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'auth_mode': 'str',
        'enable_lemon': 'bool',
        'enable_open_tsdb': 'bool',
        'instance': 'Instance',
        'name': 'str',
        'storage_size': 'int',
        'storage_type': 'str',
        'vpc_id': 'str',
        'datastore': 'Datastore'
    }

    attribute_map = {
        'auth_mode': 'auth_mode',
        'enable_lemon': 'enable_lemon',
        'enable_open_tsdb': 'enable_openTSDB',
        'instance': 'instance',
        'name': 'name',
        'storage_size': 'storage_size',
        'storage_type': 'storage_type',
        'vpc_id': 'vpc_id',
        'datastore': 'datastore'
    }

    def __init__(self, auth_mode=None, enable_lemon=None, enable_open_tsdb=None, instance=None, name=None, storage_size=None, storage_type=None, vpc_id=None, datastore=None):
        """Cluster

        The model defined in huaweicloud sdk

        :param auth_mode: 是否开启IAM权限认证。 - false：不开启 - true：开启
        :type auth_mode: str
        :param enable_lemon: 是否开启Lemon(目前已关闭该参数，填false即可) - false：不开启 - true：开启
        :type enable_lemon: bool
        :param enable_open_tsdb: 是否开启OpenTSDB。 - false：不开启 - true：开启
        :type enable_open_tsdb: bool
        :param instance: 
        :type instance: :class:`huaweicloudsdkcloudtable.v2.Instance`
        :param name: CloudTable集群的名称。
        :type name: str
        :param storage_size: 存储值的大小。  取值范围: 1-[10240-1024*1024*1024]
        :type storage_size: int
        :param storage_type: 存储类型： - ULTRAHIGH：超高IO - COMMON：普通IO
        :type storage_type: str
        :param vpc_id: 集群所在的（虚拟网络私有云）VPC。
        :type vpc_id: str
        :param datastore: 
        :type datastore: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        
        

        self._auth_mode = None
        self._enable_lemon = None
        self._enable_open_tsdb = None
        self._instance = None
        self._name = None
        self._storage_size = None
        self._storage_type = None
        self._vpc_id = None
        self._datastore = None
        self.discriminator = None

        if auth_mode is not None:
            self.auth_mode = auth_mode
        if enable_lemon is not None:
            self.enable_lemon = enable_lemon
        if enable_open_tsdb is not None:
            self.enable_open_tsdb = enable_open_tsdb
        self.instance = instance
        self.name = name
        if storage_size is not None:
            self.storage_size = storage_size
        self.storage_type = storage_type
        self.vpc_id = vpc_id
        self.datastore = datastore

    @property
    def auth_mode(self):
        """Gets the auth_mode of this Cluster.

        是否开启IAM权限认证。 - false：不开启 - true：开启

        :return: The auth_mode of this Cluster.
        :rtype: str
        """
        return self._auth_mode

    @auth_mode.setter
    def auth_mode(self, auth_mode):
        """Sets the auth_mode of this Cluster.

        是否开启IAM权限认证。 - false：不开启 - true：开启

        :param auth_mode: The auth_mode of this Cluster.
        :type auth_mode: str
        """
        self._auth_mode = auth_mode

    @property
    def enable_lemon(self):
        """Gets the enable_lemon of this Cluster.

        是否开启Lemon(目前已关闭该参数，填false即可) - false：不开启 - true：开启

        :return: The enable_lemon of this Cluster.
        :rtype: bool
        """
        return self._enable_lemon

    @enable_lemon.setter
    def enable_lemon(self, enable_lemon):
        """Sets the enable_lemon of this Cluster.

        是否开启Lemon(目前已关闭该参数，填false即可) - false：不开启 - true：开启

        :param enable_lemon: The enable_lemon of this Cluster.
        :type enable_lemon: bool
        """
        self._enable_lemon = enable_lemon

    @property
    def enable_open_tsdb(self):
        """Gets the enable_open_tsdb of this Cluster.

        是否开启OpenTSDB。 - false：不开启 - true：开启

        :return: The enable_open_tsdb of this Cluster.
        :rtype: bool
        """
        return self._enable_open_tsdb

    @enable_open_tsdb.setter
    def enable_open_tsdb(self, enable_open_tsdb):
        """Sets the enable_open_tsdb of this Cluster.

        是否开启OpenTSDB。 - false：不开启 - true：开启

        :param enable_open_tsdb: The enable_open_tsdb of this Cluster.
        :type enable_open_tsdb: bool
        """
        self._enable_open_tsdb = enable_open_tsdb

    @property
    def instance(self):
        """Gets the instance of this Cluster.

        :return: The instance of this Cluster.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.Instance`
        """
        return self._instance

    @instance.setter
    def instance(self, instance):
        """Sets the instance of this Cluster.

        :param instance: The instance of this Cluster.
        :type instance: :class:`huaweicloudsdkcloudtable.v2.Instance`
        """
        self._instance = instance

    @property
    def name(self):
        """Gets the name of this Cluster.

        CloudTable集群的名称。

        :return: The name of this Cluster.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Cluster.

        CloudTable集群的名称。

        :param name: The name of this Cluster.
        :type name: str
        """
        self._name = name

    @property
    def storage_size(self):
        """Gets the storage_size of this Cluster.

        存储值的大小。  取值范围: 1-[10240-1024*1024*1024]

        :return: The storage_size of this Cluster.
        :rtype: int
        """
        return self._storage_size

    @storage_size.setter
    def storage_size(self, storage_size):
        """Sets the storage_size of this Cluster.

        存储值的大小。  取值范围: 1-[10240-1024*1024*1024]

        :param storage_size: The storage_size of this Cluster.
        :type storage_size: int
        """
        self._storage_size = storage_size

    @property
    def storage_type(self):
        """Gets the storage_type of this Cluster.

        存储类型： - ULTRAHIGH：超高IO - COMMON：普通IO

        :return: The storage_type of this Cluster.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this Cluster.

        存储类型： - ULTRAHIGH：超高IO - COMMON：普通IO

        :param storage_type: The storage_type of this Cluster.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def vpc_id(self):
        """Gets the vpc_id of this Cluster.

        集群所在的（虚拟网络私有云）VPC。

        :return: The vpc_id of this Cluster.
        :rtype: str
        """
        return self._vpc_id

    @vpc_id.setter
    def vpc_id(self, vpc_id):
        """Sets the vpc_id of this Cluster.

        集群所在的（虚拟网络私有云）VPC。

        :param vpc_id: The vpc_id of this Cluster.
        :type vpc_id: str
        """
        self._vpc_id = vpc_id

    @property
    def datastore(self):
        """Gets the datastore of this Cluster.

        :return: The datastore of this Cluster.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        return self._datastore

    @datastore.setter
    def datastore(self, datastore):
        """Sets the datastore of this Cluster.

        :param datastore: The datastore of this Cluster.
        :type datastore: :class:`huaweicloudsdkcloudtable.v2.Datastore`
        """
        self._datastore = datastore

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
        if not isinstance(other, Cluster):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
