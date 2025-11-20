# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class CollectionInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'collection_type': 'str',
        'collection_ids': 'list[str]'
    }

    attribute_map = {
        'collection_type': 'collection_type',
        'collection_ids': 'collection_ids'
    }

    def __init__(self, collection_type=None, collection_ids=None):
        r"""CollectionInfo

        The model defined in huaweicloud sdk

        :param collection_type: 收藏项类型。 * VOICE：音色
        :type collection_type: str
        :param collection_ids: 收藏的资产或者模板ID。
        :type collection_ids: list[str]
        """
        
        

        self._collection_type = None
        self._collection_ids = None
        self.discriminator = None

        if collection_type is not None:
            self.collection_type = collection_type
        if collection_ids is not None:
            self.collection_ids = collection_ids

    @property
    def collection_type(self):
        r"""Gets the collection_type of this CollectionInfo.

        收藏项类型。 * VOICE：音色

        :return: The collection_type of this CollectionInfo.
        :rtype: str
        """
        return self._collection_type

    @collection_type.setter
    def collection_type(self, collection_type):
        r"""Sets the collection_type of this CollectionInfo.

        收藏项类型。 * VOICE：音色

        :param collection_type: The collection_type of this CollectionInfo.
        :type collection_type: str
        """
        self._collection_type = collection_type

    @property
    def collection_ids(self):
        r"""Gets the collection_ids of this CollectionInfo.

        收藏的资产或者模板ID。

        :return: The collection_ids of this CollectionInfo.
        :rtype: list[str]
        """
        return self._collection_ids

    @collection_ids.setter
    def collection_ids(self, collection_ids):
        r"""Sets the collection_ids of this CollectionInfo.

        收藏的资产或者模板ID。

        :param collection_ids: The collection_ids of this CollectionInfo.
        :type collection_ids: list[str]
        """
        self._collection_ids = collection_ids

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
        if not isinstance(other, CollectionInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
