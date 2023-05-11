# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreatePublicipTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_id': 'str',
        'body': 'BatchCreatePublicipTagsRequestBody'
    }

    attribute_map = {
        'publicip_id': 'publicip_id',
        'body': 'body'
    }

    def __init__(self, publicip_id=None, body=None):
        """BatchCreatePublicipTagsRequest

        The model defined in huaweicloud sdk

        :param publicip_id: 资源ID
        :type publicip_id: str
        :param body: Body of the BatchCreatePublicipTagsRequest
        :type body: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsRequestBody`
        """
        
        

        self._publicip_id = None
        self._body = None
        self.discriminator = None

        self.publicip_id = publicip_id
        if body is not None:
            self.body = body

    @property
    def publicip_id(self):
        """Gets the publicip_id of this BatchCreatePublicipTagsRequest.

        资源ID

        :return: The publicip_id of this BatchCreatePublicipTagsRequest.
        :rtype: str
        """
        return self._publicip_id

    @publicip_id.setter
    def publicip_id(self, publicip_id):
        """Sets the publicip_id of this BatchCreatePublicipTagsRequest.

        资源ID

        :param publicip_id: The publicip_id of this BatchCreatePublicipTagsRequest.
        :type publicip_id: str
        """
        self._publicip_id = publicip_id

    @property
    def body(self):
        """Gets the body of this BatchCreatePublicipTagsRequest.

        :return: The body of this BatchCreatePublicipTagsRequest.
        :rtype: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsRequestBody`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this BatchCreatePublicipTagsRequest.

        :param body: The body of this BatchCreatePublicipTagsRequest.
        :type body: :class:`huaweicloudsdkeip.v2.BatchCreatePublicipTagsRequestBody`
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
        if not isinstance(other, BatchCreatePublicipTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
