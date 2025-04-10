# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class MeshMetadata:

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
        'creation_timestamp': 'datetime'
    }

    attribute_map = {
        'name': 'name',
        'uid': 'uid',
        'annotations': 'annotations',
        'labels': 'labels',
        'creation_timestamp': 'creationTimestamp'
    }

    def __init__(self, name=None, uid=None, annotations=None, labels=None, creation_timestamp=None):
        r"""MeshMetadata

        The model defined in huaweicloud sdk

        :param name: 网格名称。 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-64位，且不能以中划线(-)结尾
        :type name: str
        :param uid: 网格ID，资源唯一标识，创建成功后自动生成，填写无效
        :type uid: str
        :param annotations: 网格注解，由key/value组成： &#x60;&#x60;&#x60; \&quot;annotations\&quot;: {    \&quot;key1\&quot; : \&quot;value1\&quot;,    \&quot;key2\&quot; : \&quot;value2\&quot; } &#x60;&#x60;&#x60;
        :type annotations: dict(str, str)
        :param labels: 网格标签，由key/value组成：   &#x60;&#x60;&#x60;  \&quot;labels\&quot;: {    \&quot;key1\&quot; : \&quot;value1\&quot;,    \&quot;key2\&quot; : \&quot;value2\&quot; }  &#x60;&#x60;&#x60;
        :type labels: dict(str, str)
        :param creation_timestamp: 网格创建时间
        :type creation_timestamp: datetime
        """
        
        

        self._name = None
        self._uid = None
        self._annotations = None
        self._labels = None
        self._creation_timestamp = None
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

    @property
    def name(self):
        r"""Gets the name of this MeshMetadata.

        网格名称。 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-64位，且不能以中划线(-)结尾

        :return: The name of this MeshMetadata.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this MeshMetadata.

        网格名称。 命名规则：以小写字母开头，由小写字母、数字、中划线(-)组成，长度范围4-64位，且不能以中划线(-)结尾

        :param name: The name of this MeshMetadata.
        :type name: str
        """
        self._name = name

    @property
    def uid(self):
        r"""Gets the uid of this MeshMetadata.

        网格ID，资源唯一标识，创建成功后自动生成，填写无效

        :return: The uid of this MeshMetadata.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this MeshMetadata.

        网格ID，资源唯一标识，创建成功后自动生成，填写无效

        :param uid: The uid of this MeshMetadata.
        :type uid: str
        """
        self._uid = uid

    @property
    def annotations(self):
        r"""Gets the annotations of this MeshMetadata.

        网格注解，由key/value组成： ``` \"annotations\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" } ```

        :return: The annotations of this MeshMetadata.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this MeshMetadata.

        网格注解，由key/value组成： ``` \"annotations\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" } ```

        :param annotations: The annotations of this MeshMetadata.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def labels(self):
        r"""Gets the labels of this MeshMetadata.

        网格标签，由key/value组成：   ```  \"labels\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" }  ```

        :return: The labels of this MeshMetadata.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this MeshMetadata.

        网格标签，由key/value组成：   ```  \"labels\": {    \"key1\" : \"value1\",    \"key2\" : \"value2\" }  ```

        :param labels: The labels of this MeshMetadata.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this MeshMetadata.

        网格创建时间

        :return: The creation_timestamp of this MeshMetadata.
        :rtype: datetime
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this MeshMetadata.

        网格创建时间

        :param creation_timestamp: The creation_timestamp of this MeshMetadata.
        :type creation_timestamp: datetime
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
        if not isinstance(other, MeshMetadata):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
