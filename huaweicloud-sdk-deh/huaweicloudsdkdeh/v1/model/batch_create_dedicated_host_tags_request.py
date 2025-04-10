# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class BatchCreateDedicatedHostTagsRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'dedicated_host_id': 'str',
        'body': 'ReqSetOrDeleteTags'
    }

    attribute_map = {
        'dedicated_host_id': 'dedicated_host_id',
        'body': 'body'
    }

    def __init__(self, dedicated_host_id=None, body=None):
        r"""BatchCreateDedicatedHostTagsRequest

        The model defined in huaweicloud sdk

        :param dedicated_host_id: 专属主机ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。
        :type dedicated_host_id: str
        :param body: Body of the BatchCreateDedicatedHostTagsRequest
        :type body: :class:`huaweicloudsdkdeh.v1.ReqSetOrDeleteTags`
        """
        
        

        self._dedicated_host_id = None
        self._body = None
        self.discriminator = None

        self.dedicated_host_id = dedicated_host_id
        if body is not None:
            self.body = body

    @property
    def dedicated_host_id(self):
        r"""Gets the dedicated_host_id of this BatchCreateDedicatedHostTagsRequest.

        专属主机ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。

        :return: The dedicated_host_id of this BatchCreateDedicatedHostTagsRequest.
        :rtype: str
        """
        return self._dedicated_host_id

    @dedicated_host_id.setter
    def dedicated_host_id(self, dedicated_host_id):
        r"""Sets the dedicated_host_id of this BatchCreateDedicatedHostTagsRequest.

        专属主机ID。  可以从专属主机控制台查询，或者通过调用查询专属主机列表API获取。

        :param dedicated_host_id: The dedicated_host_id of this BatchCreateDedicatedHostTagsRequest.
        :type dedicated_host_id: str
        """
        self._dedicated_host_id = dedicated_host_id

    @property
    def body(self):
        r"""Gets the body of this BatchCreateDedicatedHostTagsRequest.

        :return: The body of this BatchCreateDedicatedHostTagsRequest.
        :rtype: :class:`huaweicloudsdkdeh.v1.ReqSetOrDeleteTags`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this BatchCreateDedicatedHostTagsRequest.

        :param body: The body of this BatchCreateDedicatedHostTagsRequest.
        :type body: :class:`huaweicloudsdkdeh.v1.ReqSetOrDeleteTags`
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
        if not isinstance(other, BatchCreateDedicatedHostTagsRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
