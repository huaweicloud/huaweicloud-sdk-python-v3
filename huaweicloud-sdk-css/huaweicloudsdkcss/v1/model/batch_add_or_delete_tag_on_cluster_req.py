# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchAddOrDeleteTagOnClusterReq:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'action': 'str',
        'tags': 'list[Tag]'
    }

    attribute_map = {
        'action': 'action',
        'tags': 'tags'
    }

    def __init__(self, action=None, tags=None):
        r"""BatchAddOrDeleteTagOnClusterReq

        The model defined in huaweicloud sdk

        :param action: 操作类型。通过该属性标识当前所需的操作类型。  - create：批量添加标签。 - delete：批量删除标签。
        :type action: str
        :param tags: 标签列表。
        :type tags: list[:class:`huaweicloudsdkcss.v1.Tag`]
        """
        
        

        self._action = None
        self._tags = None
        self.discriminator = None

        self.action = action
        self.tags = tags

    @property
    def action(self):
        r"""Gets the action of this BatchAddOrDeleteTagOnClusterReq.

        操作类型。通过该属性标识当前所需的操作类型。  - create：批量添加标签。 - delete：批量删除标签。

        :return: The action of this BatchAddOrDeleteTagOnClusterReq.
        :rtype: str
        """
        return self._action

    @action.setter
    def action(self, action):
        r"""Sets the action of this BatchAddOrDeleteTagOnClusterReq.

        操作类型。通过该属性标识当前所需的操作类型。  - create：批量添加标签。 - delete：批量删除标签。

        :param action: The action of this BatchAddOrDeleteTagOnClusterReq.
        :type action: str
        """
        self._action = action

    @property
    def tags(self):
        r"""Gets the tags of this BatchAddOrDeleteTagOnClusterReq.

        标签列表。

        :return: The tags of this BatchAddOrDeleteTagOnClusterReq.
        :rtype: list[:class:`huaweicloudsdkcss.v1.Tag`]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        r"""Sets the tags of this BatchAddOrDeleteTagOnClusterReq.

        标签列表。

        :param tags: The tags of this BatchAddOrDeleteTagOnClusterReq.
        :type tags: list[:class:`huaweicloudsdkcss.v1.Tag`]
        """
        self._tags = tags

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
        if not isinstance(other, BatchAddOrDeleteTagOnClusterReq):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
