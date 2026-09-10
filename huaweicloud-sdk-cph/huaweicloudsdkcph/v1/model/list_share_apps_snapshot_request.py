# coding: utf-8

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareAppsSnapshotRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'server_id': 'str',
        'limit': 'int',
        'marker': 'str',
        'package_name': 'str'
    }

    attribute_map = {
        'server_id': 'server_id',
        'limit': 'limit',
        'marker': 'marker',
        'package_name': 'package_name'
    }

    def __init__(self, server_id=None, limit=None, marker=None, package_name=None):
        r"""ListShareAppsSnapshotRequest

        The model defined in huaweicloud sdk

        :param server_id: 云手机服务器的唯一标识。
        :type server_id: str
        :param limit: 每页返回的资源个数。取值范围：1~500（默认值为100）。
        :type limit: int
        :param marker: 分页标记。
        :type marker: str
        :param package_name: 应用包名称，只包含大小写字母、数字、下划线、点，不能以数字和下划线开头，点不能作为结尾且包名中至少有一个点，长度不超过128
        :type package_name: str
        """
        
        

        self._server_id = None
        self._limit = None
        self._marker = None
        self._package_name = None
        self.discriminator = None

        self.server_id = server_id
        if limit is not None:
            self.limit = limit
        if marker is not None:
            self.marker = marker
        if package_name is not None:
            self.package_name = package_name

    @property
    def server_id(self):
        r"""Gets the server_id of this ListShareAppsSnapshotRequest.

        云手机服务器的唯一标识。

        :return: The server_id of this ListShareAppsSnapshotRequest.
        :rtype: str
        """
        return self._server_id

    @server_id.setter
    def server_id(self, server_id):
        r"""Sets the server_id of this ListShareAppsSnapshotRequest.

        云手机服务器的唯一标识。

        :param server_id: The server_id of this ListShareAppsSnapshotRequest.
        :type server_id: str
        """
        self._server_id = server_id

    @property
    def limit(self):
        r"""Gets the limit of this ListShareAppsSnapshotRequest.

        每页返回的资源个数。取值范围：1~500（默认值为100）。

        :return: The limit of this ListShareAppsSnapshotRequest.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        r"""Sets the limit of this ListShareAppsSnapshotRequest.

        每页返回的资源个数。取值范围：1~500（默认值为100）。

        :param limit: The limit of this ListShareAppsSnapshotRequest.
        :type limit: int
        """
        self._limit = limit

    @property
    def marker(self):
        r"""Gets the marker of this ListShareAppsSnapshotRequest.

        分页标记。

        :return: The marker of this ListShareAppsSnapshotRequest.
        :rtype: str
        """
        return self._marker

    @marker.setter
    def marker(self, marker):
        r"""Sets the marker of this ListShareAppsSnapshotRequest.

        分页标记。

        :param marker: The marker of this ListShareAppsSnapshotRequest.
        :type marker: str
        """
        self._marker = marker

    @property
    def package_name(self):
        r"""Gets the package_name of this ListShareAppsSnapshotRequest.

        应用包名称，只包含大小写字母、数字、下划线、点，不能以数字和下划线开头，点不能作为结尾且包名中至少有一个点，长度不超过128

        :return: The package_name of this ListShareAppsSnapshotRequest.
        :rtype: str
        """
        return self._package_name

    @package_name.setter
    def package_name(self, package_name):
        r"""Sets the package_name of this ListShareAppsSnapshotRequest.

        应用包名称，只包含大小写字母、数字、下划线、点，不能以数字和下划线开头，点不能作为结尾且包名中至少有一个点，长度不超过128

        :param package_name: The package_name of this ListShareAppsSnapshotRequest.
        :type package_name: str
        """
        self._package_name = package_name

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
        if not isinstance(other, ListShareAppsSnapshotRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
