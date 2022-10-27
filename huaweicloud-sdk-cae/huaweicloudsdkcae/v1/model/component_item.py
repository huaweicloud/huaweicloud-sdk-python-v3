# coding: utf-8

import re
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
        'status': 'str',
        'annotations': 'dict(str, str)',
        'spec': 'ComponentSpec'
    }

    attribute_map = {
        'id': 'id',
        'name': 'name',
        'status': 'status',
        'annotations': 'annotations',
        'spec': 'spec'
    }

    def __init__(self, id=None, name=None, status=None, annotations=None, spec=None):
        """ComponentItem

        The model defined in huaweicloud sdk

        :param id: 组件id。
        :type id: str
        :param name: 组件名称。
        :type name: str
        :param status: 组件状态。
        :type status: str
        :param annotations: 资源信息。
        :type annotations: dict(str, str)
        :param spec: 
        :type spec: :class:`huaweicloudsdkcae.v1.ComponentSpec`
        """
        
        

        self._id = None
        self._name = None
        self._status = None
        self._annotations = None
        self._spec = None
        self.discriminator = None

        if id is not None:
            self.id = id
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if annotations is not None:
            self.annotations = annotations
        if spec is not None:
            self.spec = spec

    @property
    def id(self):
        """Gets the id of this ComponentItem.

        组件id。

        :return: The id of this ComponentItem.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ComponentItem.

        组件id。

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
    def status(self):
        """Gets the status of this ComponentItem.

        组件状态。

        :return: The status of this ComponentItem.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ComponentItem.

        组件状态。

        :param status: The status of this ComponentItem.
        :type status: str
        """
        self._status = status

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
