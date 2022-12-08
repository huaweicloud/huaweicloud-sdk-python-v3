# coding: utf-8

import re
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
        'desktop_id': 'str',
        'body': 'DeleteVolumesReq'
    }

    attribute_map = {
        'desktop_id': 'desktop_id',
        'body': 'body'
    }

    def __init__(self, desktop_id=None, body=None):
        """DeleteDesktopVolumesRequest

        The model defined in huaweicloud sdk

        :param desktop_id: 桌面ID。
        :type desktop_id: str
        :param body: Body of the DeleteDesktopVolumesRequest
        :type body: :class:`huaweicloudsdkworkspace.v2.DeleteVolumesReq`
        """
        
        

        self._desktop_id = None
        self._body = None
        self.discriminator = None

        self.desktop_id = desktop_id
        if body is not None:
            self.body = body

    @property
    def desktop_id(self):
        """Gets the desktop_id of this DeleteDesktopVolumesRequest.

        桌面ID。

        :return: The desktop_id of this DeleteDesktopVolumesRequest.
        :rtype: str
        """
        return self._desktop_id

    @desktop_id.setter
    def desktop_id(self, desktop_id):
        """Sets the desktop_id of this DeleteDesktopVolumesRequest.

        桌面ID。

        :param desktop_id: The desktop_id of this DeleteDesktopVolumesRequest.
        :type desktop_id: str
        """
        self._desktop_id = desktop_id

    @property
    def body(self):
        """Gets the body of this DeleteDesktopVolumesRequest.

        :return: The body of this DeleteDesktopVolumesRequest.
        :rtype: :class:`huaweicloudsdkworkspace.v2.DeleteVolumesReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this DeleteDesktopVolumesRequest.

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
