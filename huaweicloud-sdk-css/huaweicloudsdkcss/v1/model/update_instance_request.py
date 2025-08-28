# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateInstanceRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'instance_id': 'str',
        'migrate_data': 'str',
        'agency': 'str'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'instance_id': 'instance_id',
        'migrate_data': 'migrateData',
        'agency': 'agency'
    }

    def __init__(self, cluster_id=None, instance_id=None, migrate_data=None, agency=None):
        r"""UpdateInstanceRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 指定替换集群ID。
        :type cluster_id: str
        :param instance_id: 指定替换节点ID。
        :type instance_id: str
        :param migrate_data: 是否迁移数据。
        :type migrate_data: str
        :param agency: 委托名称，委托给CSS服务，允许CSS调用您的其他云服务。
        :type agency: str
        """
        
        

        self._cluster_id = None
        self._instance_id = None
        self._migrate_data = None
        self._agency = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.instance_id = instance_id
        if migrate_data is not None:
            self.migrate_data = migrate_data
        if agency is not None:
            self.agency = agency

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this UpdateInstanceRequest.

        指定替换集群ID。

        :return: The cluster_id of this UpdateInstanceRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this UpdateInstanceRequest.

        指定替换集群ID。

        :param cluster_id: The cluster_id of this UpdateInstanceRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def instance_id(self):
        r"""Gets the instance_id of this UpdateInstanceRequest.

        指定替换节点ID。

        :return: The instance_id of this UpdateInstanceRequest.
        :rtype: str
        """
        return self._instance_id

    @instance_id.setter
    def instance_id(self, instance_id):
        r"""Sets the instance_id of this UpdateInstanceRequest.

        指定替换节点ID。

        :param instance_id: The instance_id of this UpdateInstanceRequest.
        :type instance_id: str
        """
        self._instance_id = instance_id

    @property
    def migrate_data(self):
        r"""Gets the migrate_data of this UpdateInstanceRequest.

        是否迁移数据。

        :return: The migrate_data of this UpdateInstanceRequest.
        :rtype: str
        """
        return self._migrate_data

    @migrate_data.setter
    def migrate_data(self, migrate_data):
        r"""Sets the migrate_data of this UpdateInstanceRequest.

        是否迁移数据。

        :param migrate_data: The migrate_data of this UpdateInstanceRequest.
        :type migrate_data: str
        """
        self._migrate_data = migrate_data

    @property
    def agency(self):
        r"""Gets the agency of this UpdateInstanceRequest.

        委托名称，委托给CSS服务，允许CSS调用您的其他云服务。

        :return: The agency of this UpdateInstanceRequest.
        :rtype: str
        """
        return self._agency

    @agency.setter
    def agency(self, agency):
        r"""Sets the agency of this UpdateInstanceRequest.

        委托名称，委托给CSS服务，允许CSS调用您的其他云服务。

        :param agency: The agency of this UpdateInstanceRequest.
        :type agency: str
        """
        self._agency = agency

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
        if not isinstance(other, UpdateInstanceRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
