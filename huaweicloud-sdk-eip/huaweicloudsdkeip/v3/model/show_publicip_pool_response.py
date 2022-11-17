# coding: utf-8

import re
import six


from huaweicloudsdkcore.sdk_response import SdkResponse
from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ShowPublicipPoolResponse(SdkResponse):

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'publicip_pool': 'PublicipPoolShowResp',
        'request_id': 'str'
    }

    attribute_map = {
        'publicip_pool': 'publicip_pool',
        'request_id': 'request_id'
    }

    def __init__(self, publicip_pool=None, request_id=None):
        """ShowPublicipPoolResponse

        The model defined in huaweicloud sdk

        :param publicip_pool: 
        :type publicip_pool: :class:`huaweicloudsdkeip.v3.PublicipPoolShowResp`
        :param request_id: 本次请求的编号
        :type request_id: str
        """
        
        super(ShowPublicipPoolResponse, self).__init__()

        self._publicip_pool = None
        self._request_id = None
        self.discriminator = None

        if publicip_pool is not None:
            self.publicip_pool = publicip_pool
        if request_id is not None:
            self.request_id = request_id

    @property
    def publicip_pool(self):
        """Gets the publicip_pool of this ShowPublicipPoolResponse.

        :return: The publicip_pool of this ShowPublicipPoolResponse.
        :rtype: :class:`huaweicloudsdkeip.v3.PublicipPoolShowResp`
        """
        return self._publicip_pool

    @publicip_pool.setter
    def publicip_pool(self, publicip_pool):
        """Sets the publicip_pool of this ShowPublicipPoolResponse.

        :param publicip_pool: The publicip_pool of this ShowPublicipPoolResponse.
        :type publicip_pool: :class:`huaweicloudsdkeip.v3.PublicipPoolShowResp`
        """
        self._publicip_pool = publicip_pool

    @property
    def request_id(self):
        """Gets the request_id of this ShowPublicipPoolResponse.

        本次请求的编号

        :return: The request_id of this ShowPublicipPoolResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """Sets the request_id of this ShowPublicipPoolResponse.

        本次请求的编号

        :param request_id: The request_id of this ShowPublicipPoolResponse.
        :type request_id: str
        """
        self._request_id = request_id

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
        if not isinstance(other, ShowPublicipPoolResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
