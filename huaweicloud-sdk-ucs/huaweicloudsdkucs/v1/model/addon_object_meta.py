# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AddonObjectMeta:

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
        'creation_timestamp': 'str',
        'update_timestamp': 'str'
    }

    attribute_map = {
        'uid': 'uid',
        'name': 'name',
        'labels': 'labels',
        'annotations': 'annotations',
        'creation_timestamp': 'creationTimestamp',
        'update_timestamp': 'updateTimestamp'
    }

    def __init__(self, uid=None, name=None, labels=None, annotations=None, creation_timestamp=None, update_timestamp=None):
        r"""AddonObjectMeta

        The model defined in huaweicloud sdk

        :param uid: 唯一标识符
        :type uid: str
        :param name: 对象的名称
        :type name: str
        :param labels: 对象的标签
        :type labels: dict(str, str)
        :param annotations: 对象的注解
        :type annotations: dict(str, str)
        :param creation_timestamp: 创建时间
        :type creation_timestamp: str
        :param update_timestamp: 更新时间
        :type update_timestamp: str
        """
        
        

        self._uid = None
        self._name = None
        self._labels = None
        self._annotations = None
        self._creation_timestamp = None
        self._update_timestamp = None
        self.discriminator = None

        if uid is not None:
            self.uid = uid
        if name is not None:
            self.name = name
        if labels is not None:
            self.labels = labels
        if annotations is not None:
            self.annotations = annotations
        if creation_timestamp is not None:
            self.creation_timestamp = creation_timestamp
        if update_timestamp is not None:
            self.update_timestamp = update_timestamp

    @property
    def uid(self):
        r"""Gets the uid of this AddonObjectMeta.

        唯一标识符

        :return: The uid of this AddonObjectMeta.
        :rtype: str
        """
        return self._uid

    @uid.setter
    def uid(self, uid):
        r"""Sets the uid of this AddonObjectMeta.

        唯一标识符

        :param uid: The uid of this AddonObjectMeta.
        :type uid: str
        """
        self._uid = uid

    @property
    def name(self):
        r"""Gets the name of this AddonObjectMeta.

        对象的名称

        :return: The name of this AddonObjectMeta.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this AddonObjectMeta.

        对象的名称

        :param name: The name of this AddonObjectMeta.
        :type name: str
        """
        self._name = name

    @property
    def labels(self):
        r"""Gets the labels of this AddonObjectMeta.

        对象的标签

        :return: The labels of this AddonObjectMeta.
        :rtype: dict(str, str)
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this AddonObjectMeta.

        对象的标签

        :param labels: The labels of this AddonObjectMeta.
        :type labels: dict(str, str)
        """
        self._labels = labels

    @property
    def annotations(self):
        r"""Gets the annotations of this AddonObjectMeta.

        对象的注解

        :return: The annotations of this AddonObjectMeta.
        :rtype: dict(str, str)
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this AddonObjectMeta.

        对象的注解

        :param annotations: The annotations of this AddonObjectMeta.
        :type annotations: dict(str, str)
        """
        self._annotations = annotations

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this AddonObjectMeta.

        创建时间

        :return: The creation_timestamp of this AddonObjectMeta.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this AddonObjectMeta.

        创建时间

        :param creation_timestamp: The creation_timestamp of this AddonObjectMeta.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def update_timestamp(self):
        r"""Gets the update_timestamp of this AddonObjectMeta.

        更新时间

        :return: The update_timestamp of this AddonObjectMeta.
        :rtype: str
        """
        return self._update_timestamp

    @update_timestamp.setter
    def update_timestamp(self, update_timestamp):
        r"""Sets the update_timestamp of this AddonObjectMeta.

        更新时间

        :param update_timestamp: The update_timestamp of this AddonObjectMeta.
        :type update_timestamp: str
        """
        self._update_timestamp = update_timestamp

    def to_dict(self):
        result = {}

        for attr, _ in self.openapi_types.items():
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
        return json.dumps(sanitize_for_serialization(self), ensure_ascii=False)

    def __repr__(self):
        """For `print`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, AddonObjectMeta):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
