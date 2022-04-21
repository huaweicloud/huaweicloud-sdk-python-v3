# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteCloudPersistentVolumeClaimsRequest:

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
        'namespace': 'str',
        'delete_volume': 'str',
        'storage_type': 'str',
        'x_cluster_id': 'str'
    }

    attribute_map = {
        'name': 'name',
        'namespace': 'namespace',
        'delete_volume': 'deleteVolume',
        'storage_type': 'storageType',
        'x_cluster_id': 'X-Cluster-ID'
    }

    def __init__(self, name=None, namespace=None, delete_volume=None, storage_type=None, x_cluster_id=None):
        """DeleteCloudPersistentVolumeClaimsRequest

        The model defined in huaweicloud sdk

        :param name: 需要删除的PersistentVolumClaim的名称。 
        :type name: str
        :param namespace: 指定PersistentVolumeClaim所在的命名空间。 
        :type namespace: str
        :param delete_volume: 删除PersistentVolumeClaim后是否保留后端关联的云存储。false表示不删除，true表示删除，默认为false。 
        :type delete_volume: str
        :param storage_type: 删除PersistentVolumeClaim后是否保留后端关联的云存储。false表示不删除，true表示删除，默认为false。 云存储的类型，和deleteVolume搭配使用。即deleteVolume和storageType必须同时配置。     - bs：EVS云硬盘存储     - nfs：SFS弹性文件存储     - obs：OBS对象存储     - efs：SFS Turbo极速文件存储 
        :type storage_type: str
        :param x_cluster_id: 集群ID，使用**https://Endpoint/uri**这种URL格式时必须指定此参数。获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 
        :type x_cluster_id: str
        """
        
        

        self._name = None
        self._namespace = None
        self._delete_volume = None
        self._storage_type = None
        self._x_cluster_id = None
        self.discriminator = None

        self.name = name
        self.namespace = namespace
        if delete_volume is not None:
            self.delete_volume = delete_volume
        if storage_type is not None:
            self.storage_type = storage_type
        if x_cluster_id is not None:
            self.x_cluster_id = x_cluster_id

    @property
    def name(self):
        """Gets the name of this DeleteCloudPersistentVolumeClaimsRequest.

        需要删除的PersistentVolumClaim的名称。 

        :return: The name of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DeleteCloudPersistentVolumeClaimsRequest.

        需要删除的PersistentVolumClaim的名称。 

        :param name: The name of this DeleteCloudPersistentVolumeClaimsRequest.
        :type name: str
        """
        self._name = name

    @property
    def namespace(self):
        """Gets the namespace of this DeleteCloudPersistentVolumeClaimsRequest.

        指定PersistentVolumeClaim所在的命名空间。 

        :return: The namespace of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this DeleteCloudPersistentVolumeClaimsRequest.

        指定PersistentVolumeClaim所在的命名空间。 

        :param namespace: The namespace of this DeleteCloudPersistentVolumeClaimsRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def delete_volume(self):
        """Gets the delete_volume of this DeleteCloudPersistentVolumeClaimsRequest.

        删除PersistentVolumeClaim后是否保留后端关联的云存储。false表示不删除，true表示删除，默认为false。 

        :return: The delete_volume of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._delete_volume

    @delete_volume.setter
    def delete_volume(self, delete_volume):
        """Sets the delete_volume of this DeleteCloudPersistentVolumeClaimsRequest.

        删除PersistentVolumeClaim后是否保留后端关联的云存储。false表示不删除，true表示删除，默认为false。 

        :param delete_volume: The delete_volume of this DeleteCloudPersistentVolumeClaimsRequest.
        :type delete_volume: str
        """
        self._delete_volume = delete_volume

    @property
    def storage_type(self):
        """Gets the storage_type of this DeleteCloudPersistentVolumeClaimsRequest.

        删除PersistentVolumeClaim后是否保留后端关联的云存储。false表示不删除，true表示删除，默认为false。 云存储的类型，和deleteVolume搭配使用。即deleteVolume和storageType必须同时配置。     - bs：EVS云硬盘存储     - nfs：SFS弹性文件存储     - obs：OBS对象存储     - efs：SFS Turbo极速文件存储 

        :return: The storage_type of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._storage_type

    @storage_type.setter
    def storage_type(self, storage_type):
        """Sets the storage_type of this DeleteCloudPersistentVolumeClaimsRequest.

        删除PersistentVolumeClaim后是否保留后端关联的云存储。false表示不删除，true表示删除，默认为false。 云存储的类型，和deleteVolume搭配使用。即deleteVolume和storageType必须同时配置。     - bs：EVS云硬盘存储     - nfs：SFS弹性文件存储     - obs：OBS对象存储     - efs：SFS Turbo极速文件存储 

        :param storage_type: The storage_type of this DeleteCloudPersistentVolumeClaimsRequest.
        :type storage_type: str
        """
        self._storage_type = storage_type

    @property
    def x_cluster_id(self):
        """Gets the x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.

        集群ID，使用**https://Endpoint/uri**这种URL格式时必须指定此参数。获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 

        :return: The x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.
        :rtype: str
        """
        return self._x_cluster_id

    @x_cluster_id.setter
    def x_cluster_id(self, x_cluster_id):
        """Sets the x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.

        集群ID，使用**https://Endpoint/uri**这种URL格式时必须指定此参数。获取方式请参见[如何获取接口URI中参数](cce_02_0271.xml)。 

        :param x_cluster_id: The x_cluster_id of this DeleteCloudPersistentVolumeClaimsRequest.
        :type x_cluster_id: str
        """
        self._x_cluster_id = x_cluster_id

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
        if not isinstance(other, DeleteCloudPersistentVolumeClaimsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
