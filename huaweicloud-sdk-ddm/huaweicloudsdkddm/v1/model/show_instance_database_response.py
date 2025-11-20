# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowInstanceDatabaseResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'shards': 'list[Shards]',
        'status': 'str',
        'created': 'str',
        'updated': 'str',
        'name': 'str',
        'shard_mode': 'str',
        'shard_number': 'int',
        'data_nodes': 'list[DataNodes]'
    }

    attribute_map = {
        'shards': 'shards',
        'status': 'status',
        'created': 'created',
        'updated': 'updated',
        'name': 'name',
        'shard_mode': 'shard_mode',
        'shard_number': 'shard_number',
        'data_nodes': 'data_nodes'
    }

    def __init__(self, shards=None, status=None, created=None, updated=None, name=None, shard_mode=None, shard_number=None, data_nodes=None):
        r"""ShowInstanceDatabaseResponse

        The model defined in huaweicloud sdk

        :param shards: 逻辑库分片信息。
        :type shards: list[:class:`huaweicloudsdkddm.v1.Shards`]
        :param status: 逻辑库状态。
        :type status: str
        :param created: 创建时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type created: str
        :param updated: 更新时间，格式为\&quot;yyyy-MM-ddTHH:mm:ssZ\&quot;。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。
        :type updated: str
        :param name: 逻辑库名称。
        :type name: str
        :param shard_mode: 拆分模式。
        :type shard_mode: str
        :param shard_number: 逻辑库分片数。
        :type shard_number: int
        :param data_nodes: 关联的后端DN信息。
        :type data_nodes: list[:class:`huaweicloudsdkddm.v1.DataNodes`]
        """
        
        super().__init__()

        self._shards = None
        self._status = None
        self._created = None
        self._updated = None
        self._name = None
        self._shard_mode = None
        self._shard_number = None
        self._data_nodes = None
        self.discriminator = None

        if shards is not None:
            self.shards = shards
        if status is not None:
            self.status = status
        if created is not None:
            self.created = created
        if updated is not None:
            self.updated = updated
        if name is not None:
            self.name = name
        if shard_mode is not None:
            self.shard_mode = shard_mode
        if shard_number is not None:
            self.shard_number = shard_number
        if data_nodes is not None:
            self.data_nodes = data_nodes

    @property
    def shards(self):
        r"""Gets the shards of this ShowInstanceDatabaseResponse.

        逻辑库分片信息。

        :return: The shards of this ShowInstanceDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.Shards`]
        """
        return self._shards

    @shards.setter
    def shards(self, shards):
        r"""Sets the shards of this ShowInstanceDatabaseResponse.

        逻辑库分片信息。

        :param shards: The shards of this ShowInstanceDatabaseResponse.
        :type shards: list[:class:`huaweicloudsdkddm.v1.Shards`]
        """
        self._shards = shards

    @property
    def status(self):
        r"""Gets the status of this ShowInstanceDatabaseResponse.

        逻辑库状态。

        :return: The status of this ShowInstanceDatabaseResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ShowInstanceDatabaseResponse.

        逻辑库状态。

        :param status: The status of this ShowInstanceDatabaseResponse.
        :type status: str
        """
        self._status = status

    @property
    def created(self):
        r"""Gets the created of this ShowInstanceDatabaseResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The created of this ShowInstanceDatabaseResponse.
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        r"""Sets the created of this ShowInstanceDatabaseResponse.

        创建时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param created: The created of this ShowInstanceDatabaseResponse.
        :type created: str
        """
        self._created = created

    @property
    def updated(self):
        r"""Gets the updated of this ShowInstanceDatabaseResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :return: The updated of this ShowInstanceDatabaseResponse.
        :rtype: str
        """
        return self._updated

    @updated.setter
    def updated(self, updated):
        r"""Sets the updated of this ShowInstanceDatabaseResponse.

        更新时间，格式为\"yyyy-MM-ddTHH:mm:ssZ\"。 其中，T指某个时间的开始；Z指时区偏移量，例如北京时间偏移显示为+0800。

        :param updated: The updated of this ShowInstanceDatabaseResponse.
        :type updated: str
        """
        self._updated = updated

    @property
    def name(self):
        r"""Gets the name of this ShowInstanceDatabaseResponse.

        逻辑库名称。

        :return: The name of this ShowInstanceDatabaseResponse.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        r"""Sets the name of this ShowInstanceDatabaseResponse.

        逻辑库名称。

        :param name: The name of this ShowInstanceDatabaseResponse.
        :type name: str
        """
        self._name = name

    @property
    def shard_mode(self):
        r"""Gets the shard_mode of this ShowInstanceDatabaseResponse.

        拆分模式。

        :return: The shard_mode of this ShowInstanceDatabaseResponse.
        :rtype: str
        """
        return self._shard_mode

    @shard_mode.setter
    def shard_mode(self, shard_mode):
        r"""Sets the shard_mode of this ShowInstanceDatabaseResponse.

        拆分模式。

        :param shard_mode: The shard_mode of this ShowInstanceDatabaseResponse.
        :type shard_mode: str
        """
        self._shard_mode = shard_mode

    @property
    def shard_number(self):
        r"""Gets the shard_number of this ShowInstanceDatabaseResponse.

        逻辑库分片数。

        :return: The shard_number of this ShowInstanceDatabaseResponse.
        :rtype: int
        """
        return self._shard_number

    @shard_number.setter
    def shard_number(self, shard_number):
        r"""Sets the shard_number of this ShowInstanceDatabaseResponse.

        逻辑库分片数。

        :param shard_number: The shard_number of this ShowInstanceDatabaseResponse.
        :type shard_number: int
        """
        self._shard_number = shard_number

    @property
    def data_nodes(self):
        r"""Gets the data_nodes of this ShowInstanceDatabaseResponse.

        关联的后端DN信息。

        :return: The data_nodes of this ShowInstanceDatabaseResponse.
        :rtype: list[:class:`huaweicloudsdkddm.v1.DataNodes`]
        """
        return self._data_nodes

    @data_nodes.setter
    def data_nodes(self, data_nodes):
        r"""Sets the data_nodes of this ShowInstanceDatabaseResponse.

        关联的后端DN信息。

        :param data_nodes: The data_nodes of this ShowInstanceDatabaseResponse.
        :type data_nodes: list[:class:`huaweicloudsdkddm.v1.DataNodes`]
        """
        self._data_nodes = data_nodes

    def to_dict(self):
        import warnings
        warnings.warn("ShowInstanceDatabaseResponse.to_dict() is deprecated and no longer maintained, "
                      "use to_json_object() to get the response content.", DeprecationWarning)
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
        if not isinstance(other, ShowInstanceDatabaseResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
