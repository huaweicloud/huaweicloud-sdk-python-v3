# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateVolumeTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'volume_id': 'str',
        'body': 'BatchCreateVolumeTagsRequestBody'
    }

    attribute_map = {
        'volume_id': 'volume_id',
        'body': 'body'
    }

    def __init__(self, volume_id=None, body=None):
        r"""BatchCreateVolumeTagsRequest

        The model defined in huaweicloud sdk

        :param volume_id: 云硬盘ID。
        :type volume_id: str
        :param body: Body of the BatchCreateVolumeTagsRequest
        :type body: :class:`huaweicloudsdkevs.v2.BatchCreateVolumeTagsRequestBody`
        """
        
        

        self._volume_id = None
        self._body = None
        self.discriminator = None

        self.volume_id = volume_id
        if body is not None:
            self.body = body

    @property
    def volume_id(self):
        r"""Gets the volume_id of this BatchCreateVolumeTagsRequest.

        云硬盘ID。

        :return: The volume_id of this BatchCreateVolumeTagsRequest.
        :rtype: str
        """
        return self._volume_id

    @volume_id.setter
    def volume_id(self, volume_id):
        r"""Sets the volume_id of this BatchCreateVolumeTagsRequest.

        云硬盘ID。

        :param volume_id: The volume_id of this BatchCreateVolumeTagsRequest.
        :type volume_id: str
        """
        self._volume_id = volume_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateVolumeTagsRequest.

        :return: The body of this BatchCreateVolumeTagsRequest.
        :rtype: :class:`huaweicloudsdkevs.v2.BatchCreateVolumeTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateVolumeTagsRequest.

        :param body: The body of this BatchCreateVolumeTagsRequest.
        :type body: :class:`huaweicloudsdkevs.v2.BatchCreateVolumeTagsRequestBody`
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
        if not isinstance(other, BatchCreateVolumeTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
