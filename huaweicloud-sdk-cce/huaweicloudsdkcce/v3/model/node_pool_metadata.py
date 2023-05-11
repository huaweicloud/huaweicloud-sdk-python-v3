# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class NodePoolMetadata:

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
        'update_timestamp': 'str',
        'creation_timestamp': 'str'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'annotations': 'annotations',
        'update_timestamp': 'updateTimestamp',
        'creation_timestamp': 'creationTimestamp'
    }

    def __init__(self, name=None, uid=None, annotations=None, update_timestamp=None, creation_timestamp=None):
        """NodePoolMetadata

        The model defined in huaweicloud sdk

        :param name: 节点名池名称。  &gt; 命名规则： &gt; &gt;  - 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-50位，且不能以中划线(-)结尾。 &gt; &gt;  - 不允许创建名为 DefaultPool 的节点池。
        :type name: str
        :param uid: 节点池的uid。创建成功后自动生成，填写无效
        :type uid: str
        :param annotations: 节点池的注解，以key value对表示。 
        :type annotations: dict(str, str)
        :param update_timestamp: 更新时间
        :type update_timestamp: str
        :param creation_timestamp: 创建时间
        :type creation_timestamp: str
        """
        
        

        self._name = None
        self._uid = None
        self._annotations = None
        self._update_timestamp = None
        self._creation_timestamp = None
        self.discriminator = None

        self.name = name
        if uid is not None:
            self.uid = uid
        if annotations is not None:
            self.annotations = annotations
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp

    @property
    def name(self):
        """Gets the name of this NodePoolMetadata.

        节点名池名称。  > 命名规则： > >  - 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-50位，且不能以中划线(-)结尾。 > >  - 不允许创建名为 DefaultPool 的节点池。

        :return: The name of this NodePoolMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NodePoolMetadata.

        节点名池名称。  > 命名规则： > >  - 以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围1-50位，且不能以中划线(-)结尾。 > >  - 不允许创建名为 DefaultPool 的节点池。

        :param name: The name of this NodePoolMetadata.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        """Gets the uid of this NodePoolMetadata.

        节点池的uid。创建成功后自动生成，填写无效

        :return: The uid of this NodePoolMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        """Sets the uid of this NodePoolMetadata.

        节点池的uid。创建成功后自动生成，填写无效

        :param uid: The uid of this NodePoolMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def annotations(self):
        """Gets the annotations of this NodePoolMetadata.

        节点池的注解，以key value对表示。 

        :return: The annotations of this NodePoolMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this NodePoolMetadata.

        节点池的注解，以key value对表示。 

        :param annotations: The annotations of this NodePoolMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def update_timestamp(self):
        """Gets the update_timestamp of this NodePoolMetadata.

        更新时间

        :return: The update_timestamp of this NodePoolMetadata.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        """Sets the update_timestamp of this NodePoolMetadata.

        更新时间

        :param update_timestamp: The update_timestamp of this NodePoolMetadata.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    @property
    def creation_timestamp(self):
        """Gets the creation_timestamp of this NodePoolMetadata.

        创建时间

        :return: The creation_timestamp of this NodePoolMetadata.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        """Sets the creation_timestamp of this NodePoolMetadata.

        创建时间

        :param creation_timestamp: The creation_timestamp of this NodePoolMetadata.
        :type creation_timestamp: str
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
        if not isinstance(other, NodePoolMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
