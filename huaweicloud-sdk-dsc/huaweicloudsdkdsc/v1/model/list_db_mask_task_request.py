# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListDbMaskTaskRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'template_id': 'str',
        'workspace_id': 'str',
        'offset': 'int',
        'limit': 'int'
    }

    attribute_map = {
        'template_id': 'template_id',
        'workspace_id': 'workspace_id',
        'offset': 'offset',
        'limit': 'limit'
    }

    def __init__(self, template_id=None, workspace_id=None, offset=None, limit=None):
        r"""ListDbMaskTaskRequest

        The model defined in huaweicloud sdk

        :param template_id: 模板ID
        :type template_id: str
        :param workspace_id: 工作区ID
        :type workspace_id: str
        :param offset: 页码
        :type offset: int
        :param limit: 分页大小
        :type limit: int
        """
        
        

        self._template_id = None
        self._workspace_id = None
        self._offset = None
        self._limit = None
        self.discriminator = None

        self.template_id = template_id
        if workspace_id is not None:
            self.workspace_id = workspace_id
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit

    @property
    def template_id(self):
        r"""Gets the template_id of this ListDbMaskTaskRequest.

        模板ID

        :return: The template_id of this ListDbMaskTaskRequest.
        :rtype: str
        """
        return self._template_id

    @template_id.setter
    def template_id(self, template_id):
        r"""Sets the template_id of this ListDbMaskTaskRequest.

        模板ID

        :param template_id: The template_id of this ListDbMaskTaskRequest.
        :type template_id: str
        """
        self._template_id = template_id

    @property
    def workspace_id(self):
        r"""Gets the workspace_id of this ListDbMaskTaskRequest.

        工作区ID

        :return: The workspace_id of this ListDbMaskTaskRequest.
        :rtype: str
        """
        return self._workspace_id

    @workspace_id.setter
    def workspace_id(self, workspace_id):
        r"""Sets the workspace_id of this ListDbMaskTaskRequest.

        工作区ID

        :param workspace_id: The workspace_id of this ListDbMaskTaskRequest.
        :type workspace_id: str
        """
        self._workspace_id = workspace_id

    @property
    def offset(self):
        r"""Gets the offset of this ListDbMaskTaskRequest.

        页码

        :return: The offset of this ListDbMaskTaskRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListDbMaskTaskRequest.

        页码

        :param offset: The offset of this ListDbMaskTaskRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListDbMaskTaskRequest.

        分页大小

        :return: The limit of this ListDbMaskTaskRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListDbMaskTaskRequest.

        分页大小

        :param limit: The limit of this ListDbMaskTaskRequest.
        :type limit: int
        """
        self._limit = limit

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
        if not isinstance(other, ListDbMaskTaskRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
