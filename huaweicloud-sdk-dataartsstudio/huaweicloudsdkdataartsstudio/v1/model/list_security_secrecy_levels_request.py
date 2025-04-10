# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListSecuritySecrecyLevelsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'workspace': 'str',
        'offset': 'int',
        'limit': 'int',
        'order_by': 'str',
        'desc': 'bool'
    }

    attribute_map = {
        'workspace': 'workspace',
        'offset': 'offset',
        'limit': 'limit',
        'order_by': 'order_by',
        'desc': 'desc'
    }

    def __init__(self, workspace=None, offset=None, limit=None, order_by=None, desc=None):
        r"""ListSecuritySecrecyLevelsRequest

        The model defined in huaweicloud sdk

        :param workspace: DataArts Studio工作空间ID
        :type workspace: str
        :param offset: offset
        :type offset: int
        :param limit: limit
        :type limit: int
        :param order_by: 排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description
        :type order_by: str
        :param desc: 排序规则
        :type desc: bool
        """
        
        

        self._workspace = None
        self._offset = None
        self._limit = None
        self._order_by = None
        self._desc = None
        self.discriminator = None

        self.workspace = workspace
        if offset is not None:
            self.offset = offset
        if limit is not None:
            self.limit = limit
        if order_by is not None:
            self.order_by = order_by
        if desc is not None:
            self.desc = desc

    @property
    def workspace(self):
        r"""Gets the workspace of this ListSecuritySecrecyLevelsRequest.

        DataArts Studio工作空间ID

        :return: The workspace of this ListSecuritySecrecyLevelsRequest.
        :rtype: str
        """
        return self._workspace

    @workspace.setter
    def workspace(self, workspace):
        r"""Sets the workspace of this ListSecuritySecrecyLevelsRequest.

        DataArts Studio工作空间ID

        :param workspace: The workspace of this ListSecuritySecrecyLevelsRequest.
        :type workspace: str
        """
        self._workspace = workspace

    @property
    def offset(self):
        r"""Gets the offset of this ListSecuritySecrecyLevelsRequest.

        offset

        :return: The offset of this ListSecuritySecrecyLevelsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        r"""Sets the offset of this ListSecuritySecrecyLevelsRequest.

        offset

        :param offset: The offset of this ListSecuritySecrecyLevelsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def limit(self):
        r"""Gets the limit of this ListSecuritySecrecyLevelsRequest.

        limit

        :return: The limit of this ListSecuritySecrecyLevelsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListSecuritySecrecyLevelsRequest.

        limit

        :param limit: The limit of this ListSecuritySecrecyLevelsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def order_by(self):
        r"""Gets the order_by of this ListSecuritySecrecyLevelsRequest.

        排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description

        :return: The order_by of this ListSecuritySecrecyLevelsRequest.
        :rtype: str
        """
        return self._order_by

    @order_by.setter
    def order_by(self, order_by):
        r"""Sets the order_by of this ListSecuritySecrecyLevelsRequest.

        排序字段, createdAt, createdBy, updatedAt, updatedBy, name, description

        :param order_by: The order_by of this ListSecuritySecrecyLevelsRequest.
        :type order_by: str
        """
        self._order_by = order_by

    @property
    def desc(self):
        r"""Gets the desc of this ListSecuritySecrecyLevelsRequest.

        排序规则

        :return: The desc of this ListSecuritySecrecyLevelsRequest.
        :rtype: bool
        """
        return self._desc

    @desc.setter
    def desc(self, desc):
        r"""Sets the desc of this ListSecuritySecrecyLevelsRequest.

        排序规则

        :param desc: The desc of this ListSecuritySecrecyLevelsRequest.
        :type desc: bool
        """
        self._desc = desc

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
        if not isinstance(other, ListSecuritySecrecyLevelsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
