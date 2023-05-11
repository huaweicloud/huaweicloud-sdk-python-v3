# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Volume:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'size': 'int',
        'volumetype': 'str',
        'extend_param': 'dict(str, object)',
        'cluster_id': 'str',
        'cluster_type': 'str',
        'hwpassthrough': 'bool',
        'metadata': 'VolumeMetadata'
    }

    attribute_map = {
        'size': 'size',
        'volumetype': 'volumetype',
        'extend_param': 'extendParam',
        'cluster_id': 'cluster_id',
        'cluster_type': 'cluster_type',
        'hwpassthrough': 'hw:passthrough',
        'metadata': 'metadata'
    }

    def __init__(self, size=None, volumetype=None, extend_param=None, cluster_id=None, cluster_type=None, hwpassthrough=None, metadata=None):
        """Volume

        The model defined in huaweicloud sdk

        :param size: 磁盘大小，单位为GB  - 系统盘取值范围：40~1024 - 数据盘取值范围：100~32768
        :type size: int
        :param volumetype: 磁盘类型，取值请参见创建云服务器 中“root_volume字段数据结构说明”。  - SAS：高IO，是指由SAS存储提供资源的磁盘类型。 - SSD：超高IO，是指由SSD存储提供资源的磁盘类型。 - SATA：普通IO，是指由SATA存储提供资源的磁盘类型。EVS已下线SATA磁盘，仅存量节点有此类型的磁盘。
        :type volumetype: str
        :param extend_param: 磁盘扩展参数，取值请参见创建云服务器中“extendparam”参数的描述。 [链接请参见[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212668.html)](tag:hws) [链接请参见[创建云服务器](https://support.huaweicloud.com/intl/zh-cn/api-ecs/zh-cn_topic_0020212668.html)](tag:hws_hk) 
        :type extend_param: dict(str, object)
        :param cluster_id: 云服务器系统盘对应的存储池的ID。仅用作专属云集群，专属分布式存储DSS的存储池ID，即dssPoolID。  [获取方法请参见[获取单个专属分布式存储池详情](https://support.huaweicloud.com/api-dss/dss_02_1001.html)中“表3 响应参数”的ID字段。](tag:hws) [获取方法请参见[获取单个专属分布式存储池详情](https://support.huaweicloud.com/intl/zh-cn/api-dss/dss_02_1001.html)中“表3 响应参数”的ID字段。](tag:hws_hk)
        :type cluster_id: str
        :param cluster_type: 云服务器系统盘对应的磁盘存储类型。仅用作专属云集群，固定取值为dss。  
        :type cluster_type: str
        :param hwpassthrough: - 使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为SCSI类型的卷 - 节点池类型为ElasticBMS时，此参数必须填写为true - 如存在节点规格涉及本地盘并同时使用云硬盘场景时，请设置磁盘初始化配置管理参数，参见[节点磁盘挂载](node_storage_example.xml)。 
        :type hwpassthrough: bool
        :param metadata: 
        :type metadata: :class:`huaweicloudsdkcce.v3.VolumeMetadata`
        """
        
        

        self._size = None
        self._volumetype = None
        self._extend_param = None
        self._cluster_id = None
        self._cluster_type = None
        self._hwpassthrough = None
        self._metadata = None
        self.discriminator = None

        self.size = size
        self.volumetype = volumetype
        if extend_param is not None:
            self.extend_param = extend_param
        if cluster_id is not None:
            self.cluster_id = cluster_id
        if cluster_type is not None:
            self.cluster_type = cluster_type
        if hwpassthrough is not None:
            self.hwpassthrough = hwpassthrough
        if metadata is not None:
            self.metadata = metadata

    @property
    def size(self):
        """Gets the size of this Volume.

        磁盘大小，单位为GB  - 系统盘取值范围：40~1024 - 数据盘取值范围：100~32768

        :return: The size of this Volume.
        :rtype: int
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this Volume.

        磁盘大小，单位为GB  - 系统盘取值范围：40~1024 - 数据盘取值范围：100~32768

        :param size: The size of this Volume.
        :type size: int
        """
        self._size = size

    @property
    def volumetype(self):
        """Gets the volumetype of this Volume.

        磁盘类型，取值请参见创建云服务器 中“root_volume字段数据结构说明”。  - SAS：高IO，是指由SAS存储提供资源的磁盘类型。 - SSD：超高IO，是指由SSD存储提供资源的磁盘类型。 - SATA：普通IO，是指由SATA存储提供资源的磁盘类型。EVS已下线SATA磁盘，仅存量节点有此类型的磁盘。

        :return: The volumetype of this Volume.
        :rtype: str
        """
        return self._volumetype

    @volumetype.setter
    def volumetype(self, volumetype):
        """Sets the volumetype of this Volume.

        磁盘类型，取值请参见创建云服务器 中“root_volume字段数据结构说明”。  - SAS：高IO，是指由SAS存储提供资源的磁盘类型。 - SSD：超高IO，是指由SSD存储提供资源的磁盘类型。 - SATA：普通IO，是指由SATA存储提供资源的磁盘类型。EVS已下线SATA磁盘，仅存量节点有此类型的磁盘。

        :param volumetype: The volumetype of this Volume.
        :type volumetype: str
        """
        self._volumetype = volumetype

    @property
    def extend_param(self):
        """Gets the extend_param of this Volume.

        磁盘扩展参数，取值请参见创建云服务器中“extendparam”参数的描述。 [链接请参见[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212668.html)](tag:hws) [链接请参见[创建云服务器](https://support.huaweicloud.com/intl/zh-cn/api-ecs/zh-cn_topic_0020212668.html)](tag:hws_hk) 

        :return: The extend_param of this Volume.
        :rtype: dict(str, object)
        """
        return self._extend_param

    @extend_param.setter
    def extend_param(self, extend_param):
        """Sets the extend_param of this Volume.

        磁盘扩展参数，取值请参见创建云服务器中“extendparam”参数的描述。 [链接请参见[创建云服务器](https://support.huaweicloud.com/api-ecs/zh-cn_topic_0020212668.html)](tag:hws) [链接请参见[创建云服务器](https://support.huaweicloud.com/intl/zh-cn/api-ecs/zh-cn_topic_0020212668.html)](tag:hws_hk) 

        :param extend_param: The extend_param of this Volume.
        :type extend_param: dict(str, object)
        """
        self._extend_param = extend_param

    @property
    def cluster_id(self):
        """Gets the cluster_id of this Volume.

        云服务器系统盘对应的存储池的ID。仅用作专属云集群，专属分布式存储DSS的存储池ID，即dssPoolID。  [获取方法请参见[获取单个专属分布式存储池详情](https://support.huaweicloud.com/api-dss/dss_02_1001.html)中“表3 响应参数”的ID字段。](tag:hws) [获取方法请参见[获取单个专属分布式存储池详情](https://support.huaweicloud.com/intl/zh-cn/api-dss/dss_02_1001.html)中“表3 响应参数”的ID字段。](tag:hws_hk)

        :return: The cluster_id of this Volume.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this Volume.

        云服务器系统盘对应的存储池的ID。仅用作专属云集群，专属分布式存储DSS的存储池ID，即dssPoolID。  [获取方法请参见[获取单个专属分布式存储池详情](https://support.huaweicloud.com/api-dss/dss_02_1001.html)中“表3 响应参数”的ID字段。](tag:hws) [获取方法请参见[获取单个专属分布式存储池详情](https://support.huaweicloud.com/intl/zh-cn/api-dss/dss_02_1001.html)中“表3 响应参数”的ID字段。](tag:hws_hk)

        :param cluster_id: The cluster_id of this Volume.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def cluster_type(self):
        """Gets the cluster_type of this Volume.

        云服务器系统盘对应的磁盘存储类型。仅用作专属云集群，固定取值为dss。  

        :return: The cluster_type of this Volume.
        :rtype: str
        """
        return self._cluster_type

    @cluster_type.setter
    def cluster_type(self, cluster_type):
        """Sets the cluster_type of this Volume.

        云服务器系统盘对应的磁盘存储类型。仅用作专属云集群，固定取值为dss。  

        :param cluster_type: The cluster_type of this Volume.
        :type cluster_type: str
        """
        self._cluster_type = cluster_type

    @property
    def hwpassthrough(self):
        """Gets the hwpassthrough of this Volume.

        - 使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为SCSI类型的卷 - 节点池类型为ElasticBMS时，此参数必须填写为true - 如存在节点规格涉及本地盘并同时使用云硬盘场景时，请设置磁盘初始化配置管理参数，参见[节点磁盘挂载](node_storage_example.xml)。 

        :return: The hwpassthrough of this Volume.
        :rtype: bool
        """
        return self._hwpassthrough

    @hwpassthrough.setter
    def hwpassthrough(self, hwpassthrough):
        """Sets the hwpassthrough of this Volume.

        - 使用SDI规格创建虚拟机时请关注该参数，如果该参数值为true，说明创建的为SCSI类型的卷 - 节点池类型为ElasticBMS时，此参数必须填写为true - 如存在节点规格涉及本地盘并同时使用云硬盘场景时，请设置磁盘初始化配置管理参数，参见[节点磁盘挂载](node_storage_example.xml)。 

        :param hwpassthrough: The hwpassthrough of this Volume.
        :type hwpassthrough: bool
        """
        self._hwpassthrough = hwpassthrough

    @property
    def metadata(self):
        """Gets the metadata of this Volume.

        :return: The metadata of this Volume.
        :rtype: :class:`huaweicloudsdkcce.v3.VolumeMetadata`
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """Sets the metadata of this Volume.

        :param metadata: The metadata of this Volume.
        :type metadata: :class:`huaweicloudsdkcce.v3.VolumeMetadata`
        """
        self._metadata = metadata

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
        if not isinstance(other, Volume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
