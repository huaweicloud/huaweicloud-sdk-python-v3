# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListInstanceSnapshotsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'application_id': 'str',
        'component_id': 'str',
        'instance_id': 'str',
        'limit': 'int',
        'offset': 'int',
        'snapshot_order_by': 'str',
        'order': 'str'
    }

    attribute_map = {
        'application_id': 'application_id',
        'component_id': 'component_id',
        'instance_id': 'instance_id',
        'limit': 'limit',
        'offset': 'offset',
        'snapshot_order_by': 'snapshot_order_by',
        'order': 'order'
    }

    def __init__(self, application_id=None, component_id=None, instance_id=None, limit=None, offset=None, snapshot_order_by=None, order=None):
        """ListInstanceSnapshotsRequest

        The model defined in huaweicloud sdk

        :param application_id: 应用ID。
        :type application_id: str
        :param component_id: 组件ID。
        :type component_id: str
        :param instance_id: 组件实例ID。
        :type instance_id: str
        :param limit: 指定个数，明确指定的时候用于分页，取值[0, 100]。不指定的时候表示不分页，最多查询1000条记录。
        :type limit: int
        :param offset: 指定查询偏移量，默认偏移量为0.
        :type offset: int
        :param snapshot_order_by: 排序字段，默认按创建时间排序。  排序字段支持枚举值：create_time、version。 
        :type snapshot_order_by: str
        :param order: desc/asc，默认desc。
        :type order: str
        """
        
        

        self._application_id = None
        self._component_id = None
        self._instance_id = None
        self._limit = None
        self._offset = None
        self._snapshot_order_by = None
        self._order = None
        self.discriminator = None

        self.application_id = application_id
        self.component_id = component_id
        self.instance_id = instance_id
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if snapshot_order_by is not None:
            self.snapshot_order_by = snapshot_order_by
        if order is not None:
            self.order = order

    @property
    def application_id(self):
        """Gets the application_id of this ListInstanceSnapshotsRequest.

        应用ID。

        :return: The application_id of this ListInstanceSnapshotsRequest.
        :rtype: str
        """
        return self._application_id

    @application_id.setter
    def application_id(self, application_id):
        """Sets the application_id of this ListInstanceSnapshotsRequest.

        应用ID。

        :param application_id: The application_id of this ListInstanceSnapshotsRequest.
        :type application_id: str
        """
        self._application_id = application_id

    @property
    def component_id(self):
        """Gets the component_id of this ListInstanceSnapshotsRequest.

        组件ID。

        :return: The component_id of this ListInstanceSnapshotsRequest.
        :rtype: str
        """
        return self._component_id

    @component_id.setter
    def component_id(self, component_id):
        """Sets the component_id of this ListInstanceSnapshotsRequest.

        组件ID。

        :param component_id: The component_id of this ListInstanceSnapshotsRequest.
        :type component_id: str
        """
        self._component_id = component_id

    @property
    def instance_id(self):
        """Gets the instance_id of this ListInstanceSnapshotsRequest.

        组件实例ID。

        :return: The instance_id of this ListInstanceSnapshotsRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        """Sets the instance_id of this ListInstanceSnapshotsRequest.

        组件实例ID。

        :param instance_id: The instance_id of this ListInstanceSnapshotsRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def limit(self):
        """Gets the limit of this ListInstanceSnapshotsRequest.

        指定个数，明确指定的时候用于分页，取值[0, 100]。不指定的时候表示不分页，最多查询1000条记录。

        :return: The limit of this ListInstanceSnapshotsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListInstanceSnapshotsRequest.

        指定个数，明确指定的时候用于分页，取值[0, 100]。不指定的时候表示不分页，最多查询1000条记录。

        :param limit: The limit of this ListInstanceSnapshotsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListInstanceSnapshotsRequest.

        指定查询偏移量，默认偏移量为0.

        :return: The offset of this ListInstanceSnapshotsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListInstanceSnapshotsRequest.

        指定查询偏移量，默认偏移量为0.

        :param offset: The offset of this ListInstanceSnapshotsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def snapshot_order_by(self):
        """Gets the snapshot_order_by of this ListInstanceSnapshotsRequest.

        排序字段，默认按创建时间排序。  排序字段支持枚举值：create_time、version。 

        :return: The snapshot_order_by of this ListInstanceSnapshotsRequest.
        :rtype: str
        """
        return self._snapshot_order_by

    @snapshot_order_by.setter
    def snapshot_order_by(self, snapshot_order_by):
        """Sets the snapshot_order_by of this ListInstanceSnapshotsRequest.

        排序字段，默认按创建时间排序。  排序字段支持枚举值：create_time、version。 

        :param snapshot_order_by: The snapshot_order_by of this ListInstanceSnapshotsRequest.
        :type snapshot_order_by: str
        """
        self._snapshot_order_by = snapshot_order_by

    @property
    def order(self):
        """Gets the order of this ListInstanceSnapshotsRequest.

        desc/asc，默认desc。

        :return: The order of this ListInstanceSnapshotsRequest.
        :rtype: str
        """
        return self._order

    @order.setter
    def order(self, order):
        """Sets the order of this ListInstanceSnapshotsRequest.

        desc/asc，默认desc。

        :param order: The order of this ListInstanceSnapshotsRequest.
        :type order: str
        """
        self._order = order

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
        if not isinstance(other, ListInstanceSnapshotsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
