# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ClusterMetadata:


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
        'uid': 'str',
        'annotations': 'dict(str, str)',
        'labels': 'dict(str, str)',
        'creation_timestamp': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'annotations': 'annotations',
        'labels': 'labels',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, name=None, uid=None, annotations=None, labels=None, creation_timestamp=None, update_timestamp=None):
        """ClusterMetadata - a model defined in huaweicloud sdk"""
        
        

        self._name = None
        self._uid = None
        self._annotations = None
        self._labels = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        self.name = name
        if uid is not None:
            self.uid = uid
        if annotations is not None:
            self.annotations = annotations
        if labels is not None:
            self.labels = labels
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def name(self):
        """Gets the name of this ClusterMetadata.

        集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。

        :return: The name of this ClusterMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ClusterMetadata.

        集群名称。  命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-128位，且不能以中划线(-)结尾。

        :param name: The name of this ClusterMetadata.
        :type: str
        """
        self._name = name

    @property
    def uid(self):
        """Gets the uid of this ClusterMetadata.

        资源唯一标识，创建成功后自动生成，填写无效

        :return: The uid of this ClusterMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this ClusterMetadata.

        资源唯一标识，创建成功后自动生成，填写无效

        :param uid: The uid of this ClusterMetadata.
        :type: str
        """
        self._uid = uid

    @property
    def annotations(self):
        """Gets the annotations of this ClusterMetadata.

        集群注解，由key/value组成：   ```  \"annotations\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" }  ```   >    - Annotations不用于标识和选择对象。Annotations中的元数据可以是small 或large，structured 或unstructured，并且可以包括标签不允许使用的字符。 >    - 该字段不会被数据库保存，当前仅用于指定集群待安装插件。 

        :return: The annotations of this ClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ClusterMetadata.

        集群注解，由key/value组成：   ```  \"annotations\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" }  ```   >    - Annotations不用于标识和选择对象。Annotations中的元数据可以是small 或large，structured 或unstructured，并且可以包括标签不允许使用的字符。 >    - 该字段不会被数据库保存，当前仅用于指定集群待安装插件。 

        :param annotations: The annotations of this ClusterMetadata.
        :type: dict(str, str)
        """
        self._annotations = annotations

    @property
    def labels(self):
        """Gets the labels of this ClusterMetadata.

        集群标签，key/value对格式。  >  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效。

        :return: The labels of this ClusterMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this ClusterMetadata.

        集群标签，key/value对格式。  >  该字段值由系统自动生成，用于升级时前端识别集群支持的特性开关，用户指定无效。

        :param labels: The labels of this ClusterMetadata.
        :type: dict(str, str)
        """
        self._labels = labels

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this ClusterMetadata.

        集群创建时间

        :return: The creation_timestamp of this ClusterMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this ClusterMetadata.

        集群创建时间

        :param creation_timestamp: The creation_timestamp of this ClusterMetadata.
        :type: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this ClusterMetadata.

        集群更新时间

        :return: The update_timestamp of this ClusterMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this ClusterMetadata.

        集群更新时间

        :param update_timestamp: The update_timestamp of this ClusterMetadata.
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
        if not isinstance(other, ClusterMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
