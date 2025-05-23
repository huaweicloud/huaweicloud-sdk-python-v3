# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class DeleteDesktopVolumesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'service_transaction_id': 'str',
        'desktop_id': 'str',
        'body': 'DeleteVolumesReq'
    }

    attribute_map = {
        'service_transaction_id': 'Service-Transaction-Id',
        'desktop_id': 'desktop_id',
        'body': 'body'
    }

    def __init__(self, service_transaction_id=None, desktop_id=None, body=None):
        r"""DeleteDesktopVolumesRequest

        The model defined in huaweicloud sdk

        :param service_transaction_id: CBC接口回调时，请求头里带上的业务ID
        :type service_transaction_id: str
        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param body: Body of the DeleteDesktopVolumesRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.DeleteVolumesReq`
        """
        
        

        self._service_transaction_id = None
        self._desktop_id = None
        self._body = None
        self.discriminator = None

        if service_transaction_id is not None:
            self.service_transaction_id = service_transaction_id
        self.desktop_id = desktop_id
        if body is not None:
            self.body = body

    @property
    def service_transaction_id(self):
        r"""Gets the service_transaction_id of this DeleteDesktopVolumesRequest.

        CBC接口回调时，请求头里带上的业务ID

        :return: The service_transaction_id of this DeleteDesktopVolumesRequest.
        :rtype: str
        """
        return self._service_transaction_id

    @service_transaction_id.setter
    def service_transaction_id(self, service_transaction_id):
        r"""Sets the service_transaction_id of this DeleteDesktopVolumesRequest.

        CBC接口回调时，请求头里带上的业务ID

        :param service_transaction_id: The service_transaction_id of this DeleteDesktopVolumesRequest.
        :type service_transaction_id: str
        """
        self._service_transaction_id = service_transaction_id

    @property
    def desktop_id(self):
        r"""Gets the desktop_id of this DeleteDesktopVolumesRequest.

        桌面ID。

        :return: The desktop_id of this DeleteDesktopVolumesRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        r"""Sets the desktop_id of this DeleteDesktopVolumesRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this DeleteDesktopVolumesRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def body(self):
        r"""Gets the body of this DeleteDesktopVolumesRequest.

        :return: The body of this DeleteDesktopVolumesRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteVolumesReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this DeleteDesktopVolumesRequest.

        :param body: The body of this DeleteDesktopVolumesRequest.
        :type body: :class:`huaweicloudsdkworkspace.v2.DeleteVolumesReq`
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
        if not isinstance(other, DeleteDesktopVolumesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
