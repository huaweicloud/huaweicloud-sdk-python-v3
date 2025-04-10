# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ConsumerCheckpointInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'checkpoint': 'int',
        'consumer_group_name': 'str',
        'consumer_name': 'str',
        'project_id': 'str',
        'shard_id': 'str',
        'update_time': 'int'
    }

    attribute_map = {
        'checkpoint': 'checkpoint',
        'consumer_group_name': 'consumer_group_name',
        'consumer_name': 'consumer_name',
        'project_id': 'project_id',
        'shard_id': 'shard_id',
        'update_time': 'update_time'
    }

    def __init__(self, checkpoint=None, consumer_group_name=None, consumer_name=None, project_id=None, shard_id=None, update_time=None):
        r"""ConsumerCheckpointInfo

        The model defined in huaweicloud sdk

        :param checkpoint: 游标值
        :type checkpoint: int
        :param consumer_group_name: 消费组名
        :type consumer_group_name: str
        :param consumer_name: 消费者名
        :type consumer_name: str
        :param project_id: 项目ID
        :type project_id: str
        :param shard_id: 日志Shard ID
        :type shard_id: str
        :param update_time: 更新时间
        :type update_time: int
        """
        
        

        self._checkpoint = None
        self._consumer_group_name = None
        self._consumer_name = None
        self._project_id = None
        self._shard_id = None
        self._update_time = None
        self.discriminator = None

        if checkpoint is not None:
            self.checkpoint = checkpoint
        if consumer_group_name is not None:
            self.consumer_group_name = consumer_group_name
        if consumer_name is not None:
            self.consumer_name = consumer_name
        if project_id is not None:
            self.project_id = project_id
        if shard_id is not None:
            self.shard_id = shard_id
        if update_time is not None:
            self.update_time = update_time

    @property
    def checkpoint(self):
        r"""Gets the checkpoint of this ConsumerCheckpointInfo.

        游标值

        :return: The checkpoint of this ConsumerCheckpointInfo.
        :rtype: int
        """
        return self._checkpoint

    @checkpoint.setter
    def checkpoint(self, checkpoint):
        r"""Sets the checkpoint of this ConsumerCheckpointInfo.

        游标值

        :param checkpoint: The checkpoint of this ConsumerCheckpointInfo.
        :type checkpoint: int
        """
        self._checkpoint = checkpoint

    @property
    def consumer_group_name(self):
        r"""Gets the consumer_group_name of this ConsumerCheckpointInfo.

        消费组名

        :return: The consumer_group_name of this ConsumerCheckpointInfo.
        :rtype: str
        """
        return self._consumer_group_name

    @consumer_group_name.setter
    def consumer_group_name(self, consumer_group_name):
        r"""Sets the consumer_group_name of this ConsumerCheckpointInfo.

        消费组名

        :param consumer_group_name: The consumer_group_name of this ConsumerCheckpointInfo.
        :type consumer_group_name: str
        """
        self._consumer_group_name = consumer_group_name

    @property
    def consumer_name(self):
        r"""Gets the consumer_name of this ConsumerCheckpointInfo.

        消费者名

        :return: The consumer_name of this ConsumerCheckpointInfo.
        :rtype: str
        """
        return self._consumer_name

    @consumer_name.setter
    def consumer_name(self, consumer_name):
        r"""Sets the consumer_name of this ConsumerCheckpointInfo.

        消费者名

        :param consumer_name: The consumer_name of this ConsumerCheckpointInfo.
        :type consumer_name: str
        """
        self._consumer_name = consumer_name

    @property
    def project_id(self):
        r"""Gets the project_id of this ConsumerCheckpointInfo.

        项目ID

        :return: The project_id of this ConsumerCheckpointInfo.
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        r"""Sets the project_id of this ConsumerCheckpointInfo.

        项目ID

        :param project_id: The project_id of this ConsumerCheckpointInfo.
        :type project_id: str
        """
        self._project_id = project_id

    @property
    def shard_id(self):
        r"""Gets the shard_id of this ConsumerCheckpointInfo.

        日志Shard ID

        :return: The shard_id of this ConsumerCheckpointInfo.
        :rtype: str
        """
        return self._shard_id

    @shard_id.setter
    def shard_id(self, shard_id):
        r"""Sets the shard_id of this ConsumerCheckpointInfo.

        日志Shard ID

        :param shard_id: The shard_id of this ConsumerCheckpointInfo.
        :type shard_id: str
        """
        self._shard_id = shard_id

    @property
    def update_time(self):
        r"""Gets the update_time of this ConsumerCheckpointInfo.

        更新时间

        :return: The update_time of this ConsumerCheckpointInfo.
        :rtype: int
        """
        return self._update_time

    @update_time.setter
    def update_time(self, update_time):
        r"""Sets the update_time of this ConsumerCheckpointInfo.

        更新时间

        :param update_time: The update_time of this ConsumerCheckpointInfo.
        :type update_time: int
        """
        self._update_time = update_time

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
        if not isinstance(other, ConsumerCheckpointInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
