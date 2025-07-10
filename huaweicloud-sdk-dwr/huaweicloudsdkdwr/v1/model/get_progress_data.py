# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class GetProgressData:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'store_name': 'str',
        'collection_name': 'str',
        'build_progress': 'BuildProgress'
    }

    attribute_map = {
        'store_name': 'store_name',
        'collection_name': 'collection_name',
        'build_progress': 'build_progress'
    }

    def __init__(self, store_name=None, collection_name=None, build_progress=None):
        r"""GetProgressData

        The model defined in huaweicloud sdk

        :param store_name: **参数解释：** 知识仓实例名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type store_name: str
        :param collection_name: **参数解释：** Collection 名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。
        :type collection_name: str
        :param build_progress: 
        :type build_progress: :class:`huaweicloudsdkdwr.v1.BuildProgress`
        """
        
        

        self._store_name = None
        self._collection_name = None
        self._build_progress = None
        self.discriminator = None

        self.store_name = store_name
        self.collection_name = collection_name
        if build_progress is not None:
            self.build_progress = build_progress

    @property
    def store_name(self):
        r"""Gets the store_name of this GetProgressData.

        **参数解释：** 知识仓实例名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The store_name of this GetProgressData.
        :rtype: str
        """
        return self._store_name

    @store_name.setter
    def store_name(self, store_name):
        r"""Sets the store_name of this GetProgressData.

        **参数解释：** 知识仓实例名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param store_name: The store_name of this GetProgressData.
        :type store_name: str
        """
        self._store_name = store_name

    @property
    def collection_name(self):
        r"""Gets the collection_name of this GetProgressData.

        **参数解释：** Collection 名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :return: The collection_name of this GetProgressData.
        :rtype: str
        """
        return self._collection_name

    @collection_name.setter
    def collection_name(self, collection_name):
        r"""Sets the collection_name of this GetProgressData.

        **参数解释：** Collection 名称。 **约束限制：** 不涉及。 **取值范围：** 不涉及。 **默认取值:** 不涉及。

        :param collection_name: The collection_name of this GetProgressData.
        :type collection_name: str
        """
        self._collection_name = collection_name

    @property
    def build_progress(self):
        r"""Gets the build_progress of this GetProgressData.

        :return: The build_progress of this GetProgressData.
        :rtype: :class:`huaweicloudsdkdwr.v1.BuildProgress`
        """
        return self._build_progress

    @build_progress.setter
    def build_progress(self, build_progress):
        r"""Sets the build_progress of this GetProgressData.

        :param build_progress: The build_progress of this GetProgressData.
        :type build_progress: :class:`huaweicloudsdkdwr.v1.BuildProgress`
        """
        self._build_progress = build_progress

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
        if not isinstance(other, GetProgressData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
