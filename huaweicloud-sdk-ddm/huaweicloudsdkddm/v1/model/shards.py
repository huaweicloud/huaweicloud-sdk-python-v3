# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class Shards:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'data_node_id': 'str',
        'physical_db_name': 'str',
        'status': 'str',
        'shard_index': 'int'
    }

    attribute_map = {
        'data_node_id': 'data_node_id',
        'physical_db_name': 'physical_db_name',
        'status': 'status',
        'shard_index': 'shard_index'
    }

    def __init__(self, data_node_id=None, physical_db_name=None, status=None, shard_index=None):
        r"""Shards

        The model defined in huaweicloud sdk

        :param data_node_id: 物理分片所在RDS的ID。
        :type data_node_id: str
        :param physical_db_name: 物理分片名称。
        :type physical_db_name: str
        :param status: 物理分片运行状态。
        :type status: str
        :param shard_index: 物理分片序号。
        :type shard_index: int
        """
        
        

        self._data_node_id = None
        self._physical_db_name = None
        self._status = None
        self._shard_index = None
        self.discriminator = None

        if data_node_id is not None:
            self.data_node_id = data_node_id
        if physical_db_name is not None:
            self.physical_db_name = physical_db_name
        if status is not None:
            self.status = status
        if shard_index is not None:
            self.shard_index = shard_index

    @property
    def data_node_id(self):
        r"""Gets the data_node_id of this Shards.

        物理分片所在RDS的ID。

        :return: The data_node_id of this Shards.
        :rtype: str
        """
        return self._data_node_id

    @data_node_id.setter
    def data_node_id(self, data_node_id):
        r"""Sets the data_node_id of this Shards.

        物理分片所在RDS的ID。

        :param data_node_id: The data_node_id of this Shards.
        :type data_node_id: str
        """
        self._data_node_id = data_node_id

    @property
    def physical_db_name(self):
        r"""Gets the physical_db_name of this Shards.

        物理分片名称。

        :return: The physical_db_name of this Shards.
        :rtype: str
        """
        return self._physical_db_name

    @physical_db_name.setter
    def physical_db_name(self, physical_db_name):
        r"""Sets the physical_db_name of this Shards.

        物理分片名称。

        :param physical_db_name: The physical_db_name of this Shards.
        :type physical_db_name: str
        """
        self._physical_db_name = physical_db_name

    @property
    def status(self):
        r"""Gets the status of this Shards.

        物理分片运行状态。

        :return: The status of this Shards.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this Shards.

        物理分片运行状态。

        :param status: The status of this Shards.
        :type status: str
        """
        self._status = status

    @property
    def shard_index(self):
        r"""Gets the shard_index of this Shards.

        物理分片序号。

        :return: The shard_index of this Shards.
        :rtype: int
        """
        return self._shard_index

    @shard_index.setter
    def shard_index(self, shard_index):
        r"""Sets the shard_index of this Shards.

        物理分片序号。

        :param shard_index: The shard_index of this Shards.
        :type shard_index: int
        """
        self._shard_index = shard_index

    def to_dict(self):
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
        if not isinstance(other, Shards):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
