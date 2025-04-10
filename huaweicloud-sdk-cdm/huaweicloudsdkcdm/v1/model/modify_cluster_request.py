# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class ModifyClusterRequest:

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    sensitive_list = []

    openapi_types = {
        'cluster_id': 'str',
        'content_type': 'str',
        'x_language': 'str',
        'body': 'CdmModifyClusterReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'content_type': 'Content-Type',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, content_type=None, x_language=None, body=None):
        r"""ModifyClusterRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param content_type: 消息体的类型（格式），有Body体的情况下必选，没有Body体无需填写。如果请求消息体中含有中文字符，则需要通过charset&#x3D;utf8指定中文字符集，例如取值为：application/json;charset&#x3D;utf8。
        :type content_type: str
        :param x_language: 请求语言。
        :type x_language: str
        :param body: Body of the ModifyClusterRequest
        :type body: :class:`huaweicloudsdkcdm.v1.CdmModifyClusterReq`
        """
        
        

        self._cluster_id = None
        self._content_type = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.content_type = content_type
        self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        r"""Gets the cluster_id of this ModifyClusterRequest.

        集群ID

        :return: The cluster_id of this ModifyClusterRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        r"""Sets the cluster_id of this ModifyClusterRequest.

        集群ID

        :param cluster_id: The cluster_id of this ModifyClusterRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def content_type(self):
        r"""Gets the content_type of this ModifyClusterRequest.

        消息体的类型（格式），有Body体的情况下必选，没有Body体无需填写。如果请求消息体中含有中文字符，则需要通过charset=utf8指定中文字符集，例如取值为：application/json;charset=utf8。

        :return: The content_type of this ModifyClusterRequest.
        :rtype: str
        """
        return self._content_type

    @content_type.setter
    def content_type(self, content_type):
        r"""Sets the content_type of this ModifyClusterRequest.

        消息体的类型（格式），有Body体的情况下必选，没有Body体无需填写。如果请求消息体中含有中文字符，则需要通过charset=utf8指定中文字符集，例如取值为：application/json;charset=utf8。

        :param content_type: The content_type of this ModifyClusterRequest.
        :type content_type: str
        """
        self._content_type = content_type

    @property
    def x_language(self):
        r"""Gets the x_language of this ModifyClusterRequest.

        请求语言。

        :return: The x_language of this ModifyClusterRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        r"""Sets the x_language of this ModifyClusterRequest.

        请求语言。

        :param x_language: The x_language of this ModifyClusterRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        r"""Gets the body of this ModifyClusterRequest.

        :return: The body of this ModifyClusterRequest.
        :rtype: :class:`huaweicloudsdkcdm.v1.CdmModifyClusterReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        r"""Sets the body of this ModifyClusterRequest.

        :param body: The body of this ModifyClusterRequest.
        :type body: :class:`huaweicloudsdkcdm.v1.CdmModifyClusterReq`
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
        if not isinstance(other, ModifyClusterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
