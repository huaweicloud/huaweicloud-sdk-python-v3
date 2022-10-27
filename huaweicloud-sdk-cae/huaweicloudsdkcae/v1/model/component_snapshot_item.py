# coding: utf-8

import re
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
        'context': 'object',
        'created_at': 'datetime',
        'description': 'str',
        'index': 'int',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'component_id': 'component_id',
        'context': 'context',
        'created_at': 'created_at',
        'description': 'description',
        'index': 'index',
        'updated_at': 'updated_at'
    }

    def __init__(self, component_id=None, context=None, created_at=None, description=None, index=None, updated_at=None):
        """ComponentSnapshotItem

        The model defined in huaweicloud sdk

        :param component_id: 组件id。
        :type component_id: str
        :param context: 上下文信息。
        :type context: object
        :param created_at: 创建时间。
        :type created_at: datetime
        :param description: 描述。
        :type description: str
        :param index: 快照索引。
        :type index: int
        :param updated_at: 修改时间。
        :type updated_at: datetime
        """
        
        

        self._component_id = None
        self._context = None
        self._created_at = None
        self._description = None
        self._index = None
        self._updated_at = None
        self.discriminator = None

        if component_id is not None:
            self.component_id = component_id
        if context is not None:
            self.context = context
        if created_at is not None:
            self.created_at = created_at
        if description is not None:
            self.description = description
        if index is not None:
            self.index = index
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def component_id(self):
        """Gets the component_id of this ComponentSnapshotItem.

        组件id。

        :return: The component_id of this ComponentSnapshotItem.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ComponentSnapshotItem.

        组件id。

        :param component_id: The component_id of this ComponentSnapshotItem.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def context(self):
        """Gets the context of this ComponentSnapshotItem.

        上下文信息。

        :return: The context of this ComponentSnapshotItem.
        :rtype: object
        """
        return self._context

    @context.setter
    def context(self, context):
        """Sets the context of this ComponentSnapshotItem.

        上下文信息。

        :param context: The context of this ComponentSnapshotItem.
        :type context: object
        """
        self._context = context

    @property
    def created_at(self):
        """Gets the created_at of this ComponentSnapshotItem.

        创建时间。

        :return: The created_at of this ComponentSnapshotItem.
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this ComponentSnapshotItem.

        创建时间。

        :param created_at: The created_at of this ComponentSnapshotItem.
        :type created_at: datetime
        """
        self._created_at = created_at

    @property
    def description(self):
        """Gets the description of this ComponentSnapshotItem.

        描述。

        :return: The description of this ComponentSnapshotItem.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ComponentSnapshotItem.

        描述。

        :param description: The description of this ComponentSnapshotItem.
        :type description: str
        """
        self._description = description

    @property
    def index(self):
        """Gets the index of this ComponentSnapshotItem.

        快照索引。

        :return: The index of this ComponentSnapshotItem.
        :rtype: int
        """
        return self._index

    @index.setter
    def index(self, index):
        """Sets the index of this ComponentSnapshotItem.

        快照索引。

        :param index: The index of this ComponentSnapshotItem.
        :type index: int
        """
        self._index = index

    @property
    def updated_at(self):
        """Gets the updated_at of this ComponentSnapshotItem.

        修改时间。

        :return: The updated_at of this ComponentSnapshotItem.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ComponentSnapshotItem.

        修改时间。

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
