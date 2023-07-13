# coding: utf-8

import six

from huaweicloudsdkcore.utils.http_utils import sanitize_for_serialization


class EnableComponentRequest:

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
        'component_name': 'str',
        'x_language': 'str',
        'body': 'AddComponentReq'
    }

    attribute_map = {
        'cluster_id': 'cluster_id',
        'component_name': 'component_name',
        'x_language': 'X-Language',
        'body': 'body'
    }

    def __init__(self, cluster_id=None, component_name=None, x_language=None, body=None):
        """EnableComponentRequest

        The model defined in huaweicloud sdk

        :param cluster_id: 集群ID
        :type cluster_id: str
        :param component_name: 组件类型，取值为tsdb
        :type component_name: str
        :param x_language: 语言类型
        :type x_language: str
        :param body: Body of the EnableComponentRequest
        :type body: :class:`huaweicloudsdkcloudtable.v2.AddComponentReq`
        """
        
        

        self._cluster_id = None
        self._component_name = None
        self._x_language = None
        self._body = None
        self.discriminator = None

        self.cluster_id = cluster_id
        self.component_name = component_name
        if x_language is not None:
            self.x_language = x_language
        if body is not None:
            self.body = body

    @property
    def cluster_id(self):
        """Gets the cluster_id of this EnableComponentRequest.

        集群ID

        :return: The cluster_id of this EnableComponentRequest.
        :rtype: str
        """
        return self._cluster_id

    @cluster_id.setter
    def cluster_id(self, cluster_id):
        """Sets the cluster_id of this EnableComponentRequest.

        集群ID

        :param cluster_id: The cluster_id of this EnableComponentRequest.
        :type cluster_id: str
        """
        self._cluster_id = cluster_id

    @property
    def component_name(self):
        """Gets the component_name of this EnableComponentRequest.

        组件类型，取值为tsdb

        :return: The component_name of this EnableComponentRequest.
        :rtype: str
        """
        return self._component_name

    @component_name.setter
    def component_name(self, component_name):
        """Sets the component_name of this EnableComponentRequest.

        组件类型，取值为tsdb

        :param component_name: The component_name of this EnableComponentRequest.
        :type component_name: str
        """
        self._component_name = component_name

    @property
    def x_language(self):
        """Gets the x_language of this EnableComponentRequest.

        语言类型

        :return: The x_language of this EnableComponentRequest.
        :rtype: str
        """
        return self._x_language

    @x_language.setter
    def x_language(self, x_language):
        """Sets the x_language of this EnableComponentRequest.

        语言类型

        :param x_language: The x_language of this EnableComponentRequest.
        :type x_language: str
        """
        self._x_language = x_language

    @property
    def body(self):
        """Gets the body of this EnableComponentRequest.

        :return: The body of this EnableComponentRequest.
        :rtype: :class:`huaweicloudsdkcloudtable.v2.AddComponentReq`
        """
        return self._body

    @body.setter
    def body(self, body):
        """Sets the body of this EnableComponentRequest.

        :param body: The body of this EnableComponentRequest.
        :type body: :class:`huaweicloudsdkcloudtable.v2.AddComponentReq`
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
        if not isinstance(other, EnableComponentRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
