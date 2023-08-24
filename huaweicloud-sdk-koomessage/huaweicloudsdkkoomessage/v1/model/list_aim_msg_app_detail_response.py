# coding: utf-8

import six

from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ListAimMsgAppDetailResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'app_id': 'str',
        'app_name': 'str',
        'status': 'str',
        'region': 'str',
        'create_time': 'str',
        'up_link_addr': 'str'
    }

    attribute_map = {
        'app_id': 'app_id',
        'app_name': 'app_name',
        'status': 'status',
        'region': 'region',
        'create_time': 'create_time',
        'up_link_addr': 'up_link_addr'
    }

    def __init__(self, app_id=None, app_name=None, status=None, region=None, create_time=None, up_link_addr=None):
        """ListAimMsgAppDetailResponse

        The model defined in huaweicloud sdk

        :param app_id: 应用ID，用于获取、修改应用的唯一标识。
        :type app_id: str
        :param app_name: 应用名称。
        :type app_name: str
        :param status: 状态。
        :type status: str
        :param region: 地域。
        :type region: str
        :param create_time: 创建时间，格式：yyyy-MM-dd&#39;T&#39;HH:mm:ss。
        :type create_time: str
        :param up_link_addr: 上行短信地址。
        :type up_link_addr: str
        """
        
        super(ListAimMsgAppDetailResponse, self).__init__()

        self._app_id = None
        self._app_name = None
        self._status = None
        self._region = None
        self._create_time = None
        self._up_link_addr = None
        self.discriminator = None

        if app_id is not None:
            self.app_id = app_id
        if app_name is not None:
            self.app_name = app_name
        if status is not None:
            self.status = status
        if region is not None:
            self.region = region
        if create_time is not None:
            self.create_time = create_time
        if up_link_addr is not None:
            self.up_link_addr = up_link_addr

    @property
    def app_id(self):
        """Gets the app_id of this ListAimMsgAppDetailResponse.

        应用ID，用于获取、修改应用的唯一标识。

        :return: The app_id of this ListAimMsgAppDetailResponse.
        :rtype: str
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ListAimMsgAppDetailResponse.

        应用ID，用于获取、修改应用的唯一标识。

        :param app_id: The app_id of this ListAimMsgAppDetailResponse.
        :type app_id: str
        """
        self._app_id = app_id

    @property
    def app_name(self):
        """Gets the app_name of this ListAimMsgAppDetailResponse.

        应用名称。

        :return: The app_name of this ListAimMsgAppDetailResponse.
        :rtype: str
        """
        return self._app_name

    @app_name.setter
    def app_name(self, app_name):
        """Sets the app_name of this ListAimMsgAppDetailResponse.

        应用名称。

        :param app_name: The app_name of this ListAimMsgAppDetailResponse.
        :type app_name: str
        """
        self._app_name = app_name

    @property
    def status(self):
        """Gets the status of this ListAimMsgAppDetailResponse.

        状态。

        :return: The status of this ListAimMsgAppDetailResponse.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this ListAimMsgAppDetailResponse.

        状态。

        :param status: The status of this ListAimMsgAppDetailResponse.
        :type status: str
        """
        self._status = status

    @property
    def region(self):
        """Gets the region of this ListAimMsgAppDetailResponse.

        地域。

        :return: The region of this ListAimMsgAppDetailResponse.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this ListAimMsgAppDetailResponse.

        地域。

        :param region: The region of this ListAimMsgAppDetailResponse.
        :type region: str
        """
        self._region = region

    @property
    def create_time(self):
        """Gets the create_time of this ListAimMsgAppDetailResponse.

        创建时间，格式：yyyy-MM-dd'T'HH:mm:ss。

        :return: The create_time of this ListAimMsgAppDetailResponse.
        :rtype: str
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this ListAimMsgAppDetailResponse.

        创建时间，格式：yyyy-MM-dd'T'HH:mm:ss。

        :param create_time: The create_time of this ListAimMsgAppDetailResponse.
        :type create_time: str
        """
        self._create_time = create_time

    @property
    def up_link_addr(self):
        """Gets the up_link_addr of this ListAimMsgAppDetailResponse.

        上行短信地址。

        :return: The up_link_addr of this ListAimMsgAppDetailResponse.
        :rtype: str
        """
        return self._up_link_addr

    @up_link_addr.setter
    def up_link_addr(self, up_link_addr):
        """Sets the up_link_addr of this ListAimMsgAppDetailResponse.

        上行短信地址。

        :param up_link_addr: The up_link_addr of this ListAimMsgAppDetailResponse.
        :type up_link_addr: str
        """
        self._up_link_addr = up_link_addr

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
        if not isinstance(other, ListAimMsgAppDetailResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
