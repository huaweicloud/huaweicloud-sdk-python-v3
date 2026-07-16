# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class PoolMetadataDeletion:

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
        'creation_timestamp': 'str',
        'deletion_timestamp': 'str',
        'labels': 'PoolMetaLabels',
        'annotations': 'PoolMetaAnnotations'
    }

    attribute_map = {
        'name': 'name',
        'creation_timestamp': 'creationTimestamp',
        'deletion_timestamp': 'deletionTimestamp',
        'labels': 'labels',
        'annotations': 'annotations'
    }

    def __init__(self, name=None, creation_timestamp=None, deletion_timestamp=None, labels=None, annotations=None):
        r"""PoolMetadataDeletion

        The model defined in huaweicloud sdk

        :param name: **参数描述**： 系统自动生成的pool名称，相当于poolId。 **取值范围**： 不涉及。
        :type name: str
        :param creation_timestamp: **参数描述**： 时间戳，例如\&quot;2021-11-01T03:49:41Z\&quot;。 **取值范围**： 不涉及。
        :type creation_timestamp: str
        :param deletion_timestamp: **参数描述**： 时间戳，例如\&quot;2021-11-01T03:49:41Z\&quot;。 **取值范围**： 不涉及。
        :type deletion_timestamp: str
        :param labels: 
        :type labels: :class:`huaweicloudsdkmodelarts.v1.PoolMetaLabels`
        :param annotations: 
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.PoolMetaAnnotations`
        """
        
        

        self._name = None
        self._creation_timestamp = None
        self._deletion_timestamp = None
        self._labels = None
        self._annotations = None
        self.discriminator = None

        self.name = name
        self.creation_timestamp = creation_timestamp
        self.deletion_timestamp = deletion_timestamp
        self.labels = labels
        if annotations is not None:
            self.annotations = annotations

    @property
    def name(self):
        r"""Gets the name of this PoolMetadataDeletion.

        **参数描述**： 系统自动生成的pool名称，相当于poolId。 **取值范围**： 不涉及。

        :return: The name of this PoolMetadataDeletion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this PoolMetadataDeletion.

        **参数描述**： 系统自动生成的pool名称，相当于poolId。 **取值范围**： 不涉及。

        :param name: The name of this PoolMetadataDeletion.
        :type name: str
        """
        self._name = name

    @property
    def creation_timestamp(self):
        r"""Gets the creation_timestamp of this PoolMetadataDeletion.

        **参数描述**： 时间戳，例如\"2021-11-01T03:49:41Z\"。 **取值范围**： 不涉及。

        :return: The creation_timestamp of this PoolMetadataDeletion.
        :rtype: str
        """
        return self._creation_timestamp

    @creation_timestamp.setter
    def creation_timestamp(self, creation_timestamp):
        r"""Sets the creation_timestamp of this PoolMetadataDeletion.

        **参数描述**： 时间戳，例如\"2021-11-01T03:49:41Z\"。 **取值范围**： 不涉及。

        :param creation_timestamp: The creation_timestamp of this PoolMetadataDeletion.
        :type creation_timestamp: str
        """
        self._creation_timestamp = creation_timestamp

    @property
    def deletion_timestamp(self):
        r"""Gets the deletion_timestamp of this PoolMetadataDeletion.

        **参数描述**： 时间戳，例如\"2021-11-01T03:49:41Z\"。 **取值范围**： 不涉及。

        :return: The deletion_timestamp of this PoolMetadataDeletion.
        :rtype: str
        """
        return self._deletion_timestamp

    @deletion_timestamp.setter
    def deletion_timestamp(self, deletion_timestamp):
        r"""Sets the deletion_timestamp of this PoolMetadataDeletion.

        **参数描述**： 时间戳，例如\"2021-11-01T03:49:41Z\"。 **取值范围**： 不涉及。

        :param deletion_timestamp: The deletion_timestamp of this PoolMetadataDeletion.
        :type deletion_timestamp: str
        """
        self._deletion_timestamp = deletion_timestamp

    @property
    def labels(self):
        r"""Gets the labels of this PoolMetadataDeletion.

        :return: The labels of this PoolMetadataDeletion.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolMetaLabels`
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        r"""Sets the labels of this PoolMetadataDeletion.

        :param labels: The labels of this PoolMetadataDeletion.
        :type labels: :class:`huaweicloudsdkmodelarts.v1.PoolMetaLabels`
        """
        self._labels = labels

    @property
    def annotations(self):
        r"""Gets the annotations of this PoolMetadataDeletion.

        :return: The annotations of this PoolMetadataDeletion.
        :rtype: :class:`huaweicloudsdkmodelarts.v1.PoolMetaAnnotations`
        """
        return self._annotations

    @annotations.setter
    def annotations(self, annotations):
        r"""Sets the annotations of this PoolMetadataDeletion.

        :param annotations: The annotations of this PoolMetadataDeletion.
        :type annotations: :class:`huaweicloudsdkmodelarts.v1.PoolMetaAnnotations`
        """
        self._annotations = annotations

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
        if not isinstance(other, PoolMetadataDeletion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
