# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Metadata:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'uid': 'str',
        'name': 'str',
        'labels': 'dict(str, str)',
        'annotations': 'dict(str, str)',
        'update_timestamp': 'date',
        'creation_timestamp': 'date'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'labels': 'labels',
        'annotations': 'annotations',
        'update_timestamp': 'updateTimestamp',
        'creation_timestamp': 'creationTimestamp'
    }

    def __init__(self, uid=None, name=None, labels=None, annotations=None, update_timestamp=None, creation_timestamp=None):
        """Metadata

        The model defined in huaweicloud sdk

        :param uid: 唯一id标识
        :type uid: str
        :param name: 插件名称
        :type name: str
        :param labels: 插件标签，key/value对格式，接口保留字段，填写不会生效
        :type labels: dict(str, str)
        :param annotations: 插件注解，由key/value组成 - 安装：固定值为{\&quot;addon.install/type\&quot;:\&quot;install\&quot;} - 升级：固定值为{\&quot;addon.upgrade/type\&quot;:\&quot;upgrade\&quot;} 
        :type annotations: dict(str, str)
        :param update_timestamp: 更新时间
        :type update_timestamp: date
        :param creation_timestamp: 创建时间
        :type creation_timestamp: date
        """
        
        

        self._uid = None
        self._name = None
        self._labels = None
        self._annotations = None
        self._update_timestamp = None
        self._creation_timestamp = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp

    @property
    def uid(self):
        """Gets the uid of this Metadata.

        唯一id标识

        :return: The uid of this Metadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this Metadata.

        唯一id标识

        :param uid: The uid of this Metadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        """Gets the name of this Metadata.

        插件名称

        :return: The name of this Metadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Metadata.

        插件名称

        :param name: The name of this Metadata.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        """Gets the labels of this Metadata.

        插件标签，key/value对格式，接口保留字段，填写不会生效

        :return: The labels of this Metadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Metadata.

        插件标签，key/value对格式，接口保留字段，填写不会生效

        :param labels: The labels of this Metadata.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def annotations(self):
        """Gets the annotations of this Metadata.

        插件注解，由key/value组成 - 安装：固定值为{\"addon.install/type\":\"install\"} - 升级：固定值为{\"addon.upgrade/type\":\"upgrade\"} 

        :return: The annotations of this Metadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this Metadata.

        插件注解，由key/value组成 - 安装：固定值为{\"addon.install/type\":\"install\"} - 升级：固定值为{\"addon.upgrade/type\":\"upgrade\"} 

        :param annotations: The annotations of this Metadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this Metadata.

        更新时间

        :return: The update_timestamp of this Metadata.
        :rtype: date
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this Metadata.

        更新时间

        :param update_timestamp: The update_timestamp of this Metadata.
        :type update_timestamp: date
        """
        self._update_timestamp = update_timestamp

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this Metadata.

        创建时间

        :return: The creation_timestamp of this Metadata.
        :rtype: date
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this Metadata.

        创建时间

        :param creation_timestamp: The creation_timestamp of this Metadata.
        :type creation_timestamp: date
        """
        self._creation_timestamp = creation_timestamp

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
        if not isinstance(other, Metadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
