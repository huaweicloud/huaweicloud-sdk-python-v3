# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyPolicyTargetReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'add': 'list[Target]',
        'delete': 'list[Target]'
    }

    attribute_map = {
        'add': 'add',
        'delete': 'delete'
    }

    def __init__(self, add=None, delete=None):
        r"""ModifyPolicyTargetReq

        The model defined in huaweicloud sdk

        :param add: 添加应用。
        :type add: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        :param delete: 删除应用。
        :type delete: list[:class:`huaweicloudsdkworkspace.v2.Target`]
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
        r"""Gets the add of this ModifyPolicyTargetReq.

        添加应用。

        :return: The add of this ModifyPolicyTargetReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        return self._add

    @add.setter
    def add(self, add):
        r"""Sets the add of this ModifyPolicyTargetReq.

        添加应用。

        :param add: The add of this ModifyPolicyTargetReq.
        :type add: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        self._add = add

    @property
    def delete(self):
        r"""Gets the delete of this ModifyPolicyTargetReq.

        删除应用。

        :return: The delete of this ModifyPolicyTargetReq.
        :rtype: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        r"""Sets the delete of this ModifyPolicyTargetReq.

        删除应用。

        :param delete: The delete of this ModifyPolicyTargetReq.
        :type delete: list[:class:`huaweicloudsdkworkspace.v2.Target`]
        """
        self._delete = delete

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
        if not isinstance(other, ModifyPolicyTargetReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
