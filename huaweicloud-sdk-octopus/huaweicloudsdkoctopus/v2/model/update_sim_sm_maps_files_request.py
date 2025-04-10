# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class UpdateSimSmMapsFilesRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'parent_lookup_id': 'str',
        'sha256': 'str',
        'body': 'PatchedFileDetailSrlz'
    }

    attribute_map = {
        'parent_lookup_id': 'parent_lookup_id',
        'sha256': 'sha256',
        'body': 'body'
    }

    def __init__(self, parent_lookup_id=None, sha256=None, body=None):
        r"""UpdateSimSmMapsFilesRequest

        The model defined in huaweicloud sdk

        :param parent_lookup_id: 地图ID
        :type parent_lookup_id: str
        :param sha256: 文件sha256值
        :type sha256: str
        :param body: Body of the UpdateSimSmMapsFilesRequest
        :type body: :class:`huaweicloudsdkoctopus.v2.PatchedFileDetailSrlz`
        """
        
        

        self._parent_lookup_id = None
        self._sha256 = None
        self._body = None
        self.discriminator = None

        self.parent_lookup_id = parent_lookup_id
        self.sha256 = sha256
        if body is not None:
            self.body = body

    @property
    def parent_lookup_id(self):
        r"""Gets the parent_lookup_id of this UpdateSimSmMapsFilesRequest.

        地图ID

        :return: The parent_lookup_id of this UpdateSimSmMapsFilesRequest.
        :rtype: str
        """
        return self._parent_lookup_id

    @parent_lookup_id.setter
    def parent_lookup_id(self, parent_lookup_id):
        r"""Sets the parent_lookup_id of this UpdateSimSmMapsFilesRequest.

        地图ID

        :param parent_lookup_id: The parent_lookup_id of this UpdateSimSmMapsFilesRequest.
        :type parent_lookup_id: str
        """
        self._parent_lookup_id = parent_lookup_id

    @property
    def sha256(self):
        r"""Gets the sha256 of this UpdateSimSmMapsFilesRequest.

        文件sha256值

        :return: The sha256 of this UpdateSimSmMapsFilesRequest.
        :rtype: str
        """
        return self._sha256

    @sha256.setter
    def sha256(self, sha256):
        r"""Sets the sha256 of this UpdateSimSmMapsFilesRequest.

        文件sha256值

        :param sha256: The sha256 of this UpdateSimSmMapsFilesRequest.
        :type sha256: str
        """
        self._sha256 = sha256

    @property
    def body(self):
        r"""Gets the body of this UpdateSimSmMapsFilesRequest.

        :return: The body of this UpdateSimSmMapsFilesRequest.
        :rtype: :class:`huaweicloudsdkoctopus.v2.PatchedFileDetailSrlz`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this UpdateSimSmMapsFilesRequest.

        :param body: The body of this UpdateSimSmMapsFilesRequest.
        :type body: :class:`huaweicloudsdkoctopus.v2.PatchedFileDetailSrlz`
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
        if not isinstance(other, UpdateSimSmMapsFilesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
