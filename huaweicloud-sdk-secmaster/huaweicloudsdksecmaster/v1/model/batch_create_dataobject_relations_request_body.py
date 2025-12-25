# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDataobjectRelationsRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dataobject_ids': 'list[str]',
        'related_dataobject_ids': 'list[str]'
    }

    attribute_map = {
        'dataobject_ids': 'dataobject_ids',
        'related_dataobject_ids': 'related_dataobject_ids'
    }

    def __init__(self, dataobject_ids=None, related_dataobject_ids=None):
        r"""BatchCreateDataobjectRelationsRequestBody

        The model defined in huaweicloud sdk

        :param dataobject_ids: 关联数据对象的ID列表
        :type dataobject_ids: list[str]
        :param related_dataobject_ids: 被关联数据对象的ID列表
        :type related_dataobject_ids: list[str]
        """
        
        

        self._dataobject_ids = None
        self._related_dataobject_ids = None
        self.discriminator = None

        if dataobject_ids is not None:
            self.dataobject_ids = dataobject_ids
        if related_dataobject_ids is not None:
            self.related_dataobject_ids = related_dataobject_ids

    @property
    def dataobject_ids(self):
        r"""Gets the dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.

        关联数据对象的ID列表

        :return: The dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.
        :rtype: list[str]
        """
        return self._dataobject_ids

    @dataobject_ids.setter
    def dataobject_ids(self, dataobject_ids):
        r"""Sets the dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.

        关联数据对象的ID列表

        :param dataobject_ids: The dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.
        :type dataobject_ids: list[str]
        """
        self._dataobject_ids = dataobject_ids

    @property
    def related_dataobject_ids(self):
        r"""Gets the related_dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.

        被关联数据对象的ID列表

        :return: The related_dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.
        :rtype: list[str]
        """
        return self._related_dataobject_ids

    @related_dataobject_ids.setter
    def related_dataobject_ids(self, related_dataobject_ids):
        r"""Sets the related_dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.

        被关联数据对象的ID列表

        :param related_dataobject_ids: The related_dataobject_ids of this BatchCreateDataobjectRelationsRequestBody.
        :type related_dataobject_ids: list[str]
        """
        self._related_dataobject_ids = related_dataobject_ids

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
        if not isinstance(other, BatchCreateDataobjectRelationsRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
