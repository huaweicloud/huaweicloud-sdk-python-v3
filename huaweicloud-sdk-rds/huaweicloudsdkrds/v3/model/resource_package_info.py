# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ResourcePackageInfo:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'resource_id': 'str',
        'engine_name': 'str',
        'used_quota': 'int',
        'total_quota': 'int',
        'status': 'str'
    }

    attribute_map = {
        'resource_id': 'resource_id',
        'engine_name': 'engine_name',
        'used_quota': 'used_quota',
        'total_quota': 'total_quota',
        'status': 'status'
    }

    def __init__(self, resource_id=None, engine_name=None, used_quota=None, total_quota=None, status=None):
        r"""ResourcePackageInfo

        The model defined in huaweicloud sdk

        :param resource_id: 资源包ID。
        :type resource_id: str
        :param engine_name: 引擎名称。
        :type engine_name: str
        :param used_quota: 已使用配额。
        :type used_quota: int
        :param total_quota: 总配额。
        :type total_quota: int
        :param status: 资源包状态。
        :type status: str
        """
        
        

        self._resource_id = None
        self._engine_name = None
        self._used_quota = None
        self._total_quota = None
        self._status = None
        self.discriminator = None

        if resource_id is not None:
            self.resource_id = resource_id
        if engine_name is not None:
            self.engine_name = engine_name
        if used_quota is not None:
            self.used_quota = used_quota
        if total_quota is not None:
            self.total_quota = total_quota
        if status is not None:
            self.status = status

    @property
    def resource_id(self):
        r"""Gets the resource_id of this ResourcePackageInfo.

        资源包ID。

        :return: The resource_id of this ResourcePackageInfo.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        r"""Sets the resource_id of this ResourcePackageInfo.

        资源包ID。

        :param resource_id: The resource_id of this ResourcePackageInfo.
        :type resource_id: str
        """
        self._resource_id = resource_id

    @property
    def engine_name(self):
        r"""Gets the engine_name of this ResourcePackageInfo.

        引擎名称。

        :return: The engine_name of this ResourcePackageInfo.
        :rtype: str
        """
        return self._engine_name

    @engine_name.setter
    def engine_name(self, engine_name):
        r"""Sets the engine_name of this ResourcePackageInfo.

        引擎名称。

        :param engine_name: The engine_name of this ResourcePackageInfo.
        :type engine_name: str
        """
        self._engine_name = engine_name

    @property
    def used_quota(self):
        r"""Gets the used_quota of this ResourcePackageInfo.

        已使用配额。

        :return: The used_quota of this ResourcePackageInfo.
        :rtype: int
        """
        return self._used_quota

    @used_quota.setter
    def used_quota(self, used_quota):
        r"""Sets the used_quota of this ResourcePackageInfo.

        已使用配额。

        :param used_quota: The used_quota of this ResourcePackageInfo.
        :type used_quota: int
        """
        self._used_quota = used_quota

    @property
    def total_quota(self):
        r"""Gets the total_quota of this ResourcePackageInfo.

        总配额。

        :return: The total_quota of this ResourcePackageInfo.
        :rtype: int
        """
        return self._total_quota

    @total_quota.setter
    def total_quota(self, total_quota):
        r"""Sets the total_quota of this ResourcePackageInfo.

        总配额。

        :param total_quota: The total_quota of this ResourcePackageInfo.
        :type total_quota: int
        """
        self._total_quota = total_quota

    @property
    def status(self):
        r"""Gets the status of this ResourcePackageInfo.

        资源包状态。

        :return: The status of this ResourcePackageInfo.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        r"""Sets the status of this ResourcePackageInfo.

        资源包状态。

        :param status: The status of this ResourcePackageInfo.
        :type status: str
        """
        self._status = status

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
        if not isinstance(other, ResourcePackageInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
