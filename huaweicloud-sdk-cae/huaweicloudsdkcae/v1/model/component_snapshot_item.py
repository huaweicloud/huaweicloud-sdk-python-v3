# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ComponentSnapshotItem:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'component_id': 'str',
        'index': 'int',
        'context': 'ComponentSnapshotContext',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'component_id': 'component_id',
        'index': 'index',
        'context': 'context',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, component_id=None, index=None, context=None, created_at=None, updated_at=None):
        r"""ComponentSnapshotItem

        The model defined in huaweicloud sdk

        :param component_id: 组件ID。
        :type component_id: str
        :param index: 快照索引。
        :type index: int
        :param context: 
        :type context: :class:`huaweicloudsdkcae.v1.ComponentSnapshotContext`
        :param created_at: 创建时间。
        :type created_at: datetime
        :param updated_at: 更新时间。
        :type updated_at: datetime
        """
        
        

        self._component_id = None
        self._index = None
        self._context = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if index is not None:
            self.index = index
        if context is not None:
            self.context = context
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def component_id(self):
        r"""Gets the component_id of this ComponentSnapshotItem.

        组件ID。

        :return: The component_id of this ComponentSnapshotItem.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        r"""Sets the component_id of this ComponentSnapshotItem.

        组件ID。

        :param component_id: The component_id of this ComponentSnapshotItem.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def index(self):
        r"""Gets the index of this ComponentSnapshotItem.

        快照索引。

        :return: The index of this ComponentSnapshotItem.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        r"""Sets the index of this ComponentSnapshotItem.

        快照索引。

        :param index: The index of this ComponentSnapshotItem.
        :type index: int
        """
        self._index = index

    @property
    def context(self):
        r"""Gets the context of this ComponentSnapshotItem.

        :return: The context of this ComponentSnapshotItem.
        :rtype: :class:`huaweicloudsdkcae.v1.ComponentSnapshotContext`
        """
        return self._context

    @context.setter
    def context(self, context):
        r"""Sets the context of this ComponentSnapshotItem.

        :param context: The context of this ComponentSnapshotItem.
        :type context: :class:`huaweicloudsdkcae.v1.ComponentSnapshotContext`
        """
        self._context = context

    @property
    def created_at(self):
        r"""Gets the created_at of this ComponentSnapshotItem.

        创建时间。

        :return: The created_at of this ComponentSnapshotItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        r"""Sets the created_at of this ComponentSnapshotItem.

        创建时间。

        :param created_at: The created_at of this ComponentSnapshotItem.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def updated_at(self):
        r"""Gets the updated_at of this ComponentSnapshotItem.

        更新时间。

        :return: The updated_at of this ComponentSnapshotItem.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        r"""Sets the updated_at of this ComponentSnapshotItem.

        更新时间。

        :param updated_at: The updated_at of this ComponentSnapshotItem.
        :type updated_at: datetime
        """
        self._updated_at = updated_at

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
        if not isinstance(other, ComponentSnapshotItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
