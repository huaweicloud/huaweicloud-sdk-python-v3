# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ExpandDesktopVolumeRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'desktop_id': 'str',
        'service_transaction_id': 'str',
        'volume_id': 'str',
        'body': 'ExpandVolumeReq'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'service_transaction_id': 'Service-Transaction-Id',
        'volume_id': 'volume_id',
        'body': 'body'
    }

    def __init__(self, desktop_id=None, service_transaction_id=None, volume_id=None, body=None):
        """ExpandDesktopVolumeRequest

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param service_transaction_id: CBC接口回调时，请求头里带上的业务ID
        :type service_transaction_id: str
        :param volume_id: 磁盘ID。
        :type volume_id: str
        :param body: Body of the ExpandDesktopVolumeRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.ExpandVolumeReq`
        """
        
        

        self._desktop_id = None
        self._service_transaction_id = None
        self._volume_id = None
        self._body = None
        self.discriminator = None

        self.desktop_id = desktop_id
        if service_transaction_id is not None:
            self.service_transaction_id = service_transaction_id
        self.volume_id = volume_id
        if body is not None:
            self.body = body

    @property
    def desktop_id(self):
        """Gets the desktop_id of this ExpandDesktopVolumeRequest.

        桌面ID。

        :return: The desktop_id of this ExpandDesktopVolumeRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this ExpandDesktopVolumeRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this ExpandDesktopVolumeRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def service_transaction_id(self):
        """Gets the service_transaction_id of this ExpandDesktopVolumeRequest.

        CBC接口回调时，请求头里带上的业务ID

        :return: The service_transaction_id of this ExpandDesktopVolumeRequest.
        :rtype: str
        """
        return self._service_transaction_id

    @service_transaction_id.setter
    def service_transaction_id(self, service_transaction_id):
        """Sets the service_transaction_id of this ExpandDesktopVolumeRequest.

        CBC接口回调时，请求头里带上的业务ID

        :param service_transaction_id: The service_transaction_id of this ExpandDesktopVolumeRequest.
        :type service_transaction_id: str
        """
        self._service_transaction_id = service_transaction_id

    @property
    def volume_id(self):
        """Gets the volume_id of this ExpandDesktopVolumeRequest.

        磁盘ID。

        :return: The volume_id of this ExpandDesktopVolumeRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        """Sets the volume_id of this ExpandDesktopVolumeRequest.

        磁盘ID。

        :param volume_id: The volume_id of this ExpandDesktopVolumeRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def body(self):
        """Gets the body of this ExpandDesktopVolumeRequest.

        :return: The body of this ExpandDesktopVolumeRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.ExpandVolumeReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this ExpandDesktopVolumeRequest.

        :param body: The body of this ExpandDesktopVolumeRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.ExpandVolumeReq`
        """
        self._body = body

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
        if not isinstance(other, ExpandDesktopVolumeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
