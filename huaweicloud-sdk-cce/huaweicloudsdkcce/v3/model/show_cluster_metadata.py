# coding: utf-8

import pprint
import re

import six





class ShowClusterMetadata:


    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """

    sensitive_list = []

    openapi_types = {
        'annotations': 'dict(str, str)',
        'creation_timestamp': 'str',
        'labels': 'str',
        'name': 'str',
        'uid': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'annotations': 'annotations',
        'creation_timestamp': 'creationTimestamp',
        'labels': 'labels',
        'name': 'name',
        'uid': 'uid',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, annotations=None, creation_timestamp=None, labels=None, name=None, uid=None, update_timestamp=None):
        """ShowClusterMetadata - a model defined in huaweicloud sdk"""
        
        

        self._annotations = None
        self._creation_timestamp = None
        self._labels = None
        self._name = None
        self._uid = None
        self._update_timestamp = None
        self.discriminator = None

        if annotations is not None:
            self.annotations = annotations
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if labels is not None:
            self.labels = labels
        self.name = name
        if uid is not None:
            self.uid = uid
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def annotations(self):
        """Gets the annotations of this ShowClusterMetadata.

        集群注解。此字段与创建时的annotations无必然关系，查询时根据查询参数返回集群相关信息存入该字段中。  当查询参数detail设置为true时，该注解包含集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)和已安装插件名称(installedAddonInstances)。

        :return: The annotations of this ShowClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ShowClusterMetadata.

        集群注解。此字段与创建时的annotations无必然关系，查询时根据查询参数返回集群相关信息存入该字段中。  当查询参数detail设置为true时，该注解包含集群下节点总数(totalNodesNumber)、正常节点数(activeNodesNumber)、CPU总量(totalNodesCPU)、内存总量(totalNodesMemory)和已安装插件名称(installedAddonInstances)。

        :param annotations: The annotations of this ShowClusterMetadata.
        :type: dict(str, str)
        """
        self._annotations = annotations

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this ShowClusterMetadata.

        集群创建时间，集群创建成功后自动生成，填写无效

        :return: The creation_timestamp of this ShowClusterMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this ShowClusterMetadata.

        集群创建时间，集群创建成功后自动生成，填写无效

        :param creation_timestamp: The creation_timestamp of this ShowClusterMetadata.
        :type: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def labels(self):
        """Gets the labels of this ShowClusterMetadata.

        集群标签，key/value对格式。  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效，与创建时的labels无必然关系。

        :return: The labels of this ShowClusterMetadata.
        :rtype: str
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ShowClusterMetadata.

        集群标签，key/value对格式。  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效，与创建时的labels无必然关系。

        :param labels: The labels of this ShowClusterMetadata.
        :type: str
        """
        self._labels = labels

    @property
    def name(self):
        """Gets the name of this ShowClusterMetadata.

        集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。

        :return: The name of this ShowClusterMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ShowClusterMetadata.

        集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。

        :param name: The name of this ShowClusterMetadata.
        :type: str
        """
        self._name = name

    @property
    def uid(self):
        """Gets the uid of this ShowClusterMetadata.

        资源唯一标识，创建成功后自动生成，填写无效

        :return: The uid of this ShowClusterMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ShowClusterMetadata.

        资源唯一标识，创建成功后自动生成，填写无效

        :param uid: The uid of this ShowClusterMetadata.
        :type: str
        """
        self._uid = uid

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this ShowClusterMetadata.

        集群更新时间，集群创建成功后自动生成，填写无效

        :return: The update_timestamp of this ShowClusterMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this ShowClusterMetadata.

        集群更新时间，集群创建成功后自动生成，填写无效

        :param update_timestamp: The update_timestamp of this ShowClusterMetadata.
        :type: str
        """
        self._update_timestamp = update_timestamp

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
        if not isinstance(other, ShowClusterMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
