# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'id': 'str',
        'name': 'str',
        'annotations': 'dict(str, str)',
        'created_at': 'datetime',
        'updated_at': 'datetime',
        'spec': 'ComponentSpec'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'annotations': 'annotations',
        'created_at': 'created_at',
        'updated_at': 'updated_at',
        'spec': 'spec'
    }

    def __init__(self, id=None, name=None, annotations=None, created_at=None, updated_at=None, spec=None):
        """ComponentItem

        The model defined in huaweicloud sdk

        :param id: 组件ID。
        :type id: str
        :param name: 组件名称。
        :type name: str
        :param annotations: 资源信息。
        :type annotations: dict(str, str)
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.ComponentSpec`
        """
        
        

        self._id = None
        self._name = None
        self._annotations = None
        self._created_at = None
        self._updated_at = None
        self._spec = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if annotations is not None:
            self.annotations = annotations
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at
        if spec is not None:
            self.spec = spec

    @property
    def id(self):
        """Gets the id of this ComponentItem.

        组件ID。

        :return: The id of this ComponentItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentItem.

        组件ID。

        :param id: The id of this ComponentItem.
        :type id: str
        """
        self._id = id

    @property
    def name(self):
        """Gets the name of this ComponentItem.

        组件名称。

        :return: The name of this ComponentItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ComponentItem.

        组件名称。

        :param name: The name of this ComponentItem.
        :type name: str
        """
        self._name = name

    @property
    def annotations(self):
        """Gets the annotations of this ComponentItem.

        资源信息。

        :return: The annotations of this ComponentItem.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        """Sets the annotations of this ComponentItem.

        资源信息。

        :param annotations: The annotations of this ComponentItem.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def created_at(self):
        """Gets the created_at of this ComponentItem.

        创建时间。

        :return: The created_at of this ComponentItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ComponentItem.

        创建时间。

        :param created_at: The created_at of this ComponentItem.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this ComponentItem.

        更新时间。

        :return: The updated_at of this ComponentItem.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ComponentItem.

        更新时间。

        :param updated_at: The updated_at of this ComponentItem.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

    @property
    def spec(self):
        """Gets the spec of this ComponentItem.

        :return: The spec of this ComponentItem.
        :rtype: :class:`huaweicloudsdkcae.v1.ComponentSpec`
        """
        return self._spec

    @spec.setter
    def spec(self, spec):
        """Sets the spec of this ComponentItem.

        :param spec: The spec of this ComponentItem.
        :type spec: :class:`huaweicloudsdkcae.v1.ComponentSpec`
        """
        self._spec = spec

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
        if not isinstance(other, ComponentItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
