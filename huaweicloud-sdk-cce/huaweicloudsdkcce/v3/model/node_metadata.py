# coding: utf-8

import pprint
import re

import six





class NodeMetadata:


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
        'labels': 'dict(str, str)',
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
        """NodeMetadata - a model defined in huaweicloud sdk"""
        
        

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
        if name is not None:
            self.name = name
        if uid is not None:
            self.uid = uid
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def annotations(self):
        """Gets the annotations of this NodeMetadata.

        CCE自有节点注解，非Kubernetes原生annotations，格式为key/value键值对。  示例： ``` \"annotations\": {   \"key1\" : \"value1\",   \"key2\" : \"value2\" } ```  > Annotations不用于标识和选择对象。Annotations中的元数据可以是small 或large，structured 或unstructured，并且可以包括标签不允许使用的字符。

        :return: The annotations of this NodeMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this NodeMetadata.

        CCE自有节点注解，非Kubernetes原生annotations，格式为key/value键值对。  示例： ``` \"annotations\": {   \"key1\" : \"value1\",   \"key2\" : \"value2\" } ```  > Annotations不用于标识和选择对象。Annotations中的元数据可以是small 或large，structured 或unstructured，并且可以包括标签不允许使用的字符。

        :param annotations: The annotations of this NodeMetadata.
        :type: dict(str, str)
        """
        self._annotations = annotations

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this NodeMetadata.

        创建时间，创建成功后自动生成，填写无效

        :return: The creation_timestamp of this NodeMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this NodeMetadata.

        创建时间，创建成功后自动生成，填写无效

        :param creation_timestamp: The creation_timestamp of this NodeMetadata.
        :type: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def labels(self):
        """Gets the labels of this NodeMetadata.

        CCE自有节点标签，非Kubernetes原生labels。  标签可用于选择对象并查找满足某些条件的对象集合，格式为key/value键值对。  示例：  ``` \"labels\": {   \"key\" : \"value\" } ```

        :return: The labels of this NodeMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this NodeMetadata.

        CCE自有节点标签，非Kubernetes原生labels。  标签可用于选择对象并查找满足某些条件的对象集合，格式为key/value键值对。  示例：  ``` \"labels\": {   \"key\" : \"value\" } ```

        :param labels: The labels of this NodeMetadata.
        :type: dict(str, str)
        """
        self._labels = labels

    @property
    def name(self):
        """Gets the name of this NodeMetadata.

        节点名称 > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。

        :return: The name of this NodeMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodeMetadata.

        节点名称 > 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-56位，且不能以中划线(-)结尾。

        :param name: The name of this NodeMetadata.
        :type: str
        """
        self._name = name

    @property
    def uid(self):
        """Gets the uid of this NodeMetadata.

        资源唯一标识，创建成功后自动生成，填写无效

        :return: The uid of this NodeMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NodeMetadata.

        资源唯一标识，创建成功后自动生成，填写无效

        :param uid: The uid of this NodeMetadata.
        :type: str
        """
        self._uid = uid

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this NodeMetadata.

        更新时间，创建成功后自动生成，填写无效

        :return: The update_timestamp of this NodeMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this NodeMetadata.

        更新时间，创建成功后自动生成，填写无效

        :param update_timestamp: The update_timestamp of this NodeMetadata.
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
        if not isinstance(other, NodeMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
