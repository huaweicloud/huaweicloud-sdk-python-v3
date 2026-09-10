# coding: utf-8

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListShareAppsSnapshotResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'request_id': 'str',
        'collect_time': 'str',
        'share_apps': 'list[ListShareAppsSnapshotResponseBodyShareApps]',
        'page_info': 'ListCloudPhoneServersModelOfferingsResponseBodyPageInfo'
    }

    attribute_map = {
        'request_id': 'request_id',
        'collect_time': 'collect_time',
        'share_apps': 'share_apps',
        'page_info': 'page_info'
    }

    def __init__(self, request_id=None, collect_time=None, share_apps=None, page_info=None):
        r"""ListShareAppsSnapshotResponse

        The model defined in huaweicloud sdk

        :param request_id: 请求的唯一标识ID。
        :type request_id: str
        :param collect_time: 采集时间。
        :type collect_time: str
        :param share_apps: 采集的共享应用信息
        :type share_apps: list[:class:`huaweicloudsdkcph.v1.ListShareAppsSnapshotResponseBodyShareApps`]
        :param page_info: 
        :type page_info: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyPageInfo`
        """
        
        super().__init__()

        self._request_id = None
        self._collect_time = None
        self._share_apps = None
        self._page_info = None
        self.discriminator = None

        if request_id is not None:
            self.request_id = request_id
        if collect_time is not None:
            self.collect_time = collect_time
        if share_apps is not None:
            self.share_apps = share_apps
        if page_info is not None:
            self.page_info = page_info

    @property
    def request_id(self):
        r"""Gets the request_id of this ListShareAppsSnapshotResponse.

        请求的唯一标识ID。

        :return: The request_id of this ListShareAppsSnapshotResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        r"""Sets the request_id of this ListShareAppsSnapshotResponse.

        请求的唯一标识ID。

        :param request_id: The request_id of this ListShareAppsSnapshotResponse.
        :type request_id: str
        """
        self._request_id = request_id

    @property
    def collect_time(self):
        r"""Gets the collect_time of this ListShareAppsSnapshotResponse.

        采集时间。

        :return: The collect_time of this ListShareAppsSnapshotResponse.
        :rtype: str
        """
        return self._collect_time

    @collect_time.setter
    def collect_time(self, collect_time):
        r"""Sets the collect_time of this ListShareAppsSnapshotResponse.

        采集时间。

        :param collect_time: The collect_time of this ListShareAppsSnapshotResponse.
        :type collect_time: str
        """
        self._collect_time = collect_time

    @property
    def share_apps(self):
        r"""Gets the share_apps of this ListShareAppsSnapshotResponse.

        采集的共享应用信息

        :return: The share_apps of this ListShareAppsSnapshotResponse.
        :rtype: list[:class:`huaweicloudsdkcph.v1.ListShareAppsSnapshotResponseBodyShareApps`]
        """
        return self._share_apps

    @share_apps.setter
    def share_apps(self, share_apps):
        r"""Sets the share_apps of this ListShareAppsSnapshotResponse.

        采集的共享应用信息

        :param share_apps: The share_apps of this ListShareAppsSnapshotResponse.
        :type share_apps: list[:class:`huaweicloudsdkcph.v1.ListShareAppsSnapshotResponseBodyShareApps`]
        """
        self._share_apps = share_apps

    @property
    def page_info(self):
        r"""Gets the page_info of this ListShareAppsSnapshotResponse.

        :return: The page_info of this ListShareAppsSnapshotResponse.
        :rtype: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyPageInfo`
        """
        return self._page_info

    @page_info.setter
    def page_info(self, page_info):
        r"""Sets the page_info of this ListShareAppsSnapshotResponse.

        :param page_info: The page_info of this ListShareAppsSnapshotResponse.
        :type page_info: :class:`huaweicloudsdkcph.v1.ListCloudPhoneServersModelOfferingsResponseBodyPageInfo`
        """
        self._page_info = page_info

    def to_dict(self):
        import warnings
        warnings.warn("ListShareAppsSnapshotResponse.to_dict() is deprecated and no longer maintained, "
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
        if not isinstance(other, ListShareAppsSnapshotResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
