# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowEventDataRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'namespace': 'str',
        'dim_0': 'str',
        'dim_1': 'str',
        'dim_2': 'str',
        'dim_3': 'str',
        'type': 'str',
        '_from': 'int',
        'to': 'int'
    }

    attribute_map = {
        'namespace': 'namespace',
        'dim_0': 'dim.0',
        'dim_1': 'dim.1',
        'dim_2': 'dim.2',
        'dim_3': 'dim.3',
        'type': 'type',
        '_from': 'from',
        'to': 'to'
    }

    def __init__(self, namespace=None, dim_0=None, dim_1=None, dim_2=None, dim_3=None, type=None, _from=None, to=None):
        """ShowEventDataRequest

        The model defined in huaweicloud sdk

        :param namespace: 指标命名空间，如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type namespace: str
        :param dim_0: 指标的第一层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.0&#x3D;key,value，如mongodb_cluster_id,4270ff17-aba3-4138-89fa-820594c39755；key为指标的维度信息，如：文档数据库服务，则第一层维度为mongodb_cluster_id，value为文档数据库实例ID；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_0: str
        :param dim_1: 指标的第二层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.1&#x3D;key,value，如mongos_instance_id,c65d39d7-185c-4616-9aca-ad65703b15f9；key为指标的维度信息，如：文档数据库服务，则第二层维度为mongos_instance_id，value为文档数据库集群实例下的mongos节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_1: str
        :param dim_2: 指标的第三层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.2&#x3D;key,value，如mongod_primary_instance_id,5f9498e9-36f8-4317-9ea1-ebe28cba99b4；key为指标的维度信息，如：文档数据库服务，则第三层维度为mongod_primary_instance_id，value为文档数据库实例下的主节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_2: str
        :param dim_3: 指标的第四层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.3&#x3D;key,value，如mongod_secondary_instance_id,b46fa2c7-aac6-4ae3-9337-f4ea97f885cb；key为指标的维度信息，如：文档数据库服务，则第四层维度为mongod_secondary_instance_id，value为文档数据库实例下的备节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。
        :type dim_3: str
        :param type: 事件类型，只允许字母、下划线、中划线，字母开头，长度不超过64，如instance_host_info。
        :type type: str
        :param _from: 查询数据起始时间，UNIX时间戳，单位毫秒；如：1607146998177。
        :type _from: int
        :param to: 查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to；如：1607150598177。
        :type to: int
        """
        
        

        self._namespace = None
        self._dim_0 = None
        self._dim_1 = None
        self._dim_2 = None
        self._dim_3 = None
        self._type = None
        self.__from = None
        self._to = None
        self.discriminator = None

        self.namespace = namespace
        self.dim_0 = dim_0
        if dim_1 is not None:
            self.dim_1 = dim_1
        if dim_2 is not None:
            self.dim_2 = dim_2
        if dim_3 is not None:
            self.dim_3 = dim_3
        self.type = type
        self._from = _from
        self.to = to

    @property
    def namespace(self):
        """Gets the namespace of this ShowEventDataRequest.

        指标命名空间，如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The namespace of this ShowEventDataRequest.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """Sets the namespace of this ShowEventDataRequest.

        指标命名空间，如：弹性云服务器的命名空间为SYS.ECS，文档数据库的命名空间为SYS.DDS，各服务的命名空间可查看：“[服务命名空间](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param namespace: The namespace of this ShowEventDataRequest.
        :type namespace: str
        """
        self._namespace = namespace

    @property
    def dim_0(self):
        """Gets the dim_0 of this ShowEventDataRequest.

        指标的第一层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.0=key,value，如mongodb_cluster_id,4270ff17-aba3-4138-89fa-820594c39755；key为指标的维度信息，如：文档数据库服务，则第一层维度为mongodb_cluster_id，value为文档数据库实例ID；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_0 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_0

    @dim_0.setter
    def dim_0(self, dim_0):
        """Sets the dim_0 of this ShowEventDataRequest.

        指标的第一层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.0=key,value，如mongodb_cluster_id,4270ff17-aba3-4138-89fa-820594c39755；key为指标的维度信息，如：文档数据库服务，则第一层维度为mongodb_cluster_id，value为文档数据库实例ID；各服务资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_0: The dim_0 of this ShowEventDataRequest.
        :type dim_0: str
        """
        self._dim_0 = dim_0

    @property
    def dim_1(self):
        """Gets the dim_1 of this ShowEventDataRequest.

        指标的第二层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.1=key,value，如mongos_instance_id,c65d39d7-185c-4616-9aca-ad65703b15f9；key为指标的维度信息，如：文档数据库服务，则第二层维度为mongos_instance_id，value为文档数据库集群实例下的mongos节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_1 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_1

    @dim_1.setter
    def dim_1(self, dim_1):
        """Sets the dim_1 of this ShowEventDataRequest.

        指标的第二层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.1=key,value，如mongos_instance_id,c65d39d7-185c-4616-9aca-ad65703b15f9；key为指标的维度信息，如：文档数据库服务，则第二层维度为mongos_instance_id，value为文档数据库集群实例下的mongos节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_1: The dim_1 of this ShowEventDataRequest.
        :type dim_1: str
        """
        self._dim_1 = dim_1

    @property
    def dim_2(self):
        """Gets the dim_2 of this ShowEventDataRequest.

        指标的第三层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.2=key,value，如mongod_primary_instance_id,5f9498e9-36f8-4317-9ea1-ebe28cba99b4；key为指标的维度信息，如：文档数据库服务，则第三层维度为mongod_primary_instance_id，value为文档数据库实例下的主节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_2 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_2

    @dim_2.setter
    def dim_2(self, dim_2):
        """Sets the dim_2 of this ShowEventDataRequest.

        指标的第三层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.2=key,value，如mongod_primary_instance_id,5f9498e9-36f8-4317-9ea1-ebe28cba99b4；key为指标的维度信息，如：文档数据库服务，则第三层维度为mongod_primary_instance_id，value为文档数据库实例下的主节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_2: The dim_2 of this ShowEventDataRequest.
        :type dim_2: str
        """
        self._dim_2 = dim_2

    @property
    def dim_3(self):
        """Gets the dim_3 of this ShowEventDataRequest.

        指标的第四层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.3=key,value，如mongod_secondary_instance_id,b46fa2c7-aac6-4ae3-9337-f4ea97f885cb；key为指标的维度信息，如：文档数据库服务，则第四层维度为mongod_secondary_instance_id，value为文档数据库实例下的备节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :return: The dim_3 of this ShowEventDataRequest.
        :rtype: str
        """
        return self._dim_3

    @dim_3.setter
    def dim_3(self, dim_3):
        """Sets the dim_3 of this ShowEventDataRequest.

        指标的第四层维度，目前最大支持4个维度，维度编号从0开始；维度格式为dim.3=key,value，如mongod_secondary_instance_id,b46fa2c7-aac6-4ae3-9337-f4ea97f885cb；key为指标的维度信息，如：文档数据库服务，则第四层维度为mongod_secondary_instance_id，value为文档数据库实例下的备节点ID；各资源的指标维度名称可查看：“[服务指标维度](https://support.huaweicloud.com/usermanual-ces/zh-cn_topic_0202622212.html)”。

        :param dim_3: The dim_3 of this ShowEventDataRequest.
        :type dim_3: str
        """
        self._dim_3 = dim_3

    @property
    def type(self):
        """Gets the type of this ShowEventDataRequest.

        事件类型，只允许字母、下划线、中划线，字母开头，长度不超过64，如instance_host_info。

        :return: The type of this ShowEventDataRequest.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShowEventDataRequest.

        事件类型，只允许字母、下划线、中划线，字母开头，长度不超过64，如instance_host_info。

        :param type: The type of this ShowEventDataRequest.
        :type type: str
        """
        self._type = type

    @property
    def _from(self):
        """Gets the _from of this ShowEventDataRequest.

        查询数据起始时间，UNIX时间戳，单位毫秒；如：1607146998177。

        :return: The _from of this ShowEventDataRequest.
        :rtype: int
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this ShowEventDataRequest.

        查询数据起始时间，UNIX时间戳，单位毫秒；如：1607146998177。

        :param _from: The _from of this ShowEventDataRequest.
        :type _from: int
        """
        self.__from = _from

    @property
    def to(self):
        """Gets the to of this ShowEventDataRequest.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to；如：1607150598177。

        :return: The to of this ShowEventDataRequest.
        :rtype: int
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this ShowEventDataRequest.

        查询数据截止时间UNIX时间戳，单位毫秒。from必须小于to；如：1607150598177。

        :param to: The to of this ShowEventDataRequest.
        :type to: int
        """
        self._to = to

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
        if not isinstance(other, ShowEventDataRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
