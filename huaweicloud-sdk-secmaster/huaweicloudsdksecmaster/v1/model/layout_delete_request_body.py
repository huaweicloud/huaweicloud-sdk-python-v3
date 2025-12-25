# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class LayoutDeleteRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'ids': 'list[str]',
        'is_delete': 'bool'
    }

    attribute_map = {
        'ids': 'ids',
        'is_delete': 'is_delete'
    }

    def __init__(self, ids=None, is_delete=None):
        r"""LayoutDeleteRequestBody

        The model defined in huaweicloud sdk

        :param ids: 布局ID列表
        :type ids: list[str]
        :param is_delete: 是否删除，为true时直接删除；如有引用关系，则删除失败
        :type is_delete: bool
        """
        
        

        self._ids = None
        self._is_delete = None
        self.discriminator = None

        self.ids = ids
        if is_delete is not None:
            self.is_delete = is_delete

    @property
    def ids(self):
        r"""Gets the ids of this LayoutDeleteRequestBody.

        布局ID列表

        :return: The ids of this LayoutDeleteRequestBody.
        :rtype: list[str]
        """
        return self._ids

    @ids.setter
    def ids(self, ids):
        r"""Sets the ids of this LayoutDeleteRequestBody.

        布局ID列表

        :param ids: The ids of this LayoutDeleteRequestBody.
        :type ids: list[str]
        """
        self._ids = ids

    @property
    def is_delete(self):
        r"""Gets the is_delete of this LayoutDeleteRequestBody.

        是否删除，为true时直接删除；如有引用关系，则删除失败

        :return: The is_delete of this LayoutDeleteRequestBody.
        :rtype: bool
        """
        return self._is_delete

    @is_delete.setter
    def is_delete(self, is_delete):
        r"""Sets the is_delete of this LayoutDeleteRequestBody.

        是否删除，为true时直接删除；如有引用关系，则删除失败

        :param is_delete: The is_delete of this LayoutDeleteRequestBody.
        :type is_delete: bool
        """
        self._is_delete = is_delete

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
        if not isinstance(other, LayoutDeleteRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
