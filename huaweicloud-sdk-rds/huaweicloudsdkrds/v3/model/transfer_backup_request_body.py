# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class TransferBackupRequestBody:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'backups': 'list[str]',
        'instance_id': 'str',
        'destination': 'str',
        'prefix': 'str'
    }

    attribute_map = {
        'backups': 'backups',
        'instance_id': 'instance_id',
        'destination': 'destination',
        'prefix': 'prefix'
    }

    def __init__(self, backups=None, instance_id=None, destination=None, prefix=None):
        r"""TransferBackupRequestBody

        The model defined in huaweicloud sdk

        :param backups: 备份id列表
        :type backups: list[str]
        :param instance_id: 实例id
        :type instance_id: str
        :param destination: 目标OBS桶名
        :type destination: str
        :param prefix: 目标前缀
        :type prefix: str
        """
        
        

        self._backups = None
        self._instance_id = None
        self._destination = None
        self._prefix = None
        self.discriminator = None

        self.backups = backups
        self.instance_id = instance_id
        self.destination = destination
        if prefix is not None:
            self.prefix = prefix

    @property
    def backups(self):
        r"""Gets the backups of this TransferBackupRequestBody.

        备份id列表

        :return: The backups of this TransferBackupRequestBody.
        :rtype: list[str]
        """
        return self._backups

    @backups.setter
    def backups(self, backups):
        r"""Sets the backups of this TransferBackupRequestBody.

        备份id列表

        :param backups: The backups of this TransferBackupRequestBody.
        :type backups: list[str]
        """
        self._backups = backups

    @property
    def instance_id(self):
        r"""Gets the instance_id of this TransferBackupRequestBody.

        实例id

        :return: The instance_id of this TransferBackupRequestBody.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this TransferBackupRequestBody.

        实例id

        :param instance_id: The instance_id of this TransferBackupRequestBody.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def destination(self):
        r"""Gets the destination of this TransferBackupRequestBody.

        目标OBS桶名

        :return: The destination of this TransferBackupRequestBody.
        :rtype: str
        """
        return self._destination

    @destination.setter
    def destination(self, destination):
        r"""Sets the destination of this TransferBackupRequestBody.

        目标OBS桶名

        :param destination: The destination of this TransferBackupRequestBody.
        :type destination: str
        """
        self._destination = destination

    @property
    def prefix(self):
        r"""Gets the prefix of this TransferBackupRequestBody.

        目标前缀

        :return: The prefix of this TransferBackupRequestBody.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        r"""Sets the prefix of this TransferBackupRequestBody.

        目标前缀

        :param prefix: The prefix of this TransferBackupRequestBody.
        :type prefix: str
        """
        self._prefix = prefix

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
        if not isinstance(other, TransferBackupRequestBody):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
