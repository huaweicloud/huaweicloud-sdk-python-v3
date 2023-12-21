# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ValidateDeletableReplicaResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'check_result': 'bool',
        'available_zone': 'str',
        'replication_list': 'list[ReplicationInfo]'
    }

    attribute_map = {
        'check_result': 'check_result',
        'available_zone': 'available_zone',
        'replication_list': 'replication_list'
    }

    def __init__(self, check_result=None, available_zone=None, replication_list=None):
        """ValidateDeletableReplicaResponse

        The model defined in huaweicloud sdk

        :param check_result: 是否有可供选择的副本组进行删除。
        :type check_result: bool
        :param available_zone: 可选的可用区ID列表
        :type available_zone: str
        :param replication_list: 可选的保留节点列表
        :type replication_list: list[:class:`huaweicloudsdkdcs.v2.ReplicationInfo`]
        """
        
        super(ValidateDeletableReplicaResponse, self).__init__()

        self._check_result = None
        self._available_zone = None
        self._replication_list = None
        self.discriminator = None

        if check_result is not None:
            self.check_result = check_result
        if available_zone is not None:
            self.available_zone = available_zone
        if replication_list is not None:
            self.replication_list = replication_list

    @property
    def check_result(self):
        """Gets the check_result of this ValidateDeletableReplicaResponse.

        是否有可供选择的副本组进行删除。

        :return: The check_result of this ValidateDeletableReplicaResponse.
        :rtype: bool
        """
        return self._check_result

    @check_result.setter
    def check_result(self, check_result):
        """Sets the check_result of this ValidateDeletableReplicaResponse.

        是否有可供选择的副本组进行删除。

        :param check_result: The check_result of this ValidateDeletableReplicaResponse.
        :type check_result: bool
        """
        self._check_result = check_result

    @property
    def available_zone(self):
        """Gets the available_zone of this ValidateDeletableReplicaResponse.

        可选的可用区ID列表

        :return: The available_zone of this ValidateDeletableReplicaResponse.
        :rtype: str
        """
        return self._available_zone

    @available_zone.setter
    def available_zone(self, available_zone):
        """Sets the available_zone of this ValidateDeletableReplicaResponse.

        可选的可用区ID列表

        :param available_zone: The available_zone of this ValidateDeletableReplicaResponse.
        :type available_zone: str
        """
        self._available_zone = available_zone

    @property
    def replication_list(self):
        """Gets the replication_list of this ValidateDeletableReplicaResponse.

        可选的保留节点列表

        :return: The replication_list of this ValidateDeletableReplicaResponse.
        :rtype: list[:class:`huaweicloudsdkdcs.v2.ReplicationInfo`]
        """
        return self._replication_list

    @replication_list.setter
    def replication_list(self, replication_list):
        """Sets the replication_list of this ValidateDeletableReplicaResponse.

        可选的保留节点列表

        :param replication_list: The replication_list of this ValidateDeletableReplicaResponse.
        :type replication_list: list[:class:`huaweicloudsdkdcs.v2.ReplicationInfo`]
        """
        self._replication_list = replication_list

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
        if not isinstance(other, ValidateDeletableReplicaResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
