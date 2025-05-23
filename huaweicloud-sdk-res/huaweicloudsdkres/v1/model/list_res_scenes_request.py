# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListResScenesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'content_type': 'str',
        'workspace_id': 'str',
        'category': 'str'
    }

    attribute_map = {
        'content_type': 'Content-Type',
        'workspace_id': 'workspace_id',
        'category': 'category'
    }

    def __init__(self, content_type=None, workspace_id=None, category=None):
        r"""ListResScenesRequest

        The model defined in huaweicloud sdk

        :param content_type: 内容类型，取值为application/json。
        :type content_type: str
        :param workspace_id: 工作空间id。
        :type workspace_id: str
        :param category: 场景类型： - customize，自定义推荐 - intelligent，智能场景
        :type category: str
        """
        
        

        self._content_type = None
        self._workspace_id = None
        self._category = None
        self.discriminator = None

        self.content_type = content_type
        self.workspace_id = workspace_id
        self.category = category

    @property
    def content_type(self):
        r"""Gets the content_type of this ListResScenesRequest.

        内容类型，取值为application/json。

        :return: The content_type of this ListResScenesRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ListResScenesRequest.

        内容类型，取值为application/json。

        :param content_type: The content_type of this ListResScenesRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListResScenesRequest.

        工作空间id。

        :return: The workspace_id of this ListResScenesRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListResScenesRequest.

        工作空间id。

        :param workspace_id: The workspace_id of this ListResScenesRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def category(self):
        r"""Gets the category of this ListResScenesRequest.

        场景类型： - customize，自定义推荐 - intelligent，智能场景

        :return: The category of this ListResScenesRequest.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        r"""Sets the category of this ListResScenesRequest.

        场景类型： - customize，自定义推荐 - intelligent，智能场景

        :param category: The category of this ListResScenesRequest.
        :type category: str
        """
        self._category = category

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
        if not isinstance(other, ListResScenesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
