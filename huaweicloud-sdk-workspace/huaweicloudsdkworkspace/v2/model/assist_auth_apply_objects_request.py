# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class AssistAuthApplyObjectsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add': 'list[ApplyObjects]',
        'delete': 'list[ApplyObjects]'
    }

    attribute_map = {
        'add': 'add',
        'delete': 'delete'
    }

    def __init__(self, add=None, delete=None):
        r"""AssistAuthApplyObjectsRequest

        The model defined in huaweicloud sdk

        :param add: 需要新增的应用对象。
        :type add: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjects`]
        :param delete: 要移除的应用对象。
        :type delete: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjects`]
        """
        
        

        self._add = None
        self._delete = None
        self.discriminator = None

        if add is not None:
            self.add = add
        if delete is not None:
            self.delete = delete

    @property
    def add(self):
        r"""Gets the add of this AssistAuthApplyObjectsRequest.

        需要新增的应用对象。

        :return: The add of this AssistAuthApplyObjectsRequest.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjects`]
        """
        return self._add

    @add.setter
    def add(self, add):
        r"""Sets the add of this AssistAuthApplyObjectsRequest.

        需要新增的应用对象。

        :param add: The add of this AssistAuthApplyObjectsRequest.
        :type add: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjects`]
        """
        self._add = add

    @property
    def delete(self):
        r"""Gets the delete of this AssistAuthApplyObjectsRequest.

        要移除的应用对象。

        :return: The delete of this AssistAuthApplyObjectsRequest.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjects`]
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this AssistAuthApplyObjectsRequest.

        要移除的应用对象。

        :param delete: The delete of this AssistAuthApplyObjectsRequest.
        :type delete: list[:class:`huaweicloudsdkworkspace.v2.ApplyObjects`]
        """
        self._delete = delete

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
        if not isinstance(other, AssistAuthApplyObjectsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
