# coding: utf-8

import re
import six



from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListReplicationsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_group_id': 'str',
        'server_group_ids': 'str',
        'protected_instance_id': 'str',
        'protected_instance_ids': 'str',
        'name': 'str',
        'status': 'str',
        'limit': 'int',
        'offset': 'int',
        'query_type': 'str',
        'availability_zone': 'str'
    }

    attribute_map = {
        'server_group_id': 'server_group_id',
        'server_group_ids': 'server_group_ids',
        'protected_instance_id': 'protected_instance_id',
        'protected_instance_ids': 'protected_instance_ids',
        'name': 'name',
        'status': 'status',
        'limit': 'limit',
        'offset': 'offset',
        'query_type': 'query_type',
        'availability_zone': 'availability_zone'
    }

    def __init__(self, server_group_id=None, server_group_ids=None, protected_instance_id=None, protected_instance_ids=None, name=None, status=None, limit=None, offset=None, query_type=None, availability_zone=None):
        """ListReplicationsRequest

        The model defined in huaweicloud sdk

        :param server_group_id: 保护组的ID。
        :type server_group_id: str
        :param server_group_ids: 保护组的ID列表，格式为server_group_ids&#x3D;[&#39;server_group_id1&#39;,&#39;server_group_id2&#39;,...,&#39;server_group_idx&#39;]，请使用URL编码进行转换。返回“server_group_ids”中有效server_group_id的复制对列表，无效的server_group_id会被忽略。支持查询最多30个server_group_id对应的复制对列表。如果“server_group_id”和“server_group_ids”查询参数同时存在，“server_group_id”会被忽略。
        :type server_group_ids: str
        :param protected_instance_id: 保护实例的ID。
        :type protected_instance_id: str
        :param protected_instance_ids: 保护实例的ID列表，格式为protected_instance_ids&#x3D;[&#39;protected_instance_id1&#39;,&#39;protected_instance_id2&#39;,...,&#39;protected_instance_idx&#39;]，请使用URL编码进行转换。返回“protected_instance_ids”中有效protected_instance_id的复制对列表，无效的protected_instance_id会被忽略。支持查询最多30个protected_instance_id对应的复制对列表。如果“protected_instance_id”和“protected_instance_ids”查询参数同时存在，“protected_instance_id”会被忽略。
        :type protected_instance_ids: str
        :param name: 复制对的名称。支持模糊查询。
        :type name: str
        :param status: 复制对的状态。
        :type status: str
        :param limit: 每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。
        :type limit: int
        :param offset: 每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。
        :type offset: int
        :param query_type: 查询场景类型。如需查询异常状态的复制对列表，query_type的值为“status_abnormal”。否则，query_type取值为空或“general”。
        :type query_type: str
        :param availability_zone: 复制对所在的保护组的当前生产站点可用区。
        :type availability_zone: str
        """
        
        

        self._server_group_id = None
        self._server_group_ids = None
        self._protected_instance_id = None
        self._protected_instance_ids = None
        self._name = None
        self._status = None
        self._limit = None
        self._offset = None
        self._query_type = None
        self._availability_zone = None
        self.discriminator = None

        if server_group_id is not None:
            self.server_group_id = server_group_id
        if server_group_ids is not None:
            self.server_group_ids = server_group_ids
        if protected_instance_id is not None:
            self.protected_instance_id = protected_instance_id
        if protected_instance_ids is not None:
            self.protected_instance_ids = protected_instance_ids
        if name is not None:
            self.name = name
        if status is not None:
            self.status = status
        if limit is not None:
            self.limit = limit
        if offset is not None:
            self.offset = offset
        if query_type is not None:
            self.query_type = query_type
        if availability_zone is not None:
            self.availability_zone = availability_zone

    @property
    def server_group_id(self):
        """Gets the server_group_id of this ListReplicationsRequest.

        保护组的ID。

        :return: The server_group_id of this ListReplicationsRequest.
        :rtype: str
        """
        return self._server_group_id

    @server_group_id.setter
    def server_group_id(self, server_group_id):
        """Sets the server_group_id of this ListReplicationsRequest.

        保护组的ID。

        :param server_group_id: The server_group_id of this ListReplicationsRequest.
        :type server_group_id: str
        """
        self._server_group_id = server_group_id

    @property
    def server_group_ids(self):
        """Gets the server_group_ids of this ListReplicationsRequest.

        保护组的ID列表，格式为server_group_ids=['server_group_id1','server_group_id2',...,'server_group_idx']，请使用URL编码进行转换。返回“server_group_ids”中有效server_group_id的复制对列表，无效的server_group_id会被忽略。支持查询最多30个server_group_id对应的复制对列表。如果“server_group_id”和“server_group_ids”查询参数同时存在，“server_group_id”会被忽略。

        :return: The server_group_ids of this ListReplicationsRequest.
        :rtype: str
        """
        return self._server_group_ids

    @server_group_ids.setter
    def server_group_ids(self, server_group_ids):
        """Sets the server_group_ids of this ListReplicationsRequest.

        保护组的ID列表，格式为server_group_ids=['server_group_id1','server_group_id2',...,'server_group_idx']，请使用URL编码进行转换。返回“server_group_ids”中有效server_group_id的复制对列表，无效的server_group_id会被忽略。支持查询最多30个server_group_id对应的复制对列表。如果“server_group_id”和“server_group_ids”查询参数同时存在，“server_group_id”会被忽略。

        :param server_group_ids: The server_group_ids of this ListReplicationsRequest.
        :type server_group_ids: str
        """
        self._server_group_ids = server_group_ids

    @property
    def protected_instance_id(self):
        """Gets the protected_instance_id of this ListReplicationsRequest.

        保护实例的ID。

        :return: The protected_instance_id of this ListReplicationsRequest.
        :rtype: str
        """
        return self._protected_instance_id

    @protected_instance_id.setter
    def protected_instance_id(self, protected_instance_id):
        """Sets the protected_instance_id of this ListReplicationsRequest.

        保护实例的ID。

        :param protected_instance_id: The protected_instance_id of this ListReplicationsRequest.
        :type protected_instance_id: str
        """
        self._protected_instance_id = protected_instance_id

    @property
    def protected_instance_ids(self):
        """Gets the protected_instance_ids of this ListReplicationsRequest.

        保护实例的ID列表，格式为protected_instance_ids=['protected_instance_id1','protected_instance_id2',...,'protected_instance_idx']，请使用URL编码进行转换。返回“protected_instance_ids”中有效protected_instance_id的复制对列表，无效的protected_instance_id会被忽略。支持查询最多30个protected_instance_id对应的复制对列表。如果“protected_instance_id”和“protected_instance_ids”查询参数同时存在，“protected_instance_id”会被忽略。

        :return: The protected_instance_ids of this ListReplicationsRequest.
        :rtype: str
        """
        return self._protected_instance_ids

    @protected_instance_ids.setter
    def protected_instance_ids(self, protected_instance_ids):
        """Sets the protected_instance_ids of this ListReplicationsRequest.

        保护实例的ID列表，格式为protected_instance_ids=['protected_instance_id1','protected_instance_id2',...,'protected_instance_idx']，请使用URL编码进行转换。返回“protected_instance_ids”中有效protected_instance_id的复制对列表，无效的protected_instance_id会被忽略。支持查询最多30个protected_instance_id对应的复制对列表。如果“protected_instance_id”和“protected_instance_ids”查询参数同时存在，“protected_instance_id”会被忽略。

        :param protected_instance_ids: The protected_instance_ids of this ListReplicationsRequest.
        :type protected_instance_ids: str
        """
        self._protected_instance_ids = protected_instance_ids

    @property
    def name(self):
        """Gets the name of this ListReplicationsRequest.

        复制对的名称。支持模糊查询。

        :return: The name of this ListReplicationsRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ListReplicationsRequest.

        复制对的名称。支持模糊查询。

        :param name: The name of this ListReplicationsRequest.
        :type name: str
        """
        self._name = name

    @property
    def status(self):
        """Gets the status of this ListReplicationsRequest.

        复制对的状态。

        :return: The status of this ListReplicationsRequest.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListReplicationsRequest.

        复制对的状态。

        :param status: The status of this ListReplicationsRequest.
        :type status: str
        """
        self._status = status

    @property
    def limit(self):
        """Gets the limit of this ListReplicationsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :return: The limit of this ListReplicationsRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """Sets the limit of this ListReplicationsRequest.

        每次请求返回结果个数限制，取值范围为[0,1000]的正整数，默认值为1000。

        :param limit: The limit of this ListReplicationsRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def offset(self):
        """Gets the offset of this ListReplicationsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :return: The offset of this ListReplicationsRequest.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """Sets the offset of this ListReplicationsRequest.

        每次请求开始的下标，即偏移量，默认值为0。offset必须为数字，不能为负数。

        :param offset: The offset of this ListReplicationsRequest.
        :type offset: int
        """
        self._offset = offset

    @property
    def query_type(self):
        """Gets the query_type of this ListReplicationsRequest.

        查询场景类型。如需查询异常状态的复制对列表，query_type的值为“status_abnormal”。否则，query_type取值为空或“general”。

        :return: The query_type of this ListReplicationsRequest.
        :rtype: str
        """
        return self._query_type

    @query_type.setter
    def query_type(self, query_type):
        """Sets the query_type of this ListReplicationsRequest.

        查询场景类型。如需查询异常状态的复制对列表，query_type的值为“status_abnormal”。否则，query_type取值为空或“general”。

        :param query_type: The query_type of this ListReplicationsRequest.
        :type query_type: str
        """
        self._query_type = query_type

    @property
    def availability_zone(self):
        """Gets the availability_zone of this ListReplicationsRequest.

        复制对所在的保护组的当前生产站点可用区。

        :return: The availability_zone of this ListReplicationsRequest.
        :rtype: str
        """
        return self._availability_zone

    @availability_zone.setter
    def availability_zone(self, availability_zone):
        """Sets the availability_zone of this ListReplicationsRequest.

        复制对所在的保护组的当前生产站点可用区。

        :param availability_zone: The availability_zone of this ListReplicationsRequest.
        :type availability_zone: str
        """
        self._availability_zone = availability_zone

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
        if not isinstance(other, ListReplicationsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
